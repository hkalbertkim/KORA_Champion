# GPU Smoke Run Report

## Executive Summary

KORA Core now has a bounded GPU smoke workload path that can write sanitized GPU run evidence under `docs/evidence/gpu-runs/`.

The first H100 smoke measurement completed with a 100-unit CUDA workload across two visible H100 GPUs. The measurement proves the GPU smoke path can execute and record sanitized runtime evidence. It does not prove GPU reduction, infrastructure reduction, or production savings.

## Smoke Run Status

- Remote H100 snapshot collected: yes
- GPU smoke workload ran: yes
- Evidence file: `docs/evidence/gpu-runs/20260605-012607-gpu-smoke-run.json`
- Benchmark type: `gpu_smoke`
- Workload size: 100
- GPU count observed: 2
- GPU model observed: NVIDIA H100 80GB HBM3
- CUDA available: true
- Torch available: true
- Runtime seconds: 0.368211
- Throughput: 271.583413 units per second
- Claim level: `gpu_smoke_measured`

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
- The GPU smoke measurement harness can run a bounded CUDA workload on H100.
- The evidence output is JSON serializable and public-safe.
- Claim level remains `gpu_schema_only` when no GPU workload is measured.
- Claim level advances to `gpu_smoke_measured` only after a CUDA workload completes.

## What This Does Not Prove

- It does not prove GPU reduction.
- It does not prove infrastructure reduction.
- It does not prove production savings.
- It does not prove heavy or saturation workload behavior.

## Next Scaling Step

Proceed to a 10,000-unit H100 micro benchmark after the smoke result passes validation.
