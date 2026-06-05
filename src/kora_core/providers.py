"""Provider identifiers for KORA Core dry-run and future live adapters."""

from __future__ import annotations

from kora_core.compat import StrEnum


class ProviderId(StrEnum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
    BEDROCK = "bedrock"
    VLLM = "vllm"
    LOCAL_MOCK = "local_mock"


SUPPORTED_PROVIDERS: tuple[str, ...] = tuple(str(provider) for provider in ProviderId)


def validate_provider_id(provider: str | ProviderId) -> ProviderId:
    """Validate and normalize a provider identifier."""

    try:
        return ProviderId(str(provider))
    except ValueError as exc:
        supported = ", ".join(SUPPORTED_PROVIDERS)
        raise ValueError(f"unsupported provider {provider!r}; supported providers: {supported}") from exc
