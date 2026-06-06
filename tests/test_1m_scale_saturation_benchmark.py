from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
SCRIPT_FILE = SCRIPT_DIR / "run_1m_scale_saturation_benchmark.py"
SPEC = importlib.util.spec_from_file_location("run_1m_scale_saturation_benchmark", SCRIPT_FILE)
scale = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = scale
SPEC.loader.exec_module(scale)


class ScaleSaturationBenchmarkTests(unittest.TestCase):
    def test_scale_request_profile_is_1m_label(self) -> None:
        requests = scale.generate_scale_requests(profile="mixed_realistic_1m", count=5, seed=404)
        self.assertEqual(len(requests), 5)
        self.assertEqual({request["workload_profile"] for request in requests}, {"mixed_realistic_1m"})

    def test_scale_summary_uses_compute_weight_calibration(self) -> None:
        comparison = {
            "profile": "mixed_realistic_1m",
            "workload_request_count": 10,
            "mode": "dry_run_only",
            "router_results": {
                "kora_router_adapter": {
                    "route_distribution": {
                        "local_gpu": {"count": 2, "percentage": 20.0},
                        "cache": {"count": 1, "percentage": 10.0},
                        "provider": {"count": 1, "percentage": 10.0},
                        "fallback": {"count": 1, "percentage": 10.0},
                    },
                    "acceptable_route_rate": 1.0,
                    "unsafe_misroute_rate": 0.0,
                    "compute_weighted_gpu_reduction_percentage": 25.0,
                    "baseline_gpu_compute_weight": scale.GPU_004C_COMPUTE_WEIGHT_THROUGHPUT,
                    "router_gpu_compute_weight": scale.GPU_004C_COMPUTE_WEIGHT_THROUGHPUT / 2,
                }
            },
        }
        summary = scale.build_scale_summary(comparison=comparison, summary={"rows": []})
        self.assertEqual(summary["kora_1m_summary"]["estimated_all_gpu_runtime_seconds"], 1.0)
        self.assertEqual(summary["kora_1m_summary"]["estimated_kora_gpu_routed_runtime_seconds"], 0.5)


if __name__ == "__main__":
    unittest.main()
