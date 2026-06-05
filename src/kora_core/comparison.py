"""Synthetic baseline-vs-KORA comparison helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from kora_core.compat import StrEnum
from kora_core.cost_model import estimate_request_cost, estimate_total_cost
from kora_core.evidence import ClaimLevel, synthetic_claim_warnings
from kora_core.execution_targets import ExecutionTarget
from kora_core.harness import run_request_harness


class BaselinePolicy(StrEnum):
    """Supported synthetic baseline policies."""

    ALL_PROVIDER_API = "all_provider_api"
    ALL_LOCAL_GPU = "all_local_gpu"
    CONFIGURABLE = "configurable"


@dataclass(frozen=True)
class SyntheticComparison:
    """Serializable comparison between a synthetic baseline and KORA routing."""

    workload_id: str
    workload_size: int
    baseline_policy: str
    kora_policy: str
    baseline_target_counts: dict[str, int]
    kora_target_counts: dict[str, int]
    baseline_provider_calls: int
    kora_provider_calls: int
    avoided_provider_calls: int
    estimated_provider_call_reduction_percentage: float | None
    baseline_estimated_cost: float | None
    kora_estimated_cost: float | None
    estimated_savings: float | None
    estimated_savings_percentage: float | None
    baseline_claim_level: ClaimLevel
    kora_claim_level: ClaimLevel
    comparison_claim_level: ClaimLevel
    warnings: list[str] = field(default_factory=list)
    is_synthetic: bool = True
    has_real_provider_data: bool = False
    has_real_gpu_data: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "workload_id": self.workload_id,
            "workload_size": self.workload_size,
            "baseline_policy": self.baseline_policy,
            "kora_policy": self.kora_policy,
            "baseline_target_counts": self.baseline_target_counts,
            "kora_target_counts": self.kora_target_counts,
            "baseline_provider_calls": self.baseline_provider_calls,
            "kora_provider_calls": self.kora_provider_calls,
            "avoided_provider_calls": self.avoided_provider_calls,
            "estimated_provider_call_reduction_percentage": self.estimated_provider_call_reduction_percentage,
            "baseline_estimated_cost": self.baseline_estimated_cost,
            "kora_estimated_cost": self.kora_estimated_cost,
            "estimated_savings": self.estimated_savings,
            "estimated_savings_percentage": self.estimated_savings_percentage,
            "baseline_claim_level": str(self.baseline_claim_level),
            "kora_claim_level": str(self.kora_claim_level),
            "comparison_claim_level": str(self.comparison_claim_level),
            "warnings": list(self.warnings),
            "is_synthetic": self.is_synthetic,
            "has_real_provider_data": self.has_real_provider_data,
            "has_real_gpu_data": self.has_real_gpu_data,
            "claim_level": str(self.comparison_claim_level),
            "claim_warnings": list(self.warnings),
        }


def baseline_target_for_policy(
    policy: BaselinePolicy | str,
    *,
    configurable_target: ExecutionTarget | str | None = None,
) -> ExecutionTarget:
    """Resolve a synthetic baseline policy to one execution target."""

    selected_policy = BaselinePolicy(policy)
    if selected_policy == BaselinePolicy.ALL_PROVIDER_API:
        return ExecutionTarget.PROVIDER_API
    if selected_policy == BaselinePolicy.ALL_LOCAL_GPU:
        return ExecutionTarget.LOCAL_GPU
    if configurable_target is None:
        raise ValueError("configurable baseline requires configurable_target")
    return ExecutionTarget(configurable_target)


def compare_synthetic_baseline(
    requests: list[Mapping[str, Any]],
    *,
    workload_id: str = "sample_requests_v0_1",
    baseline_policy: BaselinePolicy | str = BaselinePolicy.ALL_PROVIDER_API,
    configurable_target: ExecutionTarget | str | None = None,
    include_placeholder_costs: bool = True,
) -> SyntheticComparison:
    """Compare a synthetic all-target baseline against KORA routing."""

    baseline_target = baseline_target_for_policy(
        baseline_policy,
        configurable_target=configurable_target,
    )
    workload_size = len(requests)
    baseline_counts = {baseline_target.value: workload_size}
    harness_result = run_request_harness(requests)
    kora_counts = {
        str(target): int(count)
        for target, count in harness_result["telemetry"]["target_counts"].items()
    }
    baseline_provider_calls = workload_size if baseline_target == ExecutionTarget.PROVIDER_API else 0
    kora_provider_calls = int(harness_result["metrics"]["provider_calls"])
    avoided_provider_calls = baseline_provider_calls - kora_provider_calls
    reduction = (
        None
        if baseline_provider_calls <= 0
        else round((avoided_provider_calls / baseline_provider_calls) * 100.0, 4)
    )
    baseline_cost = (
        estimate_total_cost(baseline_counts)
        if include_placeholder_costs
        else None
    )
    kora_cost = (
        float(harness_result["telemetry"]["estimated_cost"])
        if include_placeholder_costs
        else None
    )
    savings, savings_percentage = _savings(baseline_cost, kora_cost)
    warnings = synthetic_claim_warnings() + [
        "Baseline-vs-KORA comparison is synthetic and uses placeholder costs only.",
        "Comparison output must not be used as real provider, GPU, or infrastructure savings evidence.",
    ]

    return SyntheticComparison(
        workload_id=workload_id,
        workload_size=workload_size,
        baseline_policy=str(BaselinePolicy(baseline_policy)),
        kora_policy="classifier_router_harness",
        baseline_target_counts=baseline_counts,
        kora_target_counts=kora_counts,
        baseline_provider_calls=baseline_provider_calls,
        kora_provider_calls=kora_provider_calls,
        avoided_provider_calls=avoided_provider_calls,
        estimated_provider_call_reduction_percentage=reduction,
        baseline_estimated_cost=baseline_cost,
        kora_estimated_cost=kora_cost,
        estimated_savings=savings,
        estimated_savings_percentage=savings_percentage,
        baseline_claim_level=ClaimLevel.SYNTHETIC_ONLY,
        kora_claim_level=ClaimLevel.SYNTHETIC_ONLY,
        comparison_claim_level=ClaimLevel.SYNTHETIC_ONLY,
        warnings=warnings,
    )


def _savings(
    baseline_estimated_cost: float | None,
    kora_estimated_cost: float | None,
) -> tuple[float | None, float | None]:
    if baseline_estimated_cost is None or kora_estimated_cost is None:
        return None, None
    savings = baseline_estimated_cost - kora_estimated_cost
    percentage = None if baseline_estimated_cost <= 0 else (savings / baseline_estimated_cost) * 100.0
    return round(savings, 8), None if percentage is None else round(percentage, 4)
