# KORA Early Paper Results Map

## 1. Purpose

This map connects existing KORA Champion artifacts to possible sections in an early technical report. The map is intended for report drafting only. It does not add new benchmark evidence.

## 2. Results Map

| Evidence area | Existing artifact path | Paper section | What it supports | What it does not support | Safe paper wording | Non-claim warning |
| --- | --- | --- | --- | --- | --- | --- |
| Provider evidence | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json`; `docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json` | Benchmark setup; results caveats | Bounded live provider path evidence | Complete live comparison across provider and GPU routes | KORA has bounded live provider evidence that supports provider path readiness | Do not present this as broad provider benchmarking |
| H100 micro benchmark | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json`; `docs/reports/kora-champion-gpu-003-h100-micro-benchmark-report.md` | H100 runtime readiness | Measured H100 runtime evidence in a bounded benchmark setting | Route-aware demand reduction by itself | KORA has measured H100 runtime evidence for benchmark execution | Do not use this alone as execution-path selectivity proof |
| 100K routing selectivity | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json`; `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` | Main routing results | 100K dry-run execution-path selectivity evidence | Measured GPU runtime reduction | KORA shows 100K routing selectivity and compute-weighted GPU demand reduction in benchmark workloads | Label as dry-run benchmark evidence |
| H100 routed subset measurement | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json`; `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` | Measured routed subset results | Bounded H100 routed subset measurement | Complete all-GPU workload measurement | KORA connects a GPU-routed benchmark subset to measured H100 execution | Keep all complete-baseline comparisons labeled as estimates |
| Multi-profile robustness | `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json`; `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` | Robustness results | Execution-path selectivity across multiple benchmark profiles | Deployed-workload generality | KORA evaluates routing robustness across multiple benchmark distributions | Do not describe profiles as deployed-workload representative |
| 1M scale and saturation | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json`; `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json`; `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` | Scale and saturation results | 1M dry-run scale stability and bounded 1M H100 saturation subset evidence | Complete million-request GPU-only measurement | KORA combines 1M dry-run scale evidence with bounded H100 saturation subset measurement | Separate dry-run scale from measured saturation evidence |
| Dashboard evidence view | `docs/dashboard/index.html`; `docs/dashboard/dashboard-data.json`; `docs/reports/ai-champion-dashboard-evidence-view-report.md` | Evidence packaging; appendix | Static dashboard evidence view for reviewer inspection | New runtime or route measurement | KORA packages the evidence chain in a static dashboard evidence view | Do not treat the dashboard as a new experiment |
| Studio demo evidence | `docs/reports/kora-studio-launch-evidence-plan.md`; `docs/reports/kora-studio-demo-video-storyboard.md`; `docs/demo-capture/july31-package-index.md` | System explanation; appendix | Studio as a demo evidence surface for execution-path selectivity | Production deployment or external validation | KORA Studio explains route decisions and maps them to existing evidence artifacts | Do not present Studio as measured workload evidence |
| July 31 interim report package | `docs/reports/july-31-interim-result-report-draft.md`; `docs/reports/july-31-interim-result-report-evidence-table.md`; `docs/reports/july-31-interim-result-report-claim-boundary.md`; `docs/reports/july-31-interim-result-report-executive-summary.md` | Report framing; claim boundary | Organized interim evidence package | Submission-ready research result | The July 31 package provides interim evidence and claim boundaries | Do not present the package as a completed paper |

## 3. Suggested Results Ordering

1. Route taxonomy and benchmark setup.
2. 100K execution-path selectivity.
3. Bounded H100 routed subset measurement.
4. Multi-profile robustness.
5. 1M dry-run scale stability and bounded saturation evidence.
6. Dashboard and Studio evidence packaging.
7. Limitations and claim boundaries.

## 4. Evidence-Type Reminder

- Measured evidence: bounded provider, H100 micro benchmark, routed subset, or saturation subset execution was recorded.
- Dry-run benchmark evidence: route decisions and metrics were computed without live execution of every route.
- Estimated runtime evidence: runtime values are derived from measured H100 calibration and benchmark compute weight.
- Static package evidence: dashboard, Studio, and report artifacts package existing evidence for review.
