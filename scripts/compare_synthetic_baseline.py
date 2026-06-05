#!/usr/bin/env python3
"""Generate synthetic baseline-vs-KORA comparison evidence."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from kora_core.comparison import BaselinePolicy, compare_synthetic_baseline  # noqa: E402
from kora_core.harness import load_request_fixtures  # noqa: E402


def main() -> int:
    fixture_path = REPO_ROOT / "tests" / "fixtures" / "sample_requests.json"
    requests = load_request_fixtures(fixture_path)
    comparison = compare_synthetic_baseline(
        requests,
        workload_id="sample_requests_v0_1",
        baseline_policy=BaselinePolicy.ALL_PROVIDER_API,
        include_placeholder_costs=True,
    )
    output_dir = REPO_ROOT / "docs" / "evidence" / "comparisons"
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-baseline-vs-kora-synthetic.json"
    output_path = output_dir / filename
    output_path.write_text(json.dumps(comparison.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "comparison_path": str(output_path.relative_to(REPO_ROOT)),
        "workload_size": comparison.workload_size,
        "baseline_provider_calls": comparison.baseline_provider_calls,
        "kora_provider_calls": comparison.kora_provider_calls,
        "avoided_provider_calls": comparison.avoided_provider_calls,
        "estimated_provider_call_reduction_percentage": comparison.estimated_provider_call_reduction_percentage,
        "claim_level": str(comparison.comparison_claim_level),
        "warnings": comparison.warnings,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
