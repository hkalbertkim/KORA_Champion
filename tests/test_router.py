import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.execution_targets import ExecutionTarget
from kora_core.router import route_request


class RouterTests(unittest.TestCase):
    def test_deterministic_request_routes_to_deterministic_target(self) -> None:
        decision = route_request({"deterministic_available": True})
        self.assertEqual(decision.target, ExecutionTarget.DETERMINISTIC)
        self.assertTrue(decision.provider_call_avoided)

    def test_cache_hit_routes_to_cache_target(self) -> None:
        decision = route_request({"cache_hit": True})
        self.assertEqual(decision.target, ExecutionTarget.CACHE)
        self.assertTrue(decision.provider_call_avoided)

    def test_gpu_request_routes_to_local_gpu_target(self) -> None:
        decision = route_request({"requires_gpu": True})
        self.assertEqual(decision.target, ExecutionTarget.LOCAL_GPU)
        self.assertTrue(decision.provider_call_avoided)

    def test_provider_required_request_routes_to_provider_api_target(self) -> None:
        decision = route_request({"provider_required": True})
        self.assertEqual(decision.target, ExecutionTarget.PROVIDER_API)
        self.assertFalse(decision.provider_call_avoided)

    def test_default_request_routes_to_cpu_target(self) -> None:
        decision = route_request({})
        self.assertEqual(decision.target, ExecutionTarget.CPU)
        self.assertTrue(decision.provider_call_avoided)


if __name__ == "__main__":
    unittest.main()
