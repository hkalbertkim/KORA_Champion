# July 31 External Sharing Gate

## Current External Sharing Status

Status: not ready for external sharing as a final package.

The packet is ready for internal review. It should not be presented as final or publication-ready until the required fixes and review steps are complete.

## Internal Review Status

Internal review is allowed.

Internal reviewers may inspect:

- Packet index.
- Reviewer guide.
- Evidence traceability map.
- Claim boundary sheet.
- Technical report v0.1.
- Dashboard evidence view.
- Studio demo evidence package plan.
- Readiness and gap report.
- Packet review issue list.

## External Sharing Status

External sharing as a final package is not allowed yet.

External sharing as an explicitly labeled early review packet may be considered only after the required signoff checklist is completed.

## Required Fixes Before External Sharing

- Resolve or explicitly defer all Important issues in `docs/july31-review-packet/packet-review-issue-list.md`.
- Complete sentence-level evidence traceability review.
- Complete claim boundary review.
- Complete figure/table caption review.
- Confirm missing capture status.
- Confirm public-safety scan.

## Required Screenshots/Video Before External Sharing

Required unless explicitly deferred:

- Public-safe dashboard screenshots.
- Public-safe Studio screenshots.
- Two-minute demo recording summary or documented deferral.
- Capture review summary.

## Required Claim Review Before External Sharing

- Verify all uses of execution-path selectivity.
- Verify all uses of compute-weighted GPU demand reduction in benchmark workloads.
- Verify all uses of bounded H100 routed subset measurement.
- Confirm dashboard and Studio assets are labeled as evidence surfaces.
- Confirm no unsupported outcome language appears.

## Required Reviewer Signoff Checklist

- [ ] Evidence traceability reviewer.
- [ ] Claim boundary reviewer.
- [ ] Public-safety reviewer.
- [ ] Figure/table reviewer.
- [ ] Demo capture reviewer.
- [ ] Packet owner.

## Approved One-Paragraph External-Safe Summary

KORA Champion is an execution-path selectivity benchmark and evidence package. KORA is not benchmarking H100 as a raw accelerator; it benchmarks when H100 should be used. The current package shows benchmark routing across deterministic, cache, CPU, provider, GPU, and fallback paths, reports compute-weighted GPU demand reduction in benchmark workloads, and connects dry-run routing evidence to bounded H100 routed subset measurement. The package is an interim review packet and does not claim production outcomes, broad workload generality, external approval status, or final publication readiness.

## Do-Not-Say List

Do not say:

- KORA proves production cost reduction.
- KORA proves customer workload savings.
- KORA proves real infrastructure savings.
- KORA proves a fixed multiplier result.
- KORA completed a full provider/GPU live workload comparison.
- KORA measured full 1M all-GPU execution.
- KORA proves production representativeness.
- KORA has a final paper-ready result.
- KORA has formal government validation.
- KORA has signed partner validation.
- KORA proves broad workload superiority.
- KORA proves energy reduction.
