#!/usr/bin/env python3
"""Run deterministic multi-profile routing robustness comparisons."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
SCRIPT_DIR = REPO_ROOT / "scripts"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from kora_core.routing_benchmark.comparison import compare_routing_policies  # noqa: E402
from kora_core.routing_benchmark.schema import workload_to_json_dict  # noqa: E402
from kora_core.routing_benchmark.workload_generator import generate_workload  # noqa: E402
from run_routing_benchmark_comparison import build_summary  # noqa: E402


DEFAULT_PROFILE_COUNTS = {
    "mixed_realistic_100k": 100_000,
    "gpu_heavy_100k": 100_000,
    "cache_heavy_100k": 100_000,
    "adversarial_100k": 100_000,
    "service_replay_10k": 10_000,
}
ROUTES = ("deterministic", "cache", "cpu", "provider", "local_gpu", "fallback", "error")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run multi-profile routing benchmark comparisons.")
    parser.add_argument("--seed", type=int, default=404)
    parser.add_argument(
        "--profile-count",
        action="append",
        default=[],
        metavar="PROFILE=COUNT",
        help="Override or add a profile count.",
    )
    return parser.parse_args()


def parse_profile_counts(overrides: list[str]) -> dict[str, int]:
    profile_counts = dict(DEFAULT_PROFILE_COUNTS)
    for override in overrides:
        if "=" not in override:
            raise ValueError(f"profile override must use PROFILE=COUNT: {override}")
        profile, raw_count = override.split("=", 1)
        count = int(raw_count)
        if count <= 0:
            raise ValueError("profile count must be positive")
        profile_counts[profile] = count
    return profile_counts


def main() -> int:
    args = parse_args()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    profile_counts = parse_profile_counts(args.profile_count)
    fixture_dir = REPO_ROOT / "docs" / "evidence" / "routing-benchmark-fixtures"
    run_dir = REPO_ROOT / "docs" / "evidence" / "routing-benchmark-runs"
    aggregate_dir = REPO_ROOT / "docs" / "evidence" / "routing-benchmark-multi-profile"
    for directory in (fixture_dir, run_dir, aggregate_dir):
        directory.mkdir(parents=True, exist_ok=True)

    profile_results = []
    for profile, count in profile_counts.items():
        requests = generate_workload(profile, count, seed=args.seed)
        request_dicts = [request.to_dict() for request in requests]
        fixture_manifest = build_generation_manifest(
            profile=profile,
            count=count,
            seed=args.seed,
            timestamp=timestamp,
            requests=requests,
        )
        manifest_path = fixture_dir / f"{timestamp}-{profile}-{count}-generation.json"
        write_json(manifest_path, fixture_manifest)

        comparison = compare_routing_policies(request_dicts)
        comparison["profile"] = profile
        comparison["seed"] = args.seed
        comparison_path = run_dir / f"{timestamp}-{profile}-{count}.json"
        write_json(comparison_path, comparison)

        summary = build_summary(comparison)
        summary_path = run_dir / f"{timestamp}-{profile}-{count}-summary.json"
        write_json(summary_path, summary)

        profile_results.append(
            {
                "profile": profile,
                "request_count": count,
                "generation_manifest_path": str(manifest_path.relative_to(REPO_ROOT)),
                "comparison_path": str(comparison_path.relative_to(REPO_ROOT)),
                "summary_path": str(summary_path.relative_to(REPO_ROOT)),
                "comparison": comparison,
                "summary": summary,
            }
        )

    aggregate = build_aggregate(profile_results, seed=args.seed, timestamp=timestamp)
    aggregate_path = aggregate_dir / f"{timestamp}-multi-profile-routing-robustness.json"
    write_json(aggregate_path, aggregate)
    aggregate_summary = build_aggregate_summary(aggregate)
    aggregate_summary_path = aggregate_dir / f"{timestamp}-multi-profile-routing-robustness-summary.json"
    write_json(aggregate_summary_path, aggregate_summary)

    print(
        json.dumps(
            {
                "aggregate_path": str(aggregate_path.relative_to(REPO_ROOT)),
                "aggregate_summary_path": str(aggregate_summary_path.relative_to(REPO_ROOT)),
                "profile_count": len(profile_results),
                "kora_profile_metrics": aggregate_summary["kora_profile_metrics"],
                "mode": "dry_run_only",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def build_generation_manifest(
    *,
    profile: str,
    count: int,
    seed: int,
    timestamp: str,
    requests: list[Any],
) -> dict[str, Any]:
    payload = workload_to_json_dict(requests)
    payload["profile"] = profile
    payload["seed"] = seed
    serialized = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    return {
        "schema_version": "routing_benchmark_fixture_generation_v0_1",
        "profile": profile,
        "request_count": count,
        "seed": seed,
        "fixture_path_not_committed": f"docs/evidence/routing-benchmark-fixtures/{timestamp}-{profile}-{count}.json",
        "fixture_sha256": hashlib.sha256(serialized).hexdigest(),
        "fixture_size_bytes": len(serialized),
        "commit_strategy": "generation_config_and_hash",
        "reason_full_fixture_not_committed": "The deterministic fixture JSON is large; the comparison output and deterministic hash are committed instead.",
        "h100_execution_performed": False,
        "live_provider_execution_performed": False,
    }


def build_aggregate(profile_results: list[dict[str, Any]], *, seed: int, timestamp: str) -> dict[str, Any]:
    profiles: dict[str, Any] = {}
    for profile_result in profile_results:
        comparison = profile_result["comparison"]
        summary = profile_result["summary"]
        profiles[profile_result["profile"]] = {
            "request_count": profile_result["request_count"],
            "generation_manifest_path": profile_result["generation_manifest_path"],
            "comparison_path": profile_result["comparison_path"],
            "summary_path": profile_result["summary_path"],
            "router_results": comparison["router_results"],
            "summary_rows": summary["rows"],
        }
    kora_rows = [profile_kora_row(result["summary"]) for result in profile_results]
    kora_metrics = aggregate_kora_metrics(kora_rows)
    return {
        "schema_version": "routing_benchmark_multi_profile_v0_1",
        "created_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "timestamp": timestamp,
        "seed": seed,
        "mode": "dry_run_only",
        "h100_execution_performed": False,
        "live_provider_execution_performed": False,
        "profiles": profiles,
        "aggregate_metrics": {"kora_router_adapter": kora_metrics},
        "claim_boundaries": [
            "dry_run_robustness_evidence_only",
            "not_production_savings_evidence",
            "not_live_provider_execution",
            "not_h100_execution_in_gpu_005",
        ],
    }


def build_aggregate_summary(aggregate: dict[str, Any]) -> dict[str, Any]:
    rows = []
    kora_profile_metrics = {}
    for profile, profile_result in aggregate["profiles"].items():
        kora_row = next(row for row in profile_result["summary_rows"] if row["router"] == "kora_router_adapter")
        row = {
            "profile": profile,
            "request_count": profile_result["request_count"],
            "local_gpu_percentage": kora_row["local_gpu_percentage"],
            "cache_percentage": kora_row["cache_percentage"],
            "provider_percentage": kora_row["provider_percentage"],
            "fallback_percentage": kora_row["fallback_percentage"],
            "acceptable_route_rate": kora_row["acceptable_route_rate"],
            "unsafe_misroute_rate": kora_row["unsafe_misroute_rate"],
            "compute_weighted_gpu_reduction_percentage": kora_row[
                "compute_weighted_gpu_reduction_percentage"
            ],
        }
        rows.append(row)
        kora_profile_metrics[profile] = row
    return {
        "schema_version": "routing_benchmark_multi_profile_summary_v0_1",
        "aggregate_schema_version": aggregate["schema_version"],
        "mode": aggregate["mode"],
        "h100_execution_performed": aggregate["h100_execution_performed"],
        "live_provider_execution_performed": aggregate["live_provider_execution_performed"],
        "kora_profile_metrics": kora_profile_metrics,
        "aggregate_metrics": aggregate["aggregate_metrics"],
        "rows": rows,
    }


def aggregate_kora_metrics(kora_rows: list[dict[str, Any]]) -> dict[str, Any]:
    acceptable = [float(row["acceptable_route_rate"]) for row in kora_rows]
    unsafe = [float(row["unsafe_misroute_rate"]) for row in kora_rows]
    fallback = [float(row["fallback_rate"]) for row in kora_rows]
    reduction = [float(row["compute_weighted_gpu_reduction_percentage"]) for row in kora_rows]
    max_unsafe = max(unsafe)
    return {
        "mean_acceptable_route_rate": round(mean(acceptable), 6),
        "min_acceptable_route_rate": round(min(acceptable), 6),
        "mean_unsafe_misroute_rate": round(mean(unsafe), 6),
        "max_unsafe_misroute_rate": round(max_unsafe, 6),
        "mean_fallback_rate": round(mean(fallback), 6),
        "max_fallback_rate": round(max(fallback), 6),
        "mean_compute_weighted_gpu_reduction_percentage": round(mean(reduction), 6),
        "profile_with_highest_gpu_demand": max(kora_rows, key=lambda row: row["local_gpu_percentage"])["profile"],
        "profile_with_highest_fallback": max(kora_rows, key=lambda row: row["fallback_percentage"])["profile"],
        "profile_with_highest_unsafe_misroute": "none_all_profiles_zero"
        if max_unsafe == 0
        else max(kora_rows, key=lambda row: row["unsafe_misroute_rate"])["profile"],
        "profile_with_strongest_cache_dedup_savings": max(
            kora_rows,
            key=lambda row: (row["cache_percentage"], row["compute_weighted_gpu_reduction_percentage"]),
        )["profile"],
        "gpu_heavy_profile_preserves_gpu_routes": any(
            row["profile"] == "gpu_heavy_100k" and row["local_gpu_percentage"] >= 50.0 for row in kora_rows
        ),
    }


def profile_kora_row(summary: dict[str, Any]) -> dict[str, Any]:
    row = next(row for row in summary["rows"] if row["router"] == "kora_router_adapter")
    return {"profile": summary["profile"], **row}


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
