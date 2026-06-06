# July 31 Packet Review Issue List

## Review Summary

The July 31 review packet is coherent enough for internal review. The core message is consistent, the packet links the technical report v0.1 to evidence artifacts, and claim boundaries are visible. No blocker-level claim issue was found in the packet review or Goal 020 fix pass.

The packet is not ready for broader sharing as a final package. Important gaps remain around reviewed screenshots, demo recording summary, remaining figure/table drafts, sentence-level evidence traceability, and reviewer signoff.

## Goal 020 Fix Pass Summary

Goal 020 addressed packet navigation, controlling claim-boundary visibility, external gate visibility, and issue-list clarity. It did not resolve capture execution, sentence-level technical report traceability, or unfinished figure/table assets because those require separate review or capture work.

## Severity Definitions

| Severity | Definition |
| --- | --- |
| Blocker | Must be fixed before internal packet review can proceed |
| Important | Must be fixed before broader sharing or final July 31 packet use |
| Polish | Improves clarity, navigation, or reviewer confidence |

## Fix Pass Status Definitions

| Status | Meaning |
| --- | --- |
| Addressed | Packet documents were updated in Goal 020 or the issue was already resolved by Goal 019 artifacts |
| Open | Still requires follow-up before broader sharing or final packet use |
| Deferred | Explicitly moved to a later goal because the needed work is outside this fix pass |
| Non-blocking | Reviewed and kept open only as polish or future improvement |

## Claim Safety Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status | Fix pass status | Resolution notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CS-001 | Important | Claim safety | Packet uses safe wording, but external sharing gate was separate from the main review flow | Reviewers may miss the boundary between internal review and broader sharing | Add external sharing gate to the required review order | Packet owner | Addressed | `docs/july31-review-packet/packet-index.md` and `docs/july31-review-packet/reviewer-guide.md` now require gate review near the start of the flow |
| CS-002 | Polish | Claim safety | Claim boundaries are distributed across several files | Reviewers may not know which sheet is controlling | Treat `docs/july31-review-packet/claim-boundary-sheet.md` as the packet-level controlling sheet | Packet owner | Addressed | Packet index and claim-boundary sheet now state that the claim-boundary sheet is controlling |

## Evidence Traceability Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status | Fix pass status | Resolution notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ET-001 | Important | Evidence traceability | Technical report v0.1 still needs sentence-level evidence traceability review | Numeric claims are source-linked, but every interpretive sentence has not been checked | Perform sentence-level pass against `docs/july31-review-packet/evidence-traceability-map.md` | Report owner | Open | Goal 020 improved packet-level traceability labels but did not perform sentence-level report review |
| ET-002 | Important | Evidence traceability | Dashboard and Studio captures remain planned, not captured | Visual review cannot confirm the final reviewer experience | Add reviewed capture artifacts or documented exclusions | Demo package owner | Deferred | Requires Final Demo Capture Execution or an explicit capture deferral decision |
| ET-003 | Polish | Evidence traceability | Packet index links many documents but not a concise issue summary | Reviewers may need to scan multiple files to find open work | Add this issue list to the packet index | Packet owner | Addressed | Packet index now includes the issue list in the first-read path and readiness group |

## Reader Flow Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status | Fix pass status | Resolution notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RF-001 | Important | Reader flow | Review order starts with guide and traceability map, but does not explicitly require issue list review yet | Reviewers may miss known gaps | Update packet index review order after this file is committed | Packet owner | Addressed | Packet index and reviewer guide now require issue-list review before evidence interpretation |
| RF-002 | Polish | Reader flow | The packet is document-rich and may feel long for a first-pass evaluator | A shorter entry point would help | Add a one-page reviewer summary in a later pass if needed | Packet owner | Non-blocking | First-read path now provides a shorter entry sequence; a separate one-page summary remains optional |

## Dashboard/Studio Evidence Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status | Fix pass status | Resolution notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DS-001 | Important | Dashboard/Studio evidence | Final dashboard screenshots are missing | Static dashboard exists, but capture package is not complete | Capture public-safe dashboard screenshots or document deferral | Demo package owner | Deferred | Requires capture execution or explicit capture deferral |
| DS-002 | Important | Dashboard/Studio evidence | Final Studio screenshots are missing | Studio remains a planned evidence surface, not a captured demo artifact | Capture public-safe Studio screenshots or document deferral | Demo package owner | Deferred | Requires capture execution or explicit capture deferral |
| DS-003 | Important | Dashboard/Studio evidence | Demo recording summary is missing | The reviewer cannot yet inspect the intended demo narrative as a completed artifact | Add two-minute recording summary or documented deferral | Demo package owner | Deferred | Requires capture execution or explicit recording deferral |

