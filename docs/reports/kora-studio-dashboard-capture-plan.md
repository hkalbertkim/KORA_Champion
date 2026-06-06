# KORA Studio Dashboard Capture Plan

## 1. Dashboard Capture Objective

The dashboard capture objective is to create a public-safe screenshot package showing the KORA evidence chain in a reviewer-facing format. The captures should support the Studio demo by showing the benchmark reports, evidence files, and claim boundaries behind execution-path selectivity.

The dashboard captures should not be treated as new runtime evidence. They are a capture package for the existing static dashboard evidence view.

## 2. Required Dashboard Views

| Capture | Expected filename | Required data points | Existing backing evidence |
| --- | --- | --- | --- |
| Core message | `dashboard-core-message-01.png` | English core message, Korean core message, evidence framing | `docs/dashboard/index.html`; `docs/reports/july-31-interim-result-report-draft.md` |
| KPI cards | `dashboard-kpi-cards-02.png` | Provider, H100, routing, dashboard readiness indicators | `docs/dashboard/dashboard-data.json` |
| Evidence chain timeline | `dashboard-evidence-chain-03.png` | GPU-004A through GPU-006 and July 31 package sequence | `docs/reports/ai-champion-interim-package-index.md` |
| 100K routing selectivity | `dashboard-routing-selectivity-04.png` | Route distribution, acceptable route rate, unsafe misroute rate, compute-weighted GPU demand reduction in benchmark workloads | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` |
| Multi-profile robustness | `dashboard-multi-profile-05.png` | Profile-level routing robustness and unsafe misroute summary | `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` |
| H100 measured execution | `dashboard-h100-measured-06.png` | Bounded H100 routed subset measurement and measured runtime metrics | `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` |
| 1M scale and saturation | `dashboard-scale-saturation-07.png` | 1M dry-run scale stability and bounded H100 saturation subset evidence | `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` |
| Evidence links | `dashboard-evidence-links-08.png` | Links to reports and evidence files | `docs/reports/july-31-interim-result-report-evidence-table.md` |
| Claim boundaries | `dashboard-claim-boundaries-09.png` | Supported claims and non-claims | `docs/reports/july-31-interim-result-report-claim-boundary.md` |

## 3. Capture Sequence

1. Open `docs/dashboard/index.html` in a browser.
2. Set the browser width to a standard desktop capture size.
3. Capture the core message section.
4. Capture KPI cards.
5. Capture the evidence chain timeline.
6. Capture 100K routing selectivity.
7. Capture multi-profile robustness.
8. Capture H100 measured execution.
9. Capture 1M scale and saturation.
10. Capture evidence links.
11. Capture claim boundaries.
12. Review every image for public-safe content and readability.

## 4. What Each Screenshot Proves

| Screenshot | What it proves | What it does not prove |
| --- | --- | --- |
| Core message | The dashboard frames the evidence around when H100 should be used | It does not prove runtime behavior by itself |
| KPI cards | The evidence package has reviewer-facing summary metrics | It does not create new benchmark results |
| Evidence chain timeline | The work is organized as a sequence of committed evidence artifacts | It does not imply official validation |
| 100K routing selectivity | KORA has 100K dry-run execution-path selectivity evidence | It does not prove measured GPU reduction |
| Multi-profile robustness | KORA can compare route behavior across benchmark profiles | It does not prove production representativeness |
| H100 measured execution | KORA has bounded H100 routed subset measurement | It does not prove full workload execution |
| 1M scale and saturation | KORA has 1M dry-run scale stability and bounded saturation evidence | It does not prove full 1M all-GPU measured execution |
| Evidence links | The dashboard connects to committed reports and evidence files | It does not replace the underlying evidence files |
| Claim boundaries | The package states supported claims and non-claims | It does not expand the claim boundary |

## 5. Quality Checklist

- [ ] Capture uses a clean browser viewport.
- [ ] Text is readable without zooming.
- [ ] File names match the expected capture names.
- [ ] Captures avoid browser UI that contains private account or local machine details.
- [ ] Captures avoid terminal windows and raw service output.
- [ ] Every capture has a matching evidence artifact listed in this plan.
- [ ] Every capture includes enough surrounding context to be interpreted without narration.
- [ ] Claim boundary capture is included in the final package.
- [ ] Captures are reviewed before being added to a public evidence package.

## 6. Claim Boundary Checklist

- [ ] Captures use "execution-path selectivity" consistently.
- [ ] Captures use "compute-weighted GPU demand reduction in benchmark workloads" when describing the benchmark metric.
- [ ] Captures use "bounded H100 routed subset measurement" for measured GPU subset evidence.
- [ ] Captures distinguish measured, dry-run, and estimated evidence.
- [ ] Captures do not imply production savings.
- [ ] Captures do not imply customer workload savings.
- [ ] Captures do not imply real infrastructure savings.
- [ ] Captures do not imply proven 10x savings.
- [ ] Captures do not imply full provider/GPU live workload comparison.
- [ ] Captures do not imply full 1M all-GPU measured execution.
- [ ] Captures do not imply production representativeness.
- [ ] Captures do not imply official validation.
