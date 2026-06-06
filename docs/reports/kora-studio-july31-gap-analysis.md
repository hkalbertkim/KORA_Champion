# KORA Studio July 31 Gap Analysis

## 1. Current Evidence Status

KORA Champion has a strong interim evidence chain for execution-path selectivity, but KORA Studio is not yet fully captured as a July 31 demo evidence surface.

| Area | Status | Evidence |
| --- | --- | --- |
| Provider path | Available, bounded | Provider live sample and normalized comparison artifact |
| H100 runtime | Available, bounded | GPU micro benchmark, H100 routed subset, and saturation subset evidence |
| Routing framework | Available | GPU-004A framework report |
| 100K route selectivity | Available | GPU-004B dry-run routing comparison |
| H100 routed subset | Available | GPU-004C bounded H100 routed subset measurement |
| Multi-profile robustness | Available | GPU-005 benchmark report |
| 1M scale and saturation | Available | GPU-006 dry-run scale and bounded saturation subset report |
| Dashboard evidence view | Available | Static dashboard files and dashboard report |
| July 31 report package | Available | Draft, evidence table, claim boundary, next work plan, executive summary |
| Studio evidence surface | Partial planning only | Goal 010 reports |
| Demo recording and captures | Gap | Not yet captured |

## 2. Gaps Before July 31

| Gap | Impact | Priority |
| --- | --- | --- |
| Studio route surface capture | Reviewer cannot yet see Studio as a demo evidence surface | High |
| Dashboard screenshot package | Dashboard exists but capture assets are not yet packaged | High |
| Short demo recording | Reviewer walkthrough is not yet recorded | High |
| Final package index update | Studio and capture artifacts will need a single entry point | High |
| Optional broader provider sample | Provider path remains bounded and small | Medium |
| Optional additional H100 calibration | H100 evidence is bounded but sufficient for current claim level | Medium |
| Early paper draft outline | Research framing is not yet packaged as a draft outline | Medium |

## 3. Priority Ordering

1. Produce demo video and dashboard capture package.
2. Capture Studio route decision screenshots.
3. Update the interim package index with Studio and capture artifacts.
4. Perform final claim boundary review.
5. Only then consider optional broader provider or H100 measurements.
6. Prepare an early paper draft outline after the demo evidence package is stable.

## 4. Documentation-Only Work

The following can be completed with documentation only:

| Work item | Output |
| --- | --- |
| Studio launch evidence plan | `docs/reports/kora-studio-launch-evidence-plan.md` |
| Studio demo script | `docs/reports/kora-studio-demo-script.md` |
| Studio checklist | `docs/reports/kora-studio-evidence-checklist.md` |
| Studio gap analysis | `docs/reports/kora-studio-july31-gap-analysis.md` |
| Package index update | Updated index after captures exist |
| Claim boundary review | Updated claim-safe wording checklist |

## 5. Work Requiring Implementation

Implementation should remain minimal. The July 31 need is a credible demo evidence surface, not a full product.

| Work item | Minimum implementation |
| --- | --- |
| Studio route view | A static or local view showing route decision, path explanation, evidence mapping, and claim boundary |
| Evidence link panel | Links from route paths to existing reports and dashboard evidence |
| Capture-ready layout | Stable display suitable for screenshots and short recording |

Avoid broad product work before July 31 unless it directly improves the demo evidence surface.

## 6. Work Requiring Live Capture

| Capture | Minimum output |
| --- | --- |
| Studio screenshots | Route decision, path explanation, evidence mapping, claim boundary |
| Dashboard screenshots | Core message, KPIs, evidence chain, measured H100 evidence, claim boundaries |
| Short recording | Two-minute Studio plus dashboard walkthrough |
| Extended recording | Five-minute version if time allows |

Live capture should use public-safe labels and avoid exposing access details or non-public operational context.

## 7. Work Requiring Additional Benchmark, Provider, or GPU Measurement

No additional measurement is required for the minimum July 31 Studio evidence plan.

Optional measurement work:

| Optional work | Benefit | Claim boundary |
| --- | --- | --- |
| Broader bounded provider sample | Improves provider path readiness evidence | Still not a full provider/GPU live workload comparison |
| Repeated H100 routed subset run | Improves measured runtime confidence | Still bounded H100 routed subset measurement |
| Additional benchmark profiles | Improves benchmark profile coverage | Still not production representativeness |

The current evidence chain is sufficient to support a Studio demo evidence surface if the demo stays claim-safe.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Studio is interpreted as a production product | Overclaim risk | Use "demo evidence surface" and show claim boundaries |
| Benchmark reduction is interpreted as savings | Public claim risk | Use "compute-weighted GPU demand reduction in benchmark workloads" |
| H100 subset is interpreted as full workload measurement | Evidence misread | Use "bounded H100 routed subset measurement" |
| 1M scale result is interpreted as full GPU execution | Evidence misread | Label 1M routing as dry-run scale stability and saturation as bounded |
| Demo lacks visual captures | Reviewer friction | Prioritize screenshots and short recording before additional benchmarks |
| Optional measurement delays capture package | Schedule risk | Defer optional measurement until after the demo capture package |

## 9. Mitigations

- Keep Studio language tied to execution-path selectivity.
- Place non-claims near screenshots and demo recording notes.
- Use existing dashboard evidence view as the primary evidence bridge.
- Keep measured, dry-run, and estimated evidence labels visible.
- Make the next goal a capture package rather than another broad planning report.

## 10. Recommended Goal 011

Goal 011

Title: Demo Video and Dashboard Capture Package

Rationale: The most immediate July 31 gap is not additional benchmark evidence. The current evidence chain already supports a public-safe Studio explanation surface. The next useful step is to capture the Studio/demo walkthrough, dashboard screenshots, and final reviewer package links so the evidence can be inspected quickly and claim-safely.
