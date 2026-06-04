"""Offline harness primitives for routing synthetic request fixtures."""

from __future__ import annotations

import json
from pathlib import Path
from time import perf_counter
from typing import Any, Iterable, Mapping

from kora_core.cache import InMemoryCache, build_cache_key
from kora_core.classifier import RequestClassification, classify_request
from kora_core.cost_model import estimate_request_cost
from kora_core.metrics import MetricSummary, RequestMetrics, estimate_tokens
from kora_core.router import RouteDecision, route_request
from kora_core.telemetry import TelemetryEvent, record_event, summarize_events


def load_request_fixtures(path: str | Path) -> list[dict[str, Any]]:
    """Load synthetic request fixtures from JSON."""

    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("request fixture must be a JSON list")
    requests: list[dict[str, Any]] = []
    for index, item in enumerate(payload):
        if not isinstance(item, dict):
            raise ValueError(f"request fixture item {index} must be an object")
        requests.append(item)
    return requests


def _cache_key_for_request(request: Mapping[str, Any]) -> str:
    key = request.get("cache_key")
    if key:
        return str(key)
    payload = request.get("payload")
    if not isinstance(payload, Mapping):
        payload = {"id": request.get("id"), "prompt": request.get("prompt", "")}
    return build_cache_key("request", payload)


def _prepare_request_with_cache(
    request: Mapping[str, Any],
    cache: InMemoryCache,
) -> tuple[dict[str, Any], str | None, bool]:
    prepared = dict(request)
    if not bool(prepared.get("cache_eligible")) and "cache_key" not in prepared:
        return prepared, None, False

    cache_key = _cache_key_for_request(prepared)
    lookup = cache.get(cache_key)
    prepared["cache_key"] = cache_key
    prepared["cache_hit"] = lookup.hit
    return prepared, cache_key, lookup.hit


def run_request_harness(
    requests: Iterable[Mapping[str, Any]],
    *,
    cache: InMemoryCache | None = None,
) -> dict[str, Any]:
    """Classify and route synthetic requests with local telemetry only."""

    selected_cache = cache or InMemoryCache()
    events: list[TelemetryEvent] = []
    metrics: list[RequestMetrics] = []
    records: list[dict[str, Any]] = []

    for index, request in enumerate(requests):
        start = perf_counter()
        prepared, cache_key, cache_hit = _prepare_request_with_cache(request, selected_cache)
        classification = classify_request(prepared, fallback_id=f"request-{index + 1}")
        decision = route_request(prepared, classification=classification)
        latency_ms = (perf_counter() - start) * 1000.0
        prompt = str(prepared.get("prompt", ""))
        input_tokens = int(prepared.get("input_tokens", estimate_tokens(prompt)) or 0)
        output_tokens = int(prepared.get("output_tokens", 0) or 0)
        provider_calls = 0 if decision.provider_call_avoided else 1
        estimated_cost = estimate_request_cost(decision.target)

        if cache_key is not None and not cache_hit and decision.provider_call_avoided:
            selected_cache.set(cache_key, {"request_id": classification.request_id, "target": decision.target.value})

        metric = RequestMetrics(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            estimated_cost=estimated_cost,
            provider_calls=provider_calls,
        )
        metrics.append(metric)
        record_event(
            events,
            request_id=classification.request_id,
            target=decision.target,
            provider_call_avoided=decision.provider_call_avoided,
            estimated_cost=estimated_cost,
            latency_ms=latency_ms,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            metadata={"reason": decision.reason, "cache_hit": cache_hit},
        )
        records.append(_record_for(classification, decision, metric, cache_hit=cache_hit, cache_key=cache_key))

    return {
        "status": "ok",
        "external_calls_attempted": False,
        "records": records,
        "telemetry": summarize_events(events),
        "metrics": MetricSummary.from_metrics(metrics).__dict__,
    }


def _record_for(
    classification: RequestClassification,
    decision: RouteDecision,
    metric: RequestMetrics,
    *,
    cache_hit: bool,
    cache_key: str | None,
) -> dict[str, Any]:
    return {
        "request_id": classification.request_id,
        "classification": {
            "deterministic_available": classification.deterministic_available,
            "cache_eligible": classification.cache_eligible,
            "cache_hit": classification.cache_hit,
            "requires_gpu": classification.requires_gpu,
            "provider_required": classification.provider_required,
            "reasons": list(classification.reasons),
        },
        "decision": {
            "target": decision.target.value,
            "reason": decision.reason,
            "provider_call_avoided": decision.provider_call_avoided,
        },
        "cache": {"eligible": classification.cache_eligible, "hit": cache_hit, "key": cache_key},
        "metrics": metric.__dict__,
    }
