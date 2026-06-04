import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.gpu_metrics import (
    GPUClaimLevel,
    GPUDeviceSnapshot,
    GPUSample,
    summarize_gpu_run,
)


class GPUMetricsTests(unittest.TestCase):
    def test_gpu_metric_summary_creation(self) -> None:
        device = GPUDeviceSnapshot(
            gpu_provider_label="local_gpu",
            gpu_model="H100",
            gpu_count=2,
            cuda_available=True,
            driver_version="test-driver",
        )
        summary = summarize_gpu_run(
            device=device,
            workload_id="gpu_smoke_100",
            workload_size=100,
            workload_unit_type="synthetic_inference_unit",
            started_at_utc="2026-06-04T00:00:00Z",
            ended_at_utc="2026-06-04T00:00:10Z",
            runtime_seconds=10.0,
            successful_units=95,
            failed_units=5,
            samples=[
                GPUSample(utilization_percent=50, memory_used_mb=10_000),
                GPUSample(utilization_percent=80, memory_used_mb=20_000),
            ],
            latency_ms=[10, 20, 30],
            claim_level=GPUClaimLevel.GPU_SMOKE_MEASURED,
        )
        self.assertEqual(summary.throughput_units_per_second, 9.5)
        self.assertEqual(summary.gpu_utilization_average, 65.0)
        self.assertEqual(summary.gpu_utilization_max, 80.0)
        self.assertEqual(summary.gpu_memory_average_mb, 15000.0)
        self.assertEqual(summary.gpu_memory_max_mb, 20000.0)
        self.assertEqual(summary.latency_average_ms, 20.0)
        self.assertEqual(summary.latency_min_ms, 10.0)
        self.assertEqual(summary.latency_max_ms, 30.0)

    def test_missing_samples_handled_safely(self) -> None:
        device = GPUDeviceSnapshot(
            gpu_provider_label="local_gpu",
            gpu_model="unknown",
            gpu_count=0,
            cuda_available=False,
        )
        summary = summarize_gpu_run(
            device=device,
            workload_id="gpu_schema",
            workload_size=0,
            workload_unit_type="synthetic_inference_unit",
            started_at_utc="2026-06-04T00:00:00Z",
            ended_at_utc="2026-06-04T00:00:00Z",
            runtime_seconds=0.0,
            successful_units=0,
            failed_units=0,
        )
        self.assertIsNone(summary.throughput_units_per_second)
        self.assertIsNone(summary.gpu_utilization_average)
        self.assertIsNone(summary.gpu_memory_average_mb)
        self.assertIsNone(summary.latency_average_ms)


if __name__ == "__main__":
    unittest.main()
