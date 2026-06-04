import json
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ProviderDryRunScriptTests(unittest.TestCase):
    def test_provider_dry_run_script_writes_dry_run_evidence(self) -> None:
        before = set((REPO_ROOT / "docs" / "evidence" / "provider-dry-runs").glob("*-provider-dry-run.json"))
        completed = subprocess.run(
            [sys.executable, "scripts/provider_dry_run.py"],
            cwd=REPO_ROOT,
            text=True,
            check=True,
            capture_output=True,
        )
        summary = json.loads(completed.stdout)
        output_path = REPO_ROOT / summary["evidence_path"]
        self.assertTrue(output_path.exists())
        payload = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(payload["claim_level"], "dry_run")
        self.assertFalse(payload["has_real_provider_data"])
        self.assertIsNone(payload["actual_provider_cost"])
        self.assertFalse(payload["external_calls_attempted"])
        self.assertGreaterEqual(payload["provider_calls"], 1)
        if output_path not in before:
            output_path.unlink()
        after = set((REPO_ROOT / "docs" / "evidence" / "provider-dry-runs").glob("*-provider-dry-run.json"))
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
