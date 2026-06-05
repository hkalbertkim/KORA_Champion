"""Independent oracle labels for routing benchmark workloads."""

from __future__ import annotations

from typing import Any

from kora_core.routing_benchmark.schema import OracleLabels, RoutePath


def labels_for_request(workload_class: str, metadata: dict[str, Any]) -> OracleLabels:
    observable = metadata["observable"]
    inferred = metadata["inferred"]
    cache_available = bool(observable.get("cache_key_available"))
    input_size = int(observable.get("input_size", 0))

    if workload_class in {"deterministic_config_query", "deterministic_config_lookup", "deterministic_model_catalog_query"}:
        return OracleLabels(
            expected_route=RoutePath.DETERMINISTIC.value,
            acceptable_routes=[RoutePath.DETERMINISTIC.value, RoutePath.CPU.value],
            disallowed_routes=[RoutePath.LOCAL_GPU.value, RoutePath.PROVIDER.value],
            oracle_reason="Deterministic lookup should not use model execution.",
        )
    if workload_class in {"cache_exact_repeat", "repeated_user_prompt_exact"} or (
        workload_class == "near_duplicate_equivalent" and cache_available
    ):
        return OracleLabels(
            expected_route=RoutePath.CACHE.value,
            acceptable_routes=[RoutePath.CACHE.value],
            disallowed_routes=[RoutePath.LOCAL_GPU.value, RoutePath.PROVIDER.value, RoutePath.CPU.value],
            oracle_reason="Exact reusable result should route to cache.",
        )
    if workload_class in {
        "small_cpu_transform",
        "small_text_transform_cpu",
        "local_file_metadata_parse",
        "near_duplicate_not_equivalent",
        "repeated_user_prompt_near_duplicate",
    }:
        return OracleLabels(
            expected_route=RoutePath.CPU.value,
            acceptable_routes=[RoutePath.CPU.value, RoutePath.PROVIDER.value],
            disallowed_routes=[RoutePath.LOCAL_GPU.value, RoutePath.CACHE.value],
            oracle_reason="Small non-model or uncertain reuse work should avoid GPU execution.",
        )
    if workload_class in {"long_form_generation", "provider_long_form_generation", "provider_code_generation"}:
        return OracleLabels(
            expected_route=RoutePath.PROVIDER.value,
            acceptable_routes=[RoutePath.PROVIDER.value],
            disallowed_routes=[RoutePath.LOCAL_GPU.value, RoutePath.CPU.value, RoutePath.CACHE.value],
            oracle_reason="Model-dependent language generation is provider-preferred in this dry-run benchmark.",
        )
    if workload_class in {
        "embedding_similarity",
        "embedding_index_query_large",
        "rerank_batch_large",
        "gpu_batch_embedding",
        "batch_tensor_operation",
        "gpu_tensor_transform",
        "image_like_compute",
    }:
        acceptable = [RoutePath.LOCAL_GPU.value]
        if workload_class in {"embedding_similarity", "embedding_index_query_large"} and input_size <= 4096:
            acceptable.append(RoutePath.CPU.value)
        return OracleLabels(
            expected_route=RoutePath.LOCAL_GPU.value,
            acceptable_routes=acceptable,
            disallowed_routes=[RoutePath.DETERMINISTIC.value, RoutePath.CACHE.value],
            oracle_reason="Batch or tensor-heavy work is GPU-preferred for execution-path selectivity.",
        )
    if workload_class in {"embedding_index_query_small", "rerank_batch_small"}:
        return OracleLabels(
            expected_route=RoutePath.CPU.value,
            acceptable_routes=[RoutePath.CPU.value, RoutePath.LOCAL_GPU.value],
            disallowed_routes=[RoutePath.DETERMINISTIC.value, RoutePath.CACHE.value],
            oracle_reason="Small vector work is CPU-preferred but GPU-acceptable.",
        )
    if workload_class == "ambiguous_provider_or_gpu_request":
        return OracleLabels(
            expected_route=RoutePath.FALLBACK.value,
            acceptable_routes=[RoutePath.FALLBACK.value, RoutePath.PROVIDER.value, RoutePath.LOCAL_GPU.value],
            disallowed_routes=[RoutePath.DETERMINISTIC.value, RoutePath.CACHE.value],
            oracle_reason="Ambiguous provider/GPU boundary should be handled conservatively.",
        )
    if workload_class == "invalid_or_missing_metadata_request" or inferred.get("estimated_complexity") == "unknown":
        return OracleLabels(
            expected_route=RoutePath.FALLBACK.value,
            acceptable_routes=[RoutePath.FALLBACK.value],
            disallowed_routes=[
                RoutePath.DETERMINISTIC.value,
                RoutePath.CACHE.value,
                RoutePath.CPU.value,
                RoutePath.PROVIDER.value,
                RoutePath.LOCAL_GPU.value,
            ],
            oracle_reason="Missing or invalid metadata requires a failure fallback.",
        )
    return OracleLabels(
        expected_route=RoutePath.CPU.value,
        acceptable_routes=[RoutePath.CPU.value],
        disallowed_routes=[RoutePath.LOCAL_GPU.value],
        oracle_reason="Default independent oracle route is CPU.",
    )
