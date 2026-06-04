"""Synthetic local benchmark runner for KORA Core v0.1."""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from kora_core.cost_model import estimate_request_cost
from kora_core.router import RouteDecision, route_request
from kora_core.telemetry import TelemetryEvent, record_event, summarize_events


SAMPLE_REQUESTS: tuple[dict[str, Any], ...] = (
    {"id": "det-001", "deterministic_available": True},
    {"id": "cache-001", "cache_hit": True},
    {"id": "cpu-001"},
    {"id": "gpu-001", "requires_gpu": True},
    {"id": "provider-001", "provider_required": True},
)


def run_synthetic_benchmark(
    requests: Iterable[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Route synthetic requests locally and return decisions plus telemetry."""

    selected_requests = list(requests or SAMPLE_REQUESTS)
    events: list[TelemetryEvent] = []
    decisions: list[RouteDecision] = []

    for index, request in enumerate(selected_requests):
        decision = route_request(request)
        decisions.append(decision)
        request_id = str(request.get("id") or request.get("request_id") or f"request-{index + 1}")
        record_event(
            events,
            request_id=request_id,
            target=decision.target,
            provider_call_avoided=decision.provider_call_avoided,
            estimated_cost=estimate_request_cost(decision.target),
            metadata={"reason": decision.reason},
        )

    return {
        "benchmark_name": "kora_core_v0_1_synthetic_smoke",
        "status": "ok",
        "external_calls_attempted": False,
        "decisions": [
            {
                "target": decision.target.value,
                "reason": decision.reason,
                "provider_call_avoided": decision.provider_call_avoided,
            }
            for decision in decisions
        ],
        "telemetry": summarize_events(events),
        "notes": [
            "Synthetic local smoke benchmark only.",
            "No external provider, network, GPU, or model call is attempted.",
            "Future tasks should replace this with measured provider/GPU evidence.",
        ],
    }
