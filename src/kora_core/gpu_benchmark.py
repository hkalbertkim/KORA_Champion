"""GPU benchmark plan helpers for KORA runtime evidence."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from kora_core.compat import StrEnum


class GPUBenchmarkStage(StrEnum):
    SMOKE = "smoke"
    MICRO = "micro"
    HEAVY = "heavy"
    SATURATION = "saturation"


STAGE_RANGES: dict[GPUBenchmarkStage, tuple[int, int | None]] = {
    GPUBenchmarkStage.SMOKE: (10, 100),
    GPUBenchmarkStage.MICRO: (1_000, 10_000),
    GPUBenchmarkStage.HEAVY: (100_000, None),
    GPUBenchmarkStage.SATURATION: (500_000, None),
}


@dataclass(frozen=True)
class GPUWorkloadDescriptor:
    workload_id: str
    workload_size: int
    workload_unit_type: str
    stage: str
    batch_size: int
    planned_batches: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "workload_id": self.workload_id,
            "workload_size": self.workload_size,
            "workload_unit_type": self.workload_unit_type,
            "stage": self.stage,
            "batch_size": self.batch_size,
            "planned_batches": self.planned_batches,
        }


@dataclass(frozen=True)
class GPUBenchmarkPlan:
    target_gpu_count: int
    target_resource_deadline: str
    stages: list[GPUWorkloadDescriptor]
    evidence_required_per_stage: dict[str, list[str]]
    safety_notes: list[str] = field(default_factory=list)
    claim_boundaries: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_gpu_count": self.target_gpu_count,
            "target_resource_deadline": self.target_resource_deadline,
            "stages": [stage.to_dict() for stage in self.stages],
            "evidence_required_per_stage": self.evidence_required_per_stage,
            "safety_notes": list(self.safety_notes),
            "claim_boundaries": list(self.claim_boundaries),
        }


def validate_stage_size(stage: GPUBenchmarkStage | str, workload_size: int) -> None:
    selected_stage = GPUBenchmarkStage(stage)
    lower, upper = STAGE_RANGES[selected_stage]
    if workload_size < lower:
        raise ValueError(f"{selected_stage.value} stage requires at least {lower} workload units")
    if upper is not None and workload_size > upper:
        raise ValueError(f"{selected_stage.value} stage allows at most {upper} workload units")


def build_workload_descriptor(
    *,
    stage: GPUBenchmarkStage | str,
    workload_size: int,
    workload_unit_type: str = "synthetic_inference_unit",
    batch_size: int = 1_000,
) -> GPUWorkloadDescriptor:
    selected_stage = GPUBenchmarkStage(stage)
    validate_stage_size(selected_stage, workload_size)
    planned_batches = max(1, (workload_size + batch_size - 1) // batch_size)
    return GPUWorkloadDescriptor(
        workload_id=f"gpu_{selected_stage.value}_{workload_size}",
        workload_size=workload_size,
        workload_unit_type=workload_unit_type,
        stage=selected_stage.value,
        batch_size=batch_size,
        planned_batches=planned_batches,
    )


def build_default_gpu_benchmark_plan() -> GPUBenchmarkPlan:
    stages = [
        build_workload_descriptor(stage=GPUBenchmarkStage.SMOKE, workload_size=100, batch_size=50),
        build_workload_descriptor(stage=GPUBenchmarkStage.MICRO, workload_size=10_000, batch_size=1_000),
        build_workload_descriptor(stage=GPUBenchmarkStage.HEAVY, workload_size=100_000, batch_size=5_000),
        build_workload_descriptor(stage=GPUBenchmarkStage.SATURATION, workload_size=1_000_000, batch_size=10_000),
    ]
    evidence_required = {
        stage.stage: [
            "gpu_snapshot_before",
            "gpu_snapshot_after",
            "runtime_seconds",
            "successful_units",
            "failed_units",
            "throughput_units_per_second",
            "utilization_samples",
            "memory_samples",
            "claim_boundary",
        ]
        for stage in stages
    }
    return GPUBenchmarkPlan(
        target_gpu_count=2,
        target_resource_deadline="2026-07-01",
        stages=stages,
        evidence_required_per_stage=evidence_required,
        safety_notes=[
            "Do not include secret material or private access details in public evidence.",
            "Do not include machine access metadata in public evidence.",
            "Run larger stages only after smoke evidence passes automated validation.",
        ],
        claim_boundaries=[
            "GPU harness output alone does not prove GPU reduction.",
            "GPU harness output alone does not prove infrastructure reduction.",
            "Full comparison requires GPU-only and KORA-routed measured runs.",
        ],
    )
