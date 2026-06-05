import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.routing_benchmark.schema import REQUIRED_PROFILES, validate_request
from kora_core.routing_benchmark.workload_generator import generate_workload


class RoutingBenchmarkSchemaTests(unittest.TestCase):
    def test_generated_request_matches_schema_v0_1(self) -> None:
        request = generate_workload("service_replay_10k", 1)[0].to_dict()
        validate_request(request)
        self.assertEqual(request["request_id"], "req_000001")
        self.assertEqual(request["compute_weight"]["formula_version"], "cw_v0_1")
        self.assertIn("observable", request["router_visible_metadata"])
        self.assertIn("inferred", request["router_visible_metadata"])

    def test_required_profiles_are_supported(self) -> None:
        self.assertEqual(
            REQUIRED_PROFILES,
            {
                "mixed_realistic_100k",
                "gpu_heavy_100k",
                "cache_heavy_100k",
                "adversarial_100k",
                "service_replay_10k",
            },
        )

    def test_compute_weight_formula_is_size_derived(self) -> None:
        request = generate_workload("service_replay_10k", 1)[0].to_dict()
        self.assertEqual(request["compute_weight"]["method"], "size_derived_weight")
        self.assertFalse(request["compute_weight"]["measured_weight_available"])
        self.assertGreater(request["compute_weight"]["value"], 0)


if __name__ == "__main__":
    unittest.main()
