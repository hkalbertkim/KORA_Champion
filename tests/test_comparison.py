import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.comparison import BaselinePolicy, compare_synthetic_baseline
from kora_core.evidence import ClaimLevel
from kora_core.harness import load_request_fixtures


FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "sample_requests.json"


class ComparisonTests(unittest.TestCase):
    def _requests(self) -> list[dict]:
        return load_request_fixtures(FIXTURE_PATH)

    def test_all_provider_baseline_calls_equal_workload_size(self) -> None:
        comparison = compare_synthetic_baseline(self._requests())
        self.assertEqual(comparison.baseline_provider_calls, comparison.workload_size)

    def test_kora_has_fewer_provider_calls_than_all_provider_baseline(self) -> None:
        comparison = compare_synthetic_baseline(self._requests())
        self.assertLess(comparison.kora_provider_calls, comparison.baseline_provider_calls)

    def test_avoided_provider_calls_and_reduction(self) -> None:
        comparison = compare_synthetic_baseline(self._requests())
        self.assertEqual(comparison.avoided_provider_calls, 5)
        self.assertEqual(comparison.estimated_provider_call_reduction_percentage, 83.3333)

    def test_savings_none_when_cost_missing(self) -> None:
        comparison = compare_synthetic_baseline(self._requests(), include_placeholder_costs=False)
        self.assertIsNone(comparison.baseline_estimated_cost)
        self.assertIsNone(comparison.kora_estimated_cost)
        self.assertIsNone(comparison.estimated_savings)
        self.assertIsNone(comparison.estimated_savings_percentage)

    def test_savings_computed_with_placeholder_costs(self) -> None:
        comparison = compare_synthetic_baseline(self._requests(), include_placeholder_costs=True)
        self.assertEqual(comparison.baseline_estimated_cost, 0.06)
        self.assertEqual(comparison.kora_estimated_cost, 0.0112)
        self.assertEqual(comparison.estimated_savings, 0.0488)
        self.assertEqual(comparison.estimated_savings_percentage, 81.3333)

    def test_synthetic_warning_and_claim_level(self) -> None:
        comparison = compare_synthetic_baseline(self._requests())
        self.assertEqual(comparison.comparison_claim_level, ClaimLevel.SYNTHETIC_ONLY)
        self.assertTrue(comparison.is_synthetic)
        self.assertFalse(comparison.has_real_provider_data)
        self.assertFalse(comparison.has_real_gpu_data)
        self.assertTrue(any("synthetic" in warning.lower() for warning in comparison.warnings))

    def test_all_local_gpu_baseline_has_no_provider_reduction(self) -> None:
        comparison = compare_synthetic_baseline(
            self._requests(),
            baseline_policy=BaselinePolicy.ALL_LOCAL_GPU,
        )
        self.assertEqual(comparison.baseline_provider_calls, 0)
        self.assertIsNone(comparison.estimated_provider_call_reduction_percentage)


if __name__ == "__main__":
    unittest.main()
