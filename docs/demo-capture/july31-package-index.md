# July 31 KORA Studio Demo Package Index

## 1. Executive Summary

The July 31 KORA Studio demo package is intended to show how Studio explains execution-path selectivity and how the dashboard evidence view connects that explanation to committed KORA Champion benchmark evidence.

Core message:

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

The package supports a bounded benchmark claim: KORA can show compute-weighted GPU demand reduction in benchmark workloads. It does not support production savings claims or official validation claims.

## 2. Evidence Reports

| Report | Purpose |
| --- | --- |
| `docs/reports/july-31-interim-result-report-draft.md` | Main interim result report draft |
| `docs/reports/july-31-interim-result-report-evidence-table.md` | Evidence artifact mapping |
| `docs/reports/july-31-interim-result-report-claim-boundary.md` | Supported claims and non-claims |
| `docs/reports/july-31-interim-result-report-executive-summary.md` | Short reviewer summary |
| `docs/reports/ai-champion-interim-package-index.md` | Interim package entry point |

## 3. Benchmark Evidence Reports

| Report | Evidence area |
| --- | --- |
| `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` | Routing benchmark framework |
| `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` | 100K routing selectivity evidence |
| `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` | Bounded H100 routed subset measurement |
| `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` | Multi-profile routing robustness |
| `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` | 1M dry-run scale and bounded saturation evidence |

## 4. Dashboard Evidence

| Artifact | Purpose |
| --- | --- |
| `docs/dashboard/index.html` | Static dashboard evidence view |
| `docs/dashboard/dashboard-data.json` | Dashboard data source |
| `docs/dashboard/README.md` | Dashboard usage and claim boundary notes |
| `docs/reports/ai-champion-dashboard-evidence-view-report.md` | Dashboard evidence view report |

## 5. Studio Demo Captures

Planned capture artifacts:

| Capture | Status |
| --- | --- |
| `docs/demo-capture/screenshots/studio-route-decision-01.png` | Missing |
| `docs/demo-capture/screenshots/studio-path-explanation-02.png` | Missing |
| `docs/demo-capture/screenshots/studio-evidence-map-03.png` | Missing |
| `docs/demo-capture/screenshots/dashboard-core-message-04.png` | Missing |
| `docs/demo-capture/screenshots/dashboard-routing-selectivity-05.png` | Missing |
| `docs/demo-capture/screenshots/dashboard-h100-measured-06.png` | Missing |
| `docs/demo-capture/screenshots/dashboard-scale-saturation-07.png` | Missing |
| `docs/demo-capture/screenshots/dashboard-claim-boundary-08.png` | Missing |
| `docs/demo-capture/recordings/kora-studio-two-minute-demo-summary.md` | Missing |
| `docs/demo-capture/recordings/kora-studio-five-minute-demo-summary.md` | Optional |

## 6. Narration and Script

| Artifact | Purpose |
| --- | --- |
| `docs/reports/kora-studio-demo-script.md` | Initial demo script |
| `docs/reports/kora-studio-demo-video-storyboard.md` | Two-minute and five-minute storyboard |
| `docs/reports/kora-studio-demo-narration-script.md` | Approved narration and evaluator Q&A |
| `docs/reports/kora-studio-dashboard-capture-plan.md` | Dashboard capture sequence and quality checklist |

## 7. Claim Boundary Appendix

The package should use these sources for claim boundaries:

- `docs/reports/july-31-interim-result-report-claim-boundary.md`
- `docs/reports/kora-studio-launch-evidence-plan.md`
- `docs/reports/kora-studio-demo-capture-readiness-report.md`
- `docs/demo-capture/capture-manifest.md`
- `docs/demo-capture/evidence-map.md`

Allowed usage:

- Execution-path selectivity.
- Bounded live provider evidence.
- Measured H100 runtime evidence.
- Bounded H100 routed subset measurement.
- Multi-profile routing robustness evidence.
- 1M dry-run scale stability evidence.
- Bounded 1M H100 saturation subset evidence.
- Static dashboard evidence view.
- KORA Studio as a demo evidence surface.
- Compute-weighted GPU demand reduction in benchmark workloads.

Non-claims:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- Proven 10x savings.
- Full provider/GPU live workload comparison.
- Full 1M all-GPU measured execution.
- Production representativeness.
- Final paper-ready result.
- Formal government validation.
- Signed partner validation.
- Broad workload superiority proof.
- Energy reduction proof.

## 8. Gap and Readiness Notes

| Artifact | Purpose |
| --- | --- |
| `docs/reports/kora-studio-july31-gap-analysis.md` | Pre-capture gap analysis |
| `docs/reports/kora-studio-demo-capture-readiness-report.md` | Goal 011 capture readiness report |
| `docs/reports/kora-studio-july31-package-assembly-report.md` | Goal 012 package assembly report |

## 9. Missing Items Before Final Submission

- Public-safe Studio screenshots.
- Public-safe dashboard screenshots.
- Two-minute demo recording or recording summary.
- Optional five-minute demo recording or recording summary.
- Capture review summary.
- Final package index update after captures are reviewed.

## 10. Final Assembly Checklist

- [ ] All required captures exist or have documented exclusions.
- [ ] Every capture appears in `docs/demo-capture/capture-manifest.md`.
- [ ] Every capture maps to evidence in `docs/demo-capture/evidence-map.md`.
- [ ] Every capture passed public-safe review.
- [ ] Every capture passed claim-boundary review.
- [ ] Demo narration follows `docs/reports/kora-studio-demo-narration-script.md`.
- [ ] Large binary files are excluded unless explicitly approved.
- [ ] Final package references only relative repository paths.
- [ ] Final package uses execution-path selectivity language consistently.
- [ ] Final package does not imply production savings or official validation.
