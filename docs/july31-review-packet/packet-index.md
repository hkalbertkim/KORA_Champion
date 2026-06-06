# July 31 Review Packet Index

## Executive Packet Summary

This packet organizes KORA Champion materials for July 31 review. It links the current evidence package, dashboard evidence view, Studio demo evidence package, technical report v0.1, paper assets, claim boundaries, issue list, and remaining gaps.

This is a review packet. It is not a final submission package, publication package, or claim-upgrade package.

## Core Message

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

## First-Read Path

Use this path for a fast first review:

1. `docs/july31-review-packet/README.md` - packet scope and public-safety rules.
2. `docs/july31-review-packet/packet-index.md` - document map and review order.
3. `docs/july31-review-packet/packet-review-issue-list.md` - known issues and fix pass status.
4. `docs/july31-review-packet/external-sharing-gate.md` - current gate decision and required signoff.
5. `docs/july31-review-packet/reviewer-guide.md` - step-by-step reviewer flow.
6. `docs/july31-review-packet/evidence-traceability-map.md` - claim-to-evidence mapping.
7. `docs/july31-review-packet/claim-boundary-sheet.md` - controlling packet-level claim language.
8. `docs/paper-drafts/kora-technical-report-v0-1.md` - current technical report draft.

## Primary Packet Documents

| Document | Purpose | Review role |
| --- | --- | --- |
| `docs/july31-review-packet/README.md` | Packet scope, allowed contents, and safety rules | Start here |
| `docs/july31-review-packet/packet-index.md` | Packet navigation and document grouping | Start here |
| `docs/july31-review-packet/packet-review-issue-list.md` | Known issues, fix pass status, and remaining work | Required before external sharing |
| `docs/july31-review-packet/external-sharing-gate.md` | Gate decision, required fixes, capture requirements, and signoff | Required before external sharing |
| `docs/july31-review-packet/reviewer-guide.md` | Reviewer sequence and interpretation checks | Required for internal review |
| `docs/july31-review-packet/evidence-traceability-map.md` | Claim-safe statements mapped to evidence | Required for evidence review |
| `docs/july31-review-packet/claim-boundary-sheet.md` | Approved wording and unsafe inference patterns | Controlling claim sheet |
| `docs/july31-review-packet/readiness-and-gap-report.md` | Readiness state and remaining gaps | Required before final packet use |

## Evidence Reports

These documents are evidence reports or evidence indexes. They support benchmark-workload claims and should not be read as production-outcome evidence.

| Document | Purpose |
| --- | --- |
| `docs/reports/ai-champion-interim-package-index.md` | Evidence package entry point |
| `docs/reports/july-31-interim-result-report-draft.md` | Interim result report draft |
| `docs/reports/july-31-interim-result-report-evidence-table.md` | Evidence table |
| `docs/reports/july-31-interim-result-report-claim-boundary.md` | Claim boundary appendix |
| `docs/reports/july-31-interim-result-report-executive-summary.md` | Executive summary |
| `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` | 100K routing benchmark report |
| `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` | Bounded H100 routed subset measurement report |
| `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` | Multi-profile routing robustness report |
| `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` | 1M scale and saturation benchmark report |

## Dashboard And Demo Evidence Surfaces

These documents and files package or explain the evidence chain. They are not new runtime measurements.

| Document | Purpose |
| --- | --- |
| `docs/dashboard/index.html` | Static dashboard evidence view |
| `docs/dashboard/dashboard-data.json` | Dashboard data source |
| `docs/demo-capture/july31-package-index.md` | Demo capture package index |
| `docs/demo-capture/evidence-map.md` | Demo capture evidence map |
| `docs/july31-review-packet/external-sharing-gate.md` | Capture requirements before broader sharing |
| `docs/reports/kora-studio-demo-video-storyboard.md` | Demo storyboard |
| `docs/reports/kora-studio-demo-narration-script.md` | Demo narration script |

## Technical Report Drafts

