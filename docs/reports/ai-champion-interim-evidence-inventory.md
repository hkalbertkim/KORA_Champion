# AI Champion Interim Evidence Inventory

This inventory maps the current KORA Champion evidence chain to public-safe claims, caveats, and recommended report usage. It is intended for the July 31 interim evidence package and should be read as benchmark evidence for execution-path selectivity, not as production savings evidence.

## Provider Evidence

| Artifact | Stage | Claim level | Evidence type | Key metrics | Recommended usage |
| --- | --- | --- | --- | --- | --- |
| `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` | First bounded live provider call | `measured_provider_partial` | Measured | 1 successful call, 0 failed calls, 147 total tokens, 2,187.0 ms latency | GitHub evidence table, AI Champion result report, dashboard |
| `docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json` | Normalized partial provider comparison | `measured_provider_partial` | Partial live comparison | Workload size 6, one measured provider call carried into normalized comparison | AI Champion result report, paper/arXiv later with caveat |

Allowed claims:

- KORA has a working bounded live provider measurement path.
- KORA can normalize a partial provider sample into a public evidence artifact.
- Provider evidence exists only at partial-live sample scale.

Prohibited claims:

- Full provider/GPU live workload comparison.
- Production cost reduction.
- Real provider reduction.
- Customer workload savings.

Caveats:

- The live provider sample count is intentionally bounded.
- This evidence should be used as provider path readiness, not as a cost or throughput benchmark.

## GPU Runtime Evidence

| Artifact | Stage | Claim level | Evidence type | Key metrics | Recommended usage |
| --- | --- | --- | --- | --- | --- |
| `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` | H100 10K micro benchmark | `gpu_micro_benchmark_measured` | Measured | 10,000 units, 0.836763 seconds, 11,950.815225 units/sec, GPU utilization avg/max 7.5 / 15.0, memory avg/max MB 314.5 / 629.0 | GitHub evidence table, dashboard, demo video |

Allowed claims:

- The H100 runtime path was visible and executable.
- KORA can collect bounded GPU runtime, throughput, utilization, and memory evidence.

Prohibited claims:

- GPU reduction.
- Production representativeness.
- Full routing selectivity.
- Production infrastructure savings.

Caveats:

- This is a micro benchmark, not route-aware execution.
- It proves runtime readiness, not selective GPU use.

## Routing Benchmark Evidence

| Artifact | Stage | Claim level | Evidence type | Key metrics | Recommended usage |
| --- | --- | --- | --- | --- | --- |
| `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | 100K dry-run route comparison | `routing_dry_run_100k` | Dry-run | KORA local_gpu 21.203%, cache 13.637%, provider 13.635%, fallback 9.09%, acceptable route rate 1.0, unsafe misroute rate 0.0, compute-weighted GPU demand reduction 31.496734% | GitHub evidence table, AI Champion result report, dashboard |
| `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` | Routing benchmark framework | `routing_framework_ready` | Framework/report | Schema, workload generation, independent oracle labels, router comparisons, compute-weighted metrics | AI Champion result report, paper/arXiv later |
| `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` | 100K dry-run route report | `routing_dry_run_100k` | Dry-run/report | Same-workload router comparison across all implemented policies | GitHub evidence table, AI Champion result report |

Allowed claims:

- KORA can compare multiple routing policies over the same oracle-labeled workload.
- KORA can report correctness, fallback, unsafe misroute, and compute-weighted GPU demand.
- The 100K dry-run supports execution-path selectivity evidence.

Prohibited claims:

- Measured GPU reduction for the 100K dry-run alone.
- Production cost reduction.
- Customer workload savings.
- Final paper-ready result.

Caveats:

- Dry-run routing evidence does not execute provider or GPU workloads.
- Compute weights are benchmark estimates unless tied to measured calibration.

## H100 Routed Subset Evidence

| Artifact | Stage | Claim level | Evidence type | Key metrics | Recommended usage |
| --- | --- | --- | --- | --- | --- |
| `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | H100 routed subset measurement | `gpu_routed_subset_measured` | Measured | 10,000 routed GPU requests, 1.752106 seconds, 5,707.417245 req/sec, 1,279,400.497529 compute-weight/sec, GPU utilization avg/max 15.444444 / 23.0, memory avg/max MB 600.0 / 717.0, error rate 0.0 | GitHub evidence table, AI Champion result report, dashboard, demo video |
| `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` | H100 routed subset report | `gpu_routed_subset_measured` | Measured/report | Estimated all_gpu runtime 5.429518 seconds, estimated avoided GPU runtime 1.710121 seconds | AI Champion result report, paper/arXiv later with caveat |

