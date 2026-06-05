#!/usr/bin/env python3
"""Run a bounded GPU smoke workload and write sanitized evidence."""

from __future__ import annotations

import argparse
import csv
import importlib
import json
import shutil
import subprocess
import time
from datetime import UTC, datetime
from io import StringIO
from pathlib import Path
from typing import Any


QUERY_FIELDS = [
    "name",
    "index",
    "utilization.gpu",
    "memory.used",
    "memory.total",
    "temperature.gpu",
    "power.draw",
]

DEFAULT_WORKLOAD_SIZE = 100
DEFAULT_MATRIX_SIZE = 128
OUTPUT_DIR = Path("docs/evidence/gpu-runs")


def main() -> int:
    args = _parse_args()
    result = run_gpu_smoke_workload(
        workload_size=args.workload_size,
        matrix_size=args.matrix_size,
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    evidence_path = OUTPUT_DIR / f"{_timestamp()}-gpu-smoke-run.json"
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


def run_gpu_smoke_workload(*, workload_size: int = DEFAULT_WORKLOAD_SIZE, matrix_size: int = DEFAULT_MATRIX_SIZE) -> dict[str, Any]:
    if workload_size <= 0:
        raise ValueError("workload_size must be positive")
    if matrix_size <= 0 or matrix_size > 1024:
        raise ValueError("matrix_size must be between 1 and 1024")

    started_at = datetime.now(UTC)
    snapshot_before = collect_gpu_snapshot()
    torch_module = _load_torch()
    warnings: list[str] = []
    successful_units = 0
    failed_units = 0
    runtime_seconds: float | None = None
    torch_available = torch_module is not None
    cuda_available = False
    gpu_count = _snapshot_gpu_count(snapshot_before)
    gpu_models = _snapshot_gpu_models(snapshot_before)

    if not torch_available:
        warnings.extend(["torch_not_available", "gpu_smoke_not_measured"])
    else:
        cuda_available = bool(torch_module.cuda.is_available())
        gpu_count = int(torch_module.cuda.device_count()) if cuda_available else gpu_count
        gpu_models = _torch_gpu_models(torch_module) if cuda_available else gpu_models
        if not cuda_available:
            warnings.extend(["cuda_not_available", "gpu_smoke_not_measured"])
        else:
            workload = _run_torch_workload(
                torch_module=torch_module,
                workload_size=workload_size,
                matrix_size=matrix_size,
            )
            successful_units = workload["successful_units"]
            failed_units = workload["failed_units"]
            runtime_seconds = workload["runtime_seconds"]
            warnings.extend(workload["warnings"])

    ended_at = datetime.now(UTC)
    snapshot_after = collect_gpu_snapshot()
    if not snapshot_before.get("gpus") and not snapshot_after.get("gpus"):
        warnings.append("nvidia_smi_snapshot_unavailable")

    claim_level = "gpu_smoke_measured" if cuda_available and successful_units > 0 else "gpu_schema_only"
    runtime_value = round(runtime_seconds or 0.0, 6)
    throughput = calculate_throughput(successful_units=successful_units, runtime_seconds=runtime_value)
    utilization = summarize_snapshot_utilization([snapshot_before, snapshot_after])
    memory = summarize_snapshot_memory([snapshot_before, snapshot_after])
    if claim_level == "gpu_smoke_measured":
        warnings.extend(["not_gpu_reduction_evidence", "not_infrastructure_reduction_evidence"])

    return {
        "benchmark_type": "gpu_smoke",
        "workload_id": f"gpu_smoke_{workload_size}",
        "workload_size": workload_size,
        "workload_unit_type": "matrix_multiply_unit",
        "started_at_utc": started_at.isoformat(),
        "ended_at_utc": ended_at.isoformat(),
        "runtime_seconds": runtime_value,
        "throughput_units_per_second": throughput,
        "gpu_count": gpu_count,
        "gpu_model": gpu_models,
        "cuda_available": cuda_available,
        "torch_available": torch_available,
        "successful_units": successful_units,
        "failed_units": failed_units,
        "snapshot_before": snapshot_before,
        "snapshot_after": snapshot_after,
        "gpu_utilization_average": utilization["average"],
        "gpu_utilization_max": utilization["max"],
        "gpu_memory_average_mb": memory["average_mb"],
        "gpu_memory_max_mb": memory["max_mb"],
        "claim_level": claim_level,
        "warnings": sorted(set(warnings)),
    }


def collect_gpu_snapshot() -> dict[str, Any]:
    nvidia_smi = shutil.which("nvidia-smi")
    if not nvidia_smi:
        return {
            "status": "unavailable",
            "collector": "nvidia-smi",
            "captured_at_utc": datetime.now(UTC).isoformat(),
            "cuda_available": False,
            "gpu_count": 0,
            "gpus": [],
            "warnings": ["nvidia_smi_not_available"],
        }

    command = [
        nvidia_smi,
        "--query-gpu=" + ",".join(QUERY_FIELDS),
        "--format=csv,noheader,nounits",
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        return {
            "status": "error",
            "collector": "nvidia-smi",
            "captured_at_utc": datetime.now(UTC).isoformat(),
            "cuda_available": False,
            "gpu_count": 0,
            "gpus": [],
            "warnings": ["nvidia_smi_query_failed"],
        }
    gpus = [_row_to_gpu(row) for row in csv.reader(StringIO(completed.stdout.strip())) if row]
    return {
        "status": "ok",
        "collector": "nvidia-smi",
        "captured_at_utc": datetime.now(UTC).isoformat(),
        "cuda_available": bool(gpus),
        "gpu_count": len(gpus),
        "gpus": gpus,
        "warnings": [],
    }


def calculate_throughput(*, successful_units: int, runtime_seconds: float) -> float | None:
    if successful_units <= 0 or runtime_seconds <= 0:
        return None
    return round(successful_units / runtime_seconds, 6)


def summarize_snapshot_utilization(snapshots: list[dict[str, Any]]) -> dict[str, float | None]:
    values = [
        float(gpu["utilization_gpu_percent"])
        for snapshot in snapshots
        for gpu in snapshot.get("gpus", [])
        if gpu.get("utilization_gpu_percent") is not None
    ]
    return _summary(values)


def summarize_snapshot_memory(snapshots: list[dict[str, Any]]) -> dict[str, float | None]:
    values = [
        float(gpu["memory_used_mb"])
        for snapshot in snapshots
        for gpu in snapshot.get("gpus", [])
        if gpu.get("memory_used_mb") is not None
    ]
    summary = _summary(values)
    return {"average_mb": summary["average"], "max_mb": summary["max"]}


def _run_torch_workload(*, torch_module: Any, workload_size: int, matrix_size: int) -> dict[str, Any]:
    start = time.monotonic()
    successful_units = 0
    failed_units = 0
    warnings: list[str] = []
    device_count = max(1, int(torch_module.cuda.device_count()))
    for unit_index in range(workload_size):
        device_index = unit_index % device_count
        try:
            device = torch_module.device(f"cuda:{device_index}")
            left = torch_module.randn((matrix_size, matrix_size), device=device)
            right = torch_module.randn((matrix_size, matrix_size), device=device)
            product = left @ right
            _ = float(product[0, 0].item())
            successful_units += 1
        except Exception:
            failed_units += 1
            warnings.append("gpu_workload_unit_failed")
            break
    if successful_units:
        torch_module.cuda.synchronize()
    return {
        "successful_units": successful_units,
        "failed_units": failed_units,
        "runtime_seconds": round(time.monotonic() - start, 6),
        "warnings": warnings,
    }


def _load_torch() -> Any | None:
    try:
        return importlib.import_module("torch")
    except Exception:
        return None


def _row_to_gpu(row: list[str]) -> dict[str, object]:
    values = [value.strip() for value in row]
    return {
        "name": values[0] if len(values) > 0 else None,
        "index": _to_int(values[1]) if len(values) > 1 else None,
        "utilization_gpu_percent": _to_float(values[2]) if len(values) > 2 else None,
        "memory_used_mb": _to_float(values[3]) if len(values) > 3 else None,
        "memory_total_mb": _to_float(values[4]) if len(values) > 4 else None,
        "temperature_c": _to_float(values[5]) if len(values) > 5 else None,
        "power_draw_watts": _to_float(values[6]) if len(values) > 6 else None,
    }


def _snapshot_gpu_count(snapshot: dict[str, Any]) -> int:
    return int(snapshot.get("gpu_count") or len(snapshot.get("gpus", [])))


def _snapshot_gpu_models(snapshot: dict[str, Any]) -> list[str]:
    models = [str(gpu["name"]) for gpu in snapshot.get("gpus", []) if gpu.get("name")]
    return sorted(set(models))


def _torch_gpu_models(torch_module: Any) -> list[str]:
    return sorted({str(torch_module.cuda.get_device_name(index)) for index in range(torch_module.cuda.device_count())})


def _summary(values: list[float]) -> dict[str, float | None]:
    if not values:
        return {"average": None, "max": None}
    return {"average": round(sum(values) / len(values), 6), "max": round(max(values), 6)}


def _to_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def _to_int(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


def _timestamp() -> str:
    return datetime.now(UTC).strftime("%Y%m%d-%H%M%S")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a bounded GPU smoke workload.")
    parser.add_argument("--workload-size", type=int, default=DEFAULT_WORKLOAD_SIZE)
    parser.add_argument("--matrix-size", type=int, default=DEFAULT_MATRIX_SIZE)
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(main())
