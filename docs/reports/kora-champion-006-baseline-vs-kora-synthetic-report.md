# KORA Champion 006 Baseline vs KORA Synthetic Report

Date: 2026-06-04
Task: KORA-CHAMPION-006
Scope: baseline-vs-KORA synthetic comparison

## Summary

Added a synthetic baseline-vs-KORA comparison layer. The baseline sends every request in the synthetic fixture to provider API. The KORA path uses the current classifier/router/harness behavior.

This task remains synthetic and offline. No provider integration, model call, GPU access, private document copy, or KORA Studio change was made.

## Files Created

- `src/kora_core/comparison.py`
- `scripts/compare_synthetic_baseline.py`
- `tests/test_comparison.py`
- `docs/evidence/comparisons/.gitkeep`
- `docs/evidence/comparisons/20260604-043657-baseline-vs-kora-synthetic.json`
- `docs/evidence/baseline-vs-kora-synthetic-report.md`
- `docs/reports/kora-champion-006-baseline-vs-kora-synthetic-report.md`

## Files Changed

- `README.md`
- `docs/evidence/README.md`
- `docs/roadmap/kora-ai-champion-roadmap.md`

## Generated Comparison JSON Path

```text
docs/evidence/comparisons/20260604-043657-baseline-vs-kora-synthetic.json
```

## Comparison Headline Numbers

| Metric | Value |
|---|---:|
| Workload size | 6 |
| Baseline provider calls | 6 |
| KORA provider calls | 1 |
| Avoided provider calls | 5 |
| Estimated provider-call reduction | 83.3333% |
| Baseline placeholder cost | 0.06 |
| KORA placeholder cost | 0.0112 |
| Placeholder estimated savings | 0.0488 |
| Placeholder estimated savings percentage | 81.3333% |

## Validation Results

Commands run:

```bash
git pull --ff-only origin main
python3 scripts/run_smoke.py
python3 scripts/record_synthetic_evidence.py
python3 -m unittest discover -s tests
python3 -m py_compile src/kora_core/*.py scripts/*.py
python3 scripts/compare_synthetic_baseline.py
python3 -m json.tool docs/evidence/runs/*.json
python3 -m json.tool docs/evidence/comparisons/*.json
git diff --check
git status --short --branch
```

Results:

- Pull: already up to date
- Pre-change smoke: passed
- Pre-change synthetic evidence script: passed
- Pre-change tests: passed, 27 tests
- Post-change compile: passed
- Post-change comparison script: passed
- Post-change tests: passed, 34 tests
- JSON validation: run before commit
- Diff whitespace check: run before commit

## Public-Safety Scan Result

The staged public files were scanned for common provider credential, key, SSH, private host, and local account patterns.

Result:

- No API keys found.
- No SSH key material found.
- No provider credentials found.
- No private host or local account patterns from the required scan list found.
- No real provider, GPU, or infrastructure data was added.

## What This Synthetic Comparison Proves

This synthetic comparison proves:

- baseline-vs-KORA comparison JSON can be generated
- all-provider synthetic baseline accounting works
- KORA synthetic route accounting works
- avoided provider calls are computed
- placeholder costs and placeholder savings are computed
- synthetic claim warnings are attached

## What This Synthetic Comparison Does Not Prove

This synthetic comparison does not prove:

- real provider cost reduction
- real token reduction
- real latency reduction
- real GPU workload reduction
- real infrastructure reduction
- production savings

## Blockers

- No provider dry-run adapter interface exists yet.
- No live provider evidence exists yet.
- No live GPU evidence exists yet.
- Placeholder costs must be replaced with sourced measured costs before real claims.

## Recommended Next Task

`KORA-CHAMPION-007 Provider Dry-Run Adapter Interface`
