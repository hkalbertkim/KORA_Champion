import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.evidence import ClaimLevel
from kora_core.provider_harness import run_provider_harness


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE = REPO_ROOT / "tests" / "fixtures" / "sample_requests.json"


class ProviderLiveHarnessTests(unittest.TestCase):
    def test_live_harness_enforces_max_live_calls_default_one(self) -> None:
        calls = []

        def fake_transport(url, headers, payload, timeout_seconds):
            calls.append(json.loads(payload.decode("utf-8")))
            return {"usage": {"prompt_tokens": 5, "completion_tokens": 2, "total_tokens": 7}, "choices": []}

        result = run_provider_harness(
            requests=[
                {"id": "p1", "prompt": "first synthetic prompt", "provider_required": True},
                {"id": "p2", "prompt": "second synthetic prompt", "provider_required": True},
            ],
            provider_name="openai",
            model_name="gpt-4o-mini",
            mode="live",
            env={
                "KORA_PROVIDER_MODE": "live",
                "KORA_LIVE_PROVIDER": "openai",
                "KORA_OPENAI_API_KEY": "redaction-test-value",
            },
            allow_live=True,
            transport=fake_transport,
        )
        self.assertEqual(len(calls), 1)
        self.assertEqual(result.successful_provider_calls, 1)
        self.assertEqual(result.failed_provider_calls, 0)
        self.assertEqual(result.total_tokens, 7)
        self.assertEqual(result.claim_level, str(ClaimLevel.MEASURED_PROVIDER))
        self.assertTrue(result.has_real_provider_data)
        self.assertTrue(result.response_text_redacted)

    def test_live_harness_does_not_expose_secret_value(self) -> None:
        def fake_transport(url, headers, payload, timeout_seconds):
            return {"usage": {"prompt_tokens": 5, "completion_tokens": 2, "total_tokens": 7}, "choices": []}

        result = run_provider_harness(
            fixture_path=FIXTURE,
            provider_name="openai",
            model_name="gpt-4o-mini",
            mode="live",
            env={
                "KORA_PROVIDER_MODE": "live",
                "KORA_LIVE_PROVIDER": "openai",
                "KORA_OPENAI_API_KEY": "redaction-test-value",
            },
            allow_live=True,
            transport=fake_transport,
        )
        self.assertNotIn("redaction-test-value", json.dumps(result.to_dict(), sort_keys=True))

    def test_unsupported_live_provider_still_fails_safely(self) -> None:
        result = run_provider_harness(
            fixture_path=FIXTURE,
            provider_name="anthropic",
            mode="live",
            env={"KORA_PROVIDER_MODE": "live", "KORA_LIVE_PROVIDER": "anthropic"},
            allow_live=True,
        )
        self.assertEqual(result.evidence_status, "live_config_error")
        self.assertFalse(result.has_real_provider_data)

    def test_cli_live_without_allow_live_exits_nonzero(self) -> None:
        env = os.environ.copy()
        env.update(
            {
                "KORA_PROVIDER_MODE": "live",
                "KORA_LIVE_PROVIDER": "openai",
                "KORA_OPENAI_API_KEY": "redaction-test-value",
            }
        )
        completed = subprocess.run(
            [sys.executable, "scripts/run_provider_harness.py", "--mode", "live", "--provider", "openai"],
            cwd=REPO_ROOT,
            env=env,
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("live_config_error", completed.stdout)
        self.assertNotIn("redaction-test-value", completed.stdout)
        summary = json.loads(completed.stdout)
        output_path = REPO_ROOT / summary["evidence_path"]
        if output_path.exists():
            output_path.unlink()


if __name__ == "__main__":
    unittest.main()
