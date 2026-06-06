# KORA: Benchmarking When H100 Should Be Used Through Execution-Path Selectivity

## Draft Status Note

This is an early technical report draft v0 for KORA Champion. It assembles the current public evidence chain into a coherent report structure. It is not a submission package, not a completed publication, and not a deployed-system result.

Core message:

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

## Abstract

KORA Champion evaluates AI workload routing as an execution-path selectivity problem. Rather than benchmarking H100 as a raw accelerator for every request, KORA benchmarks when H100 should be used. The current evidence package routes benchmark workloads across deterministic, cache, CPU, provider, GPU, and fallback paths, then reports route correctness, path distribution, and compute-weighted GPU demand reduction in benchmark workloads. The package includes bounded live provider evidence, measured H100 runtime evidence, 100K routing selectivity evidence, bounded H100 routed subset measurement, multi-profile routing robustness evidence, 1M dry-run scale stability evidence, bounded 1M H100 saturation subset evidence, a static dashboard evidence view, Studio evidence surface planning, and early figure/table drafts. The current results support an interim benchmark evidence claim for execution-path selectivity. They do not establish deployed workload savings, complete live path comparison, or broad workload generality.

## 1. Introduction

Accelerator benchmarking often asks how fast a GPU can run a workload. KORA asks a different question: when should H100 be used at all?

This distinction matters because AI request streams can contain work that is better framed as deterministic handling, cache lookup, CPU execution, provider execution, GPU execution, or fallback. A benchmark that routes all requests to GPU by default can miss the core system behavior: selecting an appropriate execution path for each request.

KORA Champion therefore frames the current evidence chain around execution-path selectivity. The system evaluates route decisions across benchmark workloads, records path distribution and correctness metrics, and connects the GPU-routed subset to bounded H100 routed subset measurement.

## 2. Problem Statement

The technical problem is to evaluate route selection across heterogeneous execution paths without assuming that every request should use GPU execution. The benchmark should answer:

- Which execution path is selected?
- Is the selected path acceptable under the benchmark oracle?
- Are unsafe misroutes avoided?
- What compute-weighted GPU demand remains after route selection?
- Which GPU-routed subsets have measured H100 runtime evidence?

This is not a raw accelerator benchmark. The benchmark target is route selectivity under defined correctness and evidence boundaries.

## 3. KORA Execution-Path Selectivity System

KORA routes benchmark requests across six execution paths:

| Path | Role in the benchmark |
| --- | --- |
| Deterministic | Handles requests that can be resolved through deterministic logic |
| Cache | Handles cache-eligible requests without GPU execution |
| CPU | Handles local non-GPU execution cases |
| Provider | Handles requests routed to a bounded provider path |
| GPU | Handles requests routed to local H100 execution |
| Fallback | Handles requests that should not be forced into another path |

Figure 1 is drafted in `docs/paper-assets/draft-figure-1-execution-path-selectivity.md`. It shows request input, KORA routing/control, the six execution paths, output, and evidence logging.

## 4. Benchmark and Evidence Methodology

The current methodology separates evidence into four categories:

| Evidence type | Meaning | Example |
| --- | --- | --- |
| Measured | Runtime or provider behavior was executed and recorded in a bounded setting | H100 routed subset measurement |
| Bounded measured | Measured evidence with intentionally limited scale or scope | Provider path sample |
| Dry-run | Route decisions and benchmark metrics were computed without executing every live path | 100K routing benchmark |
| Static package | A report, dashboard, or Studio asset that packages existing evidence | Dashboard evidence view |

The benchmark evidence chain uses:

- Routing framework evidence from `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md`.
- 100K routing selectivity evidence from `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`.
- Bounded H100 routed subset measurement from `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md`.
- Multi-profile robustness evidence from `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md`.
- 1M dry-run scale and bounded saturation evidence from `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md`.

## 5. Evidence Summary

Table 1 is drafted in `docs/paper-assets/draft-table-1-evidence-artifact-summary.md`. The summary below highlights the current evidence chain.

