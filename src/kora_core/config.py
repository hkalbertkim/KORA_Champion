"""Secret-safe KORA Core configuration loading."""

from __future__ import annotations

import os
from dataclasses import dataclass
from enum import StrEnum
from typing import Mapping

from kora_core.providers import ProviderId, validate_provider_id


class ProviderMode(StrEnum):
    DRY_RUN = "dry_run"
    LIVE = "live"


ENV_PROVIDER_MODE = "KORA_PROVIDER_MODE"
ENV_LIVE_PROVIDER = "KORA_LIVE_PROVIDER"
ENV_OPENAI_KEY = "KORA_OPENAI_API_KEY"
ENV_ANTHROPIC_KEY = "KORA_ANTHROPIC_API_KEY"
ENV_GEMINI_KEY = "KORA_GEMINI_API_KEY"
ENV_BEDROCK_KEY = "KORA_BEDROCK_API_KEY"
ENV_BEDROCK_MODEL_ID = "KORA_BEDROCK_MODEL_ID"
ENV_AWS_REGION = "KORA_AWS_REGION"
ENV_AWS_PROFILE = "KORA_AWS_PROFILE"
ENV_VLLM_BASE_URL = "KORA_VLLM_BASE_URL"

SUPPORTED_PROVIDER_MODES: tuple[str, ...] = tuple(str(mode) for mode in ProviderMode)

PROVIDER_REQUIRED_ENV: dict[ProviderId, tuple[str, ...]] = {
    ProviderId.OPENAI: (ENV_OPENAI_KEY,),
    ProviderId.ANTHROPIC: (ENV_ANTHROPIC_KEY,),
    ProviderId.GEMINI: (ENV_GEMINI_KEY,),
    ProviderId.BEDROCK: (ENV_BEDROCK_KEY, ENV_AWS_REGION, ENV_BEDROCK_MODEL_ID),
    ProviderId.VLLM: (ENV_VLLM_BASE_URL,),
    ProviderId.LOCAL_MOCK: (),
}


@dataclass(frozen=True)
class ProviderConfig:
    mode: ProviderMode
    provider: ProviderId
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    gemini_api_key: str | None = None
    bedrock_api_key: str | None = None
    bedrock_model_id: str | None = None
    aws_region: str | None = None
    aws_profile: str | None = None
    vllm_base_url: str | None = None

    @property
    def live_enabled(self) -> bool:
        return self.mode == ProviderMode.LIVE

    def missing_required_fields(self) -> list[str]:
        missing = []
        values = self._env_values()
        for env_name in PROVIDER_REQUIRED_ENV[self.provider]:
            if not values.get(env_name):
                missing.append(env_name)
        return missing

    def redacted_summary(self) -> dict[str, object]:
        values = self._env_values()
        return {
            "mode": str(self.mode),
            "provider": str(self.provider),
            "live_enabled": self.live_enabled,
            "required_fields_missing": self.missing_required_fields(),
            "credentials": {
                ENV_OPENAI_KEY: _presence(values[ENV_OPENAI_KEY]),
                ENV_ANTHROPIC_KEY: _presence(values[ENV_ANTHROPIC_KEY]),
                ENV_GEMINI_KEY: _presence(values[ENV_GEMINI_KEY]),
                ENV_BEDROCK_KEY: _presence(values[ENV_BEDROCK_KEY]),
            },
            "runtime_config": {
                ENV_AWS_REGION: _presence(values[ENV_AWS_REGION]),
                ENV_AWS_PROFILE: _presence(values[ENV_AWS_PROFILE]),
                ENV_BEDROCK_MODEL_ID: _presence(values[ENV_BEDROCK_MODEL_ID]),
                ENV_VLLM_BASE_URL: _presence(values[ENV_VLLM_BASE_URL]),
            },
        }

    def _env_values(self) -> dict[str, str | None]:
        return {
            ENV_OPENAI_KEY: self.openai_api_key,
            ENV_ANTHROPIC_KEY: self.anthropic_api_key,
            ENV_GEMINI_KEY: self.gemini_api_key,
            ENV_BEDROCK_KEY: self.bedrock_api_key,
            ENV_BEDROCK_MODEL_ID: self.bedrock_model_id,
            ENV_AWS_REGION: self.aws_region,
            ENV_AWS_PROFILE: self.aws_profile,
            ENV_VLLM_BASE_URL: self.vllm_base_url,
        }


def load_provider_config(env: Mapping[str, str] | None = None) -> ProviderConfig:
    """Load KORA provider config from environment variables only.

    This function intentionally does not read `.env` files. Local dotenv
    loading belongs in caller-owned tooling, not the public core library.
    """

    selected_env = os.environ if env is None else env
    mode = _parse_mode(selected_env.get(ENV_PROVIDER_MODE, ProviderMode.DRY_RUN))
    provider = validate_provider_id(selected_env.get(ENV_LIVE_PROVIDER, ProviderId.LOCAL_MOCK))
    return ProviderConfig(
        mode=mode,
        provider=provider,
        openai_api_key=_blank_to_none(selected_env.get(ENV_OPENAI_KEY)),
        anthropic_api_key=_blank_to_none(selected_env.get(ENV_ANTHROPIC_KEY)),
        gemini_api_key=_blank_to_none(selected_env.get(ENV_GEMINI_KEY)),
        bedrock_api_key=_blank_to_none(selected_env.get(ENV_BEDROCK_KEY)),
        bedrock_model_id=_blank_to_none(selected_env.get(ENV_BEDROCK_MODEL_ID)),
        aws_region=_blank_to_none(selected_env.get(ENV_AWS_REGION)),
        aws_profile=_blank_to_none(selected_env.get(ENV_AWS_PROFILE)),
        vllm_base_url=_blank_to_none(selected_env.get(ENV_VLLM_BASE_URL)),
    )


def _parse_mode(value: str | ProviderMode) -> ProviderMode:
    try:
        return ProviderMode(str(value))
    except ValueError as exc:
        supported = ", ".join(SUPPORTED_PROVIDER_MODES)
        raise ValueError(f"unsupported provider mode {value!r}; supported modes: {supported}") from exc


def _blank_to_none(value: str | None) -> str | None:
    if value is None:
        return None
    stripped = value.strip()
    return stripped or None


def _presence(value: str | None) -> str:
    return "present" if value else "missing"
