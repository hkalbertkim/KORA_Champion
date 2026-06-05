"""Run record creation and JSON serialization for KORA Core evidence."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any, Mapping
from uuid import uuid4

from kora_core.evidence import (
    ClaimLevel,
    CostMetrics,
    CpuMetrics,
    EvidenceStatus,
    GpuMetrics,
    LatencyMetrics,
    ProviderMetrics,
    QualityMetrics,
    RoutingMetrics,
    RunType,
    WorkloadMetadata,
    compute_routing_percentages,
    compute_savings,
    synthetic_claim_warnings,
    to_plain_dict,
)
from kora_core.provider_adapter import ProviderAdapterResult


REQUIRED_TOP_LEVEL_FIELDS = {
    "run_id",
    "run_name",
    "run_type",
    "timestamp_utc",
    "git_commit",
    "environment_label",
    "workload",
    "routing",
    "provider",
    "latency",
    "gpu",
    "cpu",
    "cost",
    "quality",
    "evidence_status",
}


@dataclass(frozen=True)
class RunRecord:
    """Serializable evidence record for one KORA Core run."""

    run_id: str
    run_name: str
    run_type: RunType
    timestamp_utc: str
    git_commit: str | None
    environment_label: str
    workload: WorkloadMetadata
    routing: RoutingMetrics
    provider: ProviderMetrics
    latency: LatencyMetrics
    gpu: GpuMetrics
    cpu: CpuMetrics
    cost: CostMetrics
    quality: QualityMetrics
    evidence_status: EvidenceStatus
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return to_plain_dict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "RunRecord":
        validate_run_record_dict(payload)
        return cls(
            run_id=str(payload["run_id"]),
            run_name=str(payload["run_name"]),
            run_type=RunType(str(payload["run_type"])),
            timestamp_utc=str(payload["timestamp_utc"]),
            git_commit=payload.get("git_commit"),
            environment_label=str(payload["environment_label"]),
            workload=WorkloadMetadata(**payload["workload"]),
            routing=RoutingMetrics(**payload["routing"]),
            provider=ProviderMetrics(**payload["provider"]),
            latency=LatencyMetrics(**payload["latency"]),
            gpu=GpuMetrics(**payload["gpu"]),
            cpu=CpuMetrics(**payload["cpu"]),
            cost=CostMetrics(**payload["cost"]),
            quality=QualityMetrics(**payload["quality"]),
            evidence_status=EvidenceStatus(
                **{
                    **payload["evidence_status"],
                    "claim_level": ClaimLevel(str(payload["evidence_status"]["claim_level"])),
                }
            ),
            notes=list(payload.get("notes", [])),
        )

    @classmethod
    def from_json(cls, text: str) -> "RunRecord":
        payload = json.loads(text)
        if not isinstance(payload, dict):
            raise ValueError("run record JSON must be an object")
        return cls.from_dict(payload)


def validate_run_record_dict(payload: Mapping[str, Any]) -> None:
    """Validate required top-level fields for a run record dict."""

    missing = sorted(REQUIRED_TOP_LEVEL_FIELDS - set(payload))
    if missing:
        raise ValueError(f"run record missing required fields: {', '.join(missing)}")
    if not isinstance(payload["workload"], Mapping):
        raise ValueError("run record workload must be an object")
    if not isinstance(payload["routing"], Mapping):
        raise ValueError("run record routing must be an object")
    if not isinstance(payload["evidence_status"], Mapping):
        raise ValueError("run record evidence_status must be an object")


def write_run_record(record: RunRecord, path: str | Path) -> Path:
    """Write a run record as JSON and return the output path."""

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(record.to_json(), encoding="utf-8")
    return output_path


def read_run_record(path: str | Path) -> RunRecord:
    """Load a run record JSON file."""

    return RunRecord.from_json(Path(path).read_text(encoding="utf-8"))


def workload_hash_from_requests(requests: list[Mapping[str, Any]]) -> str:
    serialized = json.dumps(requests, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def create_run_record_from_harness(
    harness_output: Mapping[str, Any],
    *,
    requests: list[Mapping[str, Any]],
    run_name: str,
    run_type: RunType = RunType.SYNTHETIC,
    git_commit: str | None = None,
    environment_label: str = "local",
    workload_id: str = "sample_requests",
    workload_name: str = "Synthetic sample requests",
    workload_source: str = "tests/fixtures/sample_requests.json",
    baseline_estimated_cost: float | None = None,
    notes: list[str] | None = None,
) -> RunRecord:
    """Create a run record from the offline harness output."""

    records = list(harness_output.get("records", []))
    telemetry = dict(harness_output.get("telemetry", {}))
    target_counts = dict(telemetry.get("target_counts", {}))
    total_requests = int(telemetry.get("total_requests", len(records)) or 0)
    estimated_total_cost = _optional_float(telemetry.get("estimated_cost"))
    savings, savings_percentage = compute_savings(
        baseline_estimated_cost=baseline_estimated_cost,
        estimated_total_cost=estimated_total_cost,
    )
    latencies = [
        float(record.get("metrics", {}).get("latency_ms"))
        for record in records
        if record.get("metrics", {}).get("latency_ms") is not None
    ]
    provider_calls = int(harness_output.get("metrics", {}).get("provider_calls", 0) or 0)
    input_tokens = _optional_int(telemetry.get("total_input_tokens"))
    output_tokens = _optional_int(telemetry.get("total_output_tokens"))
    total_tokens = None if input_tokens is None or output_tokens is None else input_tokens + output_tokens
    claim_level = _claim_level_for(run_type)
    is_synthetic = run_type == RunType.SYNTHETIC

    return RunRecord(
        run_id=f"{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}-{uuid4().hex[:8]}",
        run_name=run_name,
        run_type=run_type,
        timestamp_utc=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        git_commit=git_commit,
        environment_label=environment_label,
        notes=list(notes or []),
        workload=WorkloadMetadata(
            workload_id=workload_id,
            workload_name=workload_name,
            workload_size=len(requests),
            workload_source=workload_source,
            workload_hash=workload_hash_from_requests(requests),
        ),
        routing=RoutingMetrics(
            total_requests=total_requests,
            deterministic_count=int(target_counts.get("deterministic", 0)),
            cache_count=int(target_counts.get("cache", 0)),
            cpu_count=int(target_counts.get("cpu", 0)),
            local_gpu_count=int(target_counts.get("local_gpu", 0)),
            provider_api_count=int(target_counts.get("provider_api", 0)),
            fallback_count=provider_calls,
            error_count=0,
            routing_percentages=compute_routing_percentages(target_counts, total_requests),
        ),
        provider=ProviderMetrics(
            provider_calls=provider_calls,
            avoided_provider_calls=int(telemetry.get("avoided_provider_calls", 0) or 0),
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            estimated_provider_cost=None,
            actual_provider_cost=None,
            provider_breakdown={},
        ),
        latency=_latency_metrics(latencies),
        gpu=GpuMetrics(),
        cpu=CpuMetrics(cpu_offload_count=int(target_counts.get("cpu", 0))),
        cost=CostMetrics(
            estimated_total_cost=estimated_total_cost,
            actual_total_cost=None,
            baseline_estimated_cost=baseline_estimated_cost,
            savings_estimated=savings,
            savings_percentage_estimated=savings_percentage,
        ),
        quality=QualityMetrics(
            deterministic_mismatch_count=0,
            validation_pass_count=total_requests,
            validation_fail_count=0,
            quality_notes=["Synthetic fixture validation only."],
        ),
        evidence_status=EvidenceStatus(
            is_synthetic=is_synthetic,
            has_real_provider_data=run_type in {RunType.PROVIDER_LIVE, RunType.HYBRID_LIVE},
            has_real_gpu_data=run_type in {RunType.GPU_LIVE, RunType.HYBRID_LIVE},
            claim_level=claim_level,
            claim_warnings=synthetic_claim_warnings() if is_synthetic else [],
        ),
    )


def provider_metrics_from_adapter_results(results: list[ProviderAdapterResult]) -> ProviderMetrics:
    """Aggregate provider dry-run adapter results into evidence metrics."""

    input_tokens = sum(result.usage.input_tokens for result in results)
    output_tokens = sum(result.usage.output_tokens for result in results)
    estimated_cost = round(sum(result.cost.estimated_provider_cost for result in results), 8)
    provider_breakdown: dict[str, Any] = {}
    for result in results:
        provider = result.response.provider_name
        item = provider_breakdown.setdefault(
            provider,
            {
                "provider_calls": 0,
                "input_tokens": 0,
                "output_tokens": 0,
                "total_tokens": 0,
                "estimated_provider_cost": 0.0,
                "actual_provider_cost": None,
            },
        )
        item["provider_calls"] += result.provider_calls
        item["input_tokens"] += result.usage.input_tokens
        item["output_tokens"] += result.usage.output_tokens
        item["total_tokens"] += result.usage.total_tokens
        item["estimated_provider_cost"] = round(
            item["estimated_provider_cost"] + result.cost.estimated_provider_cost,
            8,
        )
    return ProviderMetrics(
        provider_calls=sum(result.provider_calls for result in results),
        avoided_provider_calls=0,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=input_tokens + output_tokens,
        estimated_provider_cost=estimated_cost,
        actual_provider_cost=None,
        provider_breakdown=provider_breakdown,
    )


def _claim_level_for(run_type: RunType) -> ClaimLevel:
    if run_type == RunType.SYNTHETIC:
        return ClaimLevel.SYNTHETIC_ONLY
    if run_type in {RunType.PROVIDER_DRY_RUN, RunType.GPU_DRY_RUN}:
        return ClaimLevel.DRY_RUN
    if run_type == RunType.PROVIDER_LIVE:
        return ClaimLevel.MEASURED_PROVIDER
    if run_type == RunType.GPU_LIVE:
        return ClaimLevel.MEASURED_GPU
    return ClaimLevel.MEASURED_HYBRID


def _latency_metrics(latencies: list[float]) -> LatencyMetrics:
    if not latencies:
        return LatencyMetrics()
    sorted_values = sorted(latencies)
    return LatencyMetrics(
        p50_ms=round(_percentile(sorted_values, 0.50), 6),
        p95_ms=round(_percentile(sorted_values, 0.95), 6),
        p99_ms=round(_percentile(sorted_values, 0.99), 6),
        average_ms=round(mean(sorted_values), 6),
        min_ms=round(min(sorted_values), 6),
        max_ms=round(max(sorted_values), 6),
    )


def _percentile(sorted_values: list[float], percentile: float) -> float:
    if len(sorted_values) == 1:
        return sorted_values[0]
    index = (len(sorted_values) - 1) * percentile
    lower = int(index)
    upper = min(lower + 1, len(sorted_values) - 1)
    weight = index - lower
    return sorted_values[lower] * (1.0 - weight) + sorted_values[upper] * weight


def _optional_float(value: Any) -> float | None:
    return None if value is None else float(value)


def _optional_int(value: Any) -> int | None:
    return None if value is None else int(value)
