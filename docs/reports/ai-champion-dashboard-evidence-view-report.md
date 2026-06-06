# AI Champion Dashboard Evidence View Report

## Executive Summary

Goal 008 adds a static dashboard evidence view for KORA Champion. The dashboard packages the current evidence chain into a browser-openable local page for reviewer inspection, GitHub navigation, demo capture, and July 31 interim result preparation.

The dashboard is static. It does not require a backend, does not make live provider calls, and does not require H100 runtime access.

## Dashboard Sections

| Section | Purpose |
| --- | --- |
| Hero / core message | States that KORA benchmarks when H100 should be used and includes the Korean message |
| Evidence chain timeline | Shows provider live path, GPU runtime evidence, GPU-004A, GPU-004B, GPU-004C, GPU-005, GPU-006, and Goal 007 package |
| KPI cards | Summarizes provider, H100, routing, robustness, scale, saturation, and claim boundary status |
| Routing selectivity | Compares 100K and 1M route metrics |
| Multi-profile robustness | Shows KORA behavior across five workload profiles |
| H100 measured execution | Compares 10K routed subset and 50K saturation subset measurements |
| Evidence links | Links local evidence and report artifacts |
| Claim boundaries | Separates allowed and prohibited claims |
| Demo capture mode | Provides screen order, metrics to show, sources, and boundary notes |

## Evidence Sources

| Evidence | Path |
| --- | --- |
| Dashboard data model | `docs/dashboard/dashboard-data.json` |
| Provider live sample | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` |
| GPU micro benchmark | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` |
| 100K routing comparison | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` |
| H100 routed subset | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` |
| Multi-profile summary | `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json` |
| 1M scale summary | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` |
| 1M saturation subset | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` |
| Interim package index | `docs/reports/ai-champion-interim-package-index.md` |

## Metrics Shown

Provider:

- 1 successful provider call.
- 0 failed provider calls.
- 147 total tokens.
- 2,187.0 ms measured latency.

100K routing:

- local_gpu 21.203%.
- cache 13.637%.
- provider 13.635%.
- fallback 9.09%.
- acceptable route rate 1.0.
- unsafe misroute rate 0.0.
- compute-weighted GPU demand reduction 31.496734%.

H100 routed subset:

- 10,000 measured routed GPU requests.
- 1.752106 seconds runtime.
- 5,707.417245 requests/sec.
- 1,279,400.497529 compute-weight/sec.
- GPU utilization avg/max 15.444444 / 23.0.
- GPU memory MB avg/max 600.0 / 717.0.
- error count/rate 0 / 0.0.

1M scale:

- 1,000,000 dry-run requests.
- local_gpu 21.2152%.
- cache 13.6364%.
- provider 13.6362%.
- fallback 9.0908%.
- acceptable route rate 1.0.
- unsafe misroute rate 0.0.
- compute-weighted GPU demand reduction 31.564469%.
- estimated all-GPU runtime 54.230652 seconds.
- estimated KORA GPU-routed runtime 37.113035 seconds.
- estimated avoided GPU runtime 17.117617 seconds.

H100 saturation subset:

- 50,000 measured routed GPU requests.
- 7.471771 seconds runtime.
- 6,691.853913 requests/sec.
- 1,498,185.903203 compute-weight/sec.
- GPU utilization avg/max 19.161765 / 21.0.
- GPU memory MB avg/max 686.029412 / 717.0.
- error count/rate 0 / 0.0.

## Demo Capture Plan

Suggested capture flow:

1. Open `docs/dashboard/index.html`.
2. Start on the hero message and Korean statement.
3. Scroll through KPI cards.
4. Show evidence chain timeline.
5. Pause on 100K and 1M routing selectivity.
6. Show multi-profile robustness.
7. Show H100 measured execution.
8. Show evidence links.
9. End on claim boundaries and demo capture mode.

Suggested narration:

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

## Claim Boundary Notes

Allowed:

- Benchmark execution-path selectivity.
- Bounded live provider evidence.
- Measured H100 runtime evidence.
- 100K routing selectivity evidence.
- Measured H100 routed subset evidence.
- Multi-profile routing robustness evidence.
- 1M dry-run scale stability evidence.
- Bounded H100 saturation subset evidence.

Prohibited:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- Proven 10x savings.
- Full provider/GPU live workload comparison.
- Full 1M all-GPU measured execution.
- Production representativeness.
- Final paper-ready result.

## What Is Still Missing For July 31

- Recorded demo video or screen capture.
- Dashboard screenshot assets for the interim result package.
- KORA Studio launch evidence.
- Optional expanded provider sample if broader provider claims are needed.
- July 31 interim result report draft.

## Next Recommended Goal

Goal 009

Title: July 31 Interim Result Report Draft
