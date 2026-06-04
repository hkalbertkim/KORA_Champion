"""Bedrock bearer-token live provider measurement adapter."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Mapping

from kora_core.config import ProviderConfig, ProviderMode
from kora_core.cost_model import estimate_provider_placeholder_cost
from kora_core.evidence import ClaimLevel
from kora_core.live_provider_adapter import (
    LiveProviderExecutionNotAllowedError,
    MissingProviderCredentialError,
    LiveProviderNotEnabledError,
    UnsupportedLiveProviderError,
)
from kora_core.provider_adapter import (
    ProviderAdapterResult,
    ProviderCost,
    ProviderLatency,
    ProviderRequest,
    ProviderResponse,
    ProviderUsage,
)
from kora_core.providers import ProviderId


BEDROCK_LIVE_WARNINGS = [
    "single_provider_live_measurement",
    "not_cost_reduction_evidence",
    "not_gpu_evidence",
    "response_text_redacted",
]


class BedrockLiveRequestError(RuntimeError):
    """Raised for sanitized Bedrock live request failures."""


class BedrockBearerLiveAdapter:
    """Minimal Bedrock Converse adapter using bearer-token auth."""

    def __init__(
        self,
        config: ProviderConfig,
        *,
        allow_live: bool = False,
        transport: Callable[[str, Mapping[str, str], bytes, float], Mapping[str, Any]] | None = None,
        timeout_seconds: float = 30.0,
        max_tokens: int = 128,
        temperature: float = 0.2,
    ) -> None:
        self.config = config
        self.allow_live = allow_live
        self.transport = transport or _urllib_transport
        self.timeout_seconds = timeout_seconds
        self.max_tokens = max_tokens
        self.temperature = temperature
        self._validate_ready()

    def invoke(self, request: ProviderRequest) -> ProviderAdapterResult:
        self._validate_ready()
        model_id = normalize_bedrock_model_id(request.model_name or self.config.bedrock_model_id or "")
        endpoint = bedrock_converse_endpoint(self.config.aws_region or "", model_id)
        payload = {
            "messages": [{"role": "user", "content": [{"text": request.prompt}]}],
            "inferenceConfig": {"maxTokens": self.max_tokens, "temperature": self.temperature},
        }
        headers = {
            "Authorization": f"Bearer {self.config.bedrock_api_key}",
            "Content-Type": "application/json",
        }
        start = time.monotonic()
        try:
            response_payload = self.transport(endpoint, headers, json.dumps(payload).encode("utf-8"), self.timeout_seconds)
        except Exception as exc:
            raise BedrockLiveRequestError(_sanitize_error(exc)) from exc
        local_latency_ms = round((time.monotonic() - start) * 1000.0, 6)
        usage, usage_warnings = _usage_from_payload(response_payload)
        measured_latency_ms = _latency_from_payload(response_payload) or local_latency_ms
        warnings = list(BEDROCK_LIVE_WARNINGS)
        warnings.extend(usage_warnings)
        response = ProviderResponse(
            request_id=request.request_id,
            output_text="[redacted]",
            provider_name=str(ProviderId.BEDROCK),
            model_name=model_id,
            metadata={
                "mode": "live",
                "response_text_redacted": True,
                "bedrock_converse": True,
                "model_id": model_id,
            },
        )
        return ProviderAdapterResult(
            request=ProviderRequest(
                request_id=request.request_id,
                prompt=request.prompt,
                provider_name=str(ProviderId.BEDROCK),
                model_name=model_id,
                metadata={**dict(request.metadata), "response_text_redacted": True},
            ),
            response=response,
            usage=usage,
            latency=ProviderLatency(latency_ms=measured_latency_ms, is_placeholder=False),
            cost=ProviderCost(
                estimated_provider_cost=estimate_provider_placeholder_cost(
                    str(ProviderId.BEDROCK),
                    input_tokens=usage.input_tokens,
                    output_tokens=usage.output_tokens,
                ),
                actual_provider_cost=None,
                is_placeholder=True,
            ),
            provider_calls=1,
            claim_level=ClaimLevel.MEASURED_PROVIDER,
            has_real_provider_data=True,
            warnings=warnings,
            external_call_attempted=True,
        )

    def _validate_ready(self) -> None:
        if self.config.mode != ProviderMode.LIVE:
            raise LiveProviderNotEnabledError("Bedrock live adapter requires KORA_PROVIDER_MODE=live")
        if self.config.provider != ProviderId.BEDROCK:
            raise UnsupportedLiveProviderError("Bedrock live adapter requires KORA_LIVE_PROVIDER=bedrock")
        missing = []
        if not self.config.bedrock_api_key:
            missing.append("KORA_BEDROCK_API_KEY")
        if not self.config.aws_region:
            missing.append("KORA_AWS_REGION")
        if not self.config.bedrock_model_id:
            missing.append("KORA_BEDROCK_MODEL_ID")
        if missing:
            raise MissingProviderCredentialError(f"missing required live provider config: {', '.join(missing)}")
        if not self.allow_live:
            raise LiveProviderExecutionNotAllowedError("live Bedrock execution requires --allow-live")


def normalize_bedrock_model_id(model_id: str) -> str:
    selected = model_id.strip()
    if not selected:
        raise MissingProviderCredentialError("missing required live provider config: KORA_BEDROCK_MODEL_ID")
    return selected if selected.startswith("us.") else f"us.{selected}"


def bedrock_converse_endpoint(region: str, model_id: str) -> str:
    selected_region = region.strip()
    if not selected_region:
        raise MissingProviderCredentialError("missing required live provider config: KORA_AWS_REGION")
    return f"https://bedrock-runtime.{selected_region}.amazonaws.com/model/{model_id}/converse"


def _urllib_transport(
    url: str,
    headers: Mapping[str, str],
    payload: bytes,
    timeout_seconds: float,
) -> Mapping[str, Any]:
    request = urllib.request.Request(url, data=payload, headers=dict(headers), method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        raise BedrockLiveRequestError(f"bedrock_http_error:{exc.code}") from exc
    except urllib.error.URLError as exc:
        raise BedrockLiveRequestError("bedrock_network_error") from exc
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        raise BedrockLiveRequestError("bedrock_response_not_json_object")
    return parsed


def _usage_from_payload(payload: Mapping[str, Any]) -> tuple[ProviderUsage, list[str]]:
    usage = payload.get("usage")
    warnings: list[str] = []
    if not isinstance(usage, Mapping):
        warnings.append("usage_missing_from_bedrock_response")
        return ProviderUsage(input_tokens=0, output_tokens=0, total_tokens=0), warnings
    input_tokens = int(usage.get("inputTokens", usage.get("input_tokens", 0)) or 0)
    output_tokens = int(usage.get("outputTokens", usage.get("output_tokens", 0)) or 0)
    total_tokens = int(usage.get("totalTokens", usage.get("total_tokens", input_tokens + output_tokens)) or 0)
    return ProviderUsage(input_tokens=input_tokens, output_tokens=output_tokens, total_tokens=total_tokens), warnings


def _latency_from_payload(payload: Mapping[str, Any]) -> float | None:
    metrics = payload.get("metrics")
    if not isinstance(metrics, Mapping):
        return None
    latency = metrics.get("latencyMs")
    if latency is None:
        return None
    return float(latency)


def _sanitize_error(exc: Exception) -> str:
    text = str(exc)
    if isinstance(exc, BedrockLiveRequestError):
        return text
    if not text:
        return exc.__class__.__name__
    return text[:160]