## Technical Report v0.1 Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status | Fix pass status | Resolution notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | Important | Technical report v0.1 | v0.1 is suitable for internal review but not broader sharing | The draft still needs traceability and caption checks | Complete v0.1 review checklist before broader sharing | Report owner | Open | Goal 020 clarified this gate but did not complete the technical report review checklist |
| TR-002 | Polish | Technical report v0.1 | The report points to planned figures and tables that are not complete | Readers may expect more visual support | Add remaining figures/tables or keep planned status explicit | Report owner | Deferred | Packet index and reviewer guide now flag planned-vs-drafted status; asset creation remains future work |

## Figure/Table Readiness Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status | Fix pass status | Resolution notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FT-001 | Important | Figure/table readiness | Figure 2, Figure 3, and Figure 4 are planned but not drafted | Report visuals are incomplete | Draft or explicitly defer remaining figures | Paper assets owner | Deferred | Requires paper asset drafting or explicit deferral |
| FT-002 | Important | Figure/table readiness | Table 2, Table 3, Table 4, and Appendix Table A1 are planned but not drafted | Evidence and claim review tables are incomplete | Draft or explicitly defer remaining tables | Paper assets owner | Deferred | Requires paper asset drafting or explicit deferral |
| FT-003 | Polish | Figure/table readiness | Captions need a final claim-boundary pass | Captions are high-risk locations for overstatement | Run caption review after drafts exist | Paper assets owner | Deferred | Caption review should follow asset drafting |

## July 31 Readiness Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status | Fix pass status | Resolution notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| JR-001 | Important | July 31 readiness | Packet is ready for internal review, not broader sharing | Broader use requires more review and capture artifacts | Keep status explicit in readiness report and external sharing gate | Packet owner | Addressed | Readiness report and external sharing gate now state current readiness more directly |
| JR-002 | Important | July 31 readiness | Packet-level issue list was missing before Goal 019 | Known gaps needed a single tracking file | Use this file as the issue list going forward | Packet owner | Addressed | Issue list exists and now includes Goal 020 fix pass status |

## External Sharing Readiness Issues

| Issue ID | Severity | Area | Finding | Why it matters | Recommended fix | Owner/status | Fix pass status | Resolution notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ES-001 | Important | External sharing readiness | External sharing gate did not exist before Goal 019 | External readiness criteria were distributed across documents | Use `docs/july31-review-packet/external-sharing-gate.md` as the controlling gate | Packet owner | Addressed | External sharing gate exists and is now part of the first-read path |
| ES-002 | Important | External sharing readiness | Reviewer signoff is not complete | Broader sharing needs explicit review status | Complete signoff checklist before broader sharing | Packet owner | Open | Goal 020 clarified signoff requirements but did not complete reviewer signoff |

## Remaining Open Issues

- ET-001: Sentence-level evidence traceability review remains open.
- TR-001: Technical report v0.1 review checklist remains open.
- ES-002: Reviewer signoff remains open.

## Deferred Issues

- ET-002, DS-001, DS-002, and DS-003: capture execution or capture deferral.
- TR-002, FT-001, FT-002, and FT-003: remaining paper asset drafting and caption review.

## Unresolved Blockers

No blocker-level issues remain for internal July 31 packet review.

## No-Go Items Before Broader Sharing

- Do not share as a final package before sentence-level evidence traceability review.
- Do not share as a final package before claim boundary review.
- Do not share as a final package before missing capture status is resolved or explicitly deferred.
- Do not share as a final package before figure/table caption review.
- Do not share as a final package while planned assets are ambiguous.
- Do not share as a final package before reviewer signoff is complete.

## Acceptable Items For Internal Review Now

- Packet index.
- Packet review issue list.
- External sharing gate.
- Reviewer guide.
- Evidence traceability map.
- Claim boundary sheet.
- Readiness and gap report.
- Technical report v0.1.
- Static dashboard evidence view.
- Studio demo evidence package plan.
- Paper asset specs and current drafts.
