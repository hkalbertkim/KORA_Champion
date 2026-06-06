# KORA Paper Table Specs

## Table 1: Evidence Artifact Summary

Status: draft.

Purpose: summarize the key evidence chain and its claim boundaries.

Required columns:

- Evidence item.
- Primary artifact/report.
- Supports.
- Does not support.
- Claim-safe wording.

Source evidence files:

- `docs/reports/july-31-interim-result-report-evidence-table.md`
- `docs/reports/kora-early-paper-results-map.md`

Draft caption:

"KORA Champion evidence artifacts and claim-safe usage for an early technical report."

Claim-safe interpretation: the table organizes existing artifacts and does not add new measurements.

Explicit non-claims: the table does not establish deployed savings, broad workload generality, or complete GPU-only measurement.

## Table 2: Claim Boundary Matrix

Status: planned.

Purpose: separate supported claims from explicit non-claims for the paper draft.

Required columns:

- Claim area.
- Supported wording.
- Evidence backing.
- Evidence type.
- Non-claim boundary.

Source evidence files:

- `docs/reports/july-31-interim-result-report-claim-boundary.md`
- `docs/reports/kora-early-paper-limitations-and-next-work.md`

Draft caption:

"Claim boundaries for interpreting KORA Champion benchmark evidence."

Claim-safe interpretation: supported claims remain limited to benchmark evidence and bounded measurement.

Explicit non-claims: the matrix must not upgrade benchmark evidence into deployed or official outcomes.

## Table 3: Benchmark Profile Summary

Status: planned.

Purpose: compare benchmark profile behavior from the multi-profile routing robustness work.

Required columns:

- Profile.
- Route distribution summary.
- Acceptable route rate.
- Unsafe misroute rate.
- Compute-weighted GPU demand reduction in benchmark workloads.
- Claim boundary note.

Source evidence files:

- `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md`
- `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json`

Draft caption:

"Execution-path selectivity across benchmark profile distributions."

Claim-safe interpretation: profile comparisons test benchmark route robustness.

Explicit non-claims: profile comparisons do not prove broad deployed-workload generality.

## Table 4: Paper Section to Evidence Map

Status: planned.

Purpose: map early paper sections to supporting artifacts.

Required columns:

- Paper section.
- Evidence used.
- Artifact path.
- Evidence type.
- Claim-safe role.

Source evidence files:

- `docs/reports/kora-early-paper-outline.md`
- `docs/reports/kora-early-paper-results-map.md`

Draft caption:

"Mapping from early technical report sections to source evidence artifacts."

Claim-safe interpretation: each section should cite existing evidence and state limits.

Explicit non-claims: section mapping does not create new evidence or external review status.

## Appendix Table A1: Artifact Index

Status: planned.

Purpose: provide a public artifact index for reports, JSON evidence, dashboard, Studio, demo package, and paper assets.

Required columns:

- Artifact group.
- Path.
- Evidence type.
- Intended use.
- Claim boundary note.

Source evidence files:

- `docs/reports/ai-champion-interim-package-index.md`
- `docs/demo-capture/evidence-map.md`
- `docs/paper-assets/figure-specs.md`
- `docs/paper-assets/table-specs.md`

Draft caption:

"Public artifact index for KORA Champion early technical report evidence."

Claim-safe interpretation: artifact paths support review and traceability.

Explicit non-claims: artifact availability does not imply new runtime execution or deployed validation.
