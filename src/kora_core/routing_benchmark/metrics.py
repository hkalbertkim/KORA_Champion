"""Routing benchmark scoring and dry-run metric placeholders."""

from __future__ import annotations

from collections import Counter
from typing import Any, Mapping

from kora_core.routing_benchmark.schema import RoutePath

FALLBACK_COUNTS_TEMPLATE = {
    "safety_fallback": {
        "uncertain_route": 0,
        "cache_equivalence_uncertain": 0,
        "cpu_gpu_boundary_uncertain": 0,
        "provider_gpu_boundary_uncertain": 0,
    },
    "failure_fallback": {
        "execution_error": 0,
        "router_exception": 0,
        "missing_metadata": 0,
        "invalid_request_schema": 0,
    },
}


def empty_quality_validation() -> dict[str, Any]:
    return {
        "enabled": False,
        "quality_check_required_count": 0,
        "quality_checked_count": 0,
        "quality_pass_count": 0,
        "quality_fail_count": 0,
        "quality_validation_method": "not_yet_enabled",
    }


def empty_provider_validation(provider_routed_count: int) -> dict[str, Any]:
    return {
        "mode": "dry_run_only",
        "provider_routed_count": provider_routed_count,
        "live_sample_enabled": False,
        "live_sample_count": 0,
        "latency_p50_ms": None,
        "latency_p95_ms": None,
        "input_tokens_total": None,
        "output_tokens_total": None,
        "estimated_cost_per_1k": None,
    }


def provider_evidence_basis() -> dict[str, Any]:
    return {
        "existing_live_provider_sample_count": 1,
        "claim_level": "measured_provider_partial",
        "used_for_cost_claim": False,
    }


def _fallback_counts() -> dict[str, dict[str, int]]:
    return {category: dict(reasons) for category, reasons in FALLBACK_COUNTS_TEMPLATE.items()}


def _route_distribution(route_counts: Counter[str], total: int, error_count: int) -> dict[str, dict[str, float | int]]:
    distribution: dict[str, dict[str, float | int]] = {}
    for route in RoutePath:
        count = route_counts.get(route.value, 0)
        distribution[route.value] = {"count": count, "percentage": round((count / total) * 100.0, 6)}
    distribution["error"] = {"count": error_count, "percentage": round((error_count / total) * 100.0, 6)}
    return distribution


