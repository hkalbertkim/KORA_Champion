#!/usr/bin/env python3
"""Normalize committed Bedrock live evidence into partial comparison output."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from kora_core.harness import load_request_fixtures  # noqa: E402
from kora_core.live_comparison import build_partial_live_provider_comparison  # noqa: E402
from kora_core.live_evidence import normalize_live_measurement  # noqa: E402


DEFAULT_INPUT = REPO_ROOT / "docs" / "evidence" / "provider-live-runs" / "20260604-112641-provider-live-bedrock.json"


def main() -> int:
    fixture_path = REPO_ROOT / "tests" / "fixtures" / "sample_requests.json"
    requests = load_request_fixtures(fixture_path)
    measurement = normalize_live_measurement(DEFAULT_INPUT)
    comparison = build_partial_live_provider_comparison(measurement, requests)
    output_dir = REPO_ROOT / "docs" / "evidence" / "live-comparisons"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-bedrock-live-normalized-comparison.json"
    output_path.write_text(json.dumps(comparison.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "comparison_path": str(output_path.relative_to(REPO_ROOT)),
        "provider": measurement.provider,
        "model": measurement.model,
        "measured_provider_calls": comparison.measured_provider_calls,
        "total_tokens": comparison.measured_tokens,
        "measured_latency_ms": comparison.measured_latency_ms,
        "claim_level": comparison.comparison_claim_level,
        "warnings": comparison.claim_warnings,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
