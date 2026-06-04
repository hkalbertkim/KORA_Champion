import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.harness import load_request_fixtures
from kora_core.live_comparison import PARTIAL_LIVE_WARNINGS, build_partial_live_provider_comparison
from kora_core.live_evidence import normalize_live_measurement


REPO_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = REPO_ROOT / "docs" / "evidence" / "provider-live-runs" / "20260604-112641-provider-live-bedrock.json"
FIXTURE_PATH = REPO_ROOT / "tests" / "fixtures" / "sample_requests.json"


class LiveComparisonTests(unittest.TestCase):
    def test_partial_live_comparison_has_required_claim_boundary(self) -> None:
        measurement = normalize_live_measurement(EVIDENCE_PATH)
        requests = load_request_fixtures(FIXTURE_PATH)
        comparison = build_partial_live_provider_comparison(measurement, requests)
        self.assertEqual(comparison.comparison_type, "partial_live_provider")
        self.assertEqual(comparison.comparison_claim_level, "measured_provider_partial")
        for warning in PARTIAL_LIVE_WARNINGS:
            self.assertIn(warning, comparison.claim_warnings)

    def test_partial_live_comparison_uses_measured_fields(self) -> None:
        measurement = normalize_live_measurement(EVIDENCE_PATH)
        requests = load_request_fixtures(FIXTURE_PATH)
        comparison = build_partial_live_provider_comparison(measurement, requests)
        self.assertEqual(comparison.workload_size, 6)
        self.assertEqual(comparison.synthetic_baseline_provider_calls, 6)
        self.assertEqual(comparison.kora_synthetic_provider_calls, 1)
        self.assertEqual(comparison.measured_provider_calls, 1)
        self.assertEqual(comparison.measured_successful_provider_calls, 1)
        self.assertEqual(comparison.measured_failed_provider_calls, 0)
        self.assertEqual(comparison.measured_tokens, 147)
        self.assertEqual(comparison.measured_latency_ms, 2187.0)

    def test_comparison_does_not_claim_reductions(self) -> None:
        measurement = normalize_live_measurement(EVIDENCE_PATH)
        requests = load_request_fixtures(FIXTURE_PATH)
        payload = build_partial_live_provider_comparison(measurement, requests).to_dict()
        self.assertFalse(payload["claims_cost_reduction"])
        self.assertFalse(payload["claims_token_reduction"])
        self.assertFalse(payload["claims_latency_reduction"])
        self.assertFalse(payload["claims_gpu_reduction"])
        self.assertFalse(payload["claims_infrastructure_reduction"])
        self.assertNotIn("not redacted", json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
