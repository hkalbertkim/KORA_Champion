# KORA Champion GPU-005 Multi-Profile Routing Robustness Report

## Executive Summary

The multi-profile dry-run routing robustness benchmark completed across mixed, GPU-heavy, cache-heavy, adversarial, and service-replay workload distributions.

No H100 execution occurred in GPU-005. No live provider calls occurred. GPU-005 extends GPU-004B/GPU-004C evidence from one workload profile to multiple distributions. This is routing robustness and execution-path selectivity evidence, not production savings evidence.

## Evidence Context

GPU-004C already recorded measured H100 routed subset evidence at `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json`.

GPU-005 is dry-run robustness evidence only:

- Aggregate evidence: `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness.json`
- Aggregate summary: `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json`
- H100 execution in GPU-005: `false`
- Live provider execution in GPU-005: `false`

## Profile Setup

| Profile | Requests | Purpose | Expected stress behavior |
|---|---:|---|---|
| `mixed_realistic_100k` | 100,000 | Balanced routing distribution comparable to GPU-004B | Preserve high acceptable route rate and zero unsafe misroute |
| `gpu_heavy_100k` | 100,000 | GPU-preferred batch/vector/tensor classes | Preserve GPU routes and keep GPU false negatives low |
| `cache_heavy_100k` | 100,000 | Exact reusable and deterministic-heavy traffic | Route cacheable work to cache and avoid unnecessary GPU demand |
| `adversarial_100k` | 100,000 | Ambiguous, invalid, near-duplicate, and boundary cases | Prefer safety fallback over unsafe routing |
| `service_replay_10k` | 10,000 | Practical service replay class mix | Exercise repeats, deterministic queries, CPU transforms, provider generation, GPU tensor work, ambiguous cases, and invalid metadata |

## KORA Adapter Profile Summary

| Profile | Local GPU % | Cache % | Provider % | Fallback % | Acceptable route rate | Unsafe misroute rate | GPU reduction vs all_gpu |
|---|---:|---:|---:|---:|---:|---:|---:|
| `mixed_realistic_100k` | 21.203 | 13.637 | 13.635 | 9.090 | 1.000000 | 0.000000 | 31.496734 |
| `gpu_heavy_100k` | 83.314 | 0.000 | 12.500 | 0.000 | 1.000000 | 0.000000 | 5.802033 |
| `cache_heavy_100k` | 0.000 | 50.001 | 0.000 | 0.000 | 1.000000 | 0.000000 | 100.000000 |
| `adversarial_100k` | 14.285 | 0.000 | 14.285 | 28.572 | 1.000000 | 0.000000 | 44.075516 |
| `service_replay_10k` | 22.210 | 11.120 | 11.100 | 11.100 | 1.000000 | 0.000000 | 27.400575 |

## Router Comparison

All profiles compare `all_gpu`, `static_heuristic_router`, `provider_first_with_gpu_fallback`, and `kora_router_adapter` over the same deterministic workload for that profile. Full per-router metrics are stored in the profile comparison JSON files under `docs/evidence/routing-benchmark-runs/20260605-132228-*`.

Observed KORA tradeoffs:

- `mixed_realistic_100k`: KORA matched the static heuristic GPU reduction while improving acceptable route rate and unsafe misroute rate. Provider-first had higher GPU reduction, but lower acceptable route rate and nonzero unsafe misroute.
- `gpu_heavy_100k`: KORA preserved GPU routes with `83.314%` local GPU routing and matched the static heuristic. Provider-first reduced GPU demand more, but had materially lower acceptable route rate.
- `cache_heavy_100k`: KORA routed `50.001%` to cache and reached `100.0%` compute-weighted GPU reduction versus all-GPU while improving correctness over both baselines.
- `adversarial_100k`: KORA held unsafe misroute at `0.0` with fallback at `28.572%`, matching the safety behavior of the static heuristic.
- `service_replay_10k`: KORA matched static GPU reduction while improving cache use, acceptable route rate, and unsafe misroute. Provider-first had higher GPU reduction, but lower acceptable route rate and nonzero unsafe misroute.

## Aggregate KORA Metrics

- Mean acceptable route rate: `1.000000`
- Min acceptable route rate: `1.000000`
- Mean unsafe misroute rate: `0.000000`
- Max unsafe misroute rate: `0.000000`
- Mean fallback rate: `0.097524`
- Max fallback rate: `0.285720`
- Mean compute-weighted GPU reduction: `41.754972%`
- Highest GPU demand profile: `gpu_heavy_100k`
- Highest fallback profile: `adversarial_100k`
- Highest unsafe misroute profile: `none_all_profiles_zero`
- Strongest cache/dedup profile: `cache_heavy_100k`
- GPU-heavy profile preserves GPU routes: `true`

## Robustness Interpretation

KORA preserves GPU routes in the GPU-heavy profile: local GPU routing remains high at `83.314%`, and acceptable route rate remains `1.0`.

KORA increases cache use in the cache-heavy profile: cache routing reaches `50.001%`, local GPU routing falls to `0.0%`, and cache hit correctness remains represented in the comparison output.

The adversarial profile uses fallback as safety behavior. Higher fallback is acceptable here because unsafe misroute remains `0.0`; this indicates uncertain and invalid cases are not forced into unsafe execution paths.

The service replay profile retains a practical route mix across cache, deterministic, CPU, provider, GPU, and fallback paths. It is not only a single synthetic stress shape.

Across all profiles, KORA unsafe misroute remains at `0.0`, which is inside the benchmark safety boundary.

## Claim Boundaries

Allowed:

- KORA can run multi-profile routing benchmark comparisons.
- KORA can compare execution-path selectivity across mixed, GPU-heavy, cache-heavy, adversarial, and service-replay workloads.
- KORA can report route correctness, fallback, unsafe misroute, and compute-weighted GPU demand across workload profiles.
- KORA has prior measured H100 routed subset evidence from GPU-004C.

Not claimed:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- 10x cost savings.
- Full provider/GPU live workload comparison.
- Final paper-ready result.

## Next Recommended Task

KORA-CHAMPION-GPU-006 1M Scale/Saturation Benchmark.
