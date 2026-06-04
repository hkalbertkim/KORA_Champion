import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.config import load_provider_config
from kora_core.evidence import ClaimLevel
from kora_core.openai_live_adapter import (
    LiveProviderExecutionNotAllowedError,
    OpenAILiveProviderAdapter,
)
from kora_core.live_provider_adapter import MissingProviderCredentialError
from kora_core.provider_adapter import ProviderRequest


def _live_config(key: str = "redaction-test-value"):
    return load_provider_config(
        {
            "KORA_PROVIDER_MODE": "live",
            "KORA_LIVE_PROVIDER": "openai",
            "KORA_OPENAI_API_KEY": key,
        }
    )


class OpenAILiveAdapterTests(unittest.TestCase):
    def test_refuses_without_allow_live(self) -> None:
        with self.assertRaises(LiveProviderExecutionNotAllowedError):
            OpenAILiveProviderAdapter(_live_config(), allow_live=False)

    def test_refuses_without_kora_openai_key(self) -> None:
        config = load_provider_config({"KORA_PROVIDER_MODE": "live", "KORA_LIVE_PROVIDER": "openai"})
        with self.assertRaises(MissingProviderCredentialError):
            OpenAILiveProviderAdapter(config, allow_live=True)

    def test_redacted_config_summary_does_not_expose_key(self) -> None:
        config = _live_config()
        self.assertNotIn("redaction-test-value", json.dumps(config.redacted_summary(), sort_keys=True))

    def test_mocked_live_call_parses_usage_and_sets_measured_provider(self) -> None:
        captured = {}

        def fake_transport(url, headers, payload, timeout_seconds):
            captured["url"] = url
            captured["headers"] = dict(headers)
            captured["payload"] = payload
            captured["timeout_seconds"] = timeout_seconds
            return {
                "id": "response-test-id",
                "choices": [{"finish_reason": "stop", "message": {"content": "private response"}}],
                "usage": {"prompt_tokens": 7, "completion_tokens": 3, "total_tokens": 10},
            }

        adapter = OpenAILiveProviderAdapter(_live_config(), allow_live=True, transport=fake_transport)
        result = adapter.invoke(
            ProviderRequest(
                request_id="provider-001",
                prompt="Synthetic public fixture prompt.",
                provider_name="openai",
                model_name="gpt-4o-mini",
            )
        )
        self.assertEqual(result.usage.input_tokens, 7)
        self.assertEqual(result.usage.output_tokens, 3)
        self.assertEqual(result.usage.total_tokens, 10)
        self.assertGreaterEqual(result.latency.latency_ms, 0)
        self.assertTrue(result.has_real_provider_data)
        self.assertEqual(result.claim_level, ClaimLevel.MEASURED_PROVIDER)
        self.assertEqual(result.response.output_text, "[redacted]")
        self.assertTrue(result.response.metadata["response_text_redacted"])
        self.assertEqual(result.cost.actual_provider_cost, None)
        self.assertNotIn("redaction-test-value", result.to_dict()["response"]["metadata"].values())
        self.assertTrue(captured["headers"]["Authorization"].startswith("Bearer "))


if __name__ == "__main__":
    unittest.main()
