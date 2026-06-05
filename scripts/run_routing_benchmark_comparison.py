#!/usr/bin/env python3
"""Run a dry-run routing benchmark comparison."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from kora_core.routing_benchmark.comparison import compare_routing_policies  # noqa: E402
from kora_core.routing_benchmark.schema import REQUIRED_PROFILES, requests_from_json_dict  # noqa: E402
from kora_core.routing_benchmark.workload_generator import generate_workload  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a dry-run routing benchmark comparison.")
    parser.add_argument("--profile", default="service_replay_10k", choices=sorted(REQUIRED_PROFILES))
    parser.add_argument("--count", default=100, type=int)
    parser.add_argument("--seed", default=404, type=int)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


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
    output_path = args.output or output_dir / f"{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}-{profile}-{len(requests)}.json"
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "comparison_path": str(output_path.relative_to(REPO_ROOT)),
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
