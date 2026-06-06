# KORA Paper Assets

## Purpose

This directory holds public-safe draft assets for the KORA Champion technical report path. The assets support a future report about execution-path selectivity: KORA benchmarks when H100 should be used, rather than treating H100 as the default execution path for every request.

## What Belongs Here

Allowed assets:

- Figure draft specifications.
- Table draft specifications.
- Mermaid diagrams.
- Markdown table drafts.
- Source-data mapping notes.
- Caption drafts.
- Review checklists.

Assets should remain lightweight and reviewable in text form unless a later implementation task explicitly approves rendered images.

## What Must Not Be Committed

Do not commit:

- Large binary media.
- Unreviewed rendered images.
- Local machine details.
- Secret material.
- Raw service dumps.
- Account or browser session material.
- Assets that imply unsupported deployed results.

## Source-Data Requirements

Every figure or table must identify:

- Primary source report or evidence file.
- Evidence type: measured, dry-run, estimated, or static package.
- Supported claim.
- Explicit non-claim.
- Relative repository paths only.

## Figure and Table Review Rules

- Keep GPU as one possible execution path, not the default path.
- Use execution-path selectivity as the central frame.
- Separate measured, dry-run, estimated, and static package evidence.
- Use compute-weighted GPU demand reduction in benchmark workloads for the benchmark demand metric.
- Use bounded H100 routed subset measurement for measured routed GPU subset evidence.
- Include a claim boundary note in every caption draft.

## Claim Boundary Rules

The assets may support:

- Bounded live provider evidence.
- Measured H100 runtime evidence.
- Routing framework evidence.
- 100K routing selectivity evidence.
- Bounded H100 routed subset measurement.
- Multi-profile routing robustness evidence.
- 1M dry-run scale stability evidence.
- Bounded 1M H100 saturation subset evidence.
- Static dashboard evidence view.
- Studio evidence surface.
- Compute-weighted GPU demand reduction in benchmark workloads.

The assets must not imply deployed savings, customer workload outcomes, broad workload generality, official review status, complete million-request GPU-only measurement, or final publication readiness.

## Public-Safety Rules

- Use relative repository paths.
- Do not include local absolute paths.
- Do not include account material.
- Do not include environment-specific host details.
- Do not include raw operational dumps.
- Keep figure and table text public-safe and claim-bounded.

## Asset Naming Convention

Use lowercase, hyphen-separated names:

- Figure specs: `figure-specs.md`
- Table specs: `table-specs.md`
- Draft figures: `draft-figure-{number}-{short-name}.md`
- Draft tables: `draft-table-{number}-{short-name}.md`

Examples:

- `draft-figure-1-execution-path-selectivity.md`
- `draft-table-1-evidence-artifact-summary.md`