Allowed claims:

- KORA measured H100 execution for the GPU-routed subset of a 100K benchmark.
- KORA connected oracle-labeled routing output to measured GPU execution.
- KORA can report routed subset runtime, throughput, utilization, memory, and error rate.

Prohibited claims:

- Production cost reduction.
- Customer workload savings.
- Full provider/GPU live workload comparison.
- Full production representativeness.

Caveats:

- The all_gpu baseline runtime is estimated from compute weight, not fully measured.
- Synthetic GPU operations approximate benchmark classes and are not full model inference.

## Multi-Profile Robustness Evidence

| Artifact | Stage | Claim level | Evidence type | Key metrics | Recommended usage |
| --- | --- | --- | --- | --- | --- |
| `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness.json` | Multi-profile route robustness | `multi_profile_dry_run` | Dry-run | KORA acceptable route rate 1.0 and unsafe misroute rate 0.0 across mixed, GPU-heavy, cache-heavy, adversarial, and service-replay profiles | GitHub evidence table, AI Champion result report, dashboard |
| `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` | Multi-profile robustness report | `multi_profile_dry_run` | Dry-run/report | Mean compute-weighted GPU demand reduction 41.754972%; highest fallback profile: adversarial_100k | AI Champion result report, paper/arXiv later |

KORA profile summary:

| Profile | local_gpu % | cache % | provider % | fallback % | acceptable route rate | unsafe misroute rate | compute-weighted GPU demand reduction |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| mixed_realistic_100k | 21.203 | 13.637 | 13.635 | 9.09 | 1.0 | 0.0 | 31.496734% |
| gpu_heavy_100k | 83.314 | 0.0 | 12.5 | 0.0 | 1.0 | 0.0 | 5.802033% |
| cache_heavy_100k | 0.0 | 50.001 | 0.0 | 0.0 | 1.0 | 0.0 | 100.0% |
| adversarial_100k | 14.285 | 0.0 | 14.285 | 28.572 | 1.0 | 0.0 | 44.075516% |
| service_replay_10k | 22.21 | 11.12 | 11.1 | 11.1 | 1.0 | 0.0 | 27.400575% |

Allowed claims:

- KORA can compare routing behavior across multiple workload profiles.
- KORA preserves GPU routes in the GPU-heavy profile.
- Adversarial fallback is recorded as safety behavior when unsafe misroute remains 0.0.

Prohibited claims:

- Production representativeness.
- Real customer workload savings.
- Final paper-ready benchmark.

Caveats:

- GPU-005 is dry-run robustness evidence only.
- It does not perform live provider or H100 execution.

## 1M Scale/Saturation Evidence

