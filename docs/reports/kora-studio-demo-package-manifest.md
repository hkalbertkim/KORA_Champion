# KORA Studio Demo Package Manifest

## 1. Intended Final Package Structure

The final July 31 demo evidence package should use this public-safe structure:

```text
docs/demo-capture/
  README.md
  screenshots/
    studio-route-decision-01.png
    studio-path-explanation-02.png
    studio-evidence-map-03.png
    dashboard-core-message-04.png
    dashboard-routing-selectivity-05.png
    dashboard-h100-measured-06.png
    dashboard-scale-saturation-07.png
    dashboard-claim-boundary-08.png
  recordings/
    kora-studio-two-minute-demo.mp4
    kora-studio-five-minute-demo.mp4
  notes/
    capture-review-summary.md
```

Large binary recording files should not be committed unless explicitly approved. If recordings are stored outside the repository, the README should reference only public-safe filenames, checksums if available, and a short description of what each recording shows.

## 2. Required Screenshots

| Screenshot | Required | Purpose |
| --- | --- | --- |
| `studio-route-decision-01.png` | Yes | Shows Studio as a route decision surface |
| `studio-path-explanation-02.png` | Yes | Shows how the selected path is explained |
| `studio-evidence-map-03.png` | Yes | Shows links from Studio to benchmark evidence |
| `dashboard-core-message-04.png` | Yes | Shows the main evidence framing |
| `dashboard-routing-selectivity-05.png` | Yes | Shows 100K execution-path selectivity evidence |
| `dashboard-h100-measured-06.png` | Yes | Shows bounded H100 routed subset measurement |
| `dashboard-scale-saturation-07.png` | Yes | Shows 1M dry-run scale and bounded saturation evidence |
| `dashboard-claim-boundary-08.png` | Yes | Shows supported claims and non-claims |

## 3. Required Screen Recordings

| Recording | Required | Target length | Purpose |
| --- | --- | ---: | --- |
| `kora-studio-two-minute-demo.mp4` | Yes | 2 minutes | Concise reviewer walkthrough |
| `kora-studio-five-minute-demo.mp4` | Optional but useful | 5 minutes | Extended walkthrough with evidence details |

If video capture is deferred, the package should include the storyboard, narration script, capture plan, and readiness report created in Goal 011.

## 4. Required Dashboard Captures

The dashboard capture set should include:

- Core message.
- KPI cards.
- Evidence chain timeline.
- 100K execution-path selectivity section.
- Multi-profile robustness section.
- H100 measured execution section.
- 1M scale and saturation section.
- Evidence links.
- Claim boundaries.

## 5. Required Reports

| Report | Purpose |
| --- | --- |
| `docs/reports/kora-studio-launch-evidence-plan.md` | Defines Studio evidence objective and boundaries |
| `docs/reports/kora-studio-demo-script.md` | Defines the initial demo narrative |
| `docs/reports/kora-studio-evidence-checklist.md` | Tracks evidence package readiness |
| `docs/reports/kora-studio-july31-gap-analysis.md` | Defines remaining gaps and priorities |
| `docs/reports/kora-studio-demo-video-storyboard.md` | Defines scene-by-scene video plan |
| `docs/reports/kora-studio-dashboard-capture-plan.md` | Defines required dashboard captures |
| `docs/reports/kora-studio-demo-narration-script.md` | Defines safe narration and evaluator Q&A |
| `docs/reports/kora-studio-demo-capture-readiness-report.md` | Summarizes Goal 011 readiness |

## 6. Required Evidence JSON References

| Evidence JSON | Use |
| --- | --- |
| `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` | Bounded provider path evidence |
| `docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json` | Provider normalized comparison artifact |
| `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` | Measured H100 runtime evidence |
| `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | 100K routing selectivity evidence |
| `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | Bounded H100 routed subset measurement |
| `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json` | Multi-profile robustness summary |
| `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` | 1M dry-run scale summary |
| `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | Bounded 1M H100 saturation subset evidence |

## 7. Required README Summary

The final `docs/demo-capture/README.md` should include:

- Package purpose.
- Capture status.
- Screenshot inventory.
- Recording inventory.
- Evidence report links.
- Evidence JSON references.
- Claim boundary summary.
- Missing items.
- Local validation summary.

## 8. File Naming Convention

Use lowercase, hyphen-separated names:

- Screenshots: `{surface}-{section}-{sequence}.png`
- Recordings: `{surface}-{duration}-demo.mp4`
- Notes: `{package-area}-{summary-type}.md`

Examples:

- `dashboard-routing-selectivity-05.png`
- `studio-evidence-map-03.png`
- `kora-studio-two-minute-demo.mp4`
- `capture-review-summary.md`

## 9. Review Checklist

- [ ] Every screenshot has a matching evidence artifact.
- [ ] Every recording follows the approved narration script.
- [ ] Claim boundaries are visible in the package.
- [ ] Measured, dry-run, and estimated evidence are separated.
- [ ] No production savings claim appears.
- [ ] No official validation claim appears.
- [ ] No private local details appear in captures.
- [ ] Final package index is updated.
- [ ] Repository validation passes before commit.

## 10. July 31 Readiness Status

| Item | Status |
| --- | --- |
| Storyboard | Prepared in Goal 011 |
| Dashboard capture plan | Prepared in Goal 011 |
| Demo package manifest | Prepared in Goal 011 |
| Narration script | Prepared in Goal 011 |
| Capture readiness report | Prepared in Goal 011 |
| Placeholder capture directory | Prepared in Goal 011 |
| Actual screenshots | Missing |
| Actual screen recordings | Missing |
| Final package index update | Missing |

## 11. Missing Items

The final July 31 package still needs:

- Studio route decision screenshots.
- Dashboard screenshot set.
- Two-minute demo recording.
- Optional five-minute demo recording.
- Capture review summary.
- Final package index update after captures are available.
