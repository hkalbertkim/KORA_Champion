"""Evidence schema helpers for KORA Core measurement records."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Mapping

from kora_core.compat import StrEnum

class RunType(StrEnum):
    """Allowed run types for evidence records."""

    SYNTHETIC = "synthetic"
    PROVIDER_DRY_RUN = "provider_dry_run"
    PROVIDER_LIVE = "provider_live"
    GPU_DRY_RUN = "gpu_dry_run"
    GPU_LIVE = "gpu_live"
    HYBRID_LIVE = "hybrid_live"


class ClaimLevel(StrEnum):
    """Evidence claim level supported by a run record."""

    SYNTHETIC_ONLY = "synthetic_only"
    DRY_RUN = "dry_run"
    MEASURED_PROVIDER = "measured_provider"
    MEASURED_GPU = "measured_gpu"
    MEASURED_HYBRID = "measured_hybrid"


@dataclass(frozen=True)
class WorkloadMetadata:
    workload_id: str
    workload_name: str
    workload_size: int
    workload_source: str
    workload_hash: str


@dataclass(frozen=True)
class RoutingMetrics:
    total_requests: int
    deterministic_count: int = 0
    cache_count: int = 0
    cpu_count: int = 0
    local_gpu_count: int = 0
    provider_api_count: int = 0
    fallback_count: int = 0
    error_count: int = 0
    routing_percentages: dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class ProviderMetrics:
    provider_calls: int = 0
    avoided_provider_calls: int = 0
    input_tokens: int | None = None
    output_tokens: int | None = None
    total_tokens: int | None = None
    estimated_provider_cost: float | None = None
    actual_provider_cost: float | None = None
    provider_breakdown: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class LatencyMetrics:
    p50_ms: float | None = None
    p95_ms: float | None = None
    p99_ms: float | None = None
    average_ms: float | None = None
    min_ms: float | None = None
    max_ms: float | None = None


@dataclass(frozen=True)
class GpuMetrics:
    gpu_model: str | None = None
    gpu_count: int | None = None
    gpu_runtime_seconds: float | None = None
    gpu_utilization_average: float | None = None
    gpu_memory_average: float | None = None
    estimated_gpu_cost: float | None = None
    avoided_gpu_runtime_seconds: float | None = None


@dataclass(frozen=True)
class CpuMetrics:
    cpu_runtime_seconds: float | None = None
    cpu_utilization_average: float | None = None
    cpu_offload_count: int = 0


@dataclass(frozen=True)
class CostMetrics:
    estimated_total_cost: float | None = None
    actual_total_cost: float | None = None
    baseline_estimated_cost: float | None = None
    savings_estimated: float | None = None
    savings_percentage_estimated: float | None = None


@dataclass(frozen=True)
class QualityMetrics:
    deterministic_mismatch_count: int = 0
    validation_pass_count: int = 0
    validation_fail_count: int = 0
    quality_notes: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class EvidenceStatus:
    is_synthetic: bool
    has_real_provider_data: bool
    has_real_gpu_data: bool
    claim_level: ClaimLevel
    claim_warnings: list[str] = field(default_factory=list)


def compute_routing_percentages(counts: Mapping[str, int], total_requests: int) -> dict[str, float]:
    """Compute route percentages from route counts."""

    if total_requests <= 0:
        return {key: 0.0 for key in sorted(counts)}
    return {
        key: round((max(0, int(value)) / total_requests) * 100.0, 4)
        for key, value in sorted(counts.items())
    }


def compute_savings(
    *,
    baseline_estimated_cost: float | None,
    estimated_total_cost: float | None,
) -> tuple[float | None, float | None]:
    """Compute estimated savings only when both costs are available."""

    if baseline_estimated_cost is None or estimated_total_cost is None:
        return None, None
    baseline = float(baseline_estimated_cost)
    actual = float(estimated_total_cost)
    savings = baseline - actual
    percentage = None if baseline <= 0 else (savings / baseline) * 100.0
    return round(savings, 8), None if percentage is None else round(percentage, 4)


def synthetic_claim_warnings() -> list[str]:
    """Return standard warnings for synthetic-only evidence."""

    return [
        "Synthetic-only evidence validates schema and local routing behavior.",
        "Synthetic-only evidence does not prove real provider cost reduction.",
        "Synthetic-only evidence does not prove real GPU workload reduction.",
        "Synthetic-only evidence does not prove production latency reduction.",
    ]


def provider_dry_run_warnings() -> list[str]:
    """Return standard warnings for provider dry-run evidence."""

    return [
        "Provider dry-run evidence validates adapter shape and accounting fields only.",
        "Provider dry-run evidence does not include real provider API responses.",
        "Provider dry-run evidence does not prove real token, latency, or cost reduction.",
        "Provider dry-run evidence must not be reported as measured provider evidence.",
    ]


def to_plain_dict(value: Any) -> Any:
    """Convert nested dataclasses and enums into JSON-compatible values."""

    if isinstance(value, StrEnum):
        return str(value)
    if hasattr(value, "__dataclass_fields__"):
        return {key: to_plain_dict(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): to_plain_dict(item) for key, item in value.items()}
    if isinstance(value, list):
        return [to_plain_dict(item) for item in value]
    return value
