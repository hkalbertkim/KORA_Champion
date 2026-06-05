"""Baseline router policies for routing benchmark comparisons."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Mapping

from kora_core.routing_benchmark.schema import RoutePath

ALLOWED_ROUTER_INPUT_KEYS = {
    "request_id",
    "workload_profile",
    "workload_class",
    "router_visible_metadata",
}


@dataclass(frozen=True)
class RouterDecision:
    route: str
    reason: str
    fallback_category: str | None = None
    fallback_reason: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "route": self.route,
            "reason": self.reason,
            "fallback_category": self.fallback_category,
            "fallback_reason": self.fallback_reason,
            "metadata": dict(self.metadata),
        }


RouterPolicy = Callable[[Mapping[str, Any]], RouterDecision]


def router_input_from_request(request: Mapping[str, Any]) -> dict[str, Any]:
    return {key: request[key] for key in ALLOWED_ROUTER_INPUT_KEYS}


def _sections(router_input: Mapping[str, Any]) -> tuple[str, dict[str, Any], dict[str, Any]]:
    workload_class = str(router_input.get("workload_class", ""))
    metadata = dict(router_input.get("router_visible_metadata", {}))
    observable = dict(metadata.get("observable", {}))
    inferred = dict(metadata.get("inferred", {}))
    return workload_class, observable, inferred


def _missing_metadata(observable: Mapping[str, Any], inferred: Mapping[str, Any]) -> bool:
    return (
        not observable
        or not inferred
        or int(observable.get("input_size") or 0) <= 0
        or int(observable.get("batch_size") or 0) <= 0
        or inferred.get("estimated_complexity") == "unknown"
    )


def fallback_decision(reason: str, *, category: str = "failure_fallback") -> RouterDecision:
    return RouterDecision(
        route=RoutePath.FALLBACK.value,
        reason=reason,
        fallback_category=category,
        fallback_reason=reason,
    )


def all_gpu(router_input: Mapping[str, Any]) -> RouterDecision:
    workload_class, observable, inferred = _sections(router_input)
    if _missing_metadata(observable, inferred):
        return fallback_decision("invalid_request_schema")
    if workload_class in {"deterministic_config_query", "deterministic_config_lookup", "deterministic_model_catalog_query"}:
        return RouterDecision(route=RoutePath.DETERMINISTIC.value, reason="deterministic_metadata")
    if bool(observable.get("cache_key_available")):
        return RouterDecision(route=RoutePath.CACHE.value, reason="cache_key_available")
    return RouterDecision(route=RoutePath.LOCAL_GPU.value, reason="all_gpu_reference")


def static_heuristic_router(router_input: Mapping[str, Any]) -> RouterDecision:
    workload_class, observable, inferred = _sections(router_input)
    if _missing_metadata(observable, inferred):
        return fallback_decision("missing_metadata")
    input_size = int(observable.get("input_size", 0))
    batch_size = int(observable.get("batch_size", 1))
    modality = observable.get("request_modality")
    complexity = inferred.get("estimated_complexity")
    if workload_class.startswith("deterministic_") or modality == "config":
        return RouterDecision(route=RoutePath.DETERMINISTIC.value, reason="deterministic_metadata")
    if bool(observable.get("cache_key_available")) and workload_class in {"cache_exact_repeat", "repeated_user_prompt_exact"}:
        return RouterDecision(route=RoutePath.CACHE.value, reason="exact_cache_metadata")
    if modality == "language" and complexity in {"medium", "high", "very_high"}:
        return RouterDecision(route=RoutePath.PROVIDER.value, reason="language_model_metadata")
    if modality in {"embedding", "tensor"} and (batch_size >= 16 or input_size >= 8192):
        return RouterDecision(route=RoutePath.LOCAL_GPU.value, reason="batch_or_size_metadata")
    if workload_class == "ambiguous_provider_or_gpu_request":
        return fallback_decision("provider_gpu_boundary_uncertain", category="safety_fallback")
    return RouterDecision(route=RoutePath.CPU.value, reason="small_or_default_cpu_metadata")


def provider_first_with_gpu_fallback(router_input: Mapping[str, Any]) -> RouterDecision:
    workload_class, observable, inferred = _sections(router_input)
    if _missing_metadata(observable, inferred):
        return fallback_decision("missing_metadata")
    if workload_class.startswith("deterministic_") or observable.get("request_modality") == "config":
        return RouterDecision(route=RoutePath.DETERMINISTIC.value, reason="deterministic_metadata")
    if bool(observable.get("cache_key_available")) and workload_class in {"cache_exact_repeat", "repeated_user_prompt_exact"}:
        return RouterDecision(route=RoutePath.CACHE.value, reason="exact_cache_metadata")
    if workload_class in {"gpu_batch_embedding", "gpu_tensor_transform", "batch_tensor_operation", "image_like_compute"}:
        return RouterDecision(route=RoutePath.LOCAL_GPU.value, reason="explicit_gpu_required_class")
    if observable.get("request_modality") in {"language", "embedding", "mixed"}:
        return RouterDecision(route=RoutePath.PROVIDER.value, reason="provider_first_model_task")
    if inferred.get("estimated_complexity") == "low":
        return RouterDecision(route=RoutePath.CPU.value, reason="simple_non_model_transform")
    return RouterDecision(route=RoutePath.PROVIDER.value, reason="provider_first_default")


ROUTER_POLICIES: dict[str, RouterPolicy] = {
    "all_gpu": all_gpu,
    "static_heuristic_router": static_heuristic_router,
    "provider_first_with_gpu_fallback": provider_first_with_gpu_fallback,
}
