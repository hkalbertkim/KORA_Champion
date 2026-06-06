# KORA Technical Report v0.1 Assembly Report

## 1. Goal 017 Summary

Goal 017 assembled a public-safe technical report v0.1 package. The v0.1 draft incorporates the v0 claim review, improves evidence traceability, adds a clearer reader interpretation guide, and makes claim boundaries easier to review.

## 2. Files Created or Updated

| File | Purpose |
| --- | --- |
| `docs/paper-drafts/kora-technical-report-v0-1.md` | Cleaner v0.1 technical report draft |
| `docs/paper-drafts/kora-technical-report-v0-1-review-checklist.md` | v0.1 review checklist |
| `docs/paper-drafts/kora-technical-report-v0-1-change-log.md` | v0.1 change log |
| `docs/paper-drafts/README.md` | Updated draft status and v0.1 entry |
| `docs/reports/kora-technical-report-v0-1-assembly-report.md` | Goal 017 assembly report |

## 3. How v0.1 Differs From v0

v0.1 differs from v0 in these ways:

- Keeps v0 intact and creates a separate v0.1 draft.
- Moves the reader interpretation guide before the abstract.
- Adds a dedicated evidence chain section.
- Labels the results section as claim-safe interpretation.
- Adds an explicit non-claim section.
- Adds Appendix C for claim upgrade requirements.
- Improves linkage to figure/table assets and July 31 review needs.

## 4. Goal 016 Review Findings Incorporated

Incorporated findings:

- Dry-run routing evidence is separated from measured H100 routed subset evidence.
- Dashboard and Studio assets are described as evidence surfaces, not benchmark runs.
- Metrics are framed as benchmark workload results.
- Limitations are visible before future work.
- Claim upgrade requirements are separated from current claims.

## 5. Evidence Artifacts Referenced

The v0.1 draft references:

- Provider evidence artifacts.
- H100 micro benchmark artifacts.
- 100K routing benchmark artifacts.
- Bounded H100 routed subset measurement artifacts.
- Multi-profile routing robustness artifacts.
- 1M scale and bounded saturation artifacts.
- Static dashboard evidence view.
- Studio evidence surface planning.
- July 31 interim result report package.
- Paper figure and table draft package.
- Claim review report.

## 6. Claims Deliberately Bounded

The v0.1 draft keeps these claims bounded:

- Compute-weighted GPU demand reduction is described only in benchmark workloads.
- H100 routed subset evidence is described as bounded measured subset evidence.
- 100K and 1M route metrics are described as dry-run routing evidence.
- Dashboard and Studio are described as evidence surfaces.
- The report remains an early technical report and not a final publication package.

## 7. Missing Before External Sharing

Remaining gaps:

- Sentence-level evidence traceability review.
- Figure/table caption review.
- Dashboard and Studio capture artifacts if visual review packet use is required.
- Remaining figure and table drafts.
- Final July 31 packet index.

## 8. Claim-Safe Summary

The v0.1 package supports KORA as an execution-path selectivity system. It states that KORA benchmarks when H100 should be used, routes benchmark workloads across deterministic, cache, CPU, provider, GPU, and fallback paths, reports compute-weighted GPU demand reduction in benchmark workloads, and connects dry-run routing evidence to bounded H100 routed subset measurement.

The v0.1 package does not claim production outcomes, customer workload outcomes, broad workload generality, complete live comparison across all routes, GPU execution measurement for every request in the million-request benchmark, external approval status, or final publication readiness.

## 9. Recommended Goal 018

Goal 018

Title: July 31 Review Packet Assembly

Rationale: After v0.1 report assembly, the highest leverage next step is to assemble the July 31 review packet that links the report, evidence package, dashboard package, demo package, and claim review artifacts.
