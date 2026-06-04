"""Metric schemas for synthetic KORA Core measurement runs."""

from __future__ import annotations

from dataclasses import dataclass


def estimate_tokens(text: str) -> int:
    """Return a conservative local token placeholder based on whitespace."""

    return len(text.split()) if text.strip() else 0


@dataclass(frozen=True)
class RequestMetrics:
    """Per-request measurement placeholders."""

    input_tokens: int = 0
    output_tokens: int = 0
    latency_ms: float | None = None
    estimated_cost: float = 0.0
    provider_calls: int = 0


@dataclass(frozen=True)
class MetricSummary:
    """Aggregate measurement placeholders."""

    total_input_tokens: int
    total_output_tokens: int
    total_latency_ms: float | None
    estimated_cost: float
    provider_calls: int

    @classmethod
    def from_metrics(cls, metrics: list[RequestMetrics]) -> "MetricSummary":
        latencies = [metric.latency_ms for metric in metrics]
        return cls(
            total_input_tokens=sum(metric.input_tokens for metric in metrics),
            total_output_tokens=sum(metric.output_tokens for metric in metrics),
            total_latency_ms=(
                sum(latency for latency in latencies if latency is not None)
                if all(latency is not None for latency in latencies)
                else None
            ),
            estimated_cost=round(sum(metric.estimated_cost for metric in metrics), 8),
            provider_calls=sum(metric.provider_calls for metric in metrics),
        )
