# July 31 Reviewer Guide

## What To Read First

Start with:

1. `docs/july31-review-packet/packet-index.md`
2. `docs/paper-drafts/kora-technical-report-v0-1.md`
3. `docs/july31-review-packet/evidence-traceability-map.md`
4. `docs/july31-review-packet/claim-boundary-sheet.md`

Then inspect dashboard, Studio demo, paper assets, and gap reports as needed.

## What To Verify

Verify:

- The core message is visible and consistent.
- Claims use execution-path selectivity language.
- Metrics are tied to relative source paths.
- Dry-run routing evidence is separated from measured H100 subset evidence.
- Dashboard and Studio evidence surfaces are described as packaging and explanation layers.
- Remaining gaps are explicit.

## What Evidence Supports Which Claim

| Claim-safe statement | Primary evidence |
| --- | --- |
| KORA has routing framework evidence | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` |
| KORA has 100K routing selectivity evidence | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` |
| KORA has bounded H100 routed subset measurement | `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` |
| KORA has multi-profile routing robustness evidence | `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` |
| KORA has 1M dry-run scale stability evidence | `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` |
| KORA has a static dashboard evidence view | `docs/dashboard/index.html` |
| KORA has a technical report v0.1 draft | `docs/paper-drafts/kora-technical-report-v0-1.md` |

## What Should Not Be Inferred

Do not infer:

- Production outcomes.
- Customer workload outcomes.
- Broad workload generality.
- Complete live comparison across all routes.
- GPU execution measurement for every request in the million-request benchmark.
- External approval status.
- Final publication readiness.

## How To Interpret Benchmark Workload Results

Benchmark workload results show route decisions, route correctness metrics, path distribution, and compute-weighted GPU demand reduction in benchmark workloads. They should be interpreted as benchmark evidence for execution-path selectivity.

Dry-run routing evidence does not mean every path was executed live. It means route decisions and benchmark metrics were computed under the benchmark protocol.

## How To Interpret Bounded H100 Routed Subset Measurement

Bounded H100 routed subset measurement means that selected GPU-routed benchmark requests were executed and measured on H100. It strengthens the connection between dry-run route selection and measured runtime evidence for the GPU-routed subset.

It does not mean GPU execution was measured for every request in the source benchmark.

## How To Interpret Dashboard and Studio Evidence

The dashboard evidence view packages committed reports and evidence files for inspection. Studio is a Studio evidence surface for explaining route decisions and linking them to evidence.

These surfaces help communicate and navigate the evidence chain. They do not create new runtime measurements.

## Questions Before External Sharing

- Are all numeric metrics traceable to source artifacts?
- Are all planned figures and tables clearly marked as planned?
- Are missing captures clearly listed?
- Does any wording imply unsupported outcomes?
- Are limitations visible near the results?
- Has the packet passed public-safety review?

## July 31 Reviewer Checklist

- [ ] Core message reviewed.
- [ ] Technical report v0.1 reviewed.
- [ ] Evidence traceability map reviewed.
- [ ] Claim boundary sheet reviewed.
- [ ] Dashboard evidence view checked.
- [ ] Studio demo package checked.
- [ ] Readiness and gap report reviewed.
- [ ] Issue list prepared before broader sharing.
