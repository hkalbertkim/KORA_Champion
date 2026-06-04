import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.live_evidence import (
    LiveEvidenceValidationError,
    normalize_live_measurement,
    validate_sanitized_live_evidence,
)


EVIDENCE_PATH = Path(__file__).resolve().parents[1] / "docs" / "evidence" / "provider-live-runs" / "20260604-112641-provider-live-bedrock.json"


class LiveEvidenceTests(unittest.TestCase):
    def test_load_sanitized_bedrock_live_evidence(self) -> None:
        measurement = normalize_live_measurement(EVIDENCE_PATH)
        self.assertEqual(measurement.provider, "bedrock")
        self.assertEqual(measurement.claim_level, "measured_provider")
        self.assertTrue(measurement.has_real_provider_data)
        self.assertTrue(measurement.response_text_redacted)

    def test_normalizes_measurement_fields(self) -> None:
        measurement = normalize_live_measurement(EVIDENCE_PATH)
        self.assertEqual(measurement.provider_calls, 1)
        self.assertEqual(measurement.successful_provider_calls, 1)
        self.assertEqual(measurement.failed_provider_calls, 0)
        self.assertEqual(measurement.input_tokens, 19)
        self.assertEqual(measurement.output_tokens, 128)
        self.assertEqual(measurement.total_tokens, 147)
        self.assertEqual(measurement.measured_latency_ms, 2187.0)
        self.assertEqual(measurement.estimated_provider_cost, 0.000275)

    def test_rejects_unredacted_adapter_output(self) -> None:
        unsafe = {
            "has_real_provider_data": True,
            "claim_level": "measured_provider",
            "response_text_redacted": True,
            "adapter_results": [{"response": {"output_text": "not redacted"}}],
        }
        with self.assertRaises(LiveEvidenceValidationError):
            validate_sanitized_live_evidence(unsafe)

    def test_rejects_secret_like_strings(self) -> None:
        unsafe = {
            "has_real_provider_data": True,
            "claim_level": "measured_provider",
            "response_text_redacted": True,
            "adapter_results": [{"response": {"output_text": "[redacted]"}}],
            "metadata": "Be" + "arer example",
        }
        with self.assertRaises(LiveEvidenceValidationError):
            validate_sanitized_live_evidence(unsafe)


if __name__ == "__main__":
    unittest.main()
