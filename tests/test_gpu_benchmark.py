import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.gpu_benchmark import (
    GPUBenchmarkStage,
    build_default_gpu_benchmark_plan,
    build_workload_descriptor,
    validate_stage_size,
)


class GPUBenchmarkTests(unittest.TestCase):
    def test_benchmark_plan_generation(self) -> None:
        plan = build_default_gpu_benchmark_plan()
        self.assertEqual(plan.target_gpu_count, 2)
        self.assertEqual(plan.target_resource_deadline, "2026-07-01")
        self.assertEqual([stage.stage for stage in plan.stages], ["smoke", "micro", "heavy", "saturation"])
        self.assertIn("public evidence", " ".join(plan.safety_notes).lower())

    def test_stage_size_validation(self) -> None:
        validate_stage_size(GPUBenchmarkStage.SMOKE, 10)
        validate_stage_size(GPUBenchmarkStage.MICRO, 1_000)
        with self.assertRaises(ValueError):
            validate_stage_size(GPUBenchmarkStage.SMOKE, 1_000)
        with self.assertRaises(ValueError):
            validate_stage_size(GPUBenchmarkStage.MICRO, 100)

    def test_saturation_stage_supports_large_workloads(self) -> None:
        descriptor = build_workload_descriptor(
            stage=GPUBenchmarkStage.SATURATION,
            workload_size=1_000_000,
            batch_size=10_000,
        )
        self.assertEqual(descriptor.workload_size, 1_000_000)
        self.assertEqual(descriptor.planned_batches, 100)

    def test_no_private_access_fields_required(self) -> None:
        plan = build_default_gpu_benchmark_plan().to_dict()
        text = str(plan).lower()
        self.assertNotIn("@", text)
        self.assertNotIn("://", text)


if __name__ == "__main__":
    unittest.main()