These are draft report materials. They are useful for July 31 review but are not final-paper-ready.

| Document | Purpose |
| --- | --- |
| `docs/paper-drafts/kora-technical-report-v0-1.md` | Technical report v0.1 |
| `docs/paper-drafts/kora-technical-report-v0-1-review-checklist.md` | Technical report review checklist |
| `docs/paper-drafts/kora-technical-report-v0-1-change-log.md` | v0.1 change log |
| `docs/reports/kora-technical-report-v0-1-assembly-report.md` | v0.1 assembly report |
| `docs/reports/kora-early-technical-report-v0-claim-review.md` | v0 claim review |

## Claim Boundary Material

Use `docs/july31-review-packet/claim-boundary-sheet.md` as the packet-level controlling sheet. Other boundary documents provide supporting context.

| Document | Purpose |
| --- | --- |
| `docs/july31-review-packet/claim-boundary-sheet.md` | Controlling packet-level wording sheet |
| `docs/reports/july-31-interim-result-report-claim-boundary.md` | July 31 claim boundary appendix |
| `docs/reports/kora-early-technical-report-v0-claim-review.md` | Technical report claim review |
| `docs/july31-review-packet/external-sharing-gate.md` | Gate language and required review before broader sharing |

## Paper Asset Documents

These are figure and table plans or draft assets. Only Figure 1 and Table 1 have draft assets in the current packet.

| Document | Purpose |
| --- | --- |
| `docs/paper-assets/figure-specs.md` | Figure specs |
| `docs/paper-assets/table-specs.md` | Table specs |
| `docs/paper-assets/draft-figure-1-execution-path-selectivity.md` | Draft Figure 1 |
| `docs/paper-assets/draft-table-1-evidence-artifact-summary.md` | Draft Table 1 |

## Readiness And Gap Material

| Document | Purpose |
| --- | --- |
| `docs/july31-review-packet/readiness-and-gap-report.md` | Packet-level readiness and gaps |
| `docs/july31-review-packet/packet-review-issue-list.md` | Issue list and fix pass status |
| `docs/reports/kora-july31-packet-review-report.md` | Goal 019 packet review report |
| `docs/reports/kora-july31-packet-fix-pass-report.md` | Goal 020 fix pass report |
| `docs/reports/kora-studio-july31-gap-analysis.md` | Studio gap analysis |
| `docs/reports/kora-studio-demo-capture-readiness-report.md` | Demo capture readiness |
| `docs/reports/kora-technical-report-review-readiness-report.md` | Technical report review readiness |

## Recommended Full Review Order

1. Confirm packet scope in `docs/july31-review-packet/README.md`.
2. Read this packet index.
3. Review known issues in `docs/july31-review-packet/packet-review-issue-list.md`.
4. Check the gate in `docs/july31-review-packet/external-sharing-gate.md`.
5. Follow `docs/july31-review-packet/reviewer-guide.md`.
6. Verify claim/evidence mapping in `docs/july31-review-packet/evidence-traceability-map.md`.
7. Check wording against `docs/july31-review-packet/claim-boundary-sheet.md`.
8. Review the evidence table in `docs/reports/july-31-interim-result-report-evidence-table.md`.
9. Review `docs/paper-drafts/kora-technical-report-v0-1.md`.
10. Inspect dashboard and Studio evidence-surface materials.
11. Inspect paper asset specs and current drafts.
12. Finish with `docs/july31-review-packet/readiness-and-gap-report.md`.

## Missing Item Summary

Still missing or deferred:

- Final public-safe dashboard screenshots.
- Final public-safe Studio screenshots.
- Demo recording or reviewed recording summary.
- Sentence-level evidence traceability review for the technical report v0.1.
- Remaining figure and table drafts beyond Figure 1 and Table 1.
- Figure/table caption review after remaining assets exist.
- Reviewer signoff for broader sharing.

## Next Work

Recommended next work: Goal 021, Final Demo Capture Execution.
