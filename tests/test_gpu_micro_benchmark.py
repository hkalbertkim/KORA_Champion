from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
SCRIPT_FILE = SCRIPT_DIR / "run_gpu_micro_benchmark.py"
SPEC = importlib.util.spec_from_file_location("run_gpu_micro_benchmark", SCRIPT_FILE)
gpu_micro = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = gpu_micro
SPEC.loader.exec_module(gpu_micro)


def measured_base_result() -> dict[str, object]:
    return {
        "benchmark_type": "gpu_smoke",
        "workload_id": "gpu_smoke_10000",
        "workload_size": 10_000,
        "workload_unit_type": "matrix_multiply_unit",
        "started_at_utc": "2026-06-05T00:00:00+00:00",
        "ended_at_utc": "2026-06-05T00:00:10+00:00",
        "runtime_seconds": 10.0,
        "throughput_units_per_second": 1000.0,
        "gpu_count": 2,
        "gpu_model": ["NVIDIA H100 80GB HBM3"],
        "cuda_available": True,
        "torch_available": True,
        "successful_units": 10_000,
        "failed_units": 0,
        "snapshot_before": {"gpus": []},
        "snapshot_after": {"gpus": []},
        "gpu_utilization_average": 50.0,
        "gpu_utilization_max": 90.0,
        "gpu_memory_average_mb": 1024.0,
        "gpu_memory_max_mb": 2048.0,
        "claim_level": "gpu_smoke_measured",
        "warnings": ["not_gpu_reduction_evidence"],
    }


def fallback_base_result() -> dict[str, object]:
    result = measured_base_result()
    result.update(
        {
            "runtime_seconds": 0.0,
            "throughput_units_per_second": None,
            "gpu_count": 0,
            "gpu_model": [],
            "cuda_available": False,
            "torch_available": False,
            "successful_units": 0,
            "claim_level": "gpu_schema_only",
            "warnings": ["torch_not_available", "gpu_smoke_not_measured"],
        }
    )
    return result


class GPUMicroBenchmarkTests(unittest.TestCase):
    def test_micro_benchmark_result_creation(self) -> None:
        with patch.object(gpu_micro, "run_gpu_smoke_workload", return_value=measured_base_result()):
            result = gpu_micro.run_gpu_micro_benchmark()
        self.assertEqual(result["benchmark_type"], "gpu_micro_benchmark")
        self.assertEqual(result["workload_id"], "gpu_micro_benchmark_10000")
        self.assertEqual(result["workload_size"], 10_000)

    def test_micro_claim_level_requires_cuda_workload(self) -> None:
        with patch.object(gpu_micro, "run_gpu_smoke_workload", return_value=measured_base_result()):
            measured = gpu_micro.run_gpu_micro_benchmark()
        with patch.object(gpu_micro, "run_gpu_smoke_workload", return_value=fallback_base_result()):
            fallback = gpu_micro.run_gpu_micro_benchmark()
        self.assertEqual(measured["claim_level"], "gpu_micro_benchmark_measured")
        self.assertEqual(fallback["claim_level"], "gpu_schema_only")
        self.assertIn("gpu_micro_benchmark_not_measured", fallback["warnings"])

    def test_throughput_and_two_gpu_result_are_preserved(self) -> None:
        with patch.object(gpu_micro, "run_gpu_smoke_workload", return_value=measured_base_result()):
            result = gpu_micro.run_gpu_micro_benchmark()
        self.assertEqual(result["throughput_units_per_second"], 1000.0)
        self.assertEqual(result["gpu_count"], 2)
        self.assertEqual(result["gpu_model"], ["NVIDIA H100 80GB HBM3"])

    def test_output_uses_expected_public_fields(self) -> None:
        expected_keys = {
            "benchmark_type",
            "workload_id",
            "workload_size",
            "workload_unit_type",
            "started_at_utc",
            "ended_at_utc",
            "runtime_seconds",
            "throughput_units_per_second",
            "gpu_count",
            "gpu_model",
            "cuda_available",
            "torch_available",
            "successful_units",
            "failed_units",
            "snapshot_before",
            "snapshot_after",
            "gpu_utilization_average",
            "gpu_utilization_max",
            "gpu_memory_average_mb",
            "gpu_memory_max_mb",
            "claim_level",
            "warnings",
        }
        with patch.object(gpu_micro, "run_gpu_smoke_workload", return_value=measured_base_result()):
            result = gpu_micro.run_gpu_micro_benchmark()
        self.assertEqual(set(result.keys()), expected_keys)
        json.dumps(result)

    def test_custom_workload_size(self) -> None:
        base = measured_base_result()
        base["successful_units"] = 1234
        with patch.object(gpu_micro, "run_gpu_smoke_workload", return_value=base):
            result = gpu_micro.run_gpu_micro_benchmark(workload_size=1234)
        self.assertEqual(result["workload_size"], 1234)
        self.assertEqual(result["workload_id"], "gpu_micro_benchmark_1234")


if __name__ == "__main__":
    unittest.main()
