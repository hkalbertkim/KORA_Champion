"""Unified provider harness for dry-run and future live evidence runs."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping

from kora_core.config import ENV_LIVE_PROVIDER, ENV_PROVIDER_MODE, ProviderMode, load_provider_config
from kora_core.evidence import ClaimLevel, provider_dry_run_warnings
from kora_core.execution_targets import ExecutionTarget
from kora_core.harness import load_request_fixtures, run_request_harness
from kora_core.live_provider_adapter import (
    LIVE_BOUNDARY_WARNINGS,
    LiveProviderNotEnabledError,
    MissingProviderCredentialError,
)
from kora_core.openai_live_adapter import LiveProviderExecutionNotAllowedError
from kora_core.provider_adapter import ProviderRequest, create_provider_adapter
from kora_core.providers import ProviderId, validate_provider_id
from kora_core.run_record import provider_metrics_from_adapter_results


HARNESS_DRY_RUN_WARNINGS = [
    "Provider harness ran in dry-run mode.",
    "No external provider API call was attempted.",
    "Harness evidence is not measured provider evidence.",
]


@dataclass(frozen=True)
class ProviderHarnessResult:
    mode: str
    selected_provider: str
    selected_model: str
    provider_calls: int
    input_tokens: int
    output_tokens: int
    total_tokens: int
    estimated_provider_cost: float | None
    actual_provider_cost: float | None
    has_real_provider_data: bool
    claim_level: str
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    evidence_status: str = "ok"
    external_calls_attempted: bool = False
    provider_request_count: int = 0
    successful_provider_calls: int = 0
    failed_provider_calls: int = 0
    measured_latency_ms: float | None = None
    response_text_redacted: bool = True
    adapter_results: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "selected_provider": self.selected_provider,
            "selected_model": self.selected_model,
            "provider_calls": self.provider_calls,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "estimated_provider_cost": self.estimated_provider_cost,
            "actual_provider_cost": self.actual_provider_cost,
            "has_real_provider_data": self.has_real_provider_data,
            "claim_level": self.claim_level,
            "warnings": list(self.warnings),
            "errors": list(self.errors),
            "evidence_status": self.evidence_status,
            "external_calls_attempted": self.external_calls_attempted,
            "provider_request_count": self.provider_request_count,
            "successful_provider_calls": self.successful_provider_calls,
            "failed_provider_calls": self.failed_provider_calls,
            "measured_latency_ms": self.measured_latency_ms,
            "response_text_redacted": self.response_text_redacted,
            "adapter_results": list(self.adapter_results),
        }


def run_provider_harness(
    requests: Iterable[Mapping[str, Any]] | None = None,
    *,
    fixture_path: str | Path | None = None,
    provider_name: str | ProviderId = ProviderId.LOCAL_MOCK,
    model_name: str = "dry-run-model",
    mode: str | ProviderMode = ProviderMode.DRY_RUN,
    env: Mapping[str, str] | None = None,
    allow_live: bool = False,
    max_live_calls: int = 1,
    transport: Any | None = None,
) -> ProviderHarnessResult:
    """Run provider-shaped evidence for routed provider requests only."""

    selected_mode = ProviderMode(str(mode))
    provider = validate_provider_id(provider_name)
    selected_requests = _load_requests(requests, fixture_path)
    provider_records = _provider_records_for(selected_requests)

    if selected_mode == ProviderMode.LIVE:
        return _run_live_boundary(
            selected_requests,
            provider_records,
            provider=provider,
            model_name=model_name,
            env=env,
            allow_live=allow_live,
            max_live_calls=max_live_calls,
            transport=transport,
        )

    adapter = create_provider_adapter(provider, mode=str(ProviderMode.DRY_RUN))
    adapter_results = [
        adapter.invoke(
            ProviderRequest(
                request_id=record["request_id"],
                prompt=_prompt_for_request(selected_requests, record["request_id"]),
                provider_name=str(provider),
                model_name=model_name,
                metadata={"source": "provider_harness", "mode": "dry_run"},
            )
        )
        for record in provider_records
    ]
    metrics = provider_metrics_from_adapter_results(adapter_results)
    warnings = list(dict.fromkeys(HARNESS_DRY_RUN_WARNINGS + provider_dry_run_warnings()))
    return ProviderHarnessResult(
        mode=str(ProviderMode.DRY_RUN),
        selected_provider=str(provider),
        selected_model=model_name,
        provider_calls=metrics.provider_calls,
        input_tokens=metrics.input_tokens,
        output_tokens=metrics.output_tokens,
        total_tokens=metrics.total_tokens,
        estimated_provider_cost=metrics.estimated_provider_cost,
        actual_provider_cost=metrics.actual_provider_cost,
        has_real_provider_data=False,
        claim_level=str(ClaimLevel.DRY_RUN),
        warnings=warnings,
        evidence_status="dry_run_complete",
        provider_request_count=len(provider_records),
        adapter_results=[result.to_dict() for result in adapter_results],
    )


def _run_live_boundary(
    requests: list[Mapping[str, Any]],
    provider_records: list[dict[str, Any]],
    *,
    provider: ProviderId,
    model_name: str,
    env: Mapping[str, str] | None,
    allow_live: bool,
    max_live_calls: int,
    transport: Any | None,
) -> ProviderHarnessResult:
    config_env = dict(os.environ if env is None else env)
    config_env[ENV_PROVIDER_MODE] = str(ProviderMode.LIVE)
    config_env[ENV_LIVE_PROVIDER] = str(provider)
    try:
        config = load_provider_config(config_env)
        adapter = create_provider_adapter(
            provider,
            mode=str(ProviderMode.LIVE),
            config=config,
            allow_live=allow_live,
            transport=transport,
        )
        adapter_results = [
            adapter.invoke(
                ProviderRequest(
                    request_id=record["request_id"],
                    prompt=_prompt_for_request(requests, record["request_id"]),
                    provider_name=str(provider),
                    model_name=model_name,
                    metadata={"source": "provider_harness", "mode": "live_boundary"},
                )
            )
            for record in provider_records[: max(0, int(max_live_calls))]
        ]
    except (
        MissingProviderCredentialError,
        LiveProviderExecutionNotAllowedError,
        LiveProviderNotEnabledError,
        ValueError,
    ) as exc:
        return ProviderHarnessResult(
            mode=str(ProviderMode.LIVE),
            selected_provider=str(provider),
            selected_model=model_name,
            provider_calls=0,
            input_tokens=0,
            output_tokens=0,
            total_tokens=0,
            estimated_provider_cost=None,
            actual_provider_cost=None,
            has_real_provider_data=False,
            claim_level=str(ClaimLevel.DRY_RUN),
            warnings=["Live provider harness failed safely before provider execution."],
            errors=[str(exc)],
            evidence_status="live_config_error",
            provider_request_count=len(provider_records),
            failed_provider_calls=len(provider_records[: max(0, int(max_live_calls))]),
        )

    successful_provider_calls = sum(1 for result in adapter_results if result.has_real_provider_data)
    failed_provider_calls = len(adapter_results) - successful_provider_calls
    has_real_provider_data = successful_provider_calls > 0 and provider == ProviderId.OPENAI
    claim_level = ClaimLevel.MEASURED_PROVIDER if has_real_provider_data else ClaimLevel.DRY_RUN
    evidence_status = "live_measured_provider" if has_real_provider_data else "live_boundary_not_implemented"
    warnings = (
        list(dict.fromkeys(warning for result in adapter_results for warning in result.warnings))
        if adapter_results
        else list(dict.fromkeys(LIVE_BOUNDARY_WARNINGS))
    )
    return ProviderHarnessResult(
        mode=str(ProviderMode.LIVE),
        selected_provider=str(provider),
        selected_model=model_name,
        provider_calls=sum(result.provider_calls for result in adapter_results),
        input_tokens=sum(result.usage.input_tokens for result in adapter_results),
        output_tokens=sum(result.usage.output_tokens for result in adapter_results),
        total_tokens=sum(result.usage.total_tokens for result in adapter_results),
        estimated_provider_cost=round(sum(result.cost.estimated_provider_cost for result in adapter_results), 8),
        actual_provider_cost=None,
        has_real_provider_data=has_real_provider_data,
        claim_level=str(claim_level),
        warnings=warnings,
        errors=[],
        evidence_status=evidence_status,
        external_calls_attempted=any(result.external_call_attempted for result in adapter_results),
        provider_request_count=len(provider_records),
        successful_provider_calls=successful_provider_calls,
        failed_provider_calls=failed_provider_calls,
        measured_latency_ms=round(sum(result.latency.latency_ms for result in adapter_results), 6),
        response_text_redacted=True,
        adapter_results=[result.to_dict() for result in adapter_results],
    )


def _load_requests(
    requests: Iterable[Mapping[str, Any]] | None,
    fixture_path: str | Path | None,
) -> list[Mapping[str, Any]]:
    if requests is not None:
        return [dict(request) for request in requests]
    if fixture_path is None:
        raise ValueError("requests or fixture_path is required")
    return load_request_fixtures(fixture_path)


def _provider_records_for(requests: list[Mapping[str, Any]]) -> list[dict[str, Any]]:
    harness_output = run_request_harness(requests)
    return [
        record
        for record in harness_output["records"]
        if record["decision"]["target"] == ExecutionTarget.PROVIDER_API.value
    ]


def _prompt_for_request(requests: list[Mapping[str, Any]], request_id: str) -> str:
    for request in requests:
        if str(request.get("id") or request.get("request_id")) == request_id:
            return str(request.get("prompt", ""))
    return ""
