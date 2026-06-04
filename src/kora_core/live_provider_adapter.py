"""Live provider adapter boundary.

This module validates secret-safe live-provider configuration without making
external calls or importing provider SDKs.
"""

from __future__ import annotations

from kora_core.config import ProviderConfig, ProviderMode, load_provider_config
from kora_core.evidence import ClaimLevel
from kora_core.provider_adapter import (
    ProviderAdapterResult,
    ProviderCost,
    ProviderLatency,
    ProviderRequest,
    ProviderResponse,
    ProviderUsage,
)
from kora_core.providers import ProviderId, validate_provider_id


class MissingProviderCredentialError(RuntimeError):
    """Raised when live mode is requested without required provider config."""


class LiveProviderNotEnabledError(RuntimeError):
    """Raised when live provider execution is requested outside live mode."""


class UnsupportedLiveProviderError(RuntimeError):
    """Raised when a provider identifier is unsupported by the live boundary."""


class LiveProviderExecutionNotAllowedError(RuntimeError):
    """Raised when live execution lacks an explicit allow flag."""


LIVE_BOUNDARY_WARNINGS = [
    "Live provider boundary validated configuration only.",
    "No external provider API call was attempted.",
    "Live provider implementation is not enabled in this task.",
    "Boundary output must not be reported as measured provider evidence.",
]


class LiveProviderAdapter:
    """Fail-closed boundary for future live provider implementations."""

    def __init__(self, config: ProviderConfig | None = None) -> None:
        self.config = config or load_provider_config()
        self.provider = self._validate_provider(self.config.provider)
        self._validate_live_ready()

    def invoke(self, request: ProviderRequest) -> ProviderAdapterResult:
        """Return an explicit non-measured boundary result.

        Future live adapters will replace this method with provider-specific
        implementations behind the same config checks.
        """

        if self.config.mode != ProviderMode.LIVE:
            raise LiveProviderNotEnabledError("live provider execution requires KORA_PROVIDER_MODE=live")
        self._validate_live_ready()
        provider_name = str(validate_provider_id(request.provider_name or self.provider))
        response = ProviderResponse(
            request_id=request.request_id,
            output_text="live_provider_boundary_not_implemented",
            provider_name=provider_name,
            model_name=request.model_name,
            metadata={"mode": "live_boundary", "implemented": False},
        )
        return ProviderAdapterResult(
            request=ProviderRequest(
                request_id=request.request_id,
                prompt=request.prompt,
                provider_name=provider_name,
                model_name=request.model_name,
                metadata=dict(request.metadata),
            ),
            response=response,
            usage=ProviderUsage(input_tokens=0, output_tokens=0, total_tokens=0),
            latency=ProviderLatency(latency_ms=0.0, is_placeholder=True),
            cost=ProviderCost(estimated_provider_cost=0.0, actual_provider_cost=None, is_placeholder=True),
            provider_calls=0,
            claim_level=ClaimLevel.DRY_RUN,
            has_real_provider_data=False,
            warnings=list(LIVE_BOUNDARY_WARNINGS),
            external_call_attempted=False,
        )

    def _validate_live_ready(self) -> None:
        if self.config.mode != ProviderMode.LIVE:
            raise LiveProviderNotEnabledError("live provider boundary requires KORA_PROVIDER_MODE=live")
        missing = self.config.missing_required_fields()
        if missing:
            joined = ", ".join(missing)
            raise MissingProviderCredentialError(f"missing required live provider config: {joined}")

    @staticmethod
    def _validate_provider(provider: str | ProviderId) -> ProviderId:
        try:
            return validate_provider_id(provider)
        except ValueError as exc:
            raise UnsupportedLiveProviderError(str(exc)) from exc
