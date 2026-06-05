from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
SCRIPT_FILE = SCRIPT_DIR / "run_gpu_routed_subset_benchmark.py"
SPEC = importlib.util.spec_from_file_location("run_gpu_routed_subset_benchmark", SCRIPT_FILE)
gpu_subset = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = gpu_subset
SPEC.loader.exec_module(gpu_subset)

COMPARISON_RUN = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "evidence"
    / "routing-benchmark-runs"
    / "20260605-101501-mixed_realistic_100k-100000.json"
)


class GPURoutedSubsetBenchmarkTests(unittest.TestCase):
    def test_operation_dimension_is_bounded_and_deterministic(self) -> None:
        request = {
            "request_id": "req_000001",
            "workload_class": "gpu_tensor_transform",
            "router_visible_metadata": {"observable": {"input_size": 16384, "batch_size": 32}},
            "compute_weight": {"value": 1234.5},
        }
        self.assertEqual(gpu_subset.operation_dimension(request), gpu_subset.operation_dimension(request))
        self.assertGreaterEqual(gpu_subset.operation_dimension(request), 64)
        self.assertLessEqual(gpu_subset.operation_dimension(request), gpu_subset.MAX_DIMENSION)

    def test_selection_hash_is_deterministic(self) -> None:
        requests = [
            {"request_id": "req_000001", "workload_class": "gpu_batch_embedding", "compute_weight": {"value": 1.0}},
            {"request_id": "req_000002", "workload_class": "gpu_tensor_transform", "compute_weight": {"value": 2.0}},
        ]
        first = gpu_subset.subset_selection_hash(requests, router="kora_router_adapter", limit=2)
        second = gpu_subset.subset_selection_hash(requests, router="kora_router_adapter", limit=2)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 64)

    def test_local_validation_result_has_required_schema(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            evidence = gpu_subset.run_routed_subset_benchmark(
                comparison_run=COMPARISON_RUN,
                router="kora_router_adapter",
                limit=10,
                output_dir=Path(tmpdir),
                local_validation_only=True,
            )
        self.assertEqual(evidence["task_id"], "KORA-CHAMPION-GPU-004C")
        self.assertEqual(evidence["claim_level"], "local_validation_only")
        self.assertFalse(evidence["h100_execution"])
        self.assertFalse(evidence["claim_boundary"]["measured_h100_routed_subset"])
        self.assertFalse(evidence["live_provider_execution"])
        self.assertEqual(evidence["routing_source_metrics"]["total_requests"], 100000)
        self.assertEqual(evidence["routing_source_metrics"]["kora_local_gpu_routed_count"], 21203)
        self.assertEqual(evidence["measured_subset"]["measured_subset_count"], 10)
        self.assertEqual(evidence["gpu_runtime"]["error_count"], 0)
        json.dumps(evidence)

    def test_runtime_estimate_scales_by_compute_weight(self) -> None:
        estimate = gpu_subset.estimate_all_gpu_runtime_seconds(
            measured_runtime_seconds=10.0,
            measured_subset_compute_weight=100.0,
            all_gpu_baseline_compute_weight=250.0,
        )
        self.assertEqual(estimate, 25.0)


if __name__ == "__main__":
    unittest.main()
