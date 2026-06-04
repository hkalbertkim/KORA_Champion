import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.config import ProviderMode, load_provider_config


class ProviderConfigTests(unittest.TestCase):
    def test_default_mode_is_dry_run(self) -> None:
        config = load_provider_config({})
        self.assertEqual(config.mode, ProviderMode.DRY_RUN)
        self.assertEqual(str(config.provider), "local_mock")

    def test_missing_env_vars_do_not_crash(self) -> None:
        config = load_provider_config({})
        self.assertEqual(config.missing_required_fields(), [])

    def test_redacted_summary_does_not_expose_secret_value(self) -> None:
        config = load_provider_config(
            {
                "KORA_PROVIDER_MODE": "live",
                "KORA_LIVE_PROVIDER": "openai",
                "KORA_OPENAI_API_KEY": "redaction-test-value",
            }
        )
        summary = str(config.redacted_summary())
        self.assertIn("present", summary)
        self.assertNotIn("secret-test-value", summary)

    def test_dotenv_is_not_read_automatically(self) -> None:
        original_cwd = Path.cwd()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            (temp_path / ".env").write_text(
                "KORA_PROVIDER_MODE=live\nKORA_LIVE_PROVIDER=openai\nKORA_OPENAI_API_KEY=redaction-test-value\n",
                encoding="utf-8",
            )
            os.chdir(temp_path)
            try:
                config = load_provider_config({})
            finally:
                os.chdir(original_cwd)
        self.assertEqual(config.mode, ProviderMode.DRY_RUN)
        self.assertNotEqual(config.openai_api_key, "redaction-test-value")

    def test_invalid_provider_fails_clearly(self) -> None:
        with self.assertRaises(ValueError):
            load_provider_config({"KORA_LIVE_PROVIDER": "unsupported"})


if __name__ == "__main__":
    unittest.main()
