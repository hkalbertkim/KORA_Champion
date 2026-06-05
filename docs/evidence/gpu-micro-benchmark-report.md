# GPU Micro Benchmark Report

## Executive Summary

KORA Core completed a bounded 10,000-unit H100 GPU micro benchmark using the existing GPU measurement harness. The benchmark ran on two visible H100 GPUs and produced sanitized runtime evidence.

This is measured micro benchmark evidence. It does not prove GPU reduction, infrastructure reduction, production savings, or heavy workload behavior.

## Workload

- Benchmark type: `gpu_micro_benchmark`
- Workload unit type: `matrix_multiply_unit`
- Workload size: 10,000
- Successful units: 10,000
- Failed units: 0
- Evidence file: `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json`

## H100 Micro Benchmark Result

- H100 micro benchmark ran: yes
- GPU count observed: 2
- GPU model observed: NVIDIA H100 80GB HBM3
- CUDA available: true
- Torch available: true
- Runtime seconds: 0.836763
- Throughput: 11950.815225 units per second
- GPU utilization average: 7.5
- GPU utilization max: 15.0
- GPU memory average MB: 314.5
- GPU memory max MB: 629.0
- Claim level: `gpu_micro_benchmark_measured`

## Comparison To 100-Unit Smoke Run

| Metric | Smoke | Micro |
| --- | ---: | ---: |
| Workload size | 100 | 10,000 |
| Runtime seconds | 0.368211 | 0.836763 |
| Throughput units/sec | 271.583413 | 11950.815225 |
| Claim level | `gpu_smoke_measured` | `gpu_micro_benchmark_measured` |

The micro benchmark scales the measured workload from 100 units to 10,000 units. The result is not a GPU reduction claim; it is a runtime evidence milestone for the GPU measurement path.

## What This Proves

- The H100 GPU measurement harness can execute a 10,000-unit CUDA workload.
- Both visible GPUs can be used by the bounded benchmark path.
- Sanitized GPU runtime evidence can be committed without private access metadata.
- The evidence schema can represent smoke and micro benchmark stages separately.

## What This Does Not Prove

- It does not prove GPU reduction.
- It does not prove infrastructure reduction.
- It does not prove production savings.
- It does not prove 100,000-unit heavy benchmark behavior.
- It does not prove 1,000,000-unit saturation benchmark behavior.

## Next Step

Run the 100,000-unit H100 heavy benchmark after reviewing the micro benchmark output and confirming the same public-safe evidence handling.
