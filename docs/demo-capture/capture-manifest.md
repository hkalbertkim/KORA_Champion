# KORA Studio Capture Manifest

## Capture Package Status

Status: planned package assembled.

No real screenshots or video files are committed in this package. The current files define where future captures should go, how they should be named, how they map to existing evidence, and how claim boundaries should be reviewed before any capture is added.

## Required Captures

| Capture ID | Expected filename | Capture type | Source screen | Evidence backed by | Claim-safe interpretation | Current status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| STUDIO-01 | `screenshots/studio-route-decision-01.png` | Screenshot | Studio route decision surface | `docs/reports/kora-studio-launch-evidence-plan.md`; `docs/reports/kora-studio-demo-script.md` | Studio can explain execution-path selectivity as a demo evidence surface | Planned | Capture only after public-safe view is selected |
| STUDIO-02 | `screenshots/studio-path-explanation-02.png` | Screenshot | Studio path explanation panel | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md`; `docs/reports/kora-studio-demo-video-storyboard.md` | The route space includes deterministic, cache, CPU, provider, GPU, and fallback paths | Planned | Avoid implying that GPU is the default path |
| STUDIO-03 | `screenshots/studio-evidence-map-03.png` | Screenshot | Studio evidence mapping panel | `docs/reports/july-31-interim-result-report-evidence-table.md`; `docs/demo-capture/evidence-map.md` | Studio maps route explanations to committed benchmark evidence | Planned | Links should use relative repository paths |
| DASH-01 | `screenshots/dashboard-core-message-04.png` | Screenshot | Dashboard core message | `docs/dashboard/index.html`; `docs/reports/july-31-interim-result-report-draft.md` | The dashboard frames KORA around when H100 should be used | Planned | Include English and Korean core messages if visible |
| DASH-02 | `screenshots/dashboard-routing-selectivity-05.png` | Screenshot | Dashboard 100K routing section | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`; `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | KORA has 100K routing selectivity evidence | Planned | Label as dry-run benchmark evidence |
| DASH-03 | `screenshots/dashboard-h100-measured-06.png` | Screenshot | Dashboard H100 measured section | `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md`; `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | KORA has bounded H100 routed subset measurement | Planned | Do not imply full workload execution |
| DASH-04 | `screenshots/dashboard-scale-saturation-07.png` | Screenshot | Dashboard 1M scale and saturation section | `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md`; `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json`; `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | KORA has 1M dry-run scale stability and bounded H100 saturation subset evidence | Planned | Separate dry-run scale from measured saturation subset |
| DASH-05 | `screenshots/dashboard-claim-boundary-08.png` | Screenshot | Dashboard claim boundary section | `docs/reports/july-31-interim-result-report-claim-boundary.md` | Supported claims and explicit non-claims are visible | Planned | Required before final package submission |
| VIDEO-01 | `recordings/kora-studio-two-minute-demo-summary.md` | Recording summary | Two-minute Studio plus dashboard walkthrough | `docs/reports/kora-studio-demo-narration-script.md`; `docs/reports/kora-studio-demo-video-storyboard.md` | A reviewer can follow the execution-path selectivity narrative | Planned | Store video externally unless repository storage is approved |
| VIDEO-02 | `recordings/kora-studio-five-minute-demo-summary.md` | Recording summary | Five-minute extended walkthrough | `docs/reports/kora-studio-demo-narration-script.md`; `docs/reports/kora-studio-demo-video-storyboard.md` | Extended explanation is available for evidence review | Planned | Optional |
| REVIEW-01 | `notes/capture-review-summary.md` | Review note | Final capture review | `docs/reports/kora-studio-evidence-checklist.md`; `docs/demo-capture/july31-package-index.md` | Captures were reviewed before public package use | Planned | Required after captures exist |

## Status Definitions

| Status | Meaning |
| --- | --- |
| Planned | The capture is required or expected but not yet produced |
| Captured | The capture exists but has not completed review |
| Reviewed | The capture has passed public-safe and claim-boundary review |
| Excluded | The capture was intentionally left out with a documented reason |

## Missing Captures

Missing before final July 31 package assembly:

- Studio route decision screenshot.
- Studio path explanation screenshot.
- Studio evidence mapping screenshot.
- Dashboard core message screenshot.
- Dashboard routing selectivity screenshot.
- Dashboard H100 measured execution screenshot.
- Dashboard 1M scale and saturation screenshot.
- Dashboard claim boundary screenshot.
- Two-minute demo recording summary.
- Optional five-minute demo recording summary.
- Capture review summary.
