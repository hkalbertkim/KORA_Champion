#!/usr/bin/env python3
"""Run a dry-run routing benchmark comparison."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from kora_core.routing_benchmark.comparison import compare_routing_policies  # noqa: E402
from kora_core.routing_benchmark.schema import REQUIRED_PROFILES, requests_from_json_dict  # noqa: E402
from kora_core.routing_benchmark.workload_generator import generate_workload  # noqa: E402


ROUTES = ("deterministic", "cache", "cpu", "provider", "local_gpu", "fallback", "error")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a dry-run routing benchmark comparison.")
    parser.add_argument("--profile", default="service_replay_10k", choices=sorted(REQUIRED_PROFILES))
    parser.add_argument("--count", default=100, type=int)
    parser.add_argument("--seed", default=404, type=int)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--summary-output", type=Path)
    return parser.parse_args()


def build_summary(result: dict) -> dict:
    rows = []
    for policy_name, metrics in result["router_results"].items():
        distribution = metrics["route_distribution"]
        row = {
            "router": policy_name,
            "exact_route_accuracy": metrics["exact_route_accuracy"],
            "acceptable_route_rate": metrics["acceptable_route_rate"],
            "unsafe_misroute_rate": metrics["unsafe_misroute_rate"],
            "fallback_rate": metrics["fallback_rate"],
            "compute_weighted_gpu_reduction_percentage": metrics[
                "compute_weighted_gpu_reduction_percentage"
            ],
        }
        for route in ROUTES:
            route_metrics = distribution[route]
            row[f"{route}_count"] = route_metrics["count"]
            row[f"{route}_percentage"] = route_metrics["percentage"]
        rows.append(row)
    return {
        "schema_version": "routing_benchmark_summary_v0_1",
        "comparison_schema_version": result["schema_version"],
        "profile": result["profile"],
        "request_count": result["workload_request_count"],
        "mode": result["mode"],
        "h100_execution_performed": result["h100_execution_performed"],
        "live_provider_execution_performed": result["live_provider_execution_performed"],
        "rows": rows,
    }


def main() -> int:
    args = parse_args()
    if args.input:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        requests = requests_from_json_dict(payload)
        profile = str(payload.get("profile", args.profile))
    else:
        generated = generate_workload(args.profile, args.count, seed=args.seed)
        requests = [request.to_dict() for request in generated]
        profile = args.profile
    result = compare_routing_policies(requests)
    result["profile"] = profile
    result["seed"] = args.seed
    output_dir = REPO_ROOT / "docs" / "evidence" / "routing-benchmark-runs"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output or output_dir / f"{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-{profile}-{len(requests)}.json"
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary_payload = build_summary(result)
    summary_path = args.summary_output or output_path.with_name(f"{output_path.stem}-summary.json")
    summary_path.write_text(json.dumps(summary_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "comparison_path": str(output_path.relative_to(REPO_ROOT)),
        "summary_path": str(summary_path.relative_to(REPO_ROOT)),
        "request_count": len(requests),
        "kora_route_counts": result["router_results"]["kora_router_adapter"]["route_counts"],
        "kora_acceptable_route_rate": result["router_results"]["kora_router_adapter"]["acceptable_route_rate"],
        "kora_compute_weighted_gpu_reduction_percentage": result["router_results"]["kora_router_adapter"][
            "compute_weighted_gpu_reduction_percentage"
        ],
        "mode": result["mode"],
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
