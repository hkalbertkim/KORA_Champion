import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.routing_benchmark.comparison import compare_routing_policies
from kora_core.routing_benchmark.workload_generator import generate_workload


class RoutingBenchmarkComparisonTests(unittest.TestCase):
    def test_comparison_runs_all_required_policies(self) -> None:
        requests = [request.to_dict() for request in generate_workload("service_replay_10k", 25)]
        result = compare_routing_policies(requests)
        self.assertEqual(result["mode"], "dry_run_only")
        self.assertFalse(result["h100_execution_performed"])
        self.assertFalse(result["live_provider_execution_performed"])
        self.assertEqual(
            set(result["router_results"]),
            {"all_gpu", "static_heuristic_router", "provider_first_with_gpu_fallback", "kora_router_adapter"},
        )

    def test_comparison_records_oracle_and_router_boundaries(self) -> None:
        requests = [request.to_dict() for request in generate_workload("service_replay_10k", 10)]
        result = compare_routing_policies(requests)
        self.assertFalse(result["oracle_independence"]["oracle_generated_from_router_outputs"])
        self.assertFalse(result["oracle_independence"]["routers_read_oracle_labels"])
        self.assertIn("router_visible_metadata.observable", result["router_input_allowed_fields"])


if __name__ == "__main__":
    unittest.main()
