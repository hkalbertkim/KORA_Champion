# KORA Champion GPU-004B 100K Dry-Run Routing Comparison Report

## Executive Summary

The 100K mixed-realistic dry-run routing comparison completed for GPU-004B. No H100 execution occurred. No live provider execution occurred. This result is routing selectivity evidence, not production savings evidence.

The benchmark compared four policies over the same oracle-labeled workload: `all_gpu`, `static_heuristic_router`, `provider_first_with_gpu_fallback`, and `kora_router_adapter`.

## Benchmark Setup

- Workload profile: `mixed_realistic_100k`
- Request count: `100,000`
- Deterministic seed: `404`
- Compute weight formula: `cw_v0_1`
- Comparison mode: `dry_run_only`
- Oracle labels are independent from router outputs.
- Routers are restricted to router-visible metadata.

The full deterministic workload fixture was produced locally, measured at `130,313,730` bytes, and not committed because it exceeds the normal single-file size limit for a clean public repository. The committed fixture evidence stores the deterministic generation config and SHA-256 hash:

- Generation manifest: `docs/evidence/routing-benchmark-fixtures/20260605-101459-mixed_realistic_100k-100000-generation.json`
- Fixture SHA-256: `e0cd00a416d649a49b4770985256eca05f763c2d072fda3afa754cf8e61dcd04`
- Comparison run: `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json`
- Summary table: `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000-summary.json`

## Router Comparison

| Router | Local GPU % | Provider % | Fallback % | Exact route accuracy | Acceptable route rate | Unsafe misroute rate | Compute-weighted GPU reduction vs all_gpu |
|---|---:|---:|---:|---:|---:|---:|---:|
| `all_gpu` | 68.181 | 0.000 | 4.545 | 0.54545 | 0.68181 | 0.31819 | 0.000000 |
| `static_heuristic_router` | 21.203 | 13.635 | 9.090 | 0.93931 | 0.95454 | 0.04546 | 31.496734 |
| `provider_first_with_gpu_fallback` | 9.090 | 40.908 | 4.545 | 0.68181 | 0.81818 | 0.04546 | 55.735483 |
| `kora_router_adapter` | 21.203 | 13.635 | 9.090 | 0.98477 | 1.00000 | 0.00000 | 31.496734 |

## KORA Adapter Analysis

The KORA adapter reduced compute-weighted GPU demand by `31.496734%` versus the `all_gpu` upper-bound reference. Exact route accuracy was `0.98477`, acceptable route rate was `1.00000`, and unsafe misroute rate was `0.00000`.

KORA adapter fallback rate was `0.09090`. The comparison output preserves the safety and failure fallback breakdown from GPU-004A. The KORA fallback behavior is concentrated in boundary and missing-metadata cases in the dry-run policy.

## Baseline Comparison

`all_gpu` is the upper-bound GPU demand reference and is included only as a comparison baseline. It routed `68.181%` of requests to local GPU and had an unsafe misroute rate of `0.31819`.

`static_heuristic_router` is the competent rule baseline. It matched KORA adapter local GPU and provider percentages in this workload but had lower exact and acceptable route rates and a nonzero unsafe misroute rate.

`provider_first_with_gpu_fallback` is the practical provider-first baseline. It routed less work to local GPU but shifted `40.908%` of requests to provider and had lower exact and acceptable route rates than the KORA adapter.

`kora_router_adapter` is the KORA selectivity policy boundary for this benchmark. It maintained the highest acceptable route rate and lowest unsafe misroute rate while reducing compute-weighted GPU demand versus `all_gpu`.

## Claim Boundary

Allowed after GPU-004B:

- KORA Champion can run a 100K dry-run routing benchmark.
- The framework compares multiple routing strategies over the same oracle-labeled workload.
- KORA adapter can be evaluated for route correctness and compute-weighted GPU demand.
- The result provides execution-path selectivity evidence.

Not claimed after GPU-004B:

- Production cost reduction.
- Infrastructure cost reduction.
- Real GPU reduction.
- Real provider reduction.
- Customer workload savings.
- 10x savings.
- Final paper-ready benchmark.
- Measured H100 routed subset result.

## Next Step

KORA-CHAMPION-GPU-004C H100 Routed Subset Measurement.
