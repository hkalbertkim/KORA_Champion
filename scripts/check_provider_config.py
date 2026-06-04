#!/usr/bin/env python3
"""Print a redacted KORA provider configuration summary."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from kora_core.config import ProviderMode, load_provider_config


def main() -> int:
    try:
        config = load_provider_config()
    except ValueError as exc:
        print(json.dumps({"status": "invalid", "error": str(exc)}, indent=2, sort_keys=True))
        return 2

    summary = config.redacted_summary()
    missing = config.missing_required_fields()
    status = "ok"
    exit_code = 0
    if config.mode == ProviderMode.LIVE and missing:
        status = "missing_required_config"
        exit_code = 2

    print(
        json.dumps(
            {
                "status": status,
                "provider_mode": str(config.mode),
                "selected_provider": str(config.provider),
                "live_execution_enabled": config.live_enabled,
                "missing_required_fields": missing,
                "redacted_summary": summary,
                "external_calls_attempted": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
