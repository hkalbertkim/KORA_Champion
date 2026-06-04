"""Configurable placeholder cost estimates for KORA Core v0.1."""

from __future__ import annotations

from typing import Mapping

from kora_core.execution_targets import ExecutionTarget


DEFAULT_PLACEHOLDER_COSTS: dict[ExecutionTarget, float] = {
    ExecutionTarget.DETERMINISTIC: 0.0,
    ExecutionTarget.CACHE: 0.0,
    ExecutionTarget.CPU: 0.0001,
    ExecutionTarget.LOCAL_GPU: 0.001,
    ExecutionTarget.PROVIDER_API: 0.01,
}

DEFAULT_PROVIDER_PLACEHOLDER_RATES: dict[str, dict[str, float]] = {
    "local_mock": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "openai": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "anthropic": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "gemini": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "bedrock": {"input_per_1k": 0.001, "output_per_1k": 0.002},
    "vllm": {"input_per_1k": 0.0005, "output_per_1k": 0.001},
}


def estimate_request_cost(
    target: ExecutionTarget | str,
    *,
    cost_table: Mapping[ExecutionTarget | str, float] | None = None,
) -> float:
    """Return a placeholder per-request cost estimate.

    These defaults are not provider pricing claims. Real benchmark tasks must
    pass an explicit cost table that documents source, date, provider, model,
    units, and exclusions.
    """

    selected_target = ExecutionTarget(target)
    table = cost_table or DEFAULT_PLACEHOLDER_COSTS
    return float(table.get(selected_target, table.get(selected_target.value, 0.0)))


def estimate_total_cost(
    target_counts: Mapping[ExecutionTarget | str, int],
    *,
    cost_table: Mapping[ExecutionTarget | str, float] | None = None,
) -> float:
    """Estimate total placeholder cost for target counts."""

    total = 0.0
    for target, count in target_counts.items():
        total += estimate_request_cost(target, cost_table=cost_table) * max(0, int(count))
    return round(total, 8)


def estimate_provider_placeholder_cost(
    provider_name: str,
    *,
    input_tokens: int,
    output_tokens: int,
    rates: Mapping[str, Mapping[str, float]] | None = None,
) -> float:
    """Estimate provider dry-run cost from configurable placeholder rates.

    These rates are deterministic placeholders, not current market prices.
    Live evidence must provide sourced pricing metadata before making claims.
    """

    selected_rates = rates or DEFAULT_PROVIDER_PLACEHOLDER_RATES
    provider_rates = selected_rates.get(provider_name, selected_rates["local_mock"])
    input_cost = (max(0, int(input_tokens)) / 1000.0) * float(provider_rates.get("input_per_1k", 0.0))
    output_cost = (max(0, int(output_tokens)) / 1000.0) * float(provider_rates.get("output_per_1k", 0.0))
    return round(input_cost + output_cost, 8)
