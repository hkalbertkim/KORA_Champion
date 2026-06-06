# AI Champion Interim Evidence Package Report

## Executive Summary

KORA Champion now has an interim evidence package spanning provider path readiness, H100 runtime readiness, routing benchmark infrastructure, 100K execution-path selectivity evidence, measured H100 routed subset execution, multi-profile routing robustness, 1M dry-run scale stability, and bounded H100 saturation subset measurement.

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

The strongest current evidence is that KORA can route benchmark workloads across deterministic, cache, CPU, provider, GPU, and fallback paths, preserve acceptable route correctness in dry-run benchmarks, and connect GPU-routed subsets to measured H100 execution. This is execution-path selectivity evidence. It is not production savings evidence.

## What KORA Has Proven So Far

- KORA has a bounded live provider measurement path with one successful measured provider call and zero failed provider calls.
- KORA has H100 runtime evidence from a measured 10K micro benchmark.
- KORA has a routing benchmark framework with schema, workload generation, independent oracle labels, baseline routers, KORA router adapter boundary, and compute-weighted metrics.
- KORA has a 100K dry-run route comparison showing the KORA adapter at 1.0 acceptable route rate, 0.0 unsafe misroute rate, and 31.496734% compute-weighted GPU demand reduction versus the all-GPU reference.
- KORA has measured H100 execution for a 10K GPU-routed subset from the 100K benchmark.
- KORA has multi-profile dry-run robustness evidence across mixed, GPU-heavy, cache-heavy, adversarial, and service-replay workload distributions.
- KORA has 1M dry-run scale evidence and measured H100 saturation evidence for a 50K routed subset.

## What KORA Has Not Proven Yet

- KORA has not proven production cost reduction.
- KORA has not proven customer workload savings.
- KORA has not proven real infrastructure savings.
- KORA has not proven a full provider/GPU live workload comparison.
- KORA has not proven full production representativeness.
- KORA has not measured full 1M all-GPU execution.
- KORA has not produced a final paper-ready result.

## Provider Evidence

| Evidence | Path | Claim level | Key result |
| --- | --- | --- | --- |
| First bounded live provider call | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` | `measured_provider_partial` | 1 successful provider call, 0 failed calls, 147 total tokens, 2,187.0 ms measured latency |
| Normalized partial provider comparison | `docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json` | `measured_provider_partial` | Partial live provider sample carried into normalized comparison artifact |

This evidence supports provider path readiness and partial provider measurement. It should not be used for provider cost, latency, or scale claims beyond the bounded sample.

## GPU Runtime Evidence

| Evidence | Path | Claim level | Key result |
| --- | --- | --- | --- |
| H100 10K micro benchmark | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` | `gpu_micro_benchmark_measured` | 10,000 units, 0.836763 seconds, 11,950.815225 units/sec, GPU utilization avg/max 7.5 / 15.0, memory avg/max MB 314.5 / 629.0 |

This evidence proves the H100 runtime path was visible and executable. It does not prove routing selectivity because the micro benchmark is not route-aware.

## Routing/Selectivity Evidence

