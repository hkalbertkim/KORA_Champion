# KORA Studio Demo Video Storyboard

## 1. Demo Objective

The demo objective is to show KORA Studio as a demo evidence surface for explaining execution-path selectivity. The video should connect the Studio route explanation to the dashboard evidence view and the committed benchmark reports without implying production savings or official validation.

Core message:

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

## 2. Intended Audience

The intended audience is a July 31 evaluator reviewing whether KORA has a credible interim evidence package. The viewer should be able to understand the evidence chain from the demo without needing private context, live infrastructure, or a full product build.

## 3. Two-Minute Demo Storyboard

| Time | Screen/action | Narration | Evidence artifact | Claim-safe interpretation |
| --- | --- | --- | --- | --- |
| 0:00-0:15 | Show Studio title or route decision view | "KORA benchmarks when H100 should be used." | `docs/reports/kora-studio-launch-evidence-plan.md` | Studio is the explanation surface for execution-path selectivity |
| 0:15-0:35 | Show selected execution path | "A request is routed to deterministic, cache, CPU, provider, GPU, or fallback." | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` | Routing paths are explicit benchmark categories |
| 0:35-0:55 | Show path explanation | "GPU is one path, not the default path for every request." | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` | The benchmark measures route selectivity |
| 0:55-1:20 | Switch to dashboard KPI and route section | "The dashboard packages the committed evidence chain." | `docs/dashboard/index.html` | The dashboard evidence view is available for reviewer inspection |
| 1:20-1:40 | Show H100 routed subset and saturation evidence | "KORA has bounded H100 routed subset measurement and bounded saturation evidence." | `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md`; `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` | H100 evidence is measured but bounded |
| 1:40-2:00 | Show claim boundaries | "The supported claim is compute-weighted GPU demand reduction in benchmark workloads." | `docs/reports/july-31-interim-result-report-claim-boundary.md` | This is benchmark evidence, not production savings evidence |

## 4. Five-Minute Demo Storyboard

| Time | Screen/action | Narration | Evidence artifact | Claim-safe interpretation |
| --- | --- | --- | --- | --- |
| 0:00-0:30 | Open Studio route decision surface | State English and Korean core messages | `docs/reports/kora-studio-demo-script.md` | Frames the demo around when H100 should be used |
| 0:30-1:00 | Show route decision panel | Explain the six execution paths | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` | The route space is part of the benchmark framework |
| 1:00-1:35 | Show path explanation panel | Explain why the route is selected and why GPU is not automatic | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` | Execution-path selectivity is the central benchmark target |
| 1:35-2:05 | Show evidence mapping panel | Connect route decisions to report and evidence links | `docs/reports/july-31-interim-result-report-evidence-table.md` | Studio maps to existing evidence rather than creating a new broad claim |
| 2:05-2:45 | Open dashboard hero and KPI cards | Explain the committed dashboard evidence view | `docs/dashboard/index.html`; `docs/dashboard/dashboard-data.json` | The dashboard packages benchmark evidence for review |
| 2:45-3:25 | Show 100K and multi-profile sections | Explain route distribution and robustness across benchmark profiles | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`; `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` | Dry-run benchmarks support route selectivity and robustness, not production representativeness |
| 3:25-4:05 | Show H100 measured execution section | Explain bounded H100 routed subset measurement | `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` | H100 execution was measured for a routed benchmark subset |
| 4:05-4:35 | Show 1M scale and saturation section | Explain 1M dry-run scale stability and bounded saturation measurement | `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` | The 1M evidence is dry-run scale plus bounded measured saturation |
| 4:35-5:00 | Show claim boundary section | State supported claims and explicit non-claims | `docs/reports/july-31-interim-result-report-claim-boundary.md` | The final takeaway stays within benchmark evidence boundaries |

## 5. Scene-by-Scene Capture Table

| Scene | Capture filename | Screen/action | Evidence backing | What it proves |
| --- | --- | --- | --- | --- |
| S01 | `studio-route-decision-01.png` | Studio route decision surface | Studio launch evidence plan | Studio can present execution-path selectivity |
| S02 | `studio-path-explanation-02.png` | Path explanation panel | Routing framework report | The route is explained with benchmark categories |
| S03 | `studio-evidence-map-03.png` | Evidence links for route paths | July 31 evidence table | Studio maps to committed evidence |
| S04 | `dashboard-core-message-04.png` | Dashboard hero/core message | Dashboard evidence view | Dashboard is a reviewer-facing evidence view |
| S05 | `dashboard-routing-selectivity-05.png` | 100K route selectivity section | GPU-004B report | KORA has 100K routing selectivity evidence |
| S06 | `dashboard-h100-measured-06.png` | H100 routed subset section | GPU-004C report | KORA has bounded H100 routed subset measurement |
| S07 | `dashboard-scale-saturation-07.png` | 1M scale and saturation section | GPU-006 report | KORA has 1M dry-run scale stability and bounded saturation evidence |
| S08 | `dashboard-claim-boundary-08.png` | Claim boundary section | Claim boundary appendix | The demo makes non-claims explicit |

## 6. Explicit Phrases To Avoid

Avoid:

- "KORA proves production cost reduction."
- "KORA proves customer workload savings."
- "KORA proves real infrastructure savings."
- "KORA proves 10x savings."
- "KORA completed a full provider/GPU live workload comparison."
- "KORA measured full 1M all-GPU execution."
- "KORA proves production representativeness."
- "KORA has a final paper-ready result."
- "KORA has formal government validation."
- "KORA has signed partner validation."
- "KORA proves broad workload superiority."
- "KORA proves energy reduction."

## 7. Final Viewer Takeaway

The viewer should understand that KORA Studio explains execution-path selectivity, the dashboard evidence view packages the committed benchmark evidence, and the supported claim is compute-weighted GPU demand reduction in benchmark workloads. The viewer should not interpret the demo as production savings evidence, official validation, or a full all-GPU measurement.
