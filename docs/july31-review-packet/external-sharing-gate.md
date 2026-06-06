# July 31 External Sharing Gate

## Current Gate Decision

Internal review: allowed.

Broader sharing as a final package: not allowed.

Broader sharing as an explicitly labeled early review packet: conditional. It may be considered only after the required fixes, capture disposition, public-safety review, and reviewer signoff are complete.

## Reason For Current Gate

The packet is coherent enough for internal July 31 review, but important items remain open:

- Public-safe dashboard screenshots are not yet committed and reviewed.
- Public-safe Studio screenshots are not yet committed and reviewed.
- Demo recording summary is not yet committed and reviewed.
- Technical report v0.1 still needs sentence-level evidence traceability review.
- Remaining figure/table drafts and captions are incomplete.
- Reviewer signoff is not complete.

## Internal Review Status

Internal reviewers may inspect:

- Packet index.
- Packet review issue list.
- External sharing gate.
- Reviewer guide.
- Evidence traceability map.
- Claim boundary sheet.
- Technical report v0.1.
- Dashboard evidence view.
- Studio demo evidence package plan.
- Readiness and gap report.

## Required Fixes Before Broader Sharing

- Resolve or explicitly defer all Important issues in `docs/july31-review-packet/packet-review-issue-list.md`.
- Complete sentence-level evidence traceability review.
- Complete claim boundary review.
- Complete figure/table caption review after planned assets are drafted or explicitly deferred.
- Confirm missing capture status.
- Complete public-safety review.
- Complete reviewer signoff checklist.

## Required Capture Assets Before Broader Sharing

Required unless explicitly deferred with rationale:

- Public-safe dashboard screenshots.
- Public-safe Studio screenshots.
- Two-minute demo recording summary or documented deferral.
- Capture review summary.

Capture artifacts must not include local machine details, browser account details, shell details, private endpoints, or secret material.

## Required Claim Review Before Broader Sharing

- Verify all uses of execution-path selectivity.
- Verify all uses of compute-weighted GPU demand reduction in benchmark workloads.
- Verify all uses of bounded H100 routed subset measurement.
- Confirm dashboard and Studio assets are labeled as evidence surfaces.
- Confirm no unsupported outcome language appears.
- Confirm internal review readiness is not described as broader sharing readiness.

## Required Reviewer Signoff Checklist

- [ ] Evidence traceability reviewer.
- [ ] Claim boundary reviewer.
- [ ] Public-safety reviewer.
- [ ] Figure/table reviewer.
- [ ] Demo capture reviewer.
- [ ] Packet owner.

## Approved External-Safe Summary After Internal Review

KORA Champion is an execution-path selectivity benchmark and evidence package. KORA is not benchmarking H100 as a raw accelerator; it benchmarks when H100 should be used. The current package shows benchmark routing across deterministic, cache, CPU, provider, GPU, and fallback paths, reports compute-weighted GPU demand reduction in benchmark workloads, and connects dry-run routing evidence to bounded H100 routed subset measurement. The package is an interim review packet and does not claim production outcomes, broad workload generality, external approval status, or final publication readiness.

## Do-Not-Say List

Do not say:

- KORA proves deployed financial outcomes.
- KORA proves customer workload outcomes.
- KORA proves real infrastructure outcomes.
- KORA proves a fixed multiplier result.
- KORA completed a full provider/GPU live workload comparison.
- KORA measured full 1M all-GPU execution.
- KORA proves production representativeness.
- KORA has a final paper-ready result.
- KORA has formal external validation.
- KORA has signed external validation.
- KORA proves broad workload superiority.
- KORA proves energy reduction.
