"""KORA router adapter boundary for routing benchmark comparisons."""

from __future__ import annotations

from typing import Any, Mapping

from kora_core.routing_benchmark.routers import RouterDecision, fallback_decision
from kora_core.routing_benchmark.schema import RoutePath

KORA_ROUTER_ADAPTER_DECLARATION = {
    "adapter_type": "benchmark_prototype",
    "benchmark_specific_logic": True,
    "claim_level": "prototype_routing_evidence",
    "oracle_labels_used": False,
}


def kora_router_adapter(router_input: Mapping[str, Any]) -> RouterDecision:
    metadata = dict(router_input.get("router_visible_metadata", {}))
    observable = dict(metadata.get("observable", {}))
    inferred = dict(metadata.get("inferred", {}))
    workload_class = str(router_input.get("workload_class", ""))
    input_size = int(observable.get("input_size") or 0)
    batch_size = int(observable.get("batch_size") or 0)
    modality = observable.get("request_modality")
    complexity = inferred.get("estimated_complexity")

    if input_size <= 0 or batch_size <= 0 or complexity == "unknown":
        return fallback_decision("missing_metadata")
    if workload_class.startswith("deterministic_") or modality == "config":
        return RouterDecision(route=RoutePath.DETERMINISTIC.value, reason="deterministic_metadata")
    if bool(observable.get("cache_key_available")):
        if workload_class in {"cache_exact_repeat", "repeated_user_prompt_exact", "near_duplicate_equivalent"}:
            return RouterDecision(route=RoutePath.CACHE.value, reason="cache_equivalence_visible")
        return fallback_decision("cache_equivalence_uncertain", category="safety_fallback")
    if workload_class in {"ambiguous_provider_or_gpu_request"}:
        return fallback_decision("provider_gpu_boundary_uncertain", category="safety_fallback")
    if modality == "language":
        return RouterDecision(route=RoutePath.PROVIDER.value, reason="language_generation")
    if modality == "tensor" and (batch_size >= 8 or input_size >= 4096):
        return RouterDecision(route=RoutePath.LOCAL_GPU.value, reason="tensor_batch_selectivity")
    if modality == "embedding":
        if input_size >= 8192 or batch_size >= 16:
            return RouterDecision(route=RoutePath.LOCAL_GPU.value, reason="embedding_gpu_selectivity")
        return RouterDecision(route=RoutePath.CPU.value, reason="small_embedding_cpu_selectivity")
    if complexity in {"high", "very_high"} and input_size >= 16384:
        return fallback_decision("cpu_gpu_boundary_uncertain", category="safety_fallback")
    return RouterDecision(route=RoutePath.CPU.value, reason="cpu_selectivity")
