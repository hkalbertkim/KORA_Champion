"""Minimal offline workload router for KORA Core v0.1."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from kora_core.execution_targets import ExecutionTarget


@dataclass(frozen=True)
class RouteDecision:
    """Structured routing decision returned by the v0.1 router."""

    target: ExecutionTarget
    reason: str
    provider_call_avoided: bool
    metadata: dict[str, Any] = field(default_factory=dict)


def _flag(request: Mapping[str, Any], name: str) -> bool:
    return bool(request.get(name, False))


def route_request(request: Mapping[str, Any]) -> RouteDecision:
    """Route one request without making external calls.

    Priority order is deterministic, cache, local GPU, provider API, then CPU.
    The ordering intentionally prefers local/no-provider execution when a
    request explicitly declares that path is available.
    """

    request_id = request.get("id") or request.get("request_id")
    metadata = {"request_id": request_id} if request_id is not None else {}

    if _flag(request, "deterministic_available"):
        return RouteDecision(
            target=ExecutionTarget.DETERMINISTIC,
            reason="deterministic_available",
            provider_call_avoided=True,
            metadata=metadata,
        )

    if _flag(request, "cache_hit"):
        return RouteDecision(
            target=ExecutionTarget.CACHE,
            reason="cache_hit",
            provider_call_avoided=True,
            metadata=metadata,
        )

    if _flag(request, "requires_gpu"):
        return RouteDecision(
            target=ExecutionTarget.LOCAL_GPU,
            reason="requires_gpu",
            provider_call_avoided=True,
            metadata=metadata,
        )

    if _flag(request, "provider_required"):
        return RouteDecision(
            target=ExecutionTarget.PROVIDER_API,
            reason="provider_required",
            provider_call_avoided=False,
            metadata=metadata,
        )

    return RouteDecision(
        target=ExecutionTarget.CPU,
        reason="default_cpu",
        provider_call_avoided=True,
        metadata=metadata,
    )
