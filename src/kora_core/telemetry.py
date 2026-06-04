"""In-memory telemetry collection for KORA Core v0.1."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable

from kora_core.cost_model import estimate_total_cost
from kora_core.execution_targets import ExecutionTarget


@dataclass(frozen=True)
class TelemetryEvent:
    """One local routing telemetry event."""

    request_id: str
    target: ExecutionTarget
    provider_call_avoided: bool
    estimated_cost: float
    metadata: dict[str, Any] = field(default_factory=dict)


def record_event(
    events: list[TelemetryEvent],
    *,
    request_id: str,
    target: ExecutionTarget | str,
    provider_call_avoided: bool,
    estimated_cost: float = 0.0,
    metadata: dict[str, Any] | None = None,
) -> TelemetryEvent:
    """Append one event to an in-memory event list and return it."""

    event = TelemetryEvent(
        request_id=request_id,
        target=ExecutionTarget(target),
        provider_call_avoided=bool(provider_call_avoided),
        estimated_cost=float(estimated_cost),
        metadata=dict(metadata or {}),
    )
    events.append(event)
    return event


def summarize_events(events: Iterable[TelemetryEvent]) -> dict[str, Any]:
    """Summarize local route telemetry."""

    event_list = list(events)
    target_counts: dict[str, int] = {}
    avoided_provider_calls = 0
    explicit_estimated_cost = 0.0

    for event in event_list:
        target_key = event.target.value
        target_counts[target_key] = target_counts.get(target_key, 0) + 1
        if event.provider_call_avoided:
            avoided_provider_calls += 1
        explicit_estimated_cost += event.estimated_cost

    fallback_cost = estimate_total_cost(target_counts)
    estimated_cost = explicit_estimated_cost if event_list else 0.0
    if estimated_cost == 0.0 and event_list:
        estimated_cost = fallback_cost

    return {
        "total_requests": len(event_list),
        "target_counts": dict(sorted(target_counts.items())),
        "avoided_provider_calls": avoided_provider_calls,
        "estimated_cost": round(estimated_cost, 8),
    }
