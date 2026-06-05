from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
SCRIPT_FILE = SCRIPT_DIR / "run_multi_profile_routing_benchmark.py"
SPEC = importlib.util.spec_from_file_location("run_multi_profile_routing_benchmark", SCRIPT_FILE)
multi_profile = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = multi_profile
SPEC.loader.exec_module(multi_profile)


class MultiProfileRoutingBenchmarkTests(unittest.TestCase):
    def test_default_profile_counts_include_required_profiles(self) -> None:
        self.assertEqual(
            set(multi_profile.DEFAULT_PROFILE_COUNTS),
            {
                "mixed_realistic_100k",
                "gpu_heavy_100k",
                "cache_heavy_100k",
                "adversarial_100k",
                "service_replay_10k",
            },
        )
        self.assertEqual(multi_profile.DEFAULT_PROFILE_COUNTS["service_replay_10k"], 10_000)

    def test_profile_override_parsing(self) -> None:
        counts = multi_profile.parse_profile_counts(["service_replay_10k=25"])
        self.assertEqual(counts["service_replay_10k"], 25)
        self.assertEqual(counts["mixed_realistic_100k"], 100_000)

    def test_aggregate_metrics_identify_profile_extremes(self) -> None:
        rows = [
            {
                "profile": "mixed_realistic_100k",
                "acceptable_route_rate": 1.0,
                "unsafe_misroute_rate": 0.0,
                "fallback_rate": 0.1,
                "fallback_percentage": 10.0,
                "compute_weighted_gpu_reduction_percentage": 30.0,
                "local_gpu_percentage": 20.0,
                "cache_percentage": 10.0,
            },
            {
                "profile": "gpu_heavy_100k",
                "acceptable_route_rate": 0.99,
                "unsafe_misroute_rate": 0.01,
                "fallback_rate": 0.0,
                "fallback_percentage": 0.0,
                "compute_weighted_gpu_reduction_percentage": 5.0,
                "local_gpu_percentage": 75.0,
                "cache_percentage": 0.0,
            },
        ]
        metrics = multi_profile.aggregate_kora_metrics(rows)
        self.assertEqual(metrics["profile_with_highest_gpu_demand"], "gpu_heavy_100k")
        self.assertEqual(metrics["profile_with_highest_unsafe_misroute"], "gpu_heavy_100k")
        self.assertTrue(metrics["gpu_heavy_profile_preserves_gpu_routes"])

    def test_aggregate_metrics_report_no_unsafe_profile_when_all_zero(self) -> None:
        rows = [
            {
                "profile": "mixed_realistic_100k",
                "acceptable_route_rate": 1.0,
                "unsafe_misroute_rate": 0.0,
                "fallback_rate": 0.1,
                "fallback_percentage": 10.0,
                "compute_weighted_gpu_reduction_percentage": 30.0,
                "local_gpu_percentage": 20.0,
                "cache_percentage": 10.0,
            },
            {
                "profile": "gpu_heavy_100k",
                "acceptable_route_rate": 1.0,
                "unsafe_misroute_rate": 0.0,
                "fallback_rate": 0.0,
                "fallback_percentage": 0.0,
                "compute_weighted_gpu_reduction_percentage": 5.0,
                "local_gpu_percentage": 75.0,
                "cache_percentage": 0.0,
            },
        ]
        metrics = multi_profile.aggregate_kora_metrics(rows)
        self.assertEqual(metrics["profile_with_highest_unsafe_misroute"], "none_all_profiles_zero")


if __name__ == "__main__":
    unittest.main()
