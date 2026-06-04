import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.harness import load_request_fixtures, run_request_harness


FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "sample_requests.json"


class HarnessTests(unittest.TestCase):
    def test_fixture_run_produces_route_decisions(self) -> None:
        result = run_request_harness(load_request_fixtures(FIXTURE_PATH))
        self.assertEqual(result["status"], "ok")
        self.assertFalse(result["external_calls_attempted"])
        self.assertEqual(len(result["records"]), 6)
        targets = [record["decision"]["target"] for record in result["records"]]
        self.assertIn("deterministic", targets)
        self.assertIn("cache", targets)
        self.assertIn("local_gpu", targets)
        self.assertIn("provider_api", targets)
        self.assertIn("cpu", targets)

    def test_repeated_cacheable_request_can_hit_cache(self) -> None:
        result = run_request_harness(load_request_fixtures(FIXTURE_PATH))
        cache_records = [
            record for record in result["records"] if record["cache"]["key"] == "fixture-cache-alpha"
        ]
        self.assertEqual(len(cache_records), 2)
        self.assertFalse(cache_records[0]["cache"]["hit"])
        self.assertTrue(cache_records[1]["cache"]["hit"])
        self.assertEqual(cache_records[1]["decision"]["target"], "cache")

    def test_telemetry_summary_includes_expected_fields(self) -> None:
        result = run_request_harness(load_request_fixtures(FIXTURE_PATH))
        telemetry = result["telemetry"]
        self.assertEqual(telemetry["total_requests"], 6)
        self.assertIn("target_counts", telemetry)
        self.assertIn("avoided_provider_calls", telemetry)
        self.assertIn("estimated_cost", telemetry)
        self.assertIn("total_input_tokens", telemetry)
        self.assertIn("total_latency_ms", telemetry)
        self.assertEqual(result["metrics"]["provider_calls"], 1)


if __name__ == "__main__":
    unittest.main()
