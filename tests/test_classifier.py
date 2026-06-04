import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.classifier import classify_request


class ClassifierTests(unittest.TestCase):
    def test_classifies_deterministic_request(self) -> None:
        classification = classify_request({"id": "a", "deterministic_available": True})
        self.assertTrue(classification.deterministic_available)
        self.assertIn("deterministic_available", classification.reasons)

    def test_classifies_cache_eligible_and_hit(self) -> None:
        classification = classify_request({"id": "a", "cache_eligible": True, "cache_hit": True})
        self.assertTrue(classification.cache_eligible)
        self.assertTrue(classification.cache_hit)

    def test_classifies_gpu_request(self) -> None:
        classification = classify_request({"id": "a", "requires_gpu": True})
        self.assertTrue(classification.requires_gpu)

    def test_classifies_provider_request(self) -> None:
        classification = classify_request({"id": "a", "provider_required": True})
        self.assertTrue(classification.provider_required)

    def test_classifies_default_cpu_request(self) -> None:
        classification = classify_request({"id": "a"})
        self.assertEqual(classification.reasons, ("default_cpu",))


if __name__ == "__main__":
    unittest.main()
