# KORA Studio Launch Evidence Plan

## 1. July 31 Studio Evidence Objective

KORA Studio should be presented on July 31 as a demo evidence surface for explaining execution-path selectivity. The objective is to show how a reviewer can understand which execution path a request should use, how that decision connects to committed benchmark evidence, and why the evidence supports benchmark workload claims without implying production savings.

Core message:

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

The Studio evidence objective is therefore:

- Show deterministic, cache, CPU, provider, GPU, and fallback paths as distinct execution choices.
- Connect each path to the existing KORA Core evidence chain.
- Make benchmark workload boundaries visible.
- Show compute-weighted GPU demand reduction in benchmark workloads only where backed by committed evidence.
- Keep all measured, dry-run, and estimated values labeled.

## 2. Minimum Credible KORA Studio Demo Surface

The minimum credible Studio surface does not need to be a full product. It should be a clear reviewer-facing experience with enough structure to explain execution-path selectivity.

Minimum surface:

| Surface element | Purpose | July 31 requirement |
| --- | --- | --- |
| Route decision panel | Shows the selected execution path for a sample request | Required |
| Path explanation panel | Explains why deterministic, cache, CPU, provider, GPU, or fallback was selected | Required |
| Evidence link panel | Links the visible decision to benchmark reports and evidence files | Required |
| Dashboard bridge | Opens or references the static dashboard evidence view | Required |
| Claim boundary panel | States supported claims and non-claims | Required |
| Capture-ready layout | Supports screenshots and a short walkthrough recording | Required |

The demo surface can be static or locally interactive if it clearly shows the route decision, path explanation, and evidence mapping. It should not require broad live execution, production integration, or new benchmark runs to be credible for July 31.

## 3. Required Evidence Artifacts

The Studio launch evidence package should include:

| Artifact | Purpose | Status |
| --- | --- | --- |
| Studio launch evidence plan | Defines objective, artifacts, claims, and gaps | Created in Goal 010 |
| Studio demo script | Defines the reviewer walkthrough and approved wording | Created in Goal 010 |
| Studio evidence checklist | Tracks captures, links, validation, and safety review | Created in Goal 010 |
| Studio July 31 gap analysis | Prioritizes remaining work before July 31 | Created in Goal 010 |
| Dashboard captures | Shows the current evidence view in static form | Needed |
| Studio screen captures | Shows the Studio route explanation surface | Needed |
| Short demo recording | Shows the route-to-evidence narrative | Needed |
| Final package index update | Adds Studio evidence artifacts to the review package | Needed |

## 4. Mapping Studio to the Existing KORA Evidence Chain

Studio should not stand alone as a new evidence claim. It should map directly to the existing KORA Core evidence chain.

| Studio concept | Existing evidence | Claim-safe interpretation |
| --- | --- | --- |
| Deterministic path | Routing benchmark framework and dry-run route distribution | Some benchmark requests can be handled without GPU or provider execution |
| Cache path | 100K, multi-profile, and 1M route distribution evidence | Cache-eligible benchmark requests are separated from GPU-routed requests |
| CPU path | Routing framework path taxonomy | CPU is part of the benchmark routing decision space |
| Provider path | Bounded live provider evidence and normalized comparison artifact | Provider path readiness exists in a bounded sample |
| GPU path | H100 micro benchmark, routed subset measurement, and saturation subset measurement | H100 execution is measured for bounded benchmark subsets |
| Fallback path | Routing benchmark framework and route correctness metrics | Fallback is an explicit path for requests that should not be forced into an unsafe route |
| Dashboard evidence view | Static dashboard files and dashboard evidence report | The evidence chain can be inspected in a reviewer-facing view |

## 5. Evaluator Understanding After Seeing Studio

After seeing Studio, an evaluator should understand:

- KORA evaluates when H100 should be used, not whether H100 is generally fast.
- Execution-path selectivity is the central benchmark target.
- The benchmark routes include deterministic, cache, CPU, provider, GPU, and fallback paths.
- The strongest measured GPU evidence is bounded H100 routed subset measurement and bounded H100 saturation subset measurement.
- The 100K, multi-profile, and 1M results are benchmark evidence, not production representativeness evidence.
- Compute-weighted GPU demand reduction in benchmark workloads is a benchmark metric, not a real infrastructure savings claim.
- Studio is a demo evidence surface that explains and packages the evidence chain.

## 6. Evidence Already Available

| Evidence | Artifact path | Use in Studio package |
| --- | --- | --- |
| July 31 interim result report draft | `docs/reports/july-31-interim-result-report-draft.md` | Main narrative source |
| July 31 evidence table | `docs/reports/july-31-interim-result-report-evidence-table.md` | Evidence mapping source |
| July 31 claim boundary appendix | `docs/reports/july-31-interim-result-report-claim-boundary.md` | Approved wording source |
| July 31 next work plan | `docs/reports/july-31-interim-result-report-next-work-plan.md` | Roadmap source |
| Executive summary | `docs/reports/july-31-interim-result-report-executive-summary.md` | Short reviewer framing |
| Dashboard evidence view | `docs/dashboard/index.html` | Reviewer-facing evidence view |
| Dashboard data | `docs/dashboard/dashboard-data.json` | Static data source |
| Interim package index | `docs/reports/ai-champion-interim-package-index.md` | Package entry point |
| 100K routing comparison | `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md` | Execution-path selectivity evidence |
| H100 routed subset measurement | `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` | Bounded measured GPU evidence |
| Multi-profile robustness | `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` | Robustness evidence |
| 1M scale and saturation benchmark | `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` | Scale and bounded saturation evidence |

## 7. Evidence Still Needed

| Needed evidence | Minimum output | Claim supported |
| --- | --- | --- |
| Studio route screen capture | One or more screenshots showing route decision and path explanation | Studio can show execution-path selectivity as a demo surface |
| Dashboard capture set | Screenshots of core message, KPI cards, evidence table, and claim boundaries | Static dashboard evidence view is capture-ready |
| Short demo recording | Two-minute walkthrough of Studio plus dashboard evidence view | Studio can explain the evidence chain |
| Demo evidence package index | Markdown index linking captures, recording notes, and evidence reports | July 31 review package is organized |
| Public-safe validation record | Diff check, file listing, safety scan, and lightweight validation notes | Evidence package has been locally validated |

## 8. Claim-Safe Language

Use:

- "KORA Studio is a demo evidence surface for explaining execution-path selectivity."
- "KORA connects route decisions to existing benchmark evidence."
- "KORA can show compute-weighted GPU demand reduction in benchmark workloads."
- "KORA has bounded H100 routed subset measurement."
- "KORA has bounded 1M H100 saturation subset evidence."
- "The dashboard evidence view packages committed reports and evidence files for reviewer inspection."
- "Measured, dry-run, and estimated values are kept separate."

Avoid broader language that would imply production deployment, customer workload savings, or official validation.

## 9. Explicit Non-Claims

Studio must not imply:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- Proven 10x savings.
- Full provider/GPU live workload comparison.
- Full 1M all-GPU measured execution.
- Production representativeness.
- Final paper-ready result.
- Formal government validation.
- Signed partner validation.
- Broad workload superiority proof.
- Energy reduction proof.

## 10. July 31 Readiness Definition

KORA Studio launch evidence is July 31 ready when:

- The Studio demo surface is visible in screenshots.
- The demo narrative is claim-safe and rehearsable.
- The static dashboard evidence view is captured.
- Existing benchmark evidence links are included.
- Non-claims are visible in the package.
- The final package can be reviewed from committed files without relying on unstated context.
