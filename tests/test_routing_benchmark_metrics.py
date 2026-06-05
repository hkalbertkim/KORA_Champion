import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.routing_benchmark.comparison import compare_routing_policies
from kora_core.routing_benchmark.workload_generator import generate_workload


class RoutingBenchmarkMetricsTests(unittest.TestCase):
    def test_metrics_include_required_placeholders_and_counts(self) -> None:
        requests = [request.to_dict() for request in generate_workload("service_replay_10k", 30)]
        result = compare_routing_policies(requests)
        metrics = result["router_results"]["kora_router_adapter"]
        self.assertIn("exact_route_accuracy", metrics)
        self.assertIn("acceptable_route_rate", metrics)
        self.assertIn("gpu_false_positive_count", metrics)
        self.assertIn("fallback_counts", metrics)
        self.assertEqual(metrics["quality_validation"]["enabled"], False)
        self.assertEqual(metrics["provider_validation"]["mode"], "dry_run_only")
        self.assertEqual(metrics["provider_evidence_basis"]["used_for_cost_claim"], False)

    def test_compute_weighted_gpu_metrics_are_reported(self) -> None:
        requests = [request.to_dict() for request in generate_workload("gpu_heavy_100k", 20)]
        result = compare_routing_policies(requests)
        metrics = result["router_results"]["kora_router_adapter"]
        self.assertIn("avoided_gpu_compute_units", metrics)
        self.assertIn("compute_weighted_gpu_reduction_percentage", metrics)
        self.assertIn("baseline_gpu_runtime_seconds_estimated", metrics)
        self.assertIsNone(metrics["kora_gpu_runtime_seconds_measured"])


if __name__ == "__main__":
    unittest.main()
