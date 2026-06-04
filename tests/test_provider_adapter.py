import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.evidence import ClaimLevel
from kora_core.provider_adapter import DryRunProviderAdapter, ProviderRequest
from kora_core.providers import validate_provider_id


class ProviderAdapterTests(unittest.TestCase):
    def test_dry_run_provider_adapter_makes_no_external_calls(self) -> None:
        adapter = DryRunProviderAdapter()
        result = adapter.invoke(ProviderRequest(request_id="r1", prompt="hello world"))
        self.assertFalse(result.external_call_attempted)
        self.assertFalse(result.has_real_provider_data)

    def test_provider_request_creates_deterministic_response(self) -> None:
        adapter = DryRunProviderAdapter()
        request = ProviderRequest(request_id="r1", prompt="hello world")
        left = adapter.invoke(request)
        right = adapter.invoke(request)
        self.assertEqual(left.response.output_text, right.response.output_text)

    def test_token_estimate_and_cost_are_deterministic(self) -> None:
        adapter = DryRunProviderAdapter()
        request = ProviderRequest(request_id="r1", prompt="hello world")
        left = adapter.invoke(request)
        right = adapter.invoke(request)
        self.assertEqual(left.usage.input_tokens, 2)
        self.assertEqual(left.usage.input_tokens, right.usage.input_tokens)
        self.assertEqual(left.cost.estimated_provider_cost, right.cost.estimated_provider_cost)

    def test_actual_provider_cost_is_none_and_warnings_attached(self) -> None:
        adapter = DryRunProviderAdapter()
        result = adapter.invoke(ProviderRequest(request_id="r1", prompt="hello world"))
        self.assertIsNone(result.cost.actual_provider_cost)
        self.assertTrue(any("dry-run" in warning for warning in result.warnings))

    def test_provider_identifiers_are_validated(self) -> None:
        self.assertEqual(str(validate_provider_id("local_mock")), "local_mock")
        with self.assertRaises(ValueError):
            validate_provider_id("not_supported")

    def test_claim_level_is_not_measured_provider(self) -> None:
        adapter = DryRunProviderAdapter()
        result = adapter.invoke(ProviderRequest(request_id="r1", prompt="hello world"))
        self.assertEqual(result.claim_level, ClaimLevel.DRY_RUN)
        self.assertNotEqual(result.claim_level, ClaimLevel.MEASURED_PROVIDER)

    def test_no_api_key_required(self) -> None:
        adapter = DryRunProviderAdapter(provider_name="openai")
        result = adapter.invoke(ProviderRequest(request_id="r1", prompt="hello world", provider_name="openai"))
        self.assertEqual(result.response.provider_name, "openai")
        self.assertFalse(result.external_call_attempted)


if __name__ == "__main__":
    unittest.main()
