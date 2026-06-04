#!/usr/bin/env python3
"""Write a public-safe GPU benchmark plan."""

from __future__ import annotations

import json
import sys
from datetime import UTC, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from kora_core.gpu_benchmark import build_default_gpu_benchmark_plan  # noqa: E402


def main() -> int:
    plan = build_default_gpu_benchmark_plan()
    output_dir = REPO_ROOT / "docs" / "evidence" / "gpu-plans"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}-gpu-benchmark-plan.json"
    output_path.write_text(json.dumps(plan.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "plan_path": str(output_path.relative_to(REPO_ROOT)),
        "target_gpu_count": plan.target_gpu_count,
        "target_resource_deadline": plan.target_resource_deadline,
        "stages": [
            {
                "stage": stage.stage,
                "workload_size": stage.workload_size,
                "planned_batches": stage.planned_batches,
            }
            for stage in plan.stages
        ],
        "claim_boundaries": plan.claim_boundaries,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