| Artifact | Stage | Claim level | Evidence type | Key metrics | Recommended usage |
| --- | --- | --- | --- | --- | --- |
| `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` | 1M dry-run scale benchmark | `scale_1m_dry_run` | Dry-run + estimated runtime | KORA local_gpu 21.2152%, cache 13.6364%, provider 13.6362%, fallback 9.0908%, acceptable route rate 1.0, unsafe misroute rate 0.0, compute-weighted GPU demand reduction 31.564469% | GitHub evidence table, AI Champion result report, dashboard |
| `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | 1M routed subset H100 saturation measurement | `saturation_subset_measured` | Measured | 50,000 routed GPU requests, 7.471771 seconds, 6,691.853913 req/sec, 1,498,185.903203 compute-weight/sec, GPU utilization avg/max 19.161765 / 21.0, memory avg/max MB 686.029412 / 717.0, error rate 0.0 | GitHub evidence table, AI Champion result report, dashboard, demo video |
| `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` | GPU-006 scale and saturation report | `estimated_runtime_from_measured_calibration` | Report | Estimated all_gpu runtime 54.230652 seconds, estimated KORA GPU-routed runtime 37.113035 seconds, estimated avoided GPU runtime 17.117617 seconds | AI Champion result report, paper/arXiv later with caveat |

Allowed claims:

- KORA can run a 1M dry-run routing benchmark.
- KORA can report route stability and compute-weighted GPU demand at 1M scale.
- KORA can estimate 1M routed GPU runtime using prior measured H100 throughput calibration.
- KORA measured a bounded H100 subset from the 1M benchmark.

Prohibited claims:

- Full 1M all-GPU measured execution.
- Full provider/GPU live workload comparison.
- Production cost reduction.
- Real infrastructure savings.

Caveats:

- The full raw 1M fixture was not committed; a deterministic generation manifest and digest were committed.
- Runtime comparisons for the 1M full workload are estimates based on measured routed subset calibration.

## Claim Boundary Matrix

| Claim level | Evidence basis | Safe claim | Unsafe claim | Report usage |
| --- | --- | --- | --- | --- |
| `measured_provider_partial` | One bounded live provider call and normalized partial comparison | Provider path readiness has measured partial evidence | Provider cost reduction or full live comparison | GitHub table, AI Champion report |
| `gpu_micro_benchmark_measured` | H100 10K micro benchmark | H100 runtime path works and emits runtime metrics | Route-aware GPU reduction | Dashboard, demo video |
| `routing_framework_ready` | GPU-004A framework and tests | Routing benchmark schema, oracle labels, routers, and metrics exist | Measured runtime impact | AI Champion report |
| `routing_dry_run_100k` | GPU-004B 100K comparison | 100K execution-path selectivity can be evaluated | Real GPU reduction or provider reduction | GitHub table, dashboard |
| `gpu_routed_subset_measured` | GPU-004C H100 routed subset | GPU-routed subset execution was measured | Production savings or full workload representativeness | AI Champion report, demo video |
| `multi_profile_dry_run` | GPU-005 aggregate | Routing robustness can be compared across workload profiles | Real customer workload savings | Dashboard, paper/arXiv later |
| `scale_1m_dry_run` | GPU-006 scale summary | 1M dry-run routing scale stability is shown | Full 1M measured GPU execution | GitHub table, AI Champion report |
| `saturation_subset_measured` | GPU-006 50K H100 subset | Bounded H100 saturation subset was measured | Full 1M all-GPU measured execution | Demo video, dashboard |
| `estimated_runtime_from_measured_calibration` | GPU-004C/GPU-006 measured compute-weight throughput | Runtime direction can be estimated from measured calibration | Production cost savings | AI Champion report with caveat |

## July 31 Report Readiness Notes

| Item | Current status | Readiness | Remaining work |
| --- | --- | --- | --- |
| Provider path evidence | Bounded live provider sample exists | Partial | Add more live provider samples if budget and policy allow |
| H100 runtime evidence | Micro benchmark plus routed subset measurements exist | Strong for bounded benchmark evidence | Add longer measured calibration if needed |
| Routing selectivity evidence | 100K, multi-profile, and 1M dry-run evidence exist | Strong for benchmark selectivity | Add dashboard packaging |
| H100 routed subset evidence | 10K and 50K routed subsets measured | Strong for bounded routed subset evidence | Avoid claiming full workload execution |
| Scale evidence | 1M deterministic dry-run evidence exists | Strong for dry-run scale | Optional 1M routed subset calibration |
| Public report package | This inventory starts the package | In progress | Complete interim package report, evidence table, demo plan, and index |

## Missing Evidence / Next Evidence Gaps

- Larger live provider sample, if a broader provider claim is needed.
- Dashboard-ready charts for routing distribution, fallback, and compute-weighted GPU demand.
- Demo video or screen capture evidence package.
- Optional measured calibration for a larger routed H100 subset.
- KORA Studio launch evidence and user-facing workflow evidence.
- Early paper/arXiv draft that preserves the benchmark claim boundaries.