| Evidence | Path | Claim level | Key result |
| --- | --- | --- | --- |
| Routing benchmark framework | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` | `routing_framework_ready` | Schema, workload generator, independent oracle labels, baseline routers, KORA adapter boundary, and metrics implemented |
| 100K dry-run comparison | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | `routing_dry_run_100k` | KORA local_gpu 21.203%, cache 13.637%, provider 13.635%, fallback 9.09%, acceptable route rate 1.0, unsafe misroute rate 0.0 |

The 100K dry-run benchmark supports execution-path selectivity evidence. It shows that KORA can route a benchmark workload without using oracle labels inside router decisions, while preserving acceptable route rate and avoiding unsafe misroutes.

## H100 Measured Routed Subset Evidence

| Evidence | Path | Claim level | Key result |
| --- | --- | --- | --- |
| 100K benchmark H100 routed subset | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | `gpu_routed_subset_measured` | 10,000 routed GPU requests measured on H100, 1.752106 seconds, 5,707.417245 req/sec, 1,279,400.497529 compute-weight/sec, error rate 0.0 |

The estimated all-GPU runtime for the 100K source benchmark was 5.429518 seconds, and the estimated avoided GPU runtime was 1.710121 seconds. These runtime comparisons are estimates based on compute weight and measured routed subset calibration, not full all-GPU execution.

## Multi-Profile Robustness Evidence

| Profile | local_gpu % | cache % | provider % | fallback % | acceptable route rate | unsafe misroute rate | compute-weighted GPU demand reduction |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| mixed_realistic_100k | 21.203 | 13.637 | 13.635 | 9.09 | 1.0 | 0.0 | 31.496734% |
| gpu_heavy_100k | 83.314 | 0.0 | 12.5 | 0.0 | 1.0 | 0.0 | 5.802033% |
| cache_heavy_100k | 0.0 | 50.001 | 0.0 | 0.0 | 1.0 | 0.0 | 100.0% |
| adversarial_100k | 14.285 | 0.0 | 14.285 | 28.572 | 1.0 | 0.0 | 44.075516% |
| service_replay_10k | 22.21 | 11.12 | 11.1 | 11.1 | 1.0 | 0.0 | 27.400575% |

Source: `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness.json`.

This evidence shows that KORA can compare routing behavior across materially different workload profiles. The GPU-heavy profile preserves GPU routing, the cache-heavy profile routes heavily to cache, and the adversarial profile raises fallback while keeping unsafe misroute rate at 0.0.

## 1M Scale and Saturation Evidence

| Evidence | Path | Claim level | Key result |
| --- | --- | --- | --- |
| 1M dry-run scale summary | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` | `scale_1m_dry_run` | KORA local_gpu 21.2152%, cache 13.6364%, provider 13.6362%, fallback 9.0908%, acceptable route rate 1.0, unsafe misroute rate 0.0 |
| 50K H100 saturation subset | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | `saturation_subset_measured` | 50,000 routed GPU requests, 7.471771 seconds, 6,691.853913 req/sec, 1,498,185.903203 compute-weight/sec, error rate 0.0 |

The 1M dry-run estimates use measured H100 compute-weight throughput calibration:

| Runtime estimate | Seconds |
| --- | ---: |
| Estimated all-GPU runtime | 54.230652 |
| Estimated KORA GPU-routed runtime | 37.113035 |
| Estimated avoided GPU runtime | 17.117617 |

The 50K saturation subset is measured H100 runtime evidence. The 1M full-workload runtime comparison remains estimated.

## GitHub Evidence Table

