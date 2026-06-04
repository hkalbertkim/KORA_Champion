# Baseline vs KORA Synthetic Report

Status: synthetic/offline comparison only.

## Executive Summary

This report compares a synthetic all-provider baseline against KORA Core's current classifier/router/harness path on the public-safe sample request fixture.

Result:

| Metric | Synthetic baseline | KORA synthetic routing |
|---|---:|---:|
| Workload size | 6 | 6 |
| Provider API calls | 6 | 1 |
| Avoided provider calls | n/a | 5 |
| Estimated provider-call reduction | n/a | 83.3333% |
| Placeholder estimated cost | 0.06 | 0.0112 |
| Placeholder estimated savings | n/a | 0.0488 |
| Placeholder estimated savings percentage | n/a | 81.3333% |

This demonstrates the measurement path and routing behavior. It does not prove real provider cost reduction, real token reduction, real latency reduction, real GPU reduction, or production savings.

## What Was Compared

The comparison used `tests/fixtures/sample_requests.json`, a six-request synthetic fixture covering:

- deterministic request
- cacheable request
- local GPU-like request
- provider-required request
- default CPU request
- repeated cacheable request

No real user data is included.

## Baseline Policy

The baseline policy is `all_provider_api`: every request is counted as if it went to a provider API.

This is a synthetic before-state for measurement scaffolding. It is not a live provider run.

## KORA Policy

The KORA policy is `classifier_router_harness`: requests are classified and routed through the local KORA Core harness.

Observed synthetic KORA route counts:

| Target | Count |
|---|---:|
| deterministic | 1 |
| cache | 1 |
| CPU | 2 |
| local GPU | 1 |
| provider API | 1 |

## Synthetic Results Table

| Field | Value |
|---|---:|
| Workload size | 6 |
| Baseline provider calls | 6 |
| KORA provider calls | 1 |
| Avoided provider calls | 5 |
| Estimated provider-call reduction | 83.3333% |
| Baseline placeholder cost | 0.06 |
| KORA placeholder cost | 0.0112 |
| Placeholder savings | 0.0488 |
| Placeholder savings percentage | 81.3333% |

## What This Shows

This synthetic comparison shows:

- the baseline-vs-KORA comparison schema works
- provider-call counters can be compared
- routing distribution is captured
- placeholder costs can be computed
- synthetic warnings are attached
- JSON evidence can be generated without external calls

## What This Does Not Show

This synthetic comparison does not show:

- real provider cost reduction
- real token reduction
- real latency reduction
- real GPU workload reduction
- real infrastructure reduction
- production reliability
- production savings

## Why This Matters For AI Champion

The AI Champion result package needs a before/after evidence path. This task establishes the local comparison scaffold:

- baseline policy
- KORA policy
- route counts
- provider-call avoidance
- placeholder cost comparison
- claim warnings

Future live provider and GPU work can replace synthetic counters with measured data while preserving the same reporting shape.

## Next Step Toward Live Validation

The next step is a provider dry-run adapter interface that remains fail-closed by default. It should record provider intent and accounting fields without making live calls until explicit approval gates are added.
