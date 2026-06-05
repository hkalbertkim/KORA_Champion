#!/usr/bin/env python3
"""Generate a deterministic routing benchmark fixture."""

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

from kora_core.routing_benchmark.schema import REQUIRED_PROFILES, workload_to_json_dict  # noqa: E402
from kora_core.routing_benchmark.workload_generator import generate_workload  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a dry-run routing benchmark fixture.")
    parser.add_argument("--profile", default="service_replay_10k", choices=sorted(REQUIRED_PROFILES))
    parser.add_argument("--count", default=100, type=int)
    parser.add_argument("--seed", default=404, type=int)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    requests = generate_workload(args.profile, args.count, seed=args.seed)
    output_dir = REPO_ROOT / "docs" / "evidence" / "routing-benchmark-fixtures"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output or output_dir / f"{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}-{args.profile}-{args.count}.json"
    payload = workload_to_json_dict(requests)
    payload["profile"] = args.profile
    payload["seed"] = args.seed
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"fixture_path": str(output_path.relative_to(REPO_ROOT)), "request_count": len(requests)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
