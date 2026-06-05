"""Compute-weight estimates for routing benchmark workloads."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Mapping

COMPUTE_WEIGHT_FORMULA_VERSION = "cw_v0_1"

DEFAULT_CLASS_BASE_WEIGHTS: dict[str, float] = {
    "deterministic_config_query": 0.1,
    "deterministic_config_lookup": 0.1,
    "deterministic_model_catalog_query": 0.1,
    "cache_exact_repeat": 0.05,
    "repeated_user_prompt_exact": 0.05,
    "repeated_user_prompt_near_duplicate": 0.08,
    "near_duplicate_equivalent": 0.08,
    "near_duplicate_not_equivalent": 0.2,
    "small_cpu_transform": 0.5,
    "small_text_transform_cpu": 0.5,
    "local_file_metadata_parse": 0.6,
    "long_form_generation": 2.0,
    "provider_long_form_generation": 2.0,
    "provider_code_generation": 2.5,
    "embedding_similarity": 4.0,
    "embedding_index_query_small": 2.0,
    "embedding_index_query_large": 5.0,
    "rerank_batch_small": 3.0,
    "rerank_batch_large": 6.0,
    "gpu_batch_embedding": 7.0,
    "batch_tensor_operation": 8.0,
    "gpu_tensor_transform": 8.0,
    "image_like_compute": 12.0,
    "ambiguous_provider_or_gpu_request": 4.0,
    "invalid_or_missing_metadata_request": 0.1,
}

COMPLEXITY_MULTIPLIERS = {"low": 0.5, "medium": 1.0, "high": 3.0, "very_high": 5.0}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def config_path() -> Path:
    return repo_root() / "docs" / "evidence" / "routing-benchmark-config" / "compute-weight-cw-v0-1.json"


def load_class_base_weights(path: Path | None = None) -> dict[str, float]:
    selected_path = path or config_path()
    if not selected_path.exists():
        return dict(DEFAULT_CLASS_BASE_WEIGHTS)
    payload = json.loads(selected_path.read_text(encoding="utf-8"))
    weights = payload.get("class_base_weights", payload)
    return {str(key): float(value) for key, value in weights.items()}


def batch_multiplier(batch_size: int) -> float:
    if batch_size <= 1:
        return 1.0
    return max(1.0, math.log2(batch_size + 1) / 5.0)


def compute_weight_basis(
    *,
    workload_class: str,
    input_size: int,
    estimated_complexity: str,
    batch_size: int,
    class_base_weights: Mapping[str, float] | None = None,
) -> dict[str, Any]:
    weights = class_base_weights or DEFAULT_CLASS_BASE_WEIGHTS
    class_base_weight = float(weights.get(workload_class, 0.1))
    complexity_multiplier = COMPLEXITY_MULTIPLIERS.get(estimated_complexity, 1.0)
    selected_batch_multiplier = batch_multiplier(batch_size)
    value = class_base_weight * math.log2(input_size + 1) * complexity_multiplier * selected_batch_multiplier
    return {
        "value": round(value, 6),
        "method": "size_derived_weight",
        "formula_version": COMPUTE_WEIGHT_FORMULA_VERSION,
        "basis": {
            "input_size": input_size,
            "class_base_weight": class_base_weight,
            "complexity_multiplier": complexity_multiplier,
            "batch_multiplier": round(selected_batch_multiplier, 6),
        },
        "measured_weight_available": False,
    }
