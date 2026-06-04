"""Partial live-provider comparison helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from kora_core.comparison import BaselinePolicy, compare_synthetic_baseline
from kora_core.live_evidence import NormalizedLiveMeasurement


PARTIAL_LIVE_WARNINGS = [
    "partial_live_provider_only",
    "not_full_workload_live_comparison",
    "not_cost_reduction_evidence",
    "not_token_reduction_evidence",
    "not_gpu_evidence",
    "not_infrastructure_reduction_evidence",
]


@dataclass(frozen=True)
class PartialLiveProviderComparison:
    comparison_type: str
    workload_size: int
    synthetic_baseline_provider_calls: int
    kora_synthetic_provider_calls: int
    measured_provider_calls: int
    measured_successful_provider_calls: int
    measured_failed_provider_calls: int
    measured_tokens: int
    measured_latency_ms: float | None
    measured_estimated_provider_cost: float | None
    comparison_claim_level: str
    claim_warnings: list[str] = field(default_factory=list)
    normalized_live_measurement: dict[str, Any] = field(default_factory=dict)
    synthetic_reference: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "comparison_type": self.comparison_type,
            "workload_size": self.workload_size,
            "synthetic_baseline_provider_calls": self.synthetic_baseline_provider_calls,
            "kora_synthetic_provider_calls": self.kora_synthetic_provider_calls,
            "measured_provider_calls": self.measured_provider_calls,
            "measured_successful_provider_calls": self.measured_successful_provider_calls,
            "measured_failed_provider_calls": self.measured_failed_provider_calls,
            "measured_tokens": self.measured_tokens,
            "measured_latency_ms": self.measured_latency_ms,
            "measured_estimated_provider_cost": self.measured_estimated_provider_cost,
            "comparison_claim_level": self.comparison_claim_level,
            "claim_warnings": list(self.claim_warnings),
            "normalized_live_measurement": dict(self.normalized_live_measurement),
            "synthetic_reference": dict(self.synthetic_reference),
            "claims_cost_reduction": False,
            "claims_token_reduction": False,
            "claims_latency_reduction": False,
            "claims_gpu_reduction": False,
            "claims_infrastructure_reduction": False,
        }


def build_partial_live_provider_comparison(
    live_measurement: NormalizedLiveMeasurement,
    requests: list[Mapping[str, Any]],
    *,
    workload_id: str = "sample_requests_v0_1",
) -> PartialLiveProviderComparison:
    synthetic = compare_synthetic_baseline(
        requests,
        workload_id=workload_id,
        baseline_policy=BaselinePolicy.ALL_PROVIDER_API,
        include_placeholder_costs=True,
    )
    synthetic_reference = {
        "workload_id": workload_id,
        "baseline_policy": synthetic.baseline_policy,
        "kora_policy": synthetic.kora_policy,
        "baseline_provider_calls": synthetic.baseline_provider_calls,
        "kora_provider_calls": synthetic.kora_provider_calls,
        "synthetic_only_provider_call_reduction_percentage": synthetic.estimated_provider_call_reduction_percentage,
        "synthetic_placeholder_baseline_cost": synthetic.baseline_estimated_cost,
        "synthetic_placeholder_kora_cost": synthetic.kora_estimated_cost,
        "synthetic_warning": "synthetic fields are not measured live savings evidence",
    }
    return PartialLiveProviderComparison(
        comparison_type="partial_live_provider",
        workload_size=len(requests),
        synthetic_baseline_provider_calls=synthetic.baseline_provider_calls,
        kora_synthetic_provider_calls=synthetic.kora_provider_calls,
        measured_provider_calls=live_measurement.provider_calls,
        measured_successful_provider_calls=live_measurement.successful_provider_calls,
        measured_failed_provider_calls=live_measurement.failed_provider_calls,
        measured_tokens=live_measurement.total_tokens,
        measured_latency_ms=live_measurement.measured_latency_ms,
        measured_estimated_provider_cost=live_measurement.estimated_provider_cost,
        comparison_claim_level="measured_provider_partial",
        claim_warnings=list(PARTIAL_LIVE_WARNINGS),
        normalized_live_measurement=live_measurement.to_dict(),
        synthetic_reference=synthetic_reference,
    )
