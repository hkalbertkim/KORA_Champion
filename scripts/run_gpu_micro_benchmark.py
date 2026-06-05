#!/usr/bin/env python3
"""Run a bounded GPU micro benchmark and write sanitized evidence."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from run_gpu_smoke_workload import DEFAULT_MATRIX_SIZE, OUTPUT_DIR, run_gpu_smoke_workload


DEFAULT_WORKLOAD_SIZE = 10_000
BENCHMARK_TYPE = "gpu_micro_benchmark"
MEASURED_CLAIM_LEVEL = "gpu_micro_benchmark_measured"


def main() -> int:
    args = _parse_args()
    result = run_gpu_micro_benchmark(
        workload_size=args.workload_size,
        matrix_size=args.matrix_size,
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    evidence_path = OUTPUT_DIR / f"{_timestamp()}-gpu-micro-benchmark.json"
    evidence_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "evidence_path": str(evidence_path),
                "benchmark_type": result["benchmark_type"],
                "workload_size": result["workload_size"],
                "gpu_count": result["gpu_count"],
                "gpu_model": result["gpu_model"],
                "cuda_available": result["cuda_available"],
                "torch_available": result["torch_available"],
                "runtime_seconds": result["runtime_seconds"],
                "throughput_units_per_second": result["throughput_units_per_second"],
                "claim_level": result["claim_level"],
                "warnings": result["warnings"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def run_gpu_micro_benchmark(*, workload_size: int = DEFAULT_WORKLOAD_SIZE, matrix_size: int = DEFAULT_MATRIX_SIZE) -> dict[str, Any]:
    result = run_gpu_smoke_workload(workload_size=workload_size, matrix_size=matrix_size)
    successful_units = int(result.get("successful_units") or 0)
    cuda_available = bool(result.get("cuda_available"))
    warnings = set(result.get("warnings", []))
    warnings.discard("gpu_smoke_not_measured")

    if cuda_available and successful_units > 0:
        claim_level = MEASURED_CLAIM_LEVEL
        warnings.update(["not_gpu_reduction_evidence", "not_infrastructure_reduction_evidence"])
    else:
        claim_level = "gpu_schema_only"
        warnings.add("gpu_micro_benchmark_not_measured")

    result.update(
        {
            "benchmark_type": BENCHMARK_TYPE,
            "workload_id": f"gpu_micro_benchmark_{workload_size}",
            "workload_size": workload_size,
            "claim_level": claim_level,
            "warnings": sorted(warnings),
        }
    )
    return result


def _timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a bounded GPU micro benchmark.")
    parser.add_argument("--workload-size", type=int, default=DEFAULT_WORKLOAD_SIZE)
    parser.add_argument("--matrix-size", type=int, default=DEFAULT_MATRIX_SIZE)
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(main())
