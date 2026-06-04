"""Live provider evidence normalization and safety validation."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping


SECRET_MARKERS = (
    "AB" + "SK",
    "Be" + "arer",
    "Author" + "ization",
    "KORA_BEDROCK_API" + "_KEY=",
    "KORA_OPENAI_API" + "_KEY=",
    "s" + "k-",
    "ssh" + "-rsa",
    "BEGIN OPENSSH PRIVATE" + " KEY",
)

RAW_RESPONSE_KEYS = ("raw" + "_response", "con" + "tent", "mes" + "sage")


class LiveEvidenceValidationError(ValueError):
    """Raised when live evidence is not safe for normalized public output."""


@dataclass(frozen=True)
class NormalizedLiveMeasurement:
    evidence_path: str
    provider: str
    model: str
    run_type: str
    evidence_status: str
    provider_calls: int
    successful_provider_calls: int
    failed_provider_calls: int
    input_tokens: int
    output_tokens: int
    total_tokens: int
    measured_latency_ms: float | None
    estimated_provider_cost: float | None
    actual_provider_cost: float | None
    has_real_provider_data: bool
    claim_level: str
    response_text_redacted: bool
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "evidence_path": self.evidence_path,
            "provider": self.provider,
            "model": self.model,
            "run_type": self.run_type,
            "evidence_status": self.evidence_status,
            "provider_calls": self.provider_calls,
            "successful_provider_calls": self.successful_provider_calls,
            "failed_provider_calls": self.failed_provider_calls,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "measured_latency_ms": self.measured_latency_ms,
            "estimated_provider_cost": self.estimated_provider_cost,
            "actual_provider_cost": self.actual_provider_cost,
            "has_real_provider_data": self.has_real_provider_data,
            "claim_level": self.claim_level,
            "response_text_redacted": self.response_text_redacted,
            "warnings": list(self.warnings),
        }


def load_live_evidence(path: str | Path) -> dict[str, Any]:
    selected_path = Path(path)
    payload = json.loads(selected_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise LiveEvidenceValidationError("live evidence must be a JSON object")
    return payload


def normalize_live_measurement(path: str | Path) -> NormalizedLiveMeasurement:
    selected_path = Path(path)
    payload = load_live_evidence(selected_path)
    validate_sanitized_live_evidence(payload)
    provider = str(payload.get("provider") or payload.get("selected_provider") or "")
    model = str(payload.get("model") or payload.get("selected_model") or "")
    return NormalizedLiveMeasurement(
        evidence_path=_display_path(selected_path),
        provider=provider,
        model=model,
        run_type=str(payload.get("run_type", "")),
        evidence_status=str(payload.get("evidence_status", "")),
        provider_calls=int(payload.get("provider_calls", 0) or 0),
        successful_provider_calls=int(payload.get("successful_provider_calls", 0) or 0),
        failed_provider_calls=int(payload.get("failed_provider_calls", 0) or 0),
        input_tokens=int(payload.get("input_tokens", 0) or 0),
        output_tokens=int(payload.get("output_tokens", 0) or 0),
        total_tokens=int(payload.get("total_tokens", 0) or 0),
        measured_latency_ms=_optional_float(payload.get("measured_latency_ms")),
        estimated_provider_cost=_optional_float(payload.get("estimated_provider_cost")),
        actual_provider_cost=_optional_float(payload.get("actual_provider_cost")),
        has_real_provider_data=bool(payload.get("has_real_provider_data")),
        claim_level=str(payload.get("claim_level", "")),
        response_text_redacted=bool(payload.get("response_text_redacted")),
        warnings=[str(warning) for warning in payload.get("warnings", [])],
    )


def validate_sanitized_live_evidence(payload: Mapping[str, Any]) -> None:
    if not bool(payload.get("has_real_provider_data")):
        raise LiveEvidenceValidationError("live evidence must have real provider data")
    if payload.get("claim_level") != "measured_provider":
        raise LiveEvidenceValidationError("live evidence claim level must be measured_provider")
    if not bool(payload.get("response_text_redacted")):
        raise LiveEvidenceValidationError("live evidence must redact response text")
    if _contains_secret_marker(payload):
        raise LiveEvidenceValidationError("live evidence contains a secret-like marker")
    raw_path = _first_raw_response_path(payload)
    if raw_path:
        raise LiveEvidenceValidationError(f"live evidence contains raw response field: {raw_path}")
    for result in payload.get("adapter_results", []):
        if not isinstance(result, Mapping):
            continue
        response = result.get("response")
        if isinstance(response, Mapping) and response.get("output_text") != "[redacted]":
            raise LiveEvidenceValidationError("adapter response output must be redacted")


def _contains_secret_marker(value: Any) -> bool:
    if isinstance(value, str):
        return any(marker in value for marker in SECRET_MARKERS)
    if isinstance(value, Mapping):
        return any(_contains_secret_marker(item) for item in value.values())
    if isinstance(value, list):
        return any(_contains_secret_marker(item) for item in value)
    return False


def _first_raw_response_path(value: Any, path: str = "$") -> str | None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            key_str = str(key)
            if key_str in RAW_RESPONSE_KEYS:
                return f"{path}.{key_str}"
            found = _first_raw_response_path(item, f"{path}.{key_str}")
            if found:
                return found
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found = _first_raw_response_path(item, f"{path}[{index}]")
            if found:
                return found
    return None


def _optional_float(value: Any) -> float | None:
    if value is None:
        return None
    return float(value)


def _display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(path)
