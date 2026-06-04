import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.bedrock_live_adapter import (
    BedrockBearerLiveAdapter,
    BedrockLiveRequestError,
    bedrock_converse_endpoint,
    normalize_bedrock_model_id,
)
from kora_core.config import load_provider_config
from kora_core.evidence import ClaimLevel
from kora_core.live_provider_adapter import (
    LiveProviderExecutionNotAllowedError,
    MissingProviderCredentialError,
)
from kora_core.provider_adapter import ProviderRequest
from kora_core.provider_harness import run_provider_harness


FIXTURE = Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "sample_requests.json"


def _bedrock_config(token: str | None = "redaction-test-token", model: str = "anthropic.test-model:0"):
    env = {
        "KORA_PROVIDER_MODE": "live",
        "KORA_LIVE_PROVIDER": "bedrock",
        "KORA_AWS_REGION": "us-east-1",
        "KORA_BEDROCK_MODEL_ID": model,
    }
    if token is not None:
        env["KORA_BEDROCK_API_KEY"] = token
    return load_provider_config(env)


class BedrockLiveAdapterTests(unittest.TestCase):
    def test_refuses_without_allow_live(self) -> None:
        with self.assertRaises(LiveProviderExecutionNotAllowedError):
            BedrockBearerLiveAdapter(_bedrock_config(), allow_live=False)

    def test_refuses_without_bedrock_token(self) -> None:
        with self.assertRaises(MissingProviderCredentialError):
            BedrockBearerLiveAdapter(_bedrock_config(token=None), allow_live=True)

    def test_model_prefix_is_added_once(self) -> None:
        self.assertEqual(normalize_bedrock_model_id("anthropic.model:0"), "us.anthropic.model:0")
        self.assertEqual(normalize_bedrock_model_id("us.anthropic.model:0"), "us.anthropic.model:0")

    def test_builds_expected_endpoint(self) -> None:
        endpoint = bedrock_converse_endpoint("us-east-1", "us.anthropic.model:0")
        self.assertEqual(endpoint, "https://bedrock-runtime.us-east-1.amazonaws.com/model/us.anthropic.model:0/converse")

    def test_mocked_converse_response_parses_usage_and_redacts_text(self) -> None:
        captured = {}

        def fake_transport(url, headers, payload, timeout_seconds):
            captured["url"] = url
            captured["headers"] = dict(headers)
            captured["payload"] = json.loads(payload.decode("utf-8"))
            return {
                "output": {"message": {"content": [{"text": "mocked adapter output"}]}},
                "usage": {"inputTokens": 9, "outputTokens": 4, "totalTokens": 13},
                "metrics": {"latencyMs": 123.0},
            }

        adapter = BedrockBearerLiveAdapter(_bedrock_config(), allow_live=True, transport=fake_transport)
        result = adapter.invoke(
            ProviderRequest(
                request_id="provider-001",
                prompt="Synthetic public fixture prompt.",
                provider_name="bedrock",
                model_name="anthropic.test-model:0",
            )
        )
        self.assertEqual(captured["url"], "https://bedrock-runtime.us-east-1.amazonaws.com/model/us.anthropic.test-model:0/converse")
        self.assertEqual(captured["payload"]["inferenceConfig"]["maxTokens"], 128)
        self.assertEqual(captured["payload"]["inferenceConfig"]["temperature"], 0.2)
        self.assertTrue(captured["headers"]["Authorization"].startswith("Bearer "))
        self.assertEqual(result.usage.input_tokens, 9)
        self.assertEqual(result.usage.output_tokens, 4)
        self.assertEqual(result.usage.total_tokens, 13)
        self.assertEqual(result.latency.latency_ms, 123.0)
        self.assertTrue(result.has_real_provider_data)
        self.assertEqual(result.claim_level, ClaimLevel.MEASURED_PROVIDER)
        self.assertEqual(result.response.output_text, "[redacted]")
        self.assertTrue(result.response.metadata["response_text_redacted"])
        self.assertNotIn("redaction-test-token", json.dumps(result.to_dict(), sort_keys=True))

    def test_failure_response_is_sanitized(self) -> None:
        def failing_transport(url, headers, payload, timeout_seconds):
            raise BedrockLiveRequestError("bedrock_http_error:403")

        adapter = BedrockBearerLiveAdapter(_bedrock_config(), allow_live=True, transport=failing_transport)
        with self.assertRaises(BedrockLiveRequestError) as raised:
            adapter.invoke(
                ProviderRequest(
                    request_id="provider-001",
                    prompt="Synthetic public fixture prompt.",
                    provider_name="bedrock",
                    model_name="anthropic.test-model:0",
                )
            )
        self.assertNotIn("redaction-test-token", str(raised.exception))
        self.assertIn("bedrock_http_error:403", str(raised.exception))

    def test_harness_bounds_max_live_calls_for_bedrock(self) -> None:
        calls = []

        def fake_transport(url, headers, payload, timeout_seconds):
            calls.append(url)
            return {"usage": {"inputTokens": 3, "outputTokens": 2, "totalTokens": 5}, "metrics": {"latencyMs": 10}}

        result = run_provider_harness(
            requests=[
                {"id": "p1", "prompt": "first synthetic prompt", "provider_required": True},
                {"id": "p2", "prompt": "second synthetic prompt", "provider_required": True},
            ],
            provider_name="bedrock",
            mode="live",
            env={
                "KORA_PROVIDER_MODE": "live",
                "KORA_LIVE_PROVIDER": "bedrock",
                "KORA_BEDROCK_API_KEY": "redaction-test-token",
                "KORA_AWS_REGION": "us-east-1",
                "KORA_BEDROCK_MODEL_ID": "anthropic.test-model:0",
            },
            allow_live=True,
            max_live_calls=1,
            transport=fake_transport,
        )
        self.assertEqual(len(calls), 1)
        self.assertEqual(result.successful_provider_calls, 1)
        self.assertEqual(result.failed_provider_calls, 0)
        self.assertTrue(result.has_real_provider_data)
        self.assertEqual(result.claim_level, str(ClaimLevel.MEASURED_PROVIDER))
        self.assertNotIn("redaction-test-token", json.dumps(result.to_dict(), sort_keys=True))


if __name__ == "__main__":
    unittest.main()
