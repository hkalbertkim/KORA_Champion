# KORA-CHAMPION-GPU-001 Evidence Harness Report

## Summary

This implementation task adds the GPU evidence harness foundation for KORA Core. It defines GPU metrics, benchmark stages, sanitized snapshot collection, and a public-safe benchmark plan.

No real GPU reduction or infrastructure reduction is claimed.

## Why GPU Track Is Urgent

KORA has H100 x2 access only until 2026-07-01. The measurement path must begin immediately and scale from smoke validation to heavy and saturation runs where feasible.

## H100 x2 Deadline

Target resource deadline: 2026-07-01.

## Files Created

- `src/kora_core/gpu_metrics.py`
- `src/kora_core/gpu_benchmark.py`
- `scripts/collect_gpu_snapshot.py`
- `scripts/plan_gpu_benchmark.py`
- `tests/test_gpu_metrics.py`
- `tests/test_gpu_benchmark.py`
- `docs/evidence/gpu-plans/.gitkeep`
- `docs/evidence/gpu-runs/.gitkeep`
- `docs/evidence/gpu-plans/20260604-135929-gpu-benchmark-plan.json`
- `docs/architecture/gpu-evidence-harness.md`
- `docs/evidence/gpu-evidence-plan.md`
- `docs/reports/kora-champion-gpu-001-evidence-harness-report.md`

## Files Changed

- `docs/evidence/README.md`
- `docs/roadmap/kora-ai-champion-roadmap.md`

## Generated GPU Plan File

`docs/evidence/gpu-plans/20260604-135929-gpu-benchmark-plan.json`

Plan stages:

- smoke: 100 workload units
- micro: 10,000 workload units
- heavy: 100,000 workload units
- saturation: 1,000,000 workload units

## Validation Results

Validation commands run:

- `python3 -m py_compile src/kora_core/*.py scripts/*.py`
- `python3 scripts/plan_gpu_benchmark.py`
- `python3 scripts/collect_gpu_snapshot.py`
- existing local validation scripts
- `python3 -m unittest discover -s tests`
- JSON validation for GPU plans and existing evidence
- `git diff --check`
- `git status --short --branch`

Results:

- Python compile passed.
- GPU benchmark plan generation passed.
- GPU snapshot collection passed gracefully with `nvidia_smi_not_available` on the local machine.
- Existing local validation scripts passed.
- Unit tests passed: 93 tests.
- GPU plan JSON and existing evidence JSON validation passed.
- `git diff --check` passed.

## Public-Safety Scan Result

Expected scan hits may include generic safety wording and placeholders. No credentials, private access details, private endpoint details, private paths, private workflow terms, or raw operational logs should be present.

## What This Enables

- Public-safe GPU benchmark plans.
- Local GPU snapshot collection when `nvidia-smi` is available.
- Graceful non-GPU local validation.
- A path from smoke validation to 1,000,000-unit saturation plans.
- Future GPU-only vs KORA-routed measured comparison.

## What Still Cannot Be Claimed

- GPU reduction.
- Infrastructure reduction.
- Production savings.
- Full workload GPU comparison.

## Recommended Next Task

KORA-CHAMPION-GPU-002 H100 Remote GPU Snapshot and Smoke Run
