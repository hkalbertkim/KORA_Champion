"""Run dry-run routing benchmark comparisons over a shared workload."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any, Mapping

from kora_core.routing_benchmark.kora_router_adapter import KORA_ROUTER_ADAPTER_DECLARATION, kora_router_adapter
from kora_core.routing_benchmark.metrics import score_decisions
from kora_core.routing_benchmark.routers import ROUTER_POLICIES, RouterDecision, router_input_from_request


def _safe_route(policy_name: str, request: Mapping[str, Any]) -> RouterDecision:
    router_input = router_input_from_request(request)
    try:
        if policy_name == "kora_router_adapter":
            return kora_router_adapter(router_input)
        return ROUTER_POLICIES[policy_name](router_input)
    except Exception:
        return RouterDecision(
            route="fallback",
            reason="router_exception",
            fallback_category="failure_fallback",
            fallback_reason="router_exception",
        )


def compare_routing_policies(requests: list[Mapping[str, Any]]) -> dict[str, Any]:
    policy_names = ["all_gpu", "static_heuristic_router", "provider_first_with_gpu_fallback", "kora_router_adapter"]
    decisions_by_policy: dict[str, list[dict[str, Any]]] = {}
    for policy_name in policy_names:
        decisions_by_policy[policy_name] = [_safe_route(policy_name, request).to_dict() for request in requests]
    baseline = decisions_by_policy["all_gpu"]
    results = {
        policy_name: score_decisions(requests, decisions, baseline_decisions=baseline)
        for policy_name, decisions in decisions_by_policy.items()
    }
    return {
        "schema_version": "routing_benchmark_comparison_v0_1",
        "generated_at_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "mode": "dry_run_only",
        "h100_execution_performed": False,
        "live_provider_execution_performed": False,
        "workload_request_count": len(requests),
        "router_input_allowed_fields": [
            "request_id",
            "workload_profile",
            "workload_class",
            "router_visible_metadata.observable",
            "router_visible_metadata.inferred",
        ],
        "oracle_independence": {
            "oracle_generated_from_router_outputs": False,
            "routers_read_oracle_labels": False,
        },
        "kora_router_adapter_declaration": KORA_ROUTER_ADAPTER_DECLARATION,
        "router_results": results,
        "claim_boundaries": [
            "framework_schema_dry_run_infrastructure_only",
            "not_production_cost_saving_evidence",
            "not_real_gpu_reduction_evidence",
            "not_live_provider_reduction_evidence",
        ],
    }
