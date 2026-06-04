#!/usr/bin/env python3
"""Run the local KORA Core v0.1 smoke benchmark."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from kora_core.benchmark import run_synthetic_benchmark  # noqa: E402
from kora_core.harness import load_request_fixtures, run_request_harness  # noqa: E402


def main() -> int:
    fixture_path = REPO_ROOT / "tests" / "fixtures" / "sample_requests.json"
    if fixture_path.exists():
        result = {
            "benchmark_name": "kora_core_v0_1_fixture_smoke",
            **run_request_harness(load_request_fixtures(fixture_path)),
        }
    else:
        result = run_synthetic_benchmark()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
