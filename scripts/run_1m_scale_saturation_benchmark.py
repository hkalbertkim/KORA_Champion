#!/usr/bin/env python3
"""Run 1M routing scale and optional H100 saturation subset benchmarks."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
SCRIPT_DIR = REPO_ROOT / "scripts"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from kora_core.routing_benchmark.comparison import compare_routing_policies  # noqa: E402
from kora_core.routing_benchmark.workload_generator import generate_workload  # noqa: E402
from run_gpu_routed_subset_benchmark import (  # noqa: E402
    execute_gpu_subset,
    select_gpu_routed_requests,
    subset_selection_hash,
)
from run_routing_benchmark_comparison import build_summary  # noqa: E402


SCALE_PROFILE = "mixed_realistic_1m"
SOURCE_PROFILE = "mixed_realistic_100k"
DEFAULT_COUNT = 1_000_000
DEFAULT_SEED = 404
GPU_004C_COMPUTE_WEIGHT_THROUGHPUT = 1_279_400.497529
GPU_004C_UTILIZATION_AVG = 15.444444
GPU_004C_RUNTIME_SECONDS = 1.752106
GPU_004C_SUBSET_COMPUTE_WEIGHT = 2_241_645.288123
SCALE_DIR = Path("docs/evidence/routing-benchmark-scale")
SATURATION_DIR = Path("docs/evidence/gpu-saturation-runs")


def main() -> int:
    args = parse_args()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    requests = generate_scale_requests(profile=args.profile, count=args.count, seed=args.seed)
    if args.dry_run_routing_only:
        outputs = run_dry_scale_outputs(requests=requests, profile=args.profile, seed=args.seed, timestamp=timestamp)
        print(json.dumps(outputs["console_summary"], indent=2, sort_keys=True))
        return 0
    if args.measure_h100_subset:
        evidence = run_h100_saturation_subset(
            requests=requests,
            profile=args.profile,
            seed=args.seed,
            limit=args.h100_subset_limit,
            timestamp=timestamp,
        )
        print(
            json.dumps(
                {
                    "evidence_path": evidence["evidence_path"],
                    "h100_execution": evidence["h100_execution"],
                    "measured_subset_count": evidence["measured_subset"]["measured_subset_count"],
                    "runtime_seconds": evidence["gpu_runtime"]["runtime_seconds"],
                    "throughput_requests_per_second": evidence["gpu_runtime"]["throughput_requests_per_second"],
                    "error_rate": evidence["gpu_runtime"]["error_rate"],
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 0 if evidence["h100_execution"] else 2
    raise ValueError("select --dry-run-routing-only or --measure-h100-subset")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run 1M scale and saturation benchmark paths.")
    parser.add_argument("--profile", default=SCALE_PROFILE, choices=[SCALE_PROFILE])
    parser.add_argument("--count", type=int, default=DEFAULT_COUNT)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--dry-run-routing-only", action="store_true")
    parser.add_argument("--measure-h100-subset", action="store_true")
    parser.add_argument("--h100-subset-limit", type=int, default=50_000)
    return parser.parse_args()


def generate_scale_requests(*, profile: str, count: int, seed: int) -> list[dict[str, Any]]:
    if profile != SCALE_PROFILE:
        raise ValueError(f"unsupported scale profile: {profile}")
    if count <= 0:
        raise ValueError("count must be positive")
    generated = generate_workload(SOURCE_PROFILE, count, seed=seed)
    requests = []
    for request in generated:
        record = request.to_dict()
        record["workload_profile"] = profile
        requests.append(record)
    return requests


def run_dry_scale_outputs(
    *,
    requests: list[dict[str, Any]],
    profile: str,
    seed: int,
    timestamp: str,
) -> dict[str, Any]:
    output_dir = REPO_ROOT / SCALE_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    comparison = compare_routing_policies(requests)
    comparison["profile"] = profile
    comparison["seed"] = seed
    comparison["calibration"] = runtime_calibration()
    summary = build_summary(comparison)
    kora_summary = build_scale_summary(comparison=comparison, summary=summary)
    generation_manifest = build_generation_manifest(
        requests=requests,
        profile=profile,
        seed=seed,
        timestamp=timestamp,
    )

    generation_path = output_dir / f"{timestamp}-{profile}-generation.json"
    comparison_path = output_dir / f"{timestamp}-{profile}-routing-comparison.json"
    summary_path = output_dir / f"{timestamp}-{profile}-routing-summary.json"
    scale_summary_path = output_dir / f"{timestamp}-gpu-006-scale-summary.json"
    write_json(generation_path, generation_manifest)
    write_json(comparison_path, comparison)
    write_json(summary_path, summary)
    write_json(scale_summary_path, kora_summary)
    return {
        "generation_path": str(generation_path.relative_to(REPO_ROOT)),
        "comparison_path": str(comparison_path.relative_to(REPO_ROOT)),
        "summary_path": str(summary_path.relative_to(REPO_ROOT)),
        "scale_summary_path": str(scale_summary_path.relative_to(REPO_ROOT)),
        "console_summary": {
            "generation_path": str(generation_path.relative_to(REPO_ROOT)),
            "comparison_path": str(comparison_path.relative_to(REPO_ROOT)),
            "summary_path": str(summary_path.relative_to(REPO_ROOT)),
            "scale_summary_path": str(scale_summary_path.relative_to(REPO_ROOT)),
            "kora_1m_metrics": kora_summary["kora_1m_summary"],
            "h100_execution_performed": False,
            "live_provider_execution_performed": False,
        },
    }


def build_generation_manifest(
    *,
    requests: list[dict[str, Any]],
    profile: str,
    seed: int,
    timestamp: str,
) -> dict[str, Any]:
    digest = hashlib.sha256()
    total_bytes = 0
    prefix = b'{\n  "profile": '
    digest.update(prefix)
    total_bytes += len(prefix)
    encoded_profile = json.dumps(profile).encode("utf-8")
    digest.update(encoded_profile)
    total_bytes += len(encoded_profile)
    middle = f',\n  "request_count": {len(requests)},\n  "requests": [\n'.encode("utf-8")
    digest.update(middle)
    total_bytes += len(middle)
    for index, request in enumerate(requests):
        line = json.dumps(request, sort_keys=True).encode("utf-8")
        if index:
            digest.update(b",\n")
            total_bytes += 2
        digest.update(b"    ")
        digest.update(line)
        total_bytes += 4 + len(line)
    suffix = f'\n  ],\n  "schema_version": "routing_benchmark_workload_v0_1",\n  "seed": {seed}\n}}\n'.encode(
        "utf-8"
    )
    digest.update(suffix)
    total_bytes += len(suffix)
    return {
        "schema_version": "routing_benchmark_scale_generation_v0_1",
        "profile": profile,
        "request_count": len(requests),
        "seed": seed,
        "fixture_path_not_committed": f"docs/evidence/routing-benchmark-scale/{timestamp}-{profile}.json",
        "fixture_sha256": digest.hexdigest(),
        "fixture_size_bytes": total_bytes,
        "commit_strategy": "generation_config_and_hash",
        "reason_full_fixture_not_committed": "The deterministic 1M fixture JSON is large; committed evidence uses deterministic generation metadata plus comparison outputs.",
        "h100_execution_performed": False,
        "live_provider_execution_performed": False,
    }


def build_scale_summary(*, comparison: dict[str, Any], summary: dict[str, Any]) -> dict[str, Any]:
    kora_metrics = comparison["router_results"]["kora_router_adapter"]
    distribution = kora_metrics["route_distribution"]
    all_gpu_runtime = kora_metrics["baseline_gpu_compute_weight"] / GPU_004C_COMPUTE_WEIGHT_THROUGHPUT
    kora_runtime = kora_metrics["router_gpu_compute_weight"] / GPU_004C_COMPUTE_WEIGHT_THROUGHPUT
    avoided_runtime = max(0.0, all_gpu_runtime - kora_runtime)
    return {
        "schema_version": "gpu_006_scale_summary_v0_1",
        "profile": comparison["profile"],
        "total_requests": comparison["workload_request_count"],
        "mode": comparison["mode"],
        "h100_execution_performed": False,
        "live_provider_execution_performed": False,
        "router_summary_rows": summary["rows"],
        "kora_1m_summary": {
            "total_requests": comparison["workload_request_count"],
            "local_gpu_count": distribution["local_gpu"]["count"],
            "local_gpu_percentage": distribution["local_gpu"]["percentage"],
            "cache_count": distribution["cache"]["count"],
            "cache_percentage": distribution["cache"]["percentage"],
            "provider_count": distribution["provider"]["count"],
            "provider_percentage": distribution["provider"]["percentage"],
            "fallback_count": distribution["fallback"]["count"],
            "fallback_percentage": distribution["fallback"]["percentage"],
            "acceptable_route_rate": kora_metrics["acceptable_route_rate"],
            "unsafe_misroute_rate": kora_metrics["unsafe_misroute_rate"],
            "compute_weighted_gpu_reduction_percentage": kora_metrics[
                "compute_weighted_gpu_reduction_percentage"
            ],
            "baseline_gpu_compute_weight": kora_metrics["baseline_gpu_compute_weight"],
            "kora_gpu_compute_weight": kora_metrics["router_gpu_compute_weight"],
            "estimated_all_gpu_runtime_seconds": round(all_gpu_runtime, 6),
            "estimated_kora_gpu_routed_runtime_seconds": round(kora_runtime, 6),
            "estimated_avoided_gpu_runtime_seconds": round(avoided_runtime, 6),
            "runtime_estimation_method": "gpu_004c_compute_weight_throughput_calibration",
            "scale_stability_notes": [
                f"Dry-run comparison completed for {comparison['workload_request_count']:,} requests.",
                "No provider execution was performed.",
                "No H100 execution was performed in GPU-006A.",
            ],
        },
    }


def runtime_calibration() -> dict[str, Any]:
    return {
        "source": "gpu_004c_h100_routed_subset",
        "throughput_compute_weight_per_second": GPU_004C_COMPUTE_WEIGHT_THROUGHPUT,
        "runtime_formula": "compute_weight / throughput_compute_weight_per_second",
        "used_for_production_savings_claim": False,
    }


def run_h100_saturation_subset(
    *,
    requests: list[dict[str, Any]],
    profile: str,
    seed: int,
    limit: int,
    timestamp: str,
) -> dict[str, Any]:
    output_dir = REPO_ROOT / SATURATION_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    gpu_routed = select_gpu_routed_requests(requests, "kora_router_adapter")
    selected_subset = gpu_routed[: min(limit, len(gpu_routed))]
    runtime = execute_gpu_subset(
        selected_subset,
        local_validation_only=False,
        sampling_interval_seconds=0.2,
    )
    measured_compute_weight = round(sum(float(request["compute_weight"]["value"]) for request in selected_subset), 6)
    baseline_runtime = measured_compute_weight / GPU_004C_COMPUTE_WEIGHT_THROUGHPUT
    runtime_ratio = None
    if baseline_runtime > 0 and runtime["runtime_seconds"] > 0:
        runtime_ratio = round(runtime["runtime_seconds"] / baseline_runtime, 6)
    evidence = {
        "schema_version": "gpu_006_h100_saturation_subset_v0_1",
        "task_id": "KORA-CHAMPION-GPU-006B",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "profile": profile,
        "seed": seed,
        "router": "kora_router_adapter",
        "claim_level": "h100_saturation_subset_measured" if runtime["cuda_available"] else "h100_saturation_not_measured",
        "h100_execution": bool(runtime["cuda_available"]),
        "live_provider_execution": False,
        "total_requests": len(requests),
        "total_kora_local_gpu_routed_count": len(gpu_routed),
        "measured_subset": {
            "measured_subset_count": len(selected_subset),
            "measured_subset_limit": limit,
            "measured_subset_compute_weight": measured_compute_weight,
            "measured_subset_selection_method": "deterministic_first_n_local_gpu_routes",
            "measured_subset_sha256": subset_selection_hash(
                selected_subset,
                router="kora_router_adapter",
                limit=limit,
            ),
        },
        "gpu_runtime": runtime,
        "comparison_to_gpu_004c": {
            "gpu_004c_runtime_seconds": GPU_004C_RUNTIME_SECONDS,
            "gpu_004c_subset_compute_weight": GPU_004C_SUBSET_COMPUTE_WEIGHT,
            "gpu_004c_utilization_avg": GPU_004C_UTILIZATION_AVG,
            "utilization_increased_vs_gpu_004c": None
            if runtime["gpu_utilization_avg"] is None
            else runtime["gpu_utilization_avg"] > GPU_004C_UTILIZATION_AVG,
            "runtime_scales_roughly_with_compute_weight": runtime_ratio is not None and 0.25 <= runtime_ratio <= 4.0,
            "runtime_to_calibrated_estimate_ratio": runtime_ratio,
        },
        "claim_boundary": {
            "production_cost_savings_claim": False,
            "customer_workload_claim": False,
            "full_1m_all_gpu_measured_execution_claim": False,
            "provider_cost_claim": False,
        },
    }
    evidence_path = output_dir / f"{timestamp}-{profile}-kora-router-h100-saturation-subset.json"
    write_json(evidence_path, evidence)
    evidence["evidence_path"] = str(evidence_path.relative_to(REPO_ROOT))
    write_json(evidence_path, evidence)
    return evidence


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
