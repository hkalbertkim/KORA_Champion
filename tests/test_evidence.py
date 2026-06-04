import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.evidence import compute_routing_percentages, compute_savings, synthetic_claim_warnings


class EvidenceTests(unittest.TestCase):
    def test_routing_percentage_calculation(self) -> None:
        percentages = compute_routing_percentages({"cache": 1, "cpu": 3}, 4)
        self.assertEqual(percentages["cache"], 25.0)
        self.assertEqual(percentages["cpu"], 75.0)

    def test_savings_calculation_with_known_placeholder_numbers(self) -> None:
        savings, percentage = compute_savings(baseline_estimated_cost=10.0, estimated_total_cost=2.5)
        self.assertEqual(savings, 7.5)
        self.assertEqual(percentage, 75.0)

    def test_savings_remains_none_when_cost_data_missing(self) -> None:
        savings, percentage = compute_savings(baseline_estimated_cost=None, estimated_total_cost=2.5)
        self.assertIsNone(savings)
        self.assertIsNone(percentage)

    def test_synthetic_warning_is_attached(self) -> None:
        warnings = synthetic_claim_warnings()
        self.assertTrue(any("Synthetic-only evidence" in warning for warning in warnings))
        self.assertTrue(any("does not prove real provider cost reduction" in warning for warning in warnings))


if __name__ == "__main__":
    unittest.main()
