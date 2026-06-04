import os
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.config import load_provider_config
from kora_core.live_provider_adapter import (
    LiveProviderAdapter,
    LiveProviderNotEnabledError,
    MissingProviderCredentialError,
)
from kora_core.provider_adapter import DryRunProviderAdapter, ProviderRequest, create_provider_adapter


REPO_ROOT = Path(__file__).resolve().parents[1]


class LiveProviderAdapterBoundaryTests(unittest.TestCase):
    def test_live_mode_without_provider_credential_fails_safely(self) -> None:
        config = load_provider_config({"KORA_PROVIDER_MODE": "live", "KORA_LIVE_PROVIDER": "openai"})
        with self.assertRaises(MissingProviderCredentialError):
            LiveProviderAdapter(config)

    def test_dry_run_mode_does_not_require_credential(self) -> None:
        adapter = create_provider_adapter("openai", mode="dry_run")
        self.assertIsInstance(adapter, DryRunProviderAdapter)

    def test_live_adapter_requires_live_mode(self) -> None:
        config = load_provider_config({"KORA_PROVIDER_MODE": "dry_run", "KORA_LIVE_PROVIDER": "local_mock"})
        with self.assertRaises(LiveProviderNotEnabledError):
            LiveProviderAdapter(config)

    def test_create_provider_adapter_returns_live_boundary_when_config_valid(self) -> None:
        config = load_provider_config({"KORA_PROVIDER_MODE": "live", "KORA_LIVE_PROVIDER": "local_mock"})
        adapter = create_provider_adapter("local_mock", mode="live", config=config)
        self.assertIsInstance(adapter, LiveProviderAdapter)
        result = adapter.invoke(ProviderRequest(request_id="r1", prompt="hello"))
        self.assertFalse(result.external_call_attempted)
        self.assertFalse(result.has_real_provider_data)
        self.assertEqual(result.provider_calls, 0)

    def test_unsupported_provider_fails_clearly(self) -> None:
        with self.assertRaises(ValueError):
            create_provider_adapter("unsupported", mode="dry_run")

    def test_no_sdk_imports_or_network_dependencies_required(self) -> None:
        forbidden = {"openai", "anthropic", "boto3", "google", "requests", "httpx", "urllib"}
        before = set(sys.modules)
        config = load_provider_config({"KORA_PROVIDER_MODE": "live", "KORA_LIVE_PROVIDER": "local_mock"})
        adapter = LiveProviderAdapter(config)
        adapter.invoke(ProviderRequest(request_id="r1", prompt="hello"))
        imported = set(sys.modules) - before
        self.assertFalse(forbidden & imported)

    def test_check_provider_config_script_redacts_values(self) -> None:
        env = os.environ.copy()
        env.update(
            {
                "KORA_PROVIDER_MODE": "live",
                "KORA_LIVE_PROVIDER": "openai",
                "KORA_OPENAI_API_KEY": "redaction-test-value",
            }
        )
        completed = subprocess.run(
            [sys.executable, "scripts/check_provider_config.py"],
            cwd=REPO_ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("present", completed.stdout)
        self.assertNotIn("redaction-test-value", completed.stdout)

    def test_check_provider_config_live_missing_exits_nonzero(self) -> None:
        env = os.environ.copy()
        env.update({"KORA_PROVIDER_MODE": "live", "KORA_LIVE_PROVIDER": "openai"})
        env.pop("KORA_OPENAI_API_KEY", None)
        completed = subprocess.run(
            [sys.executable, "scripts/check_provider_config.py"],
            cwd=REPO_ROOT,
            env=env,
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("missing_required_config", completed.stdout)


if __name__ == "__main__":
    unittest.main()
