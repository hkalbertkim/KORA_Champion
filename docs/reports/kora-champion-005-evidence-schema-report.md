# KORA Champion 005 Evidence Schema Report

Date: 2026-06-04
Task: KORA-CHAMPION-005
Scope: measurement-first telemetry evidence schema and local synthetic validation

## Summary

Added the official KORA Core v0.1 evidence schema for AI Champion Phase-1 measurement records. The schema supports synthetic, dry-run, provider-live, GPU-live, and hybrid-live run types while keeping real provider and GPU fields nullable until they are measured.

The task also added a local CLI that generates a synthetic run record from the current fixture harness and writes reviewed JSON evidence under `docs/evidence/runs/`.

No real provider integration, model call, GPU access, private document copy, or KORA Studio change was made.

## Files Created

- `src/kora_core/evidence.py`
- `src/kora_core/run_record.py`
- `scripts/record_synthetic_evidence.py`
- `tests/test_evidence.py`
- `tests/test_run_record.py`
- `docs/evidence/evidence-schema-v0.1.md`
- `docs/evidence/runs/.gitkeep`
- `docs/evidence/runs/20260604-042117-synthetic-kora-core.json`
- `docs/reports/kora-champion-005-evidence-schema-report.md`

## Files Changed

- `src/kora_core/__init__.py`
- `docs/evidence/README.md`
- `docs/roadmap/kora-ai-champion-roadmap.md`

## Schema Fields Added

Run identity:

- run ID, name, type, UTC timestamp, git commit, environment label, notes

Workload metadata:

- workload ID, name, size, source, hash

Metric groups:

- routing metrics
- provider metrics
- latency metrics
- GPU metrics
- CPU metrics
- cost metrics
- quality metrics
- evidence status and claim warnings

Helpers added:

- run record creation from harness output
- JSON serialization and deserialization
- required-field validation
- routing percentage calculation
- estimated savings calculation when baseline and KORA costs are both present
- synthetic-only claim warnings

## Generated Synthetic Evidence File

Generated file:

```text
docs/evidence/runs/20260604-042117-synthetic-kora-core.json
```

The file is synthetic, public-safe, and contains no private data.

## Validation Results

Commands run:

```bash
git pull --ff-only origin main
python3 scripts/run_smoke.py
python3 -m unittest discover -s tests
python3 -m py_compile src/kora_core/*.py scripts/*.py
python3 scripts/record_synthetic_evidence.py
python3 -m json.tool docs/evidence/runs/*.json
git diff --check
git status --short --branch
```

Results:

- Pull: already up to date
- Smoke script: passed
- Unit tests before changes: passed, 17 tests
- Unit tests after changes: passed, 27 tests
- Synthetic evidence script: passed
- JSON validation: passed
- Diff whitespace check: passed

## Public-Safety Scan Result

The staged public files were scanned for common provider credential, key, SSH, private host, and local account patterns.

Result:

- No API keys found.
- No SSH key material found.
- No private provider credentials found.
- No private host or local account patterns from the required scan list found.
- No real provider, GPU, or infrastructure data was added.

## What This Evidence Proves

The generated synthetic evidence proves:

- the schema can be populated from the local fixture harness
- routing percentages are computed
- provider-call avoidance counters are recorded
- placeholder token, latency, and cost fields are serialized
- synthetic-only claim warnings are attached
- evidence JSON can be validated and loaded locally

## What This Evidence Does Not Prove

This evidence does not prove:

- real provider cost reduction
- real token reduction
- real latency reduction
- real GPU workload reduction
- real infrastructure reduction
- production reliability or model quality

## Blockers

- No live provider evidence exists yet.
- No live GPU evidence exists yet.
- Baseline-versus-KORA comparison records still need a report layer.
- Provider and GPU adapters must remain fail-closed until explicit approval gates are added.

## Recommended Next Task

`KORA-CHAMPION-006 Baseline-vs-KORA Synthetic Evidence Report`
