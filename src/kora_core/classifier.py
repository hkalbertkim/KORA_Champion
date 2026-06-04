"""Request classification primitives for KORA Core routing."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class RequestClassification:
    """Public-safe classification result for one synthetic request."""

    request_id: str
    deterministic_available: bool = False
    cache_eligible: bool = False
    cache_hit: bool = False
    requires_gpu: bool = False
    provider_required: bool = False
    reasons: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)


def _flag(request: Mapping[str, Any], name: str) -> bool:
    return bool(request.get(name, False))


def _request_id(request: Mapping[str, Any], fallback: str = "request") -> str:
    value = request.get("id") or request.get("request_id") or fallback
    return str(value)


def classify_request(request: Mapping[str, Any], *, fallback_id: str = "request") -> RequestClassification:
    """Classify one request without provider, network, or GPU access."""

    reasons: list[str] = []
    deterministic_available = _flag(request, "deterministic_available")
    cache_eligible = _flag(request, "cache_eligible") or _flag(request, "cache_hit") or "cache_key" in request
    cache_hit = _flag(request, "cache_hit")
    requires_gpu = _flag(request, "requires_gpu")
    provider_required = _flag(request, "provider_required")

    if deterministic_available:
        reasons.append("deterministic_available")
    if cache_eligible:
        reasons.append("cache_eligible")
    if cache_hit:
        reasons.append("cache_hit")
    if requires_gpu:
        reasons.append("requires_gpu")
    if provider_required:
        reasons.append("provider_required")
    if not reasons:
        reasons.append("default_cpu")

    metadata: dict[str, Any] = {}
    for key in ("category", "workload", "cache_key"):
        if key in request:
            metadata[key] = request[key]

    return RequestClassification(
        request_id=_request_id(request, fallback=fallback_id),
        deterministic_available=deterministic_available,
        cache_eligible=cache_eligible,
        cache_hit=cache_hit,
        requires_gpu=requires_gpu,
        provider_required=provider_required,
        reasons=tuple(reasons),
        metadata=metadata,
    )
