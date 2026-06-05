# Routing Benchmark Framework

KORA Champion benchmarks execution-path selectivity. The framework compares routing policies over the same oracle-labeled workload and reports dry-run routing correctness plus compute-weighted GPU demand estimates.

GPU-004A is framework, schema, and dry-run infrastructure only. It does not execute H100 workloads and does not call live provider APIs.

## Schema

Workload records use `routing_benchmark_workload_v0_1`. Each request includes a request id, workload profile, workload class, router-visible metadata, independent oracle labels, a `cw_v0_1` compute weight, and validation metadata.

Routers may use only:

- `request_id`
- `workload_profile`
- `workload_class`
- `router_visible_metadata.observable`
- `router_visible_metadata.inferred`

Routers must not read oracle labels, expected routes, acceptable routes, disallowed routes, validation scoring fields, or benchmark scoring outputs.

## Policies

The comparison runner includes:

- `all_gpu`: upper-bound reference that routes valid non-deterministic, non-cache work to `local_gpu`.
- `static_heuristic_router`: competent rule-based baseline using router-visible metadata.
- `provider_first_with_gpu_fallback`: common provider-first behavior with exact cache and explicit GPU fallback.
- `kora_router_adapter`: benchmark prototype boundary with `benchmark_specific_logic: true` and `claim_level: prototype_routing_evidence`.

## Oracle Independence

Oracle labels come from `oracle_generator.py` workload class and metadata rules. The oracle generator does not import or call the KORA router adapter. Router policy functions receive stripped router input and cannot access oracle labels through the comparison path.

## Metrics

The framework reports exact route accuracy, acceptable route rate, unsafe misroute rate, GPU false positives and negatives, unsafe CPU route count, cache hit correctness, fallback rates, error rate, route counts, fallback breakdown, quality placeholder fields, provider validation placeholder fields, and provider evidence basis.

Compute-weighted metrics use `cw_v0_1`:

`compute_weight = class_base_weight * log2(input_size + 1) * complexity_multiplier * batch_multiplier`

These are pre-measurement estimates and are not production cost-saving evidence.

## Claim Boundary

Allowed claim after GPU-004A: KORA Champion has a routing benchmark framework that can generate oracle-labeled workloads and compare routing policies across deterministic, cache, CPU, provider, GPU, and fallback paths.

Not allowed after GPU-004A: production cost savings, infrastructure cost reduction, real GPU reduction, real provider reduction, real customer workload savings, final paper-ready benchmark results, or H100 routed subset measurement.
