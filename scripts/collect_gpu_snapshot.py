#!/usr/bin/env python3
"""Collect a sanitized local GPU snapshot when nvidia-smi is available."""

from __future__ import annotations

import csv
import json
import shutil
import subprocess
from datetime import datetime, timezone
from io import StringIO


QUERY_FIELDS = [
    "name",
    "index",
    "utilization.gpu",
    "memory.used",
    "memory.total",
    "temperature.gpu",
    "power.draw",
]


def main() -> int:
    nvidia_smi = shutil.which("nvidia-smi")
    if not nvidia_smi:
        print(
            json.dumps(
                {
                    "status": "unavailable",
                    "collector": "nvidia-smi",
                    "captured_at_utc": datetime.now(timezone.utc).isoformat(),
                    "cuda_available": False,
                    "gpus": [],
                    "warnings": ["nvidia_smi_not_available"],
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 0

    command = [
        nvidia_smi,
        "--query-gpu=" + ",".join(QUERY_FIELDS),
        "--format=csv,noheader,nounits",
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        print(
            json.dumps(
                {
                    "status": "error",
                    "collector": "nvidia-smi",
                    "captured_at_utc": datetime.now(timezone.utc).isoformat(),
                    "cuda_available": False,
                    "gpus": [],
                    "warnings": ["nvidia_smi_query_failed"],
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 0

    gpus = [_row_to_gpu(row) for row in csv.reader(StringIO(completed.stdout.strip())) if row]
    print(
        json.dumps(
            {
                "status": "ok",
                "collector": "nvidia-smi",
                "captured_at_utc": datetime.now(timezone.utc).isoformat(),
                "cuda_available": bool(gpus),
                "gpu_count": len(gpus),
                "gpus": gpus,
                "warnings": [],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


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


if __name__ == "__main__":
    raise SystemExit(main())
