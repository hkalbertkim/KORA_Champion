import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.execution_targets import ExecutionTarget
from kora_core.telemetry import record_event, summarize_events


class TelemetryTests(unittest.TestCase):
    def test_summarize_events_tracks_counts_avoidance_and_cost(self) -> None:
        events = []
        record_event(
            events,
            request_id="det-1",
            target=ExecutionTarget.DETERMINISTIC,
            provider_call_avoided=True,
            estimated_cost=0.0,
        )
        record_event(
            events,
            request_id="provider-1",
            target=ExecutionTarget.PROVIDER_API,
            provider_call_avoided=False,
            estimated_cost=0.25,
        )
        record_event(
            events,
            request_id="cache-1",
            target=ExecutionTarget.CACHE,
            provider_call_avoided=True,
            estimated_cost=0.0,
        )

        summary = summarize_events(events)

        self.assertEqual(summary["total_requests"], 3)
        self.assertEqual(summary["target_counts"]["deterministic"], 1)
        self.assertEqual(summary["target_counts"]["provider_api"], 1)
        self.assertEqual(summary["target_counts"]["cache"], 1)
        self.assertEqual(summary["avoided_provider_calls"], 2)
        self.assertEqual(summary["estimated_cost"], 0.25)


if __name__ == "__main__":
    unittest.main()
