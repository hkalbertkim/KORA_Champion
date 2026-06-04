# KORA-CHAMPION-013 Bedrock Live Evidence Normalization Report

## Summary

Task 013 normalized the first Bedrock live provider measurement into the KORA evidence framework and created a partial live-provider comparison record.

No new live provider call was run.

## Input Evidence File

`docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json`

## Generated Normalized Comparison File

`docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json`

## Measured Provider Headline Numbers

- Provider: `bedrock`
- Model: `anthropic.claude-haiku-4-5-20251001-v1:0`
- Successful provider calls: 1
- Failed provider calls: 0
- Input tokens: 19
- Output tokens: 128
- Total tokens: 147
- Measured latency: 2187.0 ms
- Estimated provider cost: 0.000275
- Actual provider cost: null
- Claim level: `measured_provider`
- Real provider data: true
- Response text redacted: true

## Files Created

- `src/kora_core/live_evidence.py`
- `src/kora_core/live_comparison.py`
- `scripts/normalize_bedrock_live_evidence.py`
- `tests/test_live_evidence.py`
- `tests/test_live_comparison.py`
- `docs/evidence/live-comparisons/.gitkeep`
- `docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json`
- `docs/evidence/bedrock-live-normalized-comparison-report.md`
- `docs/reports/kora-champion-013-bedrock-live-evidence-normalization-report.md`

## Files Changed

- `README.md`
- `docs/evidence/README.md`
- `docs/roadmap/kora-ai-champion-roadmap.md`

## Validation Results

Validation commands are run after implementation:

- `python3 -m py_compile src/kora_core/*.py scripts/*.py`
- `python3 scripts/run_smoke.py`
- `python3 scripts/record_synthetic_evidence.py`
- `python3 scripts/compare_synthetic_baseline.py`
- `python3 scripts/provider_dry_run.py`
- `python3 scripts/check_provider_config.py`
- `python3 scripts/run_provider_harness.py`
- `python3 scripts/normalize_bedrock_live_evidence.py`
- `python3 -m unittest discover -s tests`
- JSON validation for evidence directories
- `git diff --check`
- `git status --short --branch`

Final results are recorded in the completion response.

## Public-Safety Scan Result

Expected scan hits may include redaction field names and schema keys. No secrets, raw model output, account identifiers, or private workflow terms should be present in newly staged public files.

## What This Task Proves

- The Bedrock live evidence can be validated as sanitized measured provider evidence.
- KORA Core can normalize measured provider facts.
- KORA Core can create a partial live-provider comparison without overstating claims.

## What It Does Not Prove

- It does not prove cost reduction.
- It does not prove token reduction.
- It does not prove latency reduction.
- It does not prove GPU reduction.
- It does not prove infrastructure reduction.
- It does not prove production savings.

## Blockers

- Full workload live micro-benchmarking is still required.
- Measured baseline-vs-KORA live comparison is still required.

## Recommended Next Task

KORA-CHAMPION-014 Full Workload Bedrock Live Micro-Benchmark
