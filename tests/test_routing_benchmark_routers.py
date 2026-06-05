import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.routing_benchmark.kora_router_adapter import KORA_ROUTER_ADAPTER_DECLARATION, kora_router_adapter
from kora_core.routing_benchmark.routers import all_gpu, provider_first_with_gpu_fallback, router_input_from_request, static_heuristic_router
from kora_core.routing_benchmark.workload_generator import generate_workload


def request_for_class(workload_class: str) -> dict:
    for request in generate_workload("service_replay_10k", 40):
        if request.workload_class == workload_class:
            return request.to_dict()
    raise AssertionError(f"missing class {workload_class}")


class RoutingBenchmarkRoutersTests(unittest.TestCase):
    def test_all_gpu_routes_valid_model_work_to_gpu(self) -> None:
        request = request_for_class("provider_code_generation")
        decision = all_gpu(router_input_from_request(request))
        self.assertEqual(decision.route, "local_gpu")

    def test_static_router_uses_visible_metadata(self) -> None:
        request = request_for_class("provider_code_generation")
        decision = static_heuristic_router(router_input_from_request(request))
        self.assertEqual(decision.route, "provider")

    def test_provider_first_policy_routes_explicit_gpu_classes_to_gpu(self) -> None:
        request = request_for_class("gpu_tensor_transform")
        decision = provider_first_with_gpu_fallback(router_input_from_request(request))
        self.assertEqual(decision.route, "local_gpu")

    def test_kora_adapter_declares_prototype_boundary(self) -> None:
        self.assertEqual(KORA_ROUTER_ADAPTER_DECLARATION["adapter_type"], "benchmark_prototype")
        self.assertTrue(KORA_ROUTER_ADAPTER_DECLARATION["benchmark_specific_logic"])
        self.assertFalse(KORA_ROUTER_ADAPTER_DECLARATION["oracle_labels_used"])

    def test_kora_adapter_fallbacks_on_missing_metadata(self) -> None:
        request = request_for_class("invalid_or_missing_metadata_request")
        decision = kora_router_adapter(router_input_from_request(request))
        self.assertEqual(decision.route, "fallback")
        self.assertEqual(decision.fallback_category, "failure_fallback")


if __name__ == "__main__":
    unittest.main()
