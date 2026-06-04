"""Provider adapter interfaces and dry-run implementation."""

from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol

from kora_core.evidence import ClaimLevel
from kora_core.metrics import estimate_tokens
from kora_core.providers import ProviderId, validate_provider_id


DEFAULT_PLACEHOLDER_PROVIDER_RATES: dict[str, dict[str, float]] = {
    "local_mock": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "openai": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "anthropic": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "gemini": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "bedrock": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "vllm": {"input_per_1k": 0.0005, "output_per_1k": 0.001},
}

DRY_RUN_WARNINGS = [
    "Provider adapter result is dry-run only.",
    "No external provider API call was attempted.",
    "Token, latency, and cost values are deterministic placeholders.",
    "Dry-run evidence must not be used as real provider performance or cost evidence.",
]


@dataclass(frozen=True)
class ProviderRequest:
    request_id: str
    prompt: str
    provider_name: str = "local_mock"
    model_name: str = "dry-run-model"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ProviderUsage:
    input_tokens: int
    output_tokens: int
    total_tokens: int


@dataclass(frozen=True)
class ProviderLatency:
    latency_ms: float
    is_placeholder: bool = True


@dataclass(frozen=True)
class ProviderCost:
    estimated_provider_cost: float
    actual_provider_cost: float | None
    currency: str = "USD"
    is_placeholder: bool = True


@dataclass(frozen=True)
class ProviderResponse:
    request_id: str
    output_text: str
    provider_name: str
    model_name: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ProviderAdapterResult:
    request: ProviderRequest
    response: ProviderResponse
    usage: ProviderUsage
    latency: ProviderLatency
    cost: ProviderCost
    provider_calls: int
    claim_level: ClaimLevel
    has_real_provider_data: bool
    warnings: list[str]
    external_call_attempted: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "request": {
                "request_id": self.request.request_id,
                "provider_name": self.request.provider_name,
                "model_name": self.request.model_name,
                "metadata": self.request.metadata,
            },
            "response": {
                "request_id": self.response.request_id,
                "output_text": self.response.output_text,
                "provider_name": self.response.provider_name,
                "model_name": self.response.model_name,
                "metadata": self.response.metadata,
            },
            "usage": self.usage.__dict__,
            "latency": self.latency.__dict__,
            "cost": self.cost.__dict__,
            "provider_calls": self.provider_calls,
            "claim_level": str(self.claim_level),
            "has_real_provider_data": self.has_real_provider_data,
            "warnings": list(self.warnings),
            "external_call_attempted": self.external_call_attempted,
        }


class ProviderAdapter(Protocol):
    """Provider adapter protocol for dry-run and future live adapters."""

    def invoke(self, request: ProviderRequest) -> ProviderAdapterResult:
        """Return a provider-shaped adapter result."""


class DryRunProviderAdapter:
    """Provider-shaped adapter that never calls external APIs."""

    def __init__(
        self,
        *,
        provider_name: str | ProviderId = ProviderId.LOCAL_MOCK,
        model_name: str = "dry-run-model",
        placeholder_rates: Mapping[str, Mapping[str, float]] | None = None,
    ) -> None:
        self.provider_name = str(validate_provider_id(provider_name))
        self.model_name = model_name
        self.placeholder_rates = dict(placeholder_rates or DEFAULT_PLACEHOLDER_PROVIDER_RATES)

    def invoke(self, request: ProviderRequest) -> ProviderAdapterResult:
        provider_name = str(validate_provider_id(request.provider_name or self.provider_name))
        model_name = request.model_name or self.model_name
        start = time.perf_counter()
        output_text = self._deterministic_output(request.prompt, request.request_id)
        input_tokens = estimate_tokens(request.prompt)
        output_tokens = estimate_tokens(output_text)
        usage = ProviderUsage(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
        )
        cost = ProviderCost(
            estimated_provider_cost=self._estimate_cost(provider_name, usage),
            actual_provider_cost=None,
        )
        latency = ProviderLatency(latency_ms=round((time.perf_counter() - start) * 1000.0, 6))
        response = ProviderResponse(
            request_id=request.request_id,
            output_text=output_text,
            provider_name=provider_name,
            model_name=model_name,
            metadata={"mode": "dry_run"},
        )
        return ProviderAdapterResult(
            request=ProviderRequest(
                request_id=request.request_id,
                prompt=request.prompt,
                provider_name=provider_name,
                model_name=model_name,
                metadata=dict(request.metadata),
            ),
            response=response,
            usage=usage,
            latency=latency,
            cost=cost,
            provider_calls=1,
            claim_level=ClaimLevel.DRY_RUN,
            has_real_provider_data=False,
            warnings=list(DRY_RUN_WARNINGS),
            external_call_attempted=False,
        )

    def _estimate_cost(self, provider_name: str, usage: ProviderUsage) -> float:
        rates = self.placeholder_rates.get(provider_name, self.placeholder_rates["local_mock"])
        input_cost = (usage.input_tokens / 1000.0) * float(rates.get("input_per_1k", 0.0))
        output_cost = (usage.output_tokens / 1000.0) * float(rates.get("output_per_1k", 0.0))
        return round(input_cost + output_cost, 8)

    @staticmethod
    def _deterministic_output(prompt: str, request_id: str) -> str:
        digest = hashlib.sha256(f"{request_id}:{prompt}".encode("utf-8")).hexdigest()[:12]
        return f"dry_run_response:{request_id}:{digest}"
