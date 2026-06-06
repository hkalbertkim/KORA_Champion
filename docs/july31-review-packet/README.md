# KORA July 31 Review Packet

## Purpose

This directory organizes the public-safe July 31 review packet for KORA Champion. The packet links the technical report, evidence package, dashboard package, Studio demo package, claim boundaries, and remaining gaps.

KORA is framed as an execution-path selectivity system. KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

## Packet Status

Status: assembled for review.

This packet is not a final submission package, not a publication package, and not a production-results package. It is a review packet that helps reviewers inspect the current evidence chain and remaining gaps.

## What Belongs Here

Allowed packet files:

- Packet index.
- Reviewer guide.
- Evidence traceability map.
- Claim boundary sheet.
- Readiness and gap report.
- Relative links to existing reports, evidence files, dashboard files, demo package files, paper drafts, and paper assets.

## What Must Not Be Committed

Do not commit:

- Large binary media.
- Unreviewed screenshots or recordings.
- Local machine details.
- Account or secret material.
- Raw service dumps.
- Claims that exceed the current evidence package.

## How To Review The Packet

Recommended review flow:

1. Read `docs/july31-review-packet/packet-index.md`.
2. Read `docs/july31-review-packet/reviewer-guide.md`.
3. Check `docs/july31-review-packet/evidence-traceability-map.md`.
4. Check `docs/july31-review-packet/claim-boundary-sheet.md`.
5. Review gaps in `docs/july31-review-packet/readiness-and-gap-report.md`.
6. Open the linked technical report, evidence table, dashboard package, and demo package as needed.

## Relationship To Other Assets

| Area | Primary paths |
| --- | --- |
| Evidence reports | `docs/reports/july-31-interim-result-report-draft.md`; `docs/reports/july-31-interim-result-report-evidence-table.md` |
| Dashboard package | `docs/dashboard/index.html`; `docs/dashboard/dashboard-data.json` |
| Studio demo package | `docs/demo-capture/july31-package-index.md`; `docs/reports/kora-studio-demo-video-storyboard.md` |
| Technical report | `docs/paper-drafts/kora-technical-report-v0-1.md` |
| Paper assets | `docs/paper-assets/figure-specs.md`; `docs/paper-assets/table-specs.md` |
| Claim review | `docs/reports/kora-early-technical-report-v0-claim-review.md` |

## Claim Boundary Rules

Use:

- Execution-path selectivity.
- Compute-weighted GPU demand reduction in benchmark workloads.
- Bounded H100 routed subset measurement.
- Static dashboard evidence view.
- Studio evidence surface.

Do not imply production outcomes, customer workload outcomes, broad workload generality, complete live comparison across all routes, GPU execution measurement for every request in the million-request benchmark, external approval status, or final publication readiness.

## Public-Safety Rules

- Use relative repository paths only.
- Do not include local absolute paths.
- Do not include account or secret material.
- Do not include environment-specific host details.
- Keep every metric tied to a source artifact.
- Keep measured, dry-run, estimated, and static package evidence separated.

## Review Requirements Before External Sharing

- Complete evidence traceability review.
- Complete claim boundary review.
- Complete public-safety scan.
- Confirm missing captures and planned figures/tables are clearly marked.
- Confirm the packet remains labeled as a review packet.
