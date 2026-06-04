"""OpenAI live provider measurement adapter.

This module is intentionally OpenAI-only and standard-library-only. It does
not read dotenv files and does not expose credential values in results.
"""

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


OPENAI_CHAT_COMPLETIONS_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_LIVE_WARNINGS = [
    "single_provider_live_measurement",
    "not_cost_reduction_evidence",
    "not_gpu_evidence",
    "response_text_redacted",
]


class LiveProviderExecutionNotAllowedError(RuntimeError):
    """Raised when live execution is requested without the explicit allow flag."""


class OpenAILiveProviderAdapter:
    """Minimal OpenAI chat-completions live measurement adapter."""

    def __init__(
        self,
        config: ProviderConfig,
        *,
        allow_live: bool = False,
        transport: Callable[[str, Mapping[str, str], bytes, float], Mapping[str, Any]] | None = None,
        timeout_seconds: float = 30.0,
    ) -> None:
        self.config = config
        self.allow_live = allow_live
        self.transport = transport or _urllib_transport
        self.timeout_seconds = timeout_seconds
        self._validate_ready()

    def invoke(self, request: ProviderRequest) -> ProviderAdapterResult:
        self._validate_ready()
        payload = {
            "model": request.model_name,
            "messages": [{"role": "user", "content": request.prompt}],
            "temperature": 0,
            "max_tokens": 64,
        }
        encoded = json.dumps(payload).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.config.openai_api_key}",
            "Content-Type": "application/json",
        }
        start = time.monotonic()
        response_payload = self.transport(OPENAI_CHAT_COMPLETIONS_URL, headers, encoded, self.timeout_seconds)
        latency_ms = round((time.monotonic() - start) * 1000.0, 6)
        usage = _usage_from_payload(response_payload)
        response = ProviderResponse(
            request_id=request.request_id,
            output_text="[redacted]",
            provider_name=str(ProviderId.OPENAI),
            model_name=request.model_name,
            metadata={
                "mode": "live",
                "response_text_redacted": True,
                "response_id_present": bool(response_payload.get("id")),
                "finish_reason": _finish_reason(response_payload),
            },
        )
        return ProviderAdapterResult(
            request=ProviderRequest(
                request_id=request.request_id,
                prompt=request.prompt,
                provider_name=str(ProviderId.OPENAI),
                model_name=request.model_name,
                metadata={**dict(request.metadata), "response_text_redacted": True},
            ),
            response=response,
            usage=usage,
            latency=ProviderLatency(latency_ms=latency_ms, is_placeholder=False),
            cost=ProviderCost(
                estimated_provider_cost=estimate_provider_placeholder_cost(
                    str(ProviderId.OPENAI),
                    input_tokens=usage.input_tokens,
                    output_tokens=usage.output_tokens,
                ),
                actual_provider_cost=None,
                is_placeholder=True,
            ),
            provider_calls=1,
            claim_level=ClaimLevel.MEASURED_PROVIDER,
            has_real_provider_data=True,
            warnings=list(OPENAI_LIVE_WARNINGS),
            external_call_attempted=True,
        )

    def _validate_ready(self) -> None:
        if self.config.mode != ProviderMode.LIVE:
            raise LiveProviderNotEnabledError("OpenAI live adapter requires KORA_PROVIDER_MODE=live")
        if self.config.provider != ProviderId.OPENAI:
            raise UnsupportedLiveProviderError("OpenAI live adapter requires KORA_LIVE_PROVIDER=openai")
        if not self.config.openai_api_key:
            raise MissingProviderCredentialError("missing required live provider config: KORA_OPENAI_API_KEY")
        if not self.allow_live:
            raise LiveProviderExecutionNotAllowedError("live OpenAI execution requires --allow-live")


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
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI live request failed with HTTP {exc.code}: {body[:200]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"OpenAI live request failed before completion: {exc.reason}") from exc
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        raise RuntimeError("OpenAI live request returned non-object JSON")
    return parsed


def _usage_from_payload(payload: Mapping[str, Any]) -> ProviderUsage:
    usage = payload.get("usage")
    if not isinstance(usage, Mapping):
        usage = {}
    input_tokens = int(usage.get("prompt_tokens", usage.get("input_tokens", 0)) or 0)
    output_tokens = int(usage.get("completion_tokens", usage.get("output_tokens", 0)) or 0)
    total_tokens = int(usage.get("total_tokens", input_tokens + output_tokens) or 0)
    return ProviderUsage(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
    )


def _finish_reason(payload: Mapping[str, Any]) -> str | None:
    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices:
        return None
    first = choices[0]
    if not isinstance(first, Mapping):
        return None
    reason = first.get("finish_reason")
    return str(reason) if reason is not None else None
