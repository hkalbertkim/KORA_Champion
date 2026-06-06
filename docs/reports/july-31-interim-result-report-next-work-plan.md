# July 31 Interim Result Report Next Work Plan

## 1. Remaining Work Before July 31

| Workstream | Status | Target output | Owner | Priority |
| --- | --- | --- | --- | --- |
| KORA Studio launch evidence | Gap | Public-safe launch artifact, screenshots, or local demo evidence | Product/engineering | High |
| Demo video/dashboard capture | Dashboard exists, capture not recorded | Short screencapture showing evidence chain and claim boundaries | Product/engineering | High |
| July 31 report polish | Draft package exists | Reviewer-ready interim result package | Product/engineering | High |
| Broader provider sample | Partial-live evidence exists | Optional bounded provider sample set | Engineering | Medium |
| Early paper/arXiv draft | Evidence inventory exists | Methods/results outline with caveats | Research/engineering | Medium |
| Dashboard screenshot assets | Dashboard exists | Static screenshots for report/deck | Product/engineering | Medium |
| Second-stage planning | Initial roadmap exists | Milestone plan with validation gates | Product/engineering | Medium |

## 2. KORA Studio Launch Evidence Plan

Objective: add public-safe evidence that KORA Studio exists as a reviewer-facing or user-facing experience.

Candidate artifacts:

- KORA Studio launch report.
- Static screenshots or local demo captures.
- Public-safe feature list.
- Evidence that Studio can display or navigate KORA routing/dashboard outputs.
- Known limitations and claim boundaries.

Minimum acceptable July 31 evidence:

- One public-safe launch report.
- One set of screenshots or dashboard-linked flow notes.
- Clear statement that Studio evidence is launch/demo evidence, not production representativeness.

## 3. Demo Video/Dashboard Capture Plan

Objective: produce a short screencapture using `docs/dashboard/index.html`.

Recommended flow:

1. Open dashboard hero/core message.
2. Show KPI cards.
3. Show evidence chain timeline.
4. Show 100K and 1M routing selectivity tables.
5. Show H100 measured execution table.
6. Show multi-profile robustness table.
7. Show evidence links.
8. End on claim boundaries.

Required overlay:

`Benchmark evidence for execution-path selectivity. Not production savings evidence.`

What not to say:

- Do not claim production cost reduction.
- Do not claim customer workload savings.
- Do not claim proven 10x savings.
- Do not imply full 1M all-GPU measured execution.

## 4. Broader Provider Sample Plan

Objective: expand provider path readiness only if broader provider claims are needed.

Candidate plan:

- Keep live sample count bounded.
- Use dry-run mode by default.
- Use explicit live flag only for measured samples.
- Record provider latency, token counts, success/failure counts, and claim level.
- Normalize results into public-safe comparison evidence.

Claim boundary:

- Broader provider samples may support provider path reliability evidence.
- They should not be presented as provider cost reduction or full provider/GPU live workload comparison unless those experiments are explicitly run.

## 5. Paper/arXiv Draft Plan

Objective: create an early draft that separates method, evidence, and limitations.

Recommended outline:

1. Problem: execution-path selectivity for AI workloads.
2. KORA routing benchmark framework.
3. Oracle independence and router input restrictions.
4. Workload profiles and compute weights.
5. Router policies and KORA adapter boundary.
6. 100K dry-run results.
7. Multi-profile robustness.
8. H100 routed subset measurement.
9. 1M scale and saturation subset.
10. Threats to validity.
11. Claim boundaries and future work.

Minimum July 31 target:

- Methods outline.
- Results table placeholders filled from committed evidence.
- Limitations section.
- No final-paper claim.

## 6. Second-Stage Plan If Selected

Second-stage goals should include:

| Goal | Purpose | Evidence output |
| --- | --- | --- |
| Stronger live provider sample | Improve provider path evidence | Bounded provider sample report and JSON |
| Measured provider-routed sample set | Connect provider-routed benchmark subset to measured provider calls | Provider-routed subset evidence |
| Additional H100 routed subset calibration | Strengthen measured runtime calibration | Larger or repeated H100 routed subset evidence |
| KORA Studio public demo | Show user-facing workflow | Studio launch report and screenshots |
| Dashboard/screencast package | Support reviewer inspection | Demo video notes and capture artifacts |
| Paper draft | Prepare research narrative | Draft methodology and results report |
| Broader workload profile validation | Reduce benchmark narrowness | Additional profile comparison evidence |
| Real pilot workload if available | Add practical workload evidence | Pilot evidence only if claim-safe and permissioned |

## 7. Risks and Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Evidence wording overclaims savings | Public claim risk | Use claim boundary appendix in every report and demo |
| Provider sample remains too small | Weak provider evidence | Keep provider claim limited to bounded path readiness |
| Studio evidence not ready | July 31 package gap | Provide dashboard demo as fallback and mark Studio as next-stage |
| Demo capture not recorded | Reviewer experience weaker | Use static dashboard and screenshots if video is not ready |
| H100 subset mistaken for full workload | Misinterpretation risk | Label bounded subset and estimated runtime in every table |
| Paper draft reads too final | Overclaim risk | Publish only as early draft readiness, not final result |

## 8. Evidence Gaps and Owners

| Gap | Owner | Next action | Claim-safe output |
| --- | --- | --- | --- |
| KORA Studio launch evidence | Product/engineering | Create launch/demo report | Studio launch evidence |
| Demo video/screencapture | Product/engineering | Record dashboard walkthrough | Demo capture notes and video artifact |
| Broader provider sample | Engineering | Run bounded sample if needed | Provider sample evidence |
| Paper/arXiv draft | Research/engineering | Draft methods and limitations | Early paper draft |
| Dashboard screenshots | Product/engineering | Capture static dashboard sections | Screenshot evidence package |
| Additional H100 calibration | Engineering | Run bounded routed subset calibration if needed | Runtime evidence |

## 9. Immediate Next Goal

Goal 010

Title: KORA Studio Launch Evidence Plan

Rationale: KORA Studio is the largest explicit July 31 gap after Goal 009. The benchmark and dashboard evidence chain is now strong enough for interim reporting, while Studio launch evidence remains missing.
