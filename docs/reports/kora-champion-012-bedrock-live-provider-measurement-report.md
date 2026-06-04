# KORA-CHAMPION-012 Bedrock Live Provider Measurement Report

## Summary

Task 012 added the AI Champion Bedrock bearer-token live provider adapter and harness wiring. The adapter is gated by KORA-specific environment variables and `--allow-live`.

No real Bedrock live call was run in this Codex shell because `KORA_BEDROCK_API_KEY` was not present in the environment exposed to the task.

## Bedrock Token Presence

`KORA_BEDROCK_API_KEY` was not present in this shell. The safe environment check reported:

- `KORA_BEDROCK_API_KEY_PRESENT`: false
- `KORA_BEDROCK_API_KEY_LENGTH`: 0
- `KORA_AWS_REGION`: not present
- `KORA_BEDROCK_MODEL_ID`: not present
- `KORA_PROVIDER_MODE`: not present
- `KORA_LIVE_PROVIDER`: not present

The token value was not printed, stored, or committed.

## Config Check Result

The default config check remained dry-run in this shell. Bedrock live config cannot pass here until the following variables are exported into this shell:

- `KORA_PROVIDER_MODE=live`
- `KORA_LIVE_PROVIDER=bedrock`
- `KORA_BEDROCK_API_KEY`
- `KORA_AWS_REGION`
- `KORA_BEDROCK_MODEL_ID`

## Negative Allow-Live Safety Test Result

Command:

```bash
python3 scripts/run_provider_harness.py --mode live --provider bedrock
```

Result:

- Exit code: nonzero.
- Evidence status: `live_config_error`.
- Provider calls: 0.
- Successful provider calls: 0.
- Failed provider calls: 1.
- Real provider data: false.
- Failure reason: missing Bedrock live provider config.
- No network call was made.
- No token value was printed.

The temporary live-config-error JSON was removed and was not committed.

## Whether Real Live Bedrock Call Was Run

No real Bedrock live call was run.

Reason:

- `KORA_BEDROCK_API_KEY` was not present in this shell.

## Live Adapter Implemented

- Provider: `bedrock`
- Auth: bearer token through `KORA_BEDROCK_API_KEY`
- Endpoint: `https://bedrock-runtime.{region}.amazonaws.com/model/{prefixed_model_id}/converse`
- Model prefix: adds `us.` when missing and does not duplicate it
- Request method: `POST`
- Request body: Converse messages plus `maxTokens: 128` and `temperature: 0.2`
- Response text: redacted by default

## Generated Live Evidence

No successful live evidence was generated.

Evidence committed: none.

## Validation Results

Validation commands are run after implementation:

- `python3 -m py_compile src/kora_core/*.py scripts/*.py`
- `python3 scripts/run_smoke.py`
- `python3 scripts/record_synthetic_evidence.py`
- `python3 scripts/compare_synthetic_baseline.py`
- `python3 scripts/provider_dry_run.py`
- `python3 scripts/check_provider_config.py`
- `python3 scripts/run_provider_harness.py`
- `python3 -m unittest discover -s tests`
- JSON validation for committed evidence directories
- `git diff --check`
- `git status --short --branch`

Results:

- Python compile passed.
- Existing smoke, synthetic evidence, synthetic comparison, provider dry-run, config-check, and provider harness scripts ran without external calls.
- Bedrock negative live safety test exited nonzero before live execution.
- Unit tests passed: 80 tests.
- Existing committed JSON evidence validated.
- `git diff --check` passed.

## Public-Safety Scan Result

The expected scan can match placeholder command examples and KORA-specific variable names. These are not credential values.

No actual-looking Bedrock token, SSH material, private host detail, GPU credential, raw model response, or private handoff content should be present.

## What This Proves

- KORA Core now has a Bedrock bearer-token live adapter implementation.
- The adapter has mocked test coverage for endpoint construction, `us.` prefix handling, usage parsing, latency handling, response redaction, safe failure, and max live call bounding.
- The repo is ready for a one-call Bedrock live measurement when the token is visible to the shell.

## What This Does Not Prove

- It does not prove a real Bedrock provider call succeeded.
- It does not prove cost reduction.
- It does not prove token reduction.
- It does not prove latency reduction.
- It does not prove GPU reduction.
- It does not prove infrastructure reduction.

## Blockers

- `KORA_BEDROCK_API_KEY` must be present in the shell environment before running the first live Bedrock measurement.

## Recommended Next Task

KORA-CHAMPION-012A Debug Bedrock Live Call Failure
