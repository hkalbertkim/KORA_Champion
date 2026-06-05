from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT_FILE = Path(__file__).resolve().parents[1] / "scripts" / "run_gpu_smoke_workload.py"
SPEC = importlib.util.spec_from_file_location("run_gpu_smoke_workload", SCRIPT_FILE)
gpu_smoke = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = gpu_smoke
SPEC.loader.exec_module(gpu_smoke)


class FakeCuda:
    def __init__(self, *, available: bool, count: int) -> None:
        self._available = available
        self._count = count
        self.synchronized = False

    def is_available(self) -> bool:
        return self._available

    def device_count(self) -> int:
        return self._count

    def get_device_name(self, index: int) -> str:
        return f"NVIDIA Test GPU {index}"

    def synchronize(self) -> None:
        self.synchronized = True


class FakeTensor:
    def __matmul__(self, other: object) -> "FakeTensor":
        return self

    def __getitem__(self, key: object) -> "FakeTensor":
        return self

    def item(self) -> float:
        return 1.0


class FakeTorch:
    def __init__(self, *, available: bool, count: int) -> None:
        self.cuda = FakeCuda(available=available, count=count)

    def device(self, value: str) -> str:
        return value

    def randn(self, shape: tuple[int, int], device: str) -> FakeTensor:
        return FakeTensor()


def empty_snapshot() -> dict[str, object]:
    return {
        "status": "unavailable",
        "collector": "nvidia-smi",
        "captured_at_utc": "2026-06-05T00:00:00+00:00",
        "cuda_available": False,
        "gpu_count": 0,
        "gpus": [],
        "warnings": ["nvidia_smi_not_available"],
    }


def two_gpu_snapshot() -> dict[str, object]:
    return {
        "status": "ok",
        "collector": "nvidia-smi",
        "captured_at_utc": "2026-06-05T00:00:00+00:00",
        "cuda_available": True,
        "gpu_count": 2,
        "gpus": [
            {"name": "NVIDIA H100", "index": 0, "utilization_gpu_percent": 40.0, "memory_used_mb": 1024.0},
            {"name": "NVIDIA H100", "index": 1, "utilization_gpu_percent": 60.0, "memory_used_mb": 2048.0},
        ],
        "warnings": [],
    }


class GPUSmokeWorkloadTests(unittest.TestCase):
    def test_throughput_calculation(self) -> None:
        self.assertEqual(gpu_smoke.calculate_throughput(successful_units=100, runtime_seconds=2.0), 50.0)
        self.assertIsNone(gpu_smoke.calculate_throughput(successful_units=0, runtime_seconds=2.0))
        self.assertIsNone(gpu_smoke.calculate_throughput(successful_units=100, runtime_seconds=0.0))

    def test_torch_unavailable_safe_result(self) -> None:
        with patch.object(gpu_smoke, "_load_torch", return_value=None), patch.object(
            gpu_smoke, "collect_gpu_snapshot", return_value=empty_snapshot()
        ):
            result = gpu_smoke.run_gpu_smoke_workload(workload_size=100)
        self.assertFalse(result["torch_available"])
        self.assertFalse(result["cuda_available"])
        self.assertEqual(result["claim_level"], "gpu_schema_only")
        self.assertIn("torch_not_available", result["warnings"])
        self.assertEqual(result["successful_units"], 0)
        json.dumps(result)

    def test_cuda_unavailable_safe_result(self) -> None:
        fake_torch = FakeTorch(available=False, count=0)
        with patch.object(gpu_smoke, "_load_torch", return_value=fake_torch), patch.object(
            gpu_smoke, "collect_gpu_snapshot", return_value=empty_snapshot()
        ):
            result = gpu_smoke.run_gpu_smoke_workload(workload_size=100)
        self.assertTrue(result["torch_available"])
        self.assertFalse(result["cuda_available"])
        self.assertEqual(result["claim_level"], "gpu_schema_only")
        self.assertIn("cuda_not_available", result["warnings"])

    def test_one_gpu_visible_result(self) -> None:
        fake_torch = FakeTorch(available=True, count=1)
        with patch.object(gpu_smoke, "_load_torch", return_value=fake_torch), patch.object(
            gpu_smoke, "collect_gpu_snapshot", return_value=two_gpu_snapshot()
        ):
            result = gpu_smoke.run_gpu_smoke_workload(workload_size=3)
        self.assertEqual(result["gpu_count"], 1)
        self.assertEqual(result["successful_units"], 3)
        self.assertEqual(result["claim_level"], "gpu_smoke_measured")
        self.assertGreater(result["throughput_units_per_second"], 0)

    def test_two_gpu_visible_result(self) -> None:
        fake_torch = FakeTorch(available=True, count=2)
        with patch.object(gpu_smoke, "_load_torch", return_value=fake_torch), patch.object(
            gpu_smoke, "collect_gpu_snapshot", return_value=two_gpu_snapshot()
        ):
            result = gpu_smoke.run_gpu_smoke_workload(workload_size=4)
        self.assertEqual(result["gpu_count"], 2)
        self.assertEqual(result["gpu_model"], ["NVIDIA Test GPU 0", "NVIDIA Test GPU 1"])
        self.assertEqual(result["claim_level"], "gpu_smoke_measured")
        self.assertEqual(result["gpu_utilization_average"], 50.0)
        self.assertEqual(result["gpu_memory_max_mb"], 2048.0)

    def test_result_uses_expected_public_fields(self) -> None:
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
        with patch.object(gpu_smoke, "_load_torch", return_value=None), patch.object(
            gpu_smoke, "collect_gpu_snapshot", return_value=empty_snapshot()
        ):
            result = gpu_smoke.run_gpu_smoke_workload(workload_size=100)
        self.assertEqual(set(result.keys()), expected_keys)
        json.dumps(result)


if __name__ == "__main__":
    unittest.main()
