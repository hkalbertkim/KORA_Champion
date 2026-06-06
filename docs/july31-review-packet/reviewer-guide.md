# July 31 Reviewer Guide

## Review Objective

Review the July 31 packet for internal readiness, evidence traceability, and claim safety. The packet should be read as an interim review package for KORA execution-path selectivity, not as a final publication package or external claim-upgrade package.

## Step-By-Step Reviewer Flow

| Step | Read | Verify | Do not infer |
| --- | --- | --- | --- |
| 1 | `docs/july31-review-packet/README.md` and `docs/july31-review-packet/packet-index.md` | Packet scope, document order, and missing item summary are clear | That the packet is final or externally cleared |
| 2 | `docs/july31-review-packet/packet-review-issue-list.md` | Known issues are visible before evaluating readiness | That open capture or signoff items are complete |
| 3 | `docs/july31-review-packet/external-sharing-gate.md` | Internal review is allowed and broader sharing remains gated | That internal review readiness means external readiness |
| 4 | `docs/july31-review-packet/claim-boundary-sheet.md` | Approved one-liners and unsafe inference patterns are clear | Production outcomes, broad workload generality, or external approval status |
| 5 | `docs/july31-review-packet/evidence-traceability-map.md` | Each claim-safe statement maps to a report or artifact | That every interpretive sentence has completed sentence-level review |
| 6 | `docs/reports/july-31-interim-result-report-evidence-table.md` | Evidence chain is inspectable through relative paths | That evidence supports stronger claims than listed |
| 7 | `docs/paper-drafts/kora-technical-report-v0-1.md` | Report v0.1 keeps benchmark and measurement categories separate | Final publication readiness |
| 8 | Dashboard and Studio package files | Dashboard and Studio are labeled as evidence surfaces | New runtime measurement from dashboard or Studio assets |
| 9 | Paper asset specs | Planned and drafted assets are clearly distinguished | That planned figures/tables already exist |
| 10 | `docs/july31-review-packet/readiness-and-gap-report.md` | Current readiness and remaining gaps are explicit | That missing items can be ignored before broader sharing |

## Core Message Check

Confirm this message appears consistently:

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

## Evidence-To-Claim Interpretation

| Claim-safe statement | What to verify | Primary evidence |
| --- | --- | --- |
| KORA has routing framework evidence | The routing benchmark framework is described as a measurement harness and route-decision framework | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` |
| KORA has 100K routing selectivity evidence | The claim is framed as dry-run routing evidence | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` |
| KORA has bounded H100 routed subset measurement | The claim is limited to measured GPU-routed subset execution | `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` |
| KORA has multi-profile routing robustness evidence | The claim is limited to benchmark profiles | `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` |
| KORA has 1M dry-run scale stability and bounded saturation subset evidence | The report separates dry-run scale behavior from measured saturation subset evidence | `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` |
| KORA has a static dashboard evidence view | The dashboard is presented as navigation and packaging | `docs/dashboard/index.html` |
| KORA has a Studio demo evidence package plan | Studio is presented as an explanation surface backed by existing artifacts | `docs/demo-capture/july31-package-index.md` |
| KORA has a technical report v0.1 draft | v0.1 is labeled as draft and bounded | `docs/paper-drafts/kora-technical-report-v0-1.md` |

## How To Interpret Benchmark Workload Results

Benchmark workload results show route decisions, route correctness metrics, path distribution, and compute-weighted GPU demand reduction in benchmark workloads. They support execution-path selectivity claims within the benchmark protocol.

Dry-run routing evidence does not mean every route was executed live. It means route decisions and benchmark metrics were computed under the benchmark protocol.

Measured subset evidence does not mean complete workload measurement. It means selected routed requests were executed and measured under a bounded measurement design.

## How To Interpret Bounded H100 Routed Subset Measurement

Bounded H100 routed subset measurement means selected GPU-routed benchmark requests were executed and measured on H100. It strengthens the connection between dry-run route selection and measured runtime evidence for the GPU-routed subset.

It does not mean GPU execution was measured for every request in the source benchmark.

## How To Interpret Dashboard And Studio Evidence

The dashboard evidence view packages committed reports and evidence files for inspection. Studio is a Studio evidence surface for explaining route decisions and linking them to evidence.

These surfaces help communicate and navigate the evidence chain. They do not create new runtime measurements.

## What Should Not Be Inferred

Do not infer:

- Production outcomes.
- Customer workload outcomes.
- Broad workload generality.
- Complete live comparison across all routes.
- GPU execution measurement for every request in the million-request benchmark.
- External approval status.
- Final publication readiness.
- Completion of public-safe screenshots or demo recording before those artifacts are committed and reviewed.

## Questions Before Broader Sharing

- Are all numeric metrics traceable to source artifacts?
- Has sentence-level evidence traceability review been completed for the technical report v0.1?
- Are all planned figures and tables clearly marked as planned?
- Are missing captures clearly listed or explicitly deferred?
- Does any wording imply unsupported outcomes?
- Are limitations visible near the results?
- Has the packet passed public-safety review?
- Has the external sharing gate checklist been completed?

## July 31 Reviewer Checklist

- [ ] Core message reviewed.
- [ ] Packet issue list reviewed.
- [ ] External sharing gate reviewed.
- [ ] Technical report v0.1 reviewed.
- [ ] Evidence traceability map reviewed.
- [ ] Claim boundary sheet reviewed as the controlling packet-level wording sheet.
- [ ] Dashboard evidence view checked as a static evidence surface.
- [ ] Studio demo package checked as a planned evidence surface.
- [ ] Paper figures/tables checked for planned vs drafted status.
- [ ] Readiness and gap report reviewed.
- [ ] Remaining open issues accepted for internal review or assigned for follow-up.
