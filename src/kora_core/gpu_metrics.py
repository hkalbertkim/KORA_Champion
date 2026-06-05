"""GPU runtime evidence data structures and summary helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean
from typing import Any, Iterable

from kora_core.compat import StrEnum


class GPUClaimLevel(StrEnum):
    GPU_SCHEMA_ONLY = "gpu_schema_only"
    GPU_SMOKE_MEASURED = "gpu_smoke_measured"
    GPU_MICRO_BENCHMARK_MEASURED = "gpu_micro_benchmark_measured"
    GPU_HEAVY_BENCHMARK_MEASURED = "gpu_heavy_benchmark_measured"
    GPU_SATURATION_MEASURED = "gpu_saturation_measured"


@dataclass(frozen=True)
class GPUDeviceSnapshot:
    gpu_provider_label: str
    gpu_model: str
    gpu_count: int
    cuda_available: bool
    driver_version: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "gpu_provider_label": self.gpu_provider_label,
            "gpu_model": self.gpu_model,
            "gpu_count": self.gpu_count,
            "cuda_available": self.cuda_available,
            "driver_version": self.driver_version,
        }


@dataclass(frozen=True)
class GPUSample:
    utilization_percent: float | None = None
    memory_used_mb: float | None = None
    memory_total_mb: float | None = None


@dataclass(frozen=True)
class GPURunSummary:
    gpu_provider_label: str
    gpu_model: str
    gpu_count: int
    cuda_available: bool
    driver_version: str | None
    workload_id: str
    workload_size: int
    workload_unit_type: str
    started_at_utc: str
    ended_at_utc: str
    runtime_seconds: float
    throughput_units_per_second: float | None
    gpu_utilization_average: float | None
    gpu_utilization_max: float | None
    gpu_memory_average_mb: float | None
    gpu_memory_max_mb: float | None
    successful_units: int
    failed_units: int
    latency_average_ms: float | None
    latency_min_ms: float | None
    latency_max_ms: float | None
    estimated_gpu_cost: float | None
    claim_level: str
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "gpu_provider_label": self.gpu_provider_label,
            "gpu_model": self.gpu_model,
            "gpu_count": self.gpu_count,
            "cuda_available": self.cuda_available,
            "driver_version": self.driver_version,
            "workload_id": self.workload_id,
            "workload_size": self.workload_size,
            "workload_unit_type": self.workload_unit_type,
            "started_at_utc": self.started_at_utc,
            "ended_at_utc": self.ended_at_utc,
            "runtime_seconds": self.runtime_seconds,
            "throughput_units_per_second": self.throughput_units_per_second,
            "gpu_utilization_average": self.gpu_utilization_average,
            "gpu_utilization_max": self.gpu_utilization_max,
            "gpu_memory_average_mb": self.gpu_memory_average_mb,
            "gpu_memory_max_mb": self.gpu_memory_max_mb,
            "successful_units": self.successful_units,
            "failed_units": self.failed_units,
            "latency_average_ms": self.latency_average_ms,
            "latency_min_ms": self.latency_min_ms,
            "latency_max_ms": self.latency_max_ms,
            "estimated_gpu_cost": self.estimated_gpu_cost,
            "claim_level": self.claim_level,
            "warnings": list(self.warnings),
        }


def summarize_gpu_run(
    *,
    device: GPUDeviceSnapshot,
    workload_id: str,
    workload_size: int,
    workload_unit_type: str,
    started_at_utc: str,
    ended_at_utc: str,
    runtime_seconds: float,
    successful_units: int,
    failed_units: int,
    samples: Iterable[GPUSample] = (),
    latency_ms: Iterable[float] = (),
    estimated_gpu_cost: float | None = None,
    claim_level: GPUClaimLevel | str = GPUClaimLevel.GPU_SCHEMA_ONLY,
    warnings: Iterable[str] = (),
) -> GPURunSummary:
    selected_samples = list(samples)
    selected_latency = [float(value) for value in latency_ms]
    utilization_values = [sample.utilization_percent for sample in selected_samples if sample.utilization_percent is not None]
    memory_values = [sample.memory_used_mb for sample in selected_samples if sample.memory_used_mb is not None]
    throughput = None if runtime_seconds <= 0 else round(successful_units / runtime_seconds, 6)
    return GPURunSummary(
        gpu_provider_label=device.gpu_provider_label,
        gpu_model=device.gpu_model,
        gpu_count=device.gpu_count,
        cuda_available=device.cuda_available,
        driver_version=device.driver_version,
        workload_id=workload_id,
        workload_size=workload_size,
        workload_unit_type=workload_unit_type,
        started_at_utc=started_at_utc,
        ended_at_utc=ended_at_utc,
        runtime_seconds=runtime_seconds,
        throughput_units_per_second=throughput,
        gpu_utilization_average=_average(utilization_values),
        gpu_utilization_max=_maximum(utilization_values),
        gpu_memory_average_mb=_average(memory_values),
        gpu_memory_max_mb=_maximum(memory_values),
        successful_units=successful_units,
        failed_units=failed_units,
        latency_average_ms=_average(selected_latency),
        latency_min_ms=_minimum(selected_latency),
        latency_max_ms=_maximum(selected_latency),
        estimated_gpu_cost=estimated_gpu_cost,
        claim_level=str(GPUClaimLevel(claim_level)),
        warnings=list(warnings),
    )


def _average(values: list[float]) -> float | None:
    return None if not values else round(float(mean(values)), 6)


def _minimum(values: list[float]) -> float | None:
    return None if not values else round(float(min(values)), 6)


def _maximum(values: list[float]) -> float | None:
    return None if not values else round(float(max(values)), 6)