| Category | Evidence path | What it proves | What it does not prove |
| --- | --- | --- | --- |
| Provider path | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` | Bounded live provider call succeeded | Provider cost reduction |
| H100 runtime | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` | H100 runtime path works | Route-aware selectivity |
| 100K routing | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | Dry-run execution-path selectivity | Measured GPU reduction |
| H100 routed subset | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | Routed subset execution measured on H100 | Full workload execution |
| Multi-profile | `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness.json` | Robustness across workload profiles | Production representativeness |
| 1M scale | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` | 1M dry-run route stability | Full 1M measured GPU execution |
| Saturation subset | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | 50K routed H100 subset measurement | Production savings |

## Demo Video/Dashboard Evidence Plan

The demo should show evidence artifacts and benchmark outputs rather than production claims.

Recommended scenes:

- Provider path evidence: show bounded live provider result and normalized comparison.
- H100 runtime evidence: show micro benchmark metrics.
- 100K routing selectivity: show KORA route distribution, acceptable route rate, unsafe misroute rate, and compute-weighted GPU demand reduction.
- H100 routed subset measurement: show 10K measured runtime, throughput, utilization, memory, and error rate.
- Multi-profile robustness: show KORA profile table and adversarial fallback behavior.
- 1M scale summary: show 1M route distribution and estimated runtime based on measured calibration.
- Saturation subset: show 50K measured H100 runtime and throughput.
- Final evidence dashboard: show claim boundaries beside evidence metrics.

Overlay text should say: "Benchmark evidence for execution-path selectivity. Not production savings evidence."

## July 31 Result Report Readiness

| Item | Current status | Evidence path | Readiness level | Remaining work |
| --- | --- | --- | --- | --- |
| H100 test evidence sufficient for performance/cost-direction argument | 10K micro benchmark, 10K routed subset, and 50K saturation subset exist | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | Strong for benchmark direction | Keep claim language to benchmark demand and estimated runtime |
| KORA Core launch/public GitHub evidence | Routing framework, comparisons, and reports are committed | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` | Strong for benchmark infrastructure | Add README-level pointers if needed |
| KORA Studio launch evidence | Not yet included in this evidence chain | None yet | Gap | Add Studio launch artifact or demo screen evidence |
| Demo video/screenshare/dashboard evidence | Plan defined, artifacts available | `docs/reports/ai-champion-demo-readiness-plan.md` | In progress | Record demo and prepare dashboard view |
| Early paper/arXiv draft readiness | Evidence chain is structured and caveated | `docs/reports/ai-champion-interim-evidence-inventory.md` | Partial | Draft paper outline and methodology section |
| Business significance section | Benchmark significance can be stated | This report | Partial | Tie to market-facing narrative without savings claims |
| Second-stage work plan if selected | Next tasks identified | This report | Partial | Convert to milestone plan |

## Paper/arXiv Readiness

The current evidence is suitable for an early methods-and-evidence outline. It is not final paper-ready. A future paper should separate measured evidence, dry-run evidence, and estimated runtime evidence into distinct sections.

Recommended paper components:

- Routing benchmark schema and oracle independence.
- Router policy comparison and limitations.
- Compute-weight formula and calibration caveats.
- H100 routed subset measurement method.
- Multi-profile robustness results.
- 1M scale dry-run results.
- Claim boundary and threats to validity.

## Business/Technical Significance

KORA's technical significance is selective execution-path routing: deciding which requests should use deterministic handling, cache, CPU, provider, GPU, or fallback. The evidence package shows that this can be benchmarked at 100K and 1M dry-run scale, evaluated across multiple workload profiles, and connected to bounded H100 routed subset measurement.

The business significance is directionally clear but not yet production-proven: KORA can present a disciplined measurement path for reducing unnecessary high-cost execution paths in benchmark workloads while preserving correctness boundaries. The current language should use "compute-weighted GPU demand reduction in benchmark workloads" and "estimated avoided GPU runtime based on measured H100 calibration," not production savings language.

## Next Evidence Tasks

1. KORA-CHAMPION-GPU-007B Dashboard Evidence View.
2. KORA-CHAMPION-GPU-007C Demo Video Capture Package.
3. KORA-CHAMPION-GPU-008 KORA Studio Launch Evidence.
4. KORA-CHAMPION-GPU-009 Expanded Provider Sample.
5. KORA-CHAMPION-GPU-010 Early Paper Draft.

## Claim Boundaries

Allowed claims:

- KORA has provider path readiness evidence at bounded partial-live sample scale.
- KORA has measured H100 runtime evidence for micro and routed subset benchmarks.
- KORA has a routing benchmark framework with oracle-labeled workload generation and multiple router policies.
- KORA can compare execution-path selectivity at 100K, across multiple profiles, and at 1M dry-run scale.
- KORA can estimate benchmark runtime using measured H100 compute-weight throughput calibration.
- KORA measured bounded H100 routed subsets of 10K and 50K requests.

Prohibited claims:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- 10x cost savings as proven.
- Full provider/GPU live workload comparison.
- Full 1M all-GPU measured execution.
- Production representativeness.
- Final paper-ready result.
