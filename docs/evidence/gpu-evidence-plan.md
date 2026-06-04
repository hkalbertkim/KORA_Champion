# GPU Evidence Plan

## Executive Summary

The GPU evidence track starts immediately because H100 x2 access ends on 2026-07-01. This plan establishes a public-safe path from smoke checks to heavy and saturation measurements.

No real GPU reduction or infrastructure reduction is claimed yet.

## Immediate H100 x2 Plan

The first GPU work should collect:

- sanitized device snapshot before execution
- sanitized device snapshot after execution
- runtime seconds
- successful units
- failed units
- throughput
- utilization samples
- memory samples
- claim boundary notes

## Stages

| Stage | Workload Units | Purpose |
| --- | ---: | --- |
| smoke | 10 to 100 | Validate measurement wiring |
| micro | 1,000 to 10,000 | Validate repeatable throughput collection |
| heavy | 100,000+ | Measure sustained workload behavior |
| saturation | 500,000 to 1,000,000+ | Measure high-volume capacity where feasible |

## Expected Evidence Artifacts

- `docs/evidence/gpu-plans/` benchmark plans
- `docs/evidence/gpu-runs/` reviewed GPU run summaries
- sanitized GPU snapshots
- stage-level comparison summaries
- validation commands
- claim boundary notes

## GPU-Only vs KORA-Routed Comparison

Future comparison should run the same workload definition through:

- direct GPU-only execution
- KORA-routed execution

The comparison should measure:

- total workload units
- GPU-routed units
- non-GPU-routed units
- runtime seconds
- throughput
- utilization
- memory usage
- failed units

## Claims By Stage

- smoke can prove measurement wiring only.
- micro can prove repeatable local measurement flow.
- heavy can support sustained workload evidence.
- saturation can support high-volume capacity evidence when completed.

## Current Non-Claims

This plan does not prove:

- GPU reduction
- infrastructure reduction
- provider cost reduction
- token reduction
- latency reduction
- production savings
