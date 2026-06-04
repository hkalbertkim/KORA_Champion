"""Synthetic local benchmark runner for KORA Core v0.1."""

from __future__ import annotations

from typing import Any, Iterable, Mapping

from kora_core.harness import run_request_harness


SAMPLE_REQUESTS: tuple[dict[str, Any], ...] = (
    {"id": "det-001", "deterministic_available": True},
    {"id": "cache-001", "cache_eligible": True},
    {"id": "cpu-001"},
    {"id": "gpu-001", "requires_gpu": True},
    {"id": "provider-001", "provider_required": True},
    {"id": "cache-002", "cache_eligible": True},
)


def run_synthetic_benchmark(
    requests: Iterable[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Route synthetic requests locally and return decisions plus telemetry."""

    selected_requests = list(requests or SAMPLE_REQUESTS)
    harness_result = run_request_harness(selected_requests)

    return {
        "benchmark_name": "kora_core_v0_1_synthetic_smoke",
        "status": "ok",
        "external_calls_attempted": False,
        "records": harness_result["records"],
        "decisions": [record["decision"] for record in harness_result["records"]],
        "telemetry": harness_result["telemetry"],
        "metrics": harness_result["metrics"],
        "notes": [
            "Synthetic local smoke benchmark only.",
            "No external provider, network, GPU, or model call is attempted.",
            "Future tasks should replace this with measured provider/GPU evidence.",
        ],
    }