| Evidence area | Current status | Primary source |
| --- | --- | --- |
| Provider path | Bounded live provider evidence exists | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` |
| H100 runtime | Measured H100 micro benchmark evidence exists | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` |
| Routing framework | Route taxonomy, oracle labels, router policies, and metrics exist | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` |
| 100K routing | 100K dry-run routing selectivity evidence exists | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` |
| H100 routed subset | Bounded H100 routed subset measurement exists | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` |
| Multi-profile robustness | Five benchmark profiles have route robustness evidence | `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json` |
| 1M scale and saturation | 1M dry-run scale plus bounded saturation subset evidence exists | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` |
| Dashboard | Static dashboard evidence view exists | `docs/dashboard/index.html` |
| Studio | Studio evidence surface planning exists | `docs/reports/kora-studio-launch-evidence-plan.md` |

## 6. Results and Interpretation

### 6.1 Provider Path

The bounded provider sample recorded 1 successful provider call, 0 failed calls, 147 total tokens, and 2,187.0 ms measured latency. This supports provider path readiness in a bounded sample.

Source: `docs/reports/july-31-interim-result-report-draft.md`.

This does not support broad live path comparison across provider and GPU execution.

### 6.2 H100 Runtime Evidence

The H100 micro benchmark recorded 10,000 units in 0.836763 seconds, with throughput of 11,950.815225 units per second. The H100 routed subset measurement recorded 10,000 requests in 1.752106 seconds, with throughput of 5,707.417245 requests per second and error rate 0.0. The bounded saturation subset recorded 50,000 requests in 7.471771 seconds, with throughput of 6,691.853913 requests per second and error rate 0.0.

Sources:

- `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json`
- `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json`
- `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json`

This supports measured H100 runtime evidence in bounded benchmark settings. It does not support complete GPU-only measurement for the whole million-request benchmark.

### 6.3 100K Execution-Path Selectivity

The 100K dry-run routing benchmark recorded:

| Metric | Value |
| --- | ---: |
| local_gpu | 21.203% |
| cache | 13.637% |
| provider | 13.635% |
| fallback | 9.09% |
| acceptable route rate | 1.0 |
| unsafe misroute rate | 0.0 |
| compute-weighted GPU demand reduction in benchmark workloads | 31.496734% |

Source: `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`.

This supports 100K routing selectivity evidence. It does not support measured GPU runtime reduction by itself because this benchmark is dry-run route evidence.

### 6.4 Bounded H100 Routed Subset Measurement

The routed subset measurement connects KORA routing output to measured H100 execution for the GPU-routed subset. It recorded 10,000 measured subset requests, 1.752106 seconds runtime, 5,707.417245 requests per second, 1,279,400.497529 throughput compute-weight per second, and error rate 0.0.

Source: `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md`.

This supports bounded H100 routed subset measurement. It does not support complete workload measurement.

### 6.5 Multi-Profile Robustness

GPU-005 evaluates execution-path selectivity across five benchmark profiles: mixed realistic, GPU-heavy, cache-heavy, adversarial, and service replay. Across these profiles, acceptable route rate is reported as 1.0 and unsafe misroute rate as 0.0.

Source: `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md`.

This supports benchmark profile robustness evidence. It does not establish broad deployed-workload generality.

### 6.6 1M Scale and Bounded Saturation

The 1M dry-run benchmark recorded 1,000,000 requests, acceptable route rate 1.0, unsafe misroute rate 0.0, and compute-weighted GPU demand reduction in benchmark workloads of 31.564469%. The bounded saturation subset recorded 50,000 measured requests in 7.471771 seconds.

Source: `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md`.

This supports 1M dry-run scale stability evidence and bounded 1M H100 saturation subset evidence. It does not support complete GPU-only execution for all million requests.

## 7. Dashboard and Studio Evidence Surface

The static dashboard evidence view is available at `docs/dashboard/index.html` with data in `docs/dashboard/dashboard-data.json`. It packages the benchmark evidence chain for reviewer inspection.

