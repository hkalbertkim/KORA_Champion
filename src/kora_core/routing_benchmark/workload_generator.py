"""Deterministic workload generation for routing benchmark profiles."""

from __future__ import annotations

import random
from typing import Any

from kora_core.routing_benchmark.compute_weights import compute_weight_basis, load_class_base_weights
from kora_core.routing_benchmark.oracle_generator import labels_for_request
from kora_core.routing_benchmark.schema import BenchmarkRequest, ComputeWeight, REQUIRED_PROFILES, RouterVisibleMetadata, ValidationMetadata

SERVICE_REPLAY_CLASSES = [
    "repeated_user_prompt_exact",
    "repeated_user_prompt_near_duplicate",
    "near_duplicate_equivalent",
    "near_duplicate_not_equivalent",
    "deterministic_config_lookup",
    "deterministic_model_catalog_query",
    "small_text_transform_cpu",
    "local_file_metadata_parse",
    "embedding_index_query_small",
    "embedding_index_query_large",
    "rerank_batch_small",
    "rerank_batch_large",
    "provider_long_form_generation",
    "provider_code_generation",
    "gpu_batch_embedding",
    "gpu_tensor_transform",
    "ambiguous_provider_or_gpu_request",
    "invalid_or_missing_metadata_request",
]

PROFILE_CLASSES = {
    "service_replay_10k": SERVICE_REPLAY_CLASSES,
    "mixed_realistic_100k": SERVICE_REPLAY_CLASSES
    + ["deterministic_config_query", "cache_exact_repeat", "embedding_similarity", "long_form_generation"],
    "gpu_heavy_100k": [
        "gpu_batch_embedding",
        "gpu_tensor_transform",
        "batch_tensor_operation",
        "image_like_compute",
        "embedding_similarity",
        "embedding_index_query_large",
        "rerank_batch_large",
        "provider_code_generation",
    ],
    "cache_heavy_100k": [
        "cache_exact_repeat",
        "repeated_user_prompt_exact",
        "near_duplicate_equivalent",
        "small_text_transform_cpu",
        "deterministic_config_query",
        "embedding_index_query_small",
    ],
    "adversarial_100k": [
        "near_duplicate_not_equivalent",
        "repeated_user_prompt_near_duplicate",
        "ambiguous_provider_or_gpu_request",
        "invalid_or_missing_metadata_request",
        "embedding_index_query_small",
        "provider_code_generation",
        "gpu_tensor_transform",
    ],
}


def _metadata_for_class(workload_class: str, rng: random.Random) -> dict[str, dict[str, Any]]:
    input_size = {
        "small": rng.choice([64, 128, 256, 512]),
        "medium": rng.choice([1024, 2048, 4096]),
        "large": rng.choice([8192, 16384, 32768]),
    }
    if workload_class in {"invalid_or_missing_metadata_request"}:
        return {
            "observable": {
                "input_size": 0,
                "batch_size": 0,
                "request_modality": "unknown",
                "cache_key_available": False,
            },
            "inferred": {"estimated_complexity": "unknown", "latency_sensitivity": "medium"},
        }
    cache_classes = {"cache_exact_repeat", "repeated_user_prompt_exact", "near_duplicate_equivalent"}
    deterministic_classes = {"deterministic_config_query", "deterministic_config_lookup", "deterministic_model_catalog_query"}
    gpu_classes = {"gpu_batch_embedding", "gpu_tensor_transform", "batch_tensor_operation", "image_like_compute", "rerank_batch_large"}
    provider_classes = {"long_form_generation", "provider_long_form_generation", "provider_code_generation"}
    small_classes = {"small_cpu_transform", "small_text_transform_cpu", "local_file_metadata_parse", "embedding_index_query_small", "rerank_batch_small"}

    size = input_size["medium"]
    batch_size = 1
    modality = "text"
    complexity = "medium"
    if workload_class in deterministic_classes:
        size = input_size["small"]
        complexity = "low"
        modality = "config"
    elif workload_class in cache_classes:
        size = input_size["medium"]
        complexity = "low"
    elif workload_class in small_classes:
        size = input_size["small"]
        complexity = "low"
    elif workload_class in provider_classes:
        size = input_size["large"]
        complexity = "high"
        modality = "language"
    elif workload_class in gpu_classes:
        size = input_size["large"]
        batch_size = rng.choice([16, 32, 64])
        complexity = "high"
        modality = "tensor"
    elif workload_class in {"embedding_similarity", "embedding_index_query_large"}:
        size = input_size["medium"] if workload_class == "embedding_similarity" else input_size["large"]
        batch_size = rng.choice([8, 16, 32])
        complexity = "medium"
        modality = "embedding"
    elif workload_class == "ambiguous_provider_or_gpu_request":
        size = input_size["large"]
        batch_size = rng.choice([1, 8])
        complexity = "high"
        modality = "mixed"
    elif workload_class in {"near_duplicate_not_equivalent", "repeated_user_prompt_near_duplicate"}:
        size = input_size["medium"]
        complexity = "medium"

    return {
        "observable": {
            "input_size": size,
            "batch_size": batch_size,
            "request_modality": modality,
            "cache_key_available": workload_class in cache_classes,
        },
        "inferred": {
            "estimated_complexity": complexity,
            "latency_sensitivity": rng.choice(["low", "medium", "high"]),
        },
    }


def generate_workload(profile: str, count: int, *, seed: int = 404) -> list[BenchmarkRequest]:
    if profile not in REQUIRED_PROFILES:
        raise ValueError(f"unsupported workload profile: {profile}")
    if count < 1:
        raise ValueError("count must be positive")
    rng = random.Random(seed)
    classes = PROFILE_CLASSES[profile]
    weights = load_class_base_weights()
    requests: list[BenchmarkRequest] = []
    for index in range(count):
        workload_class = classes[index % len(classes)]
        metadata = _metadata_for_class(workload_class, rng)
        observable = metadata["observable"]
        inferred = metadata["inferred"]
        oracle_labels = labels_for_request(workload_class, metadata)
        compute_weight = compute_weight_basis(
            workload_class=workload_class,
            input_size=int(observable["input_size"]),
            estimated_complexity=str(inferred["estimated_complexity"]),
            batch_size=int(observable["batch_size"]),
            class_base_weights=weights,
        )
        requests.append(
            BenchmarkRequest(
                request_id=f"req_{index + 1:06d}",
                workload_profile=profile,
                workload_class=workload_class,
                router_visible_metadata=RouterVisibleMetadata(
                    observable=dict(observable),
                    inferred=dict(inferred),
                ),
                oracle_labels=oracle_labels,
                compute_weight=ComputeWeight(**compute_weight),
                validation=ValidationMetadata(
                    quality_check_required=oracle_labels.expected_route
                    in {"provider", "local_gpu", "fallback"},
                    cache_hit_expected=oracle_labels.expected_route == "cache",
                    adversarial_tag="boundary_case" if profile == "adversarial_100k" else None,
                ),
            )
        )
    return requests
