import inspect
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import kora_core.routing_benchmark.oracle_generator as oracle_generator
from kora_core.routing_benchmark.routers import router_input_from_request
from kora_core.routing_benchmark.workload_generator import generate_workload


class RoutingBenchmarkOracleIndependenceTests(unittest.TestCase):
    def test_oracle_generator_does_not_import_router_adapter(self) -> None:
        source = inspect.getsource(oracle_generator)
        self.assertNotIn("kora_router_adapter", source)
        self.assertNotIn("ROUTER_POLICIES", source)

    def test_router_input_excludes_oracle_and_scoring_fields(self) -> None:
        request = generate_workload("service_replay_10k", 1)[0].to_dict()
        router_input = router_input_from_request(request)
        self.assertEqual(
            set(router_input),
            {"request_id", "workload_profile", "workload_class", "router_visible_metadata"},
        )
        self.assertNotIn("oracle_labels", router_input)
        self.assertNotIn("compute_weight", router_input)
        self.assertNotIn("validation", router_input)


if __name__ == "__main__":
    unittest.main()
