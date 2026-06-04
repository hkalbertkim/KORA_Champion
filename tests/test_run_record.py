import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.evidence import ClaimLevel
from kora_core.harness import load_request_fixtures, run_request_harness
from kora_core.run_record import (
    RunRecord,
    create_run_record_from_harness,
    read_run_record,
    validate_run_record_dict,
    write_run_record,
)


FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "sample_requests.json"


class RunRecordTests(unittest.TestCase):
    def _record(self, *, baseline_estimated_cost: float | None = None) -> RunRecord:
        requests = load_request_fixtures(FIXTURE_PATH)
        harness_output = run_request_harness(requests)
        return create_run_record_from_harness(
            harness_output,
            requests=requests,
            run_name="unit synthetic run",
            git_commit="test-commit",
            environment_label="unit",
            baseline_estimated_cost=baseline_estimated_cost,
        )

    def test_creates_synthetic_run_record(self) -> None:
        record = self._record()
        self.assertEqual(record.evidence_status.claim_level, ClaimLevel.SYNTHETIC_ONLY)
        self.assertTrue(record.evidence_status.is_synthetic)
        self.assertFalse(record.evidence_status.has_real_provider_data)
        self.assertFalse(record.evidence_status.has_real_gpu_data)
        self.assertEqual(record.routing.total_requests, 6)
        self.assertEqual(record.provider.provider_calls, 1)

    def test_json_serialization_deserialization(self) -> None:
        record = self._record()
        restored = RunRecord.from_json(record.to_json())
        self.assertEqual(restored.run_name, record.run_name)
        self.assertEqual(restored.routing.total_requests, record.routing.total_requests)
        self.assertEqual(restored.evidence_status.claim_level, ClaimLevel.SYNTHETIC_ONLY)

    def test_required_field_validation(self) -> None:
        payload = json.loads(self._record().to_json())
        payload.pop("routing")
        with self.assertRaises(ValueError):
            validate_run_record_dict(payload)

    def test_savings_calculation_from_record(self) -> None:
        record = self._record(baseline_estimated_cost=0.05)
        self.assertIsNotNone(record.cost.savings_estimated)
        self.assertIsNotNone(record.cost.savings_percentage_estimated)

    def test_savings_remains_none_when_missing_baseline(self) -> None:
        record = self._record()
        self.assertIsNone(record.cost.savings_estimated)
        self.assertIsNone(record.cost.savings_percentage_estimated)

    def test_evidence_output_does_not_require_provider_credentials(self) -> None:
        record = self._record()
        with tempfile.TemporaryDirectory() as tmpdir:
            output = write_run_record(record, Path(tmpdir) / "record.json")
            restored = read_run_record(output)
        self.assertEqual(restored.provider.provider_calls, 1)
        self.assertEqual(restored.provider.actual_provider_cost, None)


if __name__ == "__main__":
    unittest.main()
