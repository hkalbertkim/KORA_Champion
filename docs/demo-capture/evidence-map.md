# KORA Studio Demo Capture Evidence Map

## Purpose

This map connects each planned Studio or dashboard capture to existing KORA Champion evidence artifacts. The capture package should not create new benchmark claims. It should make the existing evidence chain easier to inspect.

## Capture-to-Evidence Map

| Planned capture | Capture file | Evidence artifacts | Claim-safe usage |
| --- | --- | --- | --- |
| Studio route decision view | `docs/demo-capture/screenshots/studio-route-decision-01.png` | `docs/reports/kora-studio-launch-evidence-plan.md`; `docs/reports/kora-studio-demo-script.md`; `docs/reports/kora-studio-demo-video-storyboard.md` | Shows Studio as a demo evidence surface for execution-path selectivity |
| Studio path explanation view | `docs/demo-capture/screenshots/studio-path-explanation-02.png` | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md`; `docs/reports/kora-studio-demo-narration-script.md` | Explains deterministic, cache, CPU, provider, GPU, and fallback paths |
| Studio evidence mapping view | `docs/demo-capture/screenshots/studio-evidence-map-03.png` | `docs/reports/july-31-interim-result-report-evidence-table.md`; `docs/reports/ai-champion-interim-package-index.md` | Shows how Studio links to committed benchmark evidence |
| Dashboard core message view | `docs/demo-capture/screenshots/dashboard-core-message-04.png` | `docs/dashboard/index.html`; `docs/dashboard/dashboard-data.json`; `docs/reports/july-31-interim-result-report-draft.md` | Shows the dashboard evidence framing around when H100 should be used |
| Dashboard 100K routing view | `docs/demo-capture/screenshots/dashboard-routing-selectivity-05.png` | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`; `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | Supports 100K routing selectivity evidence and compute-weighted GPU demand reduction in benchmark workloads |
| Dashboard H100 routed subset view | `docs/demo-capture/screenshots/dashboard-h100-measured-06.png` | `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md`; `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | Supports bounded H100 routed subset measurement |
| Dashboard multi-profile view | `docs/demo-capture/screenshots/dashboard-multi-profile-optional.png` | `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md`; `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json` | Supports multi-profile routing robustness evidence |
| Dashboard 1M scale view | `docs/demo-capture/screenshots/dashboard-scale-saturation-07.png` | `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md`; `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json`; `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | Supports 1M dry-run scale stability evidence and bounded 1M H100 saturation subset evidence |
| Dashboard claim boundary view | `docs/demo-capture/screenshots/dashboard-claim-boundary-08.png` | `docs/reports/july-31-interim-result-report-claim-boundary.md`; `docs/reports/kora-studio-demo-capture-readiness-report.md` | Shows supported claims and non-claims |
| July 31 report view | `docs/demo-capture/screenshots/july31-report-summary-optional.png` | `docs/reports/july-31-interim-result-report-draft.md`; `docs/reports/july-31-interim-result-report-executive-summary.md`; `docs/reports/july-31-interim-result-report-next-work-plan.md` | Connects demo captures to the interim result report package |
| Two-minute demo summary | `docs/demo-capture/recordings/kora-studio-two-minute-demo-summary.md` | `docs/reports/kora-studio-demo-narration-script.md`; `docs/reports/kora-studio-demo-video-storyboard.md` | Documents the concise walkthrough without committing large video files |
| Five-minute demo summary | `docs/demo-capture/recordings/kora-studio-five-minute-demo-summary.md` | `docs/reports/kora-studio-demo-narration-script.md`; `docs/reports/kora-studio-demo-video-storyboard.md` | Documents the extended walkthrough if produced |

## Evidence Chain Summary

| Evidence area | Primary artifacts |
| --- | --- |
| Dashboard evidence view | `docs/dashboard/index.html`; `docs/dashboard/dashboard-data.json`; `docs/reports/ai-champion-dashboard-evidence-view-report.md` |
| 100K routing evidence | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`; `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` |
| H100 routed subset evidence | `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md`; `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` |
| Multi-profile evidence | `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md`; `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json` |
| 1M scale and saturation evidence | `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md`; `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json`; `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` |
| Studio demo view | `docs/reports/kora-studio-launch-evidence-plan.md`; `docs/reports/kora-studio-demo-script.md`; `docs/reports/kora-studio-demo-video-storyboard.md`; `docs/reports/kora-studio-demo-narration-script.md` |
| July 31 report package | `docs/reports/july-31-interim-result-report-draft.md`; `docs/reports/july-31-interim-result-report-evidence-table.md`; `docs/reports/july-31-interim-result-report-claim-boundary.md`; `docs/reports/july-31-interim-result-report-executive-summary.md` |

## Claim Boundary

The capture package may support execution-path selectivity and compute-weighted GPU demand reduction in benchmark workloads. It must not be used to imply production savings, customer workload savings, real infrastructure savings, full provider/GPU live workload comparison, full 1M all-GPU measured execution, production representativeness, official validation, signed partner validation, broad workload superiority, or energy reduction proof.
