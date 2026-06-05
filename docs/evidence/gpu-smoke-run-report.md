# GPU Smoke Run Report

## Executive Summary

KORA Core now has a bounded GPU smoke workload path that can write sanitized GPU run evidence under `docs/evidence/gpu-runs/`.

The current local shell did not expose CUDA devices or `nvidia-smi`, so the first generated record is schema-only fallback evidence. It verifies that the smoke runner, snapshot fallback, JSON output, and claim boundary work without requiring GPU access. It is not H100 measurement evidence.

## Smoke Run Status

- Remote H100 snapshot collected: no
- GPU smoke workload ran: no
- Evidence file: `docs/evidence/gpu-runs/20260605-010635-gpu-smoke-run.json`
- Benchmark type: `gpu_smoke`
- Workload size: 100
- GPU count observed: 0
- GPU model observed: none
- CUDA available: false
- Torch available: true
- Runtime seconds: 0.0
- Throughput: null
- Claim level: `gpu_schema_only`

## Measurement Fields

The smoke runner records:

- before/after `nvidia-smi` snapshots when available
- CUDA availability
- torch availability
- GPU count and model labels when visible
- workload size
- successful and failed workload units
- runtime seconds
- throughput units per second
- aggregate utilization and memory fields when available
- claim level and warnings

## What This Proves

- The GPU smoke measurement harness can run safely on a non-GPU machine.
- The evidence output is JSON serializable and public-safe.
- Claim level remains `gpu_schema_only` when no GPU workload is measured.
- The path is ready to run the same bounded workload on H100 access.

## What This Does Not Prove

- It does not prove H100 availability.
- It does not prove GPU workload execution.
- It does not prove GPU reduction.
- It does not prove infrastructure reduction.
- It does not prove production savings.

## Next Scaling Step

Run the same smoke workload in the H100 environment, commit only sanitized aggregate evidence, then proceed to a 10,000-unit micro benchmark after the smoke result passes validation.
