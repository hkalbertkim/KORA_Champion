# July 31 Packet Review Issue List

## Review Summary

The July 31 review packet is coherent enough for internal review. The core message is consistent, the packet links the technical report v0.1 to evidence artifacts, and claim boundaries are visible. No blocker-level claim issue was found in the packet review.

The packet is not ready for external sharing as a final package. Important gaps remain around reviewed screenshots, demo recording summaries, remaining figure/table drafts, sentence-level evidence traceability, and external sharing signoff.

## Severity Definitions

| Severity | Definition |
| --- | --- |
| Blocker | Must be fixed before internal packet review can proceed |
| Important | Must be fixed before external sharing or final July 31 packet use |
| Polish | Improves clarity, navigation, or reviewer confidence |

## Claim Safety Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status |
| --- | --- | --- | --- | --- | --- | --- |
| CS-001 | Important | Claim safety | Packet uses safe wording, but external sharing gate is still separate from the main review flow | Reviewers may miss the boundary between internal review and external sharing | Add external sharing gate to the required review order | Packet owner / open |
| CS-002 | Polish | Claim safety | Claim boundaries are distributed across several files | Reviewers may not know which sheet is controlling | Treat `docs/july31-review-packet/claim-boundary-sheet.md` as the packet-level controlling sheet | Packet owner / open |

## Evidence Traceability Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status |
| --- | --- | --- | --- | --- | --- | --- |
| ET-001 | Important | Evidence traceability | Technical report v0.1 still needs sentence-level evidence traceability review | Numeric claims are source-linked, but every interpretive sentence has not been checked | Perform sentence-level pass against `docs/july31-review-packet/evidence-traceability-map.md` | Report owner / open |
| ET-002 | Important | Evidence traceability | Dashboard and Studio captures remain planned, not captured | Visual review cannot confirm the final reviewer experience | Add reviewed capture artifacts or documented exclusions | Demo package owner / open |
| ET-003 | Polish | Evidence traceability | Packet index links many documents but not a concise issue summary | Reviewers may need to scan multiple files to find open work | Add this issue list to the packet index in a later fix pass | Packet owner / open |

## Reader Flow Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status |
| --- | --- | --- | --- | --- | --- | --- |
| RF-001 | Important | Reader flow | Review order starts with guide and traceability map, but does not explicitly require issue list review yet | Reviewers may miss known gaps | Update packet index review order after this file is committed | Packet owner / open |
| RF-002 | Polish | Reader flow | The packet is document-rich and may feel long for a first-pass evaluator | A shorter entry point would help | Add a one-page reviewer summary in a later pass if needed | Packet owner / open |

## Dashboard/Studio Evidence Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status |
| --- | --- | --- | --- | --- | --- | --- |
| DS-001 | Important | Dashboard/Studio evidence | Final dashboard screenshots are missing | Static dashboard exists, but capture package is not complete | Capture public-safe dashboard screenshots or document deferral | Demo package owner / open |
| DS-002 | Important | Dashboard/Studio evidence | Final Studio screenshots are missing | Studio remains a planned evidence surface, not a captured demo artifact | Capture public-safe Studio screenshots or document deferral | Demo package owner / open |
| DS-003 | Important | Dashboard/Studio evidence | Demo recording summary is missing | The reviewer cannot yet inspect the intended demo narrative as a completed artifact | Add two-minute recording summary or documented deferral | Demo package owner / open |

## Technical Report v0.1 Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status |
| --- | --- | --- | --- | --- | --- | --- |
| TR-001 | Important | Technical report v0.1 | v0.1 is suitable for internal review but not broader sharing | The draft still needs traceability and caption checks | Complete v0.1 review checklist before broader sharing | Report owner / open |
| TR-002 | Polish | Technical report v0.1 | The report points to planned figures and tables that are not complete | Readers may expect more visual support | Add remaining figures/tables or keep planned status explicit | Report owner / open |

## Figure/Table Readiness Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status |
| --- | --- | --- | --- | --- | --- | --- |
| FT-001 | Important | Figure/table readiness | Figure 2, Figure 3, and Figure 4 are planned but not drafted | Report visuals are incomplete | Draft or explicitly defer remaining figures | Paper assets owner / open |
| FT-002 | Important | Figure/table readiness | Table 2, Table 3, Table 4, and Appendix Table A1 are planned but not drafted | Evidence and claim review tables are incomplete | Draft or explicitly defer remaining tables | Paper assets owner / open |
| FT-003 | Polish | Figure/table readiness | Captions need a final claim-boundary pass | Captions are high-risk locations for overstatement | Run caption review after drafts exist | Paper assets owner / open |

## July 31 Readiness Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status |
| --- | --- | --- | --- | --- | --- | --- |
| JR-001 | Important | July 31 readiness | Packet is ready for internal review, not external sharing | External use requires more review and capture artifacts | Keep status explicit in readiness report and external sharing gate | Packet owner / open |
| JR-002 | Important | July 31 readiness | Packet-level issue list was missing before Goal 019 | Known gaps needed a single tracking file | Use this file as the issue list going forward | Packet owner / created |

## External Sharing Readiness Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status |
| --- | --- | --- | --- | --- | --- | --- |
| ES-001 | Important | External sharing readiness | External sharing gate did not exist before Goal 019 | External readiness criteria were distributed across documents | Use `docs/july31-review-packet/external-sharing-gate.md` as the controlling gate | Packet owner / created |
| ES-002 | Important | External sharing readiness | Reviewer signoff is not complete | Broader sharing needs explicit review status | Complete signoff checklist before broader sharing | Packet owner / open |

## No-Go Items Before External Sharing

- Do not share as a final package before sentence-level evidence traceability review.
- Do not share as a final package before claim boundary review.
- Do not share as a final package before missing capture status is resolved or explicitly deferred.
- Do not share as a final package before figure/table caption review.
- Do not share as a final package while planned assets are ambiguous.

## Acceptable Items For Internal Review Now

- Packet index.
- Reviewer guide.
- Evidence traceability map.
- Claim boundary sheet.
- Readiness and gap report.
- Technical report v0.1.
- Static dashboard evidence view.
- Studio demo evidence package plan.
- Paper asset specs and current drafts.