def score_decisions(
    requests: list[Mapping[str, Any]],
    decisions: list[Mapping[str, Any]],
    *,
    baseline_decisions: list[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    if len(requests) != len(decisions):
        raise ValueError("requests and decisions must have the same length")
    route_counts = Counter(str(decision["route"]) for decision in decisions)
    exact = acceptable = unsafe = cache_expected = cache_correct = 0
    gpu_false_positive = gpu_false_negative = unsafe_cpu = error_count = 0
    fallback_counts = _fallback_counts()
    quality_required_count = 0
    gpu_compute_weight = 0.0
    baseline_gpu_compute_weight = 0.0
    avoided_gpu_calls = 0
    avoided_gpu_compute_units = 0.0

    for index, (request, decision) in enumerate(zip(requests, decisions, strict=True)):
        route = str(decision["route"])
        labels = request["oracle_labels"]
        expected = labels["expected_route"]
        acceptable_routes = set(labels["acceptable_routes"])
        disallowed_routes = set(labels["disallowed_routes"])
        compute_weight = float(request["compute_weight"]["value"])
        if request["validation"]["quality_check_required"]:
            quality_required_count += 1
        if route == expected:
            exact += 1
        if route in acceptable_routes:
            acceptable += 1
        if route in disallowed_routes:
            unsafe += 1
        if expected == RoutePath.CACHE.value:
            cache_expected += 1
            if route == RoutePath.CACHE.value:
                cache_correct += 1
        if route == RoutePath.LOCAL_GPU.value:
            gpu_compute_weight += compute_weight
        if route == RoutePath.LOCAL_GPU.value and RoutePath.LOCAL_GPU.value not in acceptable_routes:
            gpu_false_positive += 1
        if route != RoutePath.LOCAL_GPU.value and expected == RoutePath.LOCAL_GPU.value:
            gpu_false_negative += 1
        if route == RoutePath.CPU.value and RoutePath.CPU.value in disallowed_routes:
            unsafe_cpu += 1
        if route == RoutePath.FALLBACK.value:
            category = str(decision.get("fallback_category") or "safety_fallback")
            reason = str(decision.get("fallback_reason") or "uncertain_route")
            fallback_counts.setdefault(category, {})
            fallback_counts[category][reason] = fallback_counts[category].get(reason, 0) + 1
        if str(decision.get("reason", "")).endswith("exception"):
            error_count += 1
        if baseline_decisions is not None:
            baseline_route = str(baseline_decisions[index]["route"])
            if baseline_route == RoutePath.LOCAL_GPU.value:
                baseline_gpu_compute_weight += compute_weight
                if route != RoutePath.LOCAL_GPU.value:
                    avoided_gpu_calls += 1
                    avoided_gpu_compute_units += compute_weight

    total = len(requests)
    if baseline_decisions is None:
        baseline_gpu_compute_weight = gpu_compute_weight
    reduction = 0.0
    if baseline_gpu_compute_weight > 0:
        reduction = avoided_gpu_compute_units / baseline_gpu_compute_weight
    safety_fallback_total = sum(fallback_counts["safety_fallback"].values())
    failure_fallback_total = sum(fallback_counts["failure_fallback"].values())
    fallback_total = safety_fallback_total + failure_fallback_total
    acceptable_rate = acceptable / total
    unsafe_rate = unsafe / total
    normalized_reduction = max(0.0, min(1.0, reduction))
    gpu_routed_calls = route_counts.get(RoutePath.LOCAL_GPU.value, 0)
    router_gpu_compute_weight = round(gpu_compute_weight, 6)
    baseline_gpu_runtime_seconds_estimated = round(baseline_gpu_compute_weight / 100.0, 6)
    router_gpu_runtime_seconds_estimated = round(gpu_compute_weight / 100.0, 6)
    return {
        "route_counts": dict(sorted(route_counts.items())),
        "route_distribution": _route_distribution(route_counts, total, error_count),
        "exact_route_accuracy": exact / total,
        "acceptable_route_rate": acceptable_rate,
        "unsafe_misroute_rate": unsafe_rate,
        "gpu_false_positive_count": gpu_false_positive,
        "gpu_false_negative_count": gpu_false_negative,
        "unsafe_cpu_route_count": unsafe_cpu,
        "cache_hit_correctness_rate": cache_correct / cache_expected if cache_expected else 1.0,
        "fallback_rate": fallback_total / total,
        "safety_fallback_rate": safety_fallback_total / total,
        "failure_fallback_rate": failure_fallback_total / total,
        "error_rate": error_count / total,
        "error_count": error_count,
        "gpu_routed_calls": gpu_routed_calls,
        "gpu_compute_weight": router_gpu_compute_weight,
        "avoided_gpu_calls": avoided_gpu_calls,
        "avoided_gpu_compute_units": round(avoided_gpu_compute_units, 6),
        "compute_weighted_gpu_reduction_percentage": round(reduction * 100.0, 6),
        "baseline_gpu_compute_weight": round(baseline_gpu_compute_weight, 6),
        "router_gpu_compute_weight": router_gpu_compute_weight,
        "kora_gpu_compute_weight": router_gpu_compute_weight,
        "baseline_gpu_runtime_seconds_estimated": baseline_gpu_runtime_seconds_estimated,
        "router_gpu_runtime_seconds_estimated": router_gpu_runtime_seconds_estimated,
        "kora_gpu_runtime_seconds_measured": None,
        "avoided_gpu_seconds_estimated": round(avoided_gpu_compute_units / 100.0, 6),
        "fallback_counts": fallback_counts,
        "quality_validation": empty_quality_validation(),
        "quality_check_required_count_observed": quality_required_count,
        "provider_validation": empty_provider_validation(route_counts.get(RoutePath.PROVIDER.value, 0)),
        "provider_evidence_basis": provider_evidence_basis(),
        "selectivity_score_experimental": {
            "value": round(acceptable_rate * (1 - unsafe_rate) * normalized_reduction, 6),
            "label": "experimental/dashboard-only",
            "official_claim_basis": False,
        },
    }