KORA Studio is positioned as a Studio evidence surface for explaining execution-path selectivity. The Studio package is documented in:

- `docs/reports/kora-studio-launch-evidence-plan.md`
- `docs/reports/kora-studio-demo-video-storyboard.md`
- `docs/demo-capture/july31-package-index.md`

Dashboard and Studio artifacts help explain and navigate the evidence chain. They are static or planned package assets; they do not create new runtime measurements.

## 8. Claim Boundaries

The safe central claim is:

KORA can show compute-weighted GPU demand reduction in benchmark workloads through execution-path selectivity.

Supported evidence includes bounded provider evidence, measured H100 runtime evidence, routing framework evidence, 100K routing selectivity evidence, bounded H100 routed subset measurement, multi-profile routing robustness evidence, 1M dry-run scale stability evidence, bounded 1M H100 saturation subset evidence, dashboard evidence view, Studio evidence surface planning, and paper asset drafts.

The current package does not support deployed savings, customer workload outcomes, broad workload generality, complete live comparison of provider and GPU routes, complete million-request GPU-only measurement, external approval status, or finished publication readiness.

## 9. Limitations

Current limitations:

- Provider evidence is bounded and limited in sample scale.
- H100 measurements are bounded to benchmark settings and selected subsets.
- 100K and 1M routing results are dry-run route evidence.
- Runtime comparisons using complete GPU-only baselines are estimates unless separately measured.
- Benchmark profile coverage does not establish broad deployed-workload generality.
- Dashboard and Studio artifacts package evidence but do not add new runtime measurements.
- Figure and table assets are draft-level and need review.

## 10. Future Work

Recommended future work:

- Review and tighten the technical report draft.
- Complete claim boundary review.
- Draft the remaining figures and tables.
- Add public-safe dashboard and Studio capture artifacts when ready.
- Consider additional bounded provider sampling if needed.
- Consider repeated bounded H100 routed subset measurement if stronger runtime confidence is needed.
- Prepare a later reviewed report version only after evidence and caption review.

## Appendix A. Evidence Artifact Index

| Artifact group | Path | Use |
| --- | --- | --- |
| Provider sample | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` | Bounded provider path evidence |
| Provider comparison artifact | `docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json` | Normalized provider evidence package |
| H100 micro benchmark | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` | Measured H100 runtime evidence |
| 100K routing | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | 100K routing selectivity evidence |
| H100 routed subset | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | Bounded H100 routed subset measurement |
| Multi-profile summary | `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json` | Multi-profile routing robustness |
| 1M scale summary | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` | 1M dry-run scale stability |
| Saturation subset | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | Bounded 1M H100 saturation subset evidence |
| Dashboard | `docs/dashboard/index.html` | Static dashboard evidence view |
| Paper assets | `docs/paper-assets/figure-specs.md` | Figure draft plan |
| Paper table assets | `docs/paper-assets/table-specs.md` | Table draft plan |

## Appendix B. Planned Figures and Tables

| Asset | Path | Status |
| --- | --- | --- |
| Figure 1: Execution-path selectivity overview | `docs/paper-assets/draft-figure-1-execution-path-selectivity.md` | Draft |
| Figure 2: Routing benchmark evidence chain | `docs/paper-assets/figure-specs.md` | Planned |
| Figure 3: Compute-weighted GPU demand reduction framing | `docs/paper-assets/figure-specs.md` | Planned |
| Figure 4: Dashboard and Studio evidence surface | `docs/paper-assets/figure-specs.md` | Planned |
| Table 1: Evidence artifact summary | `docs/paper-assets/draft-table-1-evidence-artifact-summary.md` | Draft |
| Table 2: Claim boundary matrix | `docs/paper-assets/table-specs.md` | Planned |
| Table 3: Benchmark profile summary | `docs/paper-assets/table-specs.md` | Planned |
| Table 4: Paper section to evidence map | `docs/paper-assets/table-specs.md` | Planned |
| Appendix Table A1: Artifact index | `docs/paper-assets/table-specs.md` | Planned |
