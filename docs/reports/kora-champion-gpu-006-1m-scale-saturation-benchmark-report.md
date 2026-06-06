# KORA Champion GPU-006 1M Scale/Saturation Benchmark Report

## Executive Summary

GPU-006 completed a 1,000,000-request dry-run routing scale benchmark for the `mixed_realistic_1m` profile and completed a bounded H100 subset measurement from the KORA GPU-routed subset.

No live provider calls occurred. The dry-run routing comparison did not require H100 execution. The H100 measurement was limited to a bounded routed subset and is not a full 1M all-GPU execution.

This extends the evidence chain from single-profile routing, measured routed subset execution, and multi-profile robustness to 1M-scale route stability and bounded saturation evidence. It is execution-path selectivity evidence, not production savings evidence.

## Prior Evidence Context

GPU-004C measured H100 execution for the GPU-routed subset of the 100K `mixed_realistic_100k` benchmark. That run measured 10,000 routed GPU requests with 1.752106 seconds of runtime, 5,707.417245 requests per second, 1,279,400.497529 compute-weight units per second, and zero execution errors.

GPU-005 added multi-profile dry-run robustness evidence across mixed, GPU-heavy, cache-heavy, adversarial, and service-replay workload distributions. The KORA adapter preserved an acceptable route rate of 1.0 and unsafe misroute rate of 0.0 across those profiles.

GPU-006 uses that evidence chain as context and adds 1M dry-run scale evidence plus bounded H100 saturation evidence.

## 1M Workload Setup

| Field | Value |
| --- | --- |
| Profile | `mixed_realistic_1m` |
| Request count | 1,000,000 |
| Generation method | Deterministic streaming workload generation |
| Raw fixture storage | Full raw 1M fixture was not committed |
| Generation manifest | `docs/evidence/routing-benchmark-scale/20260606-052807-mixed_realistic_1m-generation.json` |
| Routing comparison | `docs/evidence/routing-benchmark-scale/20260606-052807-mixed_realistic_1m-routing-comparison.json` |
| Routing summary | `docs/evidence/routing-benchmark-scale/20260606-052807-mixed_realistic_1m-routing-summary.json` |
| Scale summary | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` |

The committed generation manifest records deterministic generation settings and a workload SHA-256 digest. The full raw 1M fixture was intentionally omitted to keep the public evidence package compact.

## Router Comparison

| Router | local_gpu % | cache % | provider % | fallback % | acceptable route rate | unsafe misroute rate | compute-weighted GPU reduction vs all_gpu |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `all_gpu` | 68.1818 | 13.6364 | 0.0000 | 4.5454 | 0.681818 | 0.318182 | 0.000000 |
| `static_heuristic_router` | 21.2152 | 9.0909 | 13.6362 | 9.0908 | 0.954545 | 0.045455 | 31.564469 |
| `provider_first_with_gpu_fallback` | 9.0908 | 9.0909 | 40.9090 | 4.5454 | 0.818181 | 0.045455 | 55.784807 |
| `kora_router_adapter` | 21.2152 | 13.6364 | 13.6362 | 9.0908 | 1.000000 | 0.000000 | 31.564469 |

The provider-first baseline produced the lowest GPU demand estimate, but at materially lower acceptable route rate. The KORA adapter matched the static heuristic GPU demand estimate while preserving a higher acceptable route rate and lower unsafe misroute rate.

## KORA Scale Summary

| Metric | Value |
| --- | ---: |
| Total requests | 1,000,000 |
| local_gpu-routed requests | 212,152 |
| local_gpu percentage | 21.2152 |
| cache-routed requests | 136,364 |
| cache percentage | 13.6364 |
| provider-routed requests | 136,362 |
| provider percentage | 13.6362 |
| fallback-routed requests | 90,908 |
| fallback percentage | 9.0908 |
| acceptable route rate | 1.000000 |
| unsafe misroute rate | 0.000000 |
| baseline all_gpu compute weight | 69,382,722.735373 |
| KORA GPU compute weight | 47,482,434.946665 |
| compute-weighted GPU reduction vs all_gpu | 31.564469% |

Runtime estimates use the GPU-004C measured compute-weight throughput calibration of 1,279,400.497529 compute-weight units per second.

| Runtime estimate | Seconds |
| --- | ---: |
| Estimated all_gpu runtime | 54.230652 |
| Estimated KORA GPU-routed runtime | 37.113035 |
| Estimated avoided GPU runtime | 17.117617 |

The 1M dry-run completed with deterministic route counts, zero error rate in the comparison output, and no live provider execution.

## H100 Saturation Subset Summary

The bounded H100 saturation subset was measured from the KORA GPU-routed subset of the 1M benchmark.

| Field | Value |
| --- | ---: |
| Evidence path | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` |
| Measured subset count | 50,000 |
| Measured subset compute weight | 11,194,101.984163 |
| Runtime seconds | 7.471771 |
| Throughput requests/sec | 6,691.853913 |
| Throughput compute-weight/sec | 1,498,185.903203 |
| GPU utilization avg/max | 19.161765 / 21.000000 |
| GPU memory MB avg/max | 686.029412 / 717.000000 |
| Error count/rate | 0 / 0.000000 |

Compared with the GPU-004C 10K routed subset, the 50K saturation subset increased measured utilization from 15.444444 average / 23.0 max to 19.161765 average / 21.0 max. Throughput also increased from 5,707.417245 requests/sec to 6,691.853913 requests/sec, and compute-weight throughput increased from 1,279,400.497529 to 1,498,185.903203 compute-weight units/sec.

The saturation evidence reports that utilization increased versus GPU-004C and that runtime scaled roughly with compute weight. The measurement remains a bounded routed subset run, not a full measured 1M all-GPU execution.

## Interpretation

KORA now has 1M-scale dry-run route stability evidence and measured H100 saturation evidence for a bounded subset of the 1M GPU-routed requests.

The KORA adapter preserved acceptable route rate at 1.0 and unsafe misroute rate at 0.0 in the 1M dry-run while routing 21.2152% of requests to local GPU and reducing compute-weighted GPU demand by 31.564469% versus the all-GPU reference.

The H100 saturation subset confirms that the routed GPU subset can be connected to measured execution at a larger bounded size than GPU-004C. It supports execution-path selectivity evidence and scale measurement continuity, but it does not establish production savings.

## Claim Boundaries

Allowed claims after GPU-006:

- KORA can run a 1M dry-run routing benchmark.
- KORA can report route stability and compute-weighted GPU demand at 1M scale.
- KORA can estimate 1M routed GPU runtime using prior measured H100 throughput calibration.
- KORA measured a bounded H100 subset from the 1M benchmark.
- KORA can compare 10K and 50K routed subset measurements as bounded runtime evidence.

Prohibited claims after GPU-006:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- 10x cost savings.
- Full 1M all-GPU measured execution.
- Full provider/GPU live workload comparison.
- Final paper-ready result.

## Next Recommended Task

KORA-CHAMPION-GPU-007 AI Champion Interim Evidence Package.
