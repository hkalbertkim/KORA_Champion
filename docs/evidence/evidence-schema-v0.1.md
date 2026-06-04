# KORA Core Evidence Schema v0.1

Status: measurement-first schema for synthetic and future live KORA Core evidence.

## Purpose

The evidence schema gives KORA Core a stable way to record and compare runs before live provider or GPU validation begins. It separates synthetic schema validation from future measured evidence so public claims can stay aligned with available data.

## Schema Overview

Each run record includes:

- run identity
- workload metadata
- routing metrics
- provider metrics
- latency metrics
- GPU metrics
- CPU metrics
- cost metrics
- quality metrics
- evidence status and claim warnings

Fields may be `null` when not measured. Synthetic records must use explicit unknown values for real provider and real GPU fields.

## Metric Groups

Run identity:

- `run_id`
- `run_name`
- `run_type`
- `timestamp_utc`
- `git_commit`
- `environment_label`
- `notes`

Workload metadata:

- `workload_id`
- `workload_name`
- `workload_size`
- `workload_source`
- `workload_hash`

Routing metrics:

- total requests
- deterministic, cache, CPU, local GPU, and provider API counts
- fallback count
- error count
- routing percentages

Provider metrics:

- provider calls
- avoided provider calls
- input, output, and total token counters
- estimated and actual provider cost
- provider breakdown

Latency metrics:

- p50, p95, p99
- average, minimum, and maximum milliseconds

GPU metrics:

- GPU model and count
- runtime seconds
- average utilization and memory
- estimated GPU cost
- avoided GPU runtime seconds

CPU metrics:

- runtime seconds
- average utilization
- CPU offload count

Cost metrics:

- estimated total cost
- actual total cost
- baseline estimated cost
- estimated savings
- estimated savings percentage

Quality metrics:

- deterministic mismatch count
- validation pass and fail counts
- quality notes

## Claim Levels

Supported claim levels:

- `synthetic_only`: local synthetic validation only
- `dry_run`: dry-run provider or GPU route validation, no live measurement
- `measured_provider`: measured provider evidence exists
- `measured_gpu`: measured GPU evidence exists
- `measured_hybrid`: measured provider and GPU evidence exist

Provider dry-run records use `dry_run`. They may populate provider name, model name, provider call count, local token estimates, placeholder latency, placeholder estimated provider cost, and warnings. They must keep `actual_provider_cost` as `null`, `has_real_provider_data` as `false`, and must not be interpreted as measured provider evidence.

## What Synthetic Evidence Can Prove

Synthetic evidence can prove:

- schema creation works
- JSON serialization and deserialization work
- route counts are recorded
- routing percentages are computed
- placeholder token, latency, and cost fields are present
- claim warnings are attached
- no provider credential is required for local evidence generation

## What Synthetic Evidence Cannot Prove

Synthetic evidence cannot prove:

- real provider cost reduction
- real token reduction
- real latency reduction
- real GPU workload reduction
- real infrastructure reduction
- production reliability
- model quality improvement

## Future Provider Evidence Requirements

Future provider evidence must add:

- provider family
- model identifier and version
- real call attempted flag
- provider token accounting source
- latency measurement method
- estimated and actual cost source
- retry and error accounting
- public claim boundary review

## Future GPU Evidence Requirements

Future GPU evidence must add:

- runtime family and version
- public-safe GPU class metadata
- runtime duration
- utilization and memory aggregation method
- local versus provider route comparison
- artifact retention policy
- public claim boundary review

## Public-Safety Rules

Do not commit secrets, provider credentials, SSH material, private server access details, raw private logs, private provider responses, local-only handoff notes, or unreviewed raw benchmark dumps.

Use `private/` for sensitive local artifacts. Commit only reviewed public-safe summaries and synthetic fixtures.
