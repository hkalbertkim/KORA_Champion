# GPU Evidence Harness

## Purpose

KORA Core needs measured GPU runtime evidence before any GPU reduction or infrastructure reduction claim can be made. The GPU evidence harness defines the metrics, benchmark stages, and public-safety rules needed to move from local smoke checks to large workload measurements.

## Urgency

KORA has access to H100 x2 only until 2026-07-01. The GPU evidence track must begin immediately and scale from smoke validation to heavy and saturation measurements where feasible.

## Measurement Goals

- Record sanitized GPU device snapshots.
- Record runtime seconds and throughput.
- Record utilization and memory samples.
- Record successful and failed workload units.
- Record latency average, minimum, and maximum.
- Preserve claim boundaries for each stage.

## Metrics

The harness tracks:

- GPU provider label
- GPU model
- GPU count
- CUDA availability
- driver version
- workload ID
- workload size
- workload unit type
- runtime seconds
- throughput units per second
- utilization average and maximum
- memory average and maximum
- successful units
- failed units
- claim level
- warnings

## Benchmark Stages

- smoke: 10 to 100 workload units
- micro: 1,000 to 10,000 workload units
- heavy: 100,000 or more workload units
- saturation: 500,000 to 1,000,000 or more workload units where feasible

## Claim Boundaries

GPU harness output alone does not prove:

- GPU reduction
- infrastructure reduction
- production savings

Measured comparison requires both direct GPU-only runs and KORA-routed runs over the same workload definition.

## Public-Safety Rules

Public GPU evidence must not include credentials, private access details, private paths, endpoint details, or raw operational logs. Commit only reviewed, sanitized JSON summaries and reports.

## KORA Routing Connection

The GPU evidence harness will later compare direct GPU execution against KORA-routed execution across deterministic, cache, CPU, local GPU, and provider paths.
