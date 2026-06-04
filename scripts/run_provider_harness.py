#!/usr/bin/env python3
"""Run canonical provider harness evidence without external calls."""

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

from kora_core.config import SUPPORTED_PROVIDER_MODES  # noqa: E402
from kora_core.provider_harness import run_provider_harness  # noqa: E402
from kora_core.providers import SUPPORTED_PROVIDERS, validate_provider_id  # noqa: E402


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run KORA provider harness evidence.")
    parser.add_argument("--provider", default="local_mock", choices=SUPPORTED_PROVIDERS)
    parser.add_argument("--model", default=None)
    parser.add_argument("--mode", default="dry_run", choices=SUPPORTED_PROVIDER_MODES)
    parser.add_argument("--fixture", default="tests/fixtures/sample_requests.json")
    parser.add_argument("--allow-live", action="store_true")
    parser.add_argument("--max-live-calls", type=int, default=1)
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    provider = str(validate_provider_id(args.provider))
    model = args.model or ("gpt-4o-mini" if args.mode == "live" else "dry-run-model")
    fixture_path = REPO_ROOT / args.fixture
    result = run_provider_harness(
        fixture_path=fixture_path,
        provider_name=provider,
        model_name=model,
        mode=args.mode,
        allow_live=args.allow_live,
        max_live_calls=args.max_live_calls,
    )

    output_dir = (
        REPO_ROOT / "docs" / "evidence" / "provider-live-runs"
        if args.mode == "live"
        else REPO_ROOT / "docs" / "evidence" / "provider-harness"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    if args.mode == "live":
        filename = f"{timestamp}-provider-live-{provider}.json"
    else:
        filename = f"{timestamp}-provider-harness-{args.mode}-{provider}.json"
    output_path = output_dir / filename
    evidence = result.to_dict()
    evidence.update(
        {
            "run_type": f"provider_harness_{args.mode}",
            "fixture_path": args.fixture,
            "max_live_calls": args.max_live_calls,
            "allow_live": args.allow_live,
            "external_calls_attempted": result.external_calls_attempted,
        }
    )
    output_path.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    summary = {
        "evidence_path": str(output_path.relative_to(REPO_ROOT)),
        "mode": result.mode,
        "provider": result.selected_provider,
        "model": result.selected_model,
        "provider_calls": result.provider_calls,
        "successful_provider_calls": result.successful_provider_calls,
        "failed_provider_calls": result.failed_provider_calls,
        "input_tokens": result.input_tokens,
        "output_tokens": result.output_tokens,
        "total_tokens": result.total_tokens,
        "measured_latency_ms": result.measured_latency_ms,
        "estimated_provider_cost": result.estimated_provider_cost,
        "actual_provider_cost": result.actual_provider_cost,
        "claim_level": result.claim_level,
        "has_real_provider_data": result.has_real_provider_data,
        "response_text_redacted": result.response_text_redacted,
        "warnings": result.warnings,
        "errors": result.errors,
        "evidence_status": result.evidence_status,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    if result.evidence_status == "live_config_error":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
