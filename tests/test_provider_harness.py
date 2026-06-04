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


class ProviderHarnessTests(unittest.TestCase):
    def test_default_harness_mode_is_dry_run(self) -> None:
        result = run_provider_harness(fixture_path=FIXTURE)
        self.assertEqual(result.mode, "dry_run")

    def test_dry_run_harness_outputs_provider_metrics(self) -> None:
        result = run_provider_harness(fixture_path=FIXTURE, provider_name="local_mock")
        self.assertEqual(result.evidence_status, "dry_run_complete")
        self.assertEqual(result.provider_request_count, 1)
        self.assertEqual(result.provider_calls, 1)
        self.assertEqual(result.input_tokens, 11)
        self.assertEqual(result.output_tokens, 1)
        self.assertEqual(result.total_tokens, 12)
        self.assertFalse(result.has_real_provider_data)
        self.assertEqual(result.claim_level, str(ClaimLevel.DRY_RUN))
        self.assertIsNone(result.actual_provider_cost)
        self.assertTrue(result.warnings)

    def test_no_api_key_required_in_dry_run_mode(self) -> None:
        result = run_provider_harness(fixture_path=FIXTURE, provider_name="openai", mode="dry_run", env={})
        self.assertEqual(result.selected_provider, "openai")
        self.assertFalse(result.has_real_provider_data)

    def test_live_mode_without_required_config_fails_safely(self) -> None:
        result = run_provider_harness(
            fixture_path=FIXTURE,
            provider_name="openai",
            mode="live",
            env={"KORA_PROVIDER_MODE": "live", "KORA_LIVE_PROVIDER": "openai"},
        )
        self.assertEqual(result.evidence_status, "live_config_error")
        self.assertFalse(result.has_real_provider_data)
        self.assertEqual(result.provider_calls, 0)
        self.assertTrue(result.errors)

    def test_live_mode_with_key_without_allow_live_fails_safely(self) -> None:
        result = run_provider_harness(
            fixture_path=FIXTURE,
            provider_name="openai",
            mode="live",
            env={
                "KORA_PROVIDER_MODE": "live",
                "KORA_LIVE_PROVIDER": "openai",
                "KORA_OPENAI_API_KEY": "redaction-test-value",
            },
        )
        self.assertEqual(result.evidence_status, "live_config_error")
        self.assertFalse(result.external_calls_attempted)
        self.assertFalse(result.has_real_provider_data)

    def test_live_mode_does_not_expose_secret_values(self) -> None:
        result = run_provider_harness(
            fixture_path=FIXTURE,
            provider_name="openai",
            mode="live",
            env={
                "KORA_PROVIDER_MODE": "live",
                "KORA_LIVE_PROVIDER": "openai",
                "KORA_OPENAI_API_KEY": "redaction-test-value",
            },
        )
        payload = json.dumps(result.to_dict(), sort_keys=True)
        self.assertNotIn("redaction-test-value", payload)

    def test_live_boundary_result_is_not_measured_provider(self) -> None:
        result = run_provider_harness(
            fixture_path=FIXTURE,
            provider_name="local_mock",
            mode="live",
            env={"KORA_PROVIDER_MODE": "live", "KORA_LIVE_PROVIDER": "local_mock"},
        )
        self.assertEqual(result.evidence_status, "live_boundary_not_implemented")
        self.assertFalse(result.has_real_provider_data)
        self.assertNotEqual(result.claim_level, str(ClaimLevel.MEASURED_PROVIDER))
        self.assertEqual(result.provider_calls, 0)

    def test_unsupported_provider_fails_clearly(self) -> None:
        with self.assertRaises(ValueError):
            run_provider_harness(fixture_path=FIXTURE, provider_name="unsupported")

    def test_harness_script_writes_dry_run_evidence(self) -> None:
        before = set((REPO_ROOT / "docs" / "evidence" / "provider-harness").glob("*provider-harness*.json"))
        completed = subprocess.run(
            [sys.executable, "scripts/run_provider_harness.py"],
            cwd=REPO_ROOT,
            text=True,
            check=True,
            capture_output=True,
        )
        summary = json.loads(completed.stdout)
        output_path = REPO_ROOT / summary["evidence_path"]
        self.assertTrue(output_path.exists())
        payload = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(payload["mode"], "dry_run")
        self.assertFalse(payload["has_real_provider_data"])
        self.assertIsNone(payload["actual_provider_cost"])
        self.assertTrue(payload["warnings"])
        if output_path not in before:
            output_path.unlink()
        after = set((REPO_ROOT / "docs" / "evidence" / "provider-harness").glob("*provider-harness*.json"))
        self.assertEqual(before, after)

    def test_harness_script_live_negative_exits_nonzero_without_secret(self) -> None:
        env = os.environ.copy()
        env.update({"KORA_PROVIDER_MODE": "live", "KORA_LIVE_PROVIDER": "openai"})
        env.pop("KORA_OPENAI_API_KEY", None)
        completed = subprocess.run(
            [
                sys.executable,
                "scripts/run_provider_harness.py",
                "--mode",
                "live",
                "--provider",
                "openai",
            ],
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
