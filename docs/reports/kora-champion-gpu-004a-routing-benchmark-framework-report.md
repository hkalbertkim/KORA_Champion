# KORA Champion GPU-004A Routing Benchmark Framework Report

GPU-004A implemented the routing benchmark framework for execution-path selectivity.

KORA는 GPU를 많이 쓰는 시스템이 아니라, GPU를 정확히 쓰는 시스템이다.

## Scope

This is framework, schema, and dry-run infrastructure only. No H100 execution was performed in GPU-004A. No live provider execution was performed in GPU-004A. Results are not production cost-saving evidence.

The benchmark evaluates execution-path selectivity across deterministic, cache, CPU, provider, local GPU, and fallback paths.

## Independence Boundary

Oracle labels are independent from router outputs. The oracle generator does not import or call the KORA router adapter. Routers only receive router-visible metadata and do not receive oracle labels, expected routes, acceptable routes, disallowed routes, validation scoring fields, or benchmark scoring outputs.

## Compute Weights

Compute weights use `cw_v0_1` and are pre-measurement estimates:

`compute_weight = class_base_weight * log2(input_size + 1) * complexity_multiplier * batch_multiplier`

The class base weight table is stored at `docs/evidence/routing-benchmark-config/compute-weight-cw-v0-1.json`.

## Implemented Outputs

- Workload schema and validation helpers.
- Deterministic workload generation for `mixed_realistic_100k`, `gpu_heavy_100k`, `cache_heavy_100k`, `adversarial_100k`, and `service_replay_10k`.
- Independent oracle labeling.
- Baseline routers: `all_gpu`, `static_heuristic_router`, and `provider_first_with_gpu_fallback`.
- KORA router adapter boundary declared as `benchmark_prototype` with `benchmark_specific_logic: true` and `claim_level: prototype_routing_evidence`.
- Routing correctness metrics, compute-weighted GPU demand metrics, fallback breakdown, quality placeholder, provider validation placeholder, and provider evidence basis.
- Dry-run fixture and comparison scripts.

## Claim Boundary

Allowed after GPU-004A:

- KORA Champion now has a routing benchmark framework.
- The framework can generate oracle-labeled workloads.
- The framework can compare routing policies across deterministic, cache, CPU, provider, GPU, and fallback paths.
- The framework can compute routing correctness and compute-weighted GPU demand metrics.

Not claimed after GPU-004A:

- Production cost savings.
- Infrastructure cost reduction.
- Real GPU reduction.
- Real provider reduction.
- Real customer workload savings.
- 10x savings.
- Final paper-ready benchmark.
- H100 routed subset measurement.

## Next Work

GPU-004B should run the 100K dry-run routing comparison. GPU-004C should measure the H100-routed subset execution.
