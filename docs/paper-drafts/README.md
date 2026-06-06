# KORA Paper Drafts

## Purpose

This directory holds early technical report drafts for KORA Champion. The drafts assemble existing benchmark evidence into a coherent report path while preserving claim boundaries.

KORA is framed as an execution-path selectivity system. It benchmarks when H100 should be used, rather than treating H100 as the default path for every request.

## Draft Status

Current status: early draft package with v0 and v0.1 drafts.

The documents in this directory are not submission materials. They are working drafts for technical review, evidence traceability, and claim-boundary tightening.

## Draft Inventory

| Draft | Path | Status |
| --- | --- | --- |
| v0 | `docs/paper-drafts/kora-early-technical-report-v0.md` | Claim-tightened early draft from Goal 016 |
| v0.1 | `docs/paper-drafts/kora-technical-report-v0-1.md` | Cleaner assembly draft from Goal 017 |

v0.1 is more reviewable than v0 because it incorporates the claim review, separates evidence categories more explicitly, and adds claim upgrade requirements. It is still not final-paper-ready.

## What Belongs Here

Allowed content:

- Early technical report drafts.
- Draft review checklists.
- Draft change logs.
- Section-level evidence notes.
- Relative links to reports, evidence files, dashboard assets, Studio evidence surface assets, and paper asset drafts.

## What Must Not Be Committed

Do not commit:

- Unreviewed publication files.
- Large binary media.
- Local machine details.
- Account or secret material.
- Raw service dumps.
- Unreviewed screenshots.
- Claims that exceed the committed evidence package.

## Claim Boundary Rules

Drafts may state that KORA has:

- Bounded live provider evidence.
- Measured H100 runtime evidence.
- Routing framework evidence.
- 100K routing selectivity evidence.
- Bounded H100 routed subset measurement.
- Multi-profile routing robustness evidence.
- 1M dry-run scale stability evidence.
- Bounded 1M H100 saturation subset evidence.
- Static dashboard evidence view.
- Studio evidence surface planning.
- Paper figure and table draft package.
- Compute-weighted GPU demand reduction in benchmark workloads.

Drafts must not imply deployed savings, customer workload outcomes, broad workload generality, complete million-request GPU-only measurement, external approval status, or finished publication readiness.

## Public-Safety Rules

- Use relative repository paths only.
- Do not include local absolute paths.
- Do not include account or secret material.
- Do not include environment-specific host details.
- Keep every metric tied to a source artifact.
- Keep measured, dry-run, estimated, and static package evidence visibly separated.

## Relationship To Reports and Paper Assets

This directory depends on:

- `docs/reports/kora-early-paper-outline.md`
- `docs/reports/kora-early-paper-results-map.md`
- `docs/reports/kora-early-paper-limitations-and-next-work.md`
- `docs/paper-assets/figure-specs.md`
- `docs/paper-assets/table-specs.md`
- `docs/paper-assets/draft-figure-1-execution-path-selectivity.md`
- `docs/paper-assets/draft-table-1-evidence-artifact-summary.md`

The paper assets provide figure and table drafts. The reports provide evidence inventory, claim boundaries, and methodology framing.

## Review Requirements Before Future Submission Use

Before any later external use:

- Verify every metric against its source artifact.
- Review all claim boundary language.
- Confirm all paths are relative.
- Confirm no private or environment-specific details appear.
- Review figure and table captions.
- Complete limitations and future work review.
- Confirm that draft status remains visible unless the document has completed a separate publication review process.
- Confirm v0.1 has completed sentence-level evidence traceability review.
- Confirm v0.1 has completed claim boundary review.
