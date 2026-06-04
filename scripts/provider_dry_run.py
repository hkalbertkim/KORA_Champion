#!/usr/bin/env python3
"""Generate provider-shaped dry-run evidence without external calls."""

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

from kora_core.evidence import ClaimLevel, provider_dry_run_warnings  # noqa: E402
from kora_core.harness import load_request_fixtures, run_request_harness  # noqa: E402
from kora_core.provider_adapter import DryRunProviderAdapter, ProviderRequest  # noqa: E402
from kora_core.run_record import provider_metrics_from_adapter_results  # noqa: E402
from kora_core.providers import SUPPORTED_PROVIDERS, validate_provider_id  # noqa: E402


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run provider-shaped dry-run evidence.")
    parser.add_argument("--provider", default="local_mock", choices=SUPPORTED_PROVIDERS)
    parser.add_argument("--model", default="dry-run-model")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    provider = str(validate_provider_id(args.provider))
    fixture_path = REPO_ROOT / "tests" / "fixtures" / "sample_requests.json"
    requests = load_request_fixtures(fixture_path)
    harness_output = run_request_harness(requests)
    provider_records = [
        record for record in harness_output["records"] if record["decision"]["target"] == "provider_api"
    ]
    adapter = DryRunProviderAdapter(provider_name=provider, model_name=args.model)
    results = [
        adapter.invoke(
            ProviderRequest(
                request_id=record["request_id"],
                prompt=_prompt_for_request(requests, record["request_id"]),
                provider_name=provider,
                model_name=args.model,
                metadata={"source": "synthetic_fixture"},
            )
        )
        for record in provider_records
    ]
    provider_metrics = provider_metrics_from_adapter_results(results)
    evidence = {
        "run_type": "provider_dry_run",
        "claim_level": str(ClaimLevel.DRY_RUN),
        "is_synthetic": False,
        "has_real_provider_data": False,
        "has_real_gpu_data": False,
        "provider_name": provider,
        "model_name": args.model,
        "provider_calls": provider_metrics.provider_calls,
        "input_tokens": provider_metrics.input_tokens,
        "output_tokens": provider_metrics.output_tokens,
        "total_tokens": provider_metrics.total_tokens,
        "estimated_provider_cost": provider_metrics.estimated_provider_cost,
        "actual_provider_cost": provider_metrics.actual_provider_cost,
        "provider_breakdown": provider_metrics.provider_breakdown,
        "latency_ms": round(sum(result.latency.latency_ms for result in results), 6),
        "external_calls_attempted": False,
        "warnings": provider_dry_run_warnings(),
        "adapter_results": [result.to_dict() for result in results],
    }
    output_dir = REPO_ROOT / "docs" / "evidence" / "provider-dry-runs"
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}-provider-dry-run.json"
    output_path = output_dir / filename
    output_path.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "evidence_path": str(output_path.relative_to(REPO_ROOT)),
        "provider_name": provider,
        "model_name": args.model,
        "provider_calls": provider_metrics.provider_calls,
        "input_tokens": provider_metrics.input_tokens,
        "output_tokens": provider_metrics.output_tokens,
        "total_tokens": provider_metrics.total_tokens,
        "estimated_provider_cost": provider_metrics.estimated_provider_cost,
        "actual_provider_cost": provider_metrics.actual_provider_cost,
        "claim_level": str(ClaimLevel.DRY_RUN),
        "warnings": evidence["warnings"],
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def _prompt_for_request(requests: list[dict], request_id: str) -> str:
    for request in requests:
        if str(request.get("id") or request.get("request_id")) == request_id:
            return str(request.get("prompt", ""))
    return ""


if __name__ == "__main__":
    raise SystemExit(main())
