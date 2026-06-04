# KORA-CHAMPION-009 Provider Harness Switch Report

## Summary

Task 009 added the canonical provider harness switch for KORA Core. The harness runs provider-shaped dry-run evidence by default and gates live intent through the secret-safe live provider boundary.

No real provider calls, provider credentials, GPU usage, or infrastructure evidence were added.

## Files Created

- `src/kora_core/provider_harness.py`
- `scripts/run_provider_harness.py`
- `tests/test_provider_harness.py`
- `docs/evidence/provider-harness/.gitkeep`
- `docs/evidence/provider-harness/20260604-084815-provider-harness-dry_run-local_mock.json`
- `docs/architecture/provider-harness-switch.md`
- `docs/reports/kora-champion-009-provider-harness-switch-report.md`

## Files Changed

- `README.md`
- `src/kora_core/__init__.py`
- `scripts/provider_dry_run.py`
- `docs/architecture/provider-live-boundary.md`
- `docs/evidence/README.md`
- `docs/roadmap/kora-ai-champion-roadmap.md`

## Generated Provider Harness JSON Path

`docs/evidence/provider-harness/20260604-084815-provider-harness-dry_run-local_mock.json`

## Provider Harness Headline Numbers

- Mode: `dry_run`
- Provider: `local_mock`
- Model: `dry-run-model`
- Provider-routed fixture requests: 1
- Provider calls: 1
- Input tokens: 11
- Output tokens: 1
- Total tokens: 12
- Estimated provider cost: 0.000013
- Actual provider cost: null
- Claim level: `dry_run`
- Real provider data: false
- Evidence status: `dry_run_complete`

## Dry-Run Result

Dry-run mode completed successfully without credentials and without external calls. It produced provider-shaped JSON evidence with warnings and dry-run claim status.

## Live-Mode Safety Behavior

Live mode without required OpenAI config fails safely:

```bash
KORA_PROVIDER_MODE=live KORA_LIVE_PROVIDER=openai python3 scripts/run_provider_harness.py --mode live --provider openai
```

The result exits nonzero with `evidence_status: live_config_error`, zero provider calls, no real provider data, and no secret values printed.

If live config is valid but no live adapter exists, the harness returns `live_boundary_not_implemented` and does not claim measured provider evidence.

## Validation Results

Validation commands run:

- `python3 -m py_compile src/kora_core/*.py scripts/*.py`
- `python3 scripts/run_smoke.py`
- `python3 scripts/record_synthetic_evidence.py`
- `python3 scripts/compare_synthetic_baseline.py`
- `python3 scripts/provider_dry_run.py`
- `python3 scripts/check_provider_config.py`
- `python3 scripts/run_provider_harness.py`
- `KORA_PROVIDER_MODE=live KORA_LIVE_PROVIDER=openai python3 scripts/run_provider_harness.py --mode live --provider openai`
- `python3 -m unittest discover -s tests`
- JSON validation for evidence directories
- `git diff --check`
- `git status --short --branch`

Results:

- Python compile passed.
- Existing smoke, synthetic evidence, synthetic comparison, provider dry-run, config-check, and provider harness scripts ran without external calls.
- Live-mode negative provider harness check exited nonzero as expected for missing `KORA_OPENAI_API_KEY`.
- Unit tests passed: 64 tests.
- Existing committed JSON evidence plus the new provider harness JSON validated.
- `git diff --check` passed.

## Public-Safety Scan Result

The expected scan can match KORA-specific placeholder environment variable names such as `KORA_OPENAI_API_KEY`, `KORA_ANTHROPIC_API_KEY`, and `KORA_GEMINI_API_KEY`, plus code/test identifiers that reference those names. These are names only, not credential values.

No actual-looking provider credential, SSH material, private host detail, GPU credential, or private handoff content should be present.

## What This Harness Enables

- One canonical provider evidence entrypoint.
- Dry-run provider evidence by default.
- Live-intent detection and config validation.
- Safe failure before live execution when config is missing.
- Boundary-only live status for future live adapter work.
- Future live provider implementation behind a small controlled adapter change.

## What It Still Does Not Do

- It does not call GPT, Claude, Gemini, Bedrock, vLLM, or any external provider.
- It does not import provider SDKs.
- It does not require real credentials for tests.
- It does not prove real provider call, token, cost, latency, GPU, or infrastructure reduction.

## Blockers

- First live provider adapter still needs implementation and review.
- Live measurement needs request scrubbing, timing, token accounting, cost metadata, and claim review.

## Recommended Next Task

KORA-CHAMPION-010 First Live Provider Measurement Adapter
