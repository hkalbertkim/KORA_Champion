# KORA Early Technical Report v0 Claim Review

## 1. Review Objective

This review tightens the early technical report draft v0 so it remains claim-safe, evidence-traceable, and clear for July 31 review. The review focuses on execution-path selectivity, benchmark evidence, bounded H100 routed subset measurement, and static evidence surfaces.

## 2. Claim Review Summary

The v0 report was tightened in these areas:

- Added a reader interpretation guide.
- Labeled evidence types more explicitly.
- Added interpretation boundaries to result subsections.
- Clarified that dry-run routing evidence is not measured runtime evidence.
- Clarified that dashboard and Studio assets package evidence rather than adding runtime measurements.
- Strengthened limitations and future work.

## 3. Approved Claim Language

Use:

- KORA benchmarks when H100 should be used.
- KORA evaluates execution-path selectivity across deterministic, cache, CPU, provider, GPU, and fallback paths.
- KORA can show compute-weighted GPU demand reduction in benchmark workloads.
- KORA has bounded H100 routed subset measurement.
- KORA has 100K dry-run routing selectivity evidence.
- KORA has 1M dry-run scale stability evidence.
- KORA has bounded 1M H100 saturation subset evidence.
- The dashboard evidence view packages committed benchmark evidence for review.
- KORA Studio is a Studio evidence surface for explaining route decisions when backed by existing evidence artifacts.

## 4. Rejected Claim Patterns

Avoid patterns that:

- Present benchmark demand metrics as deployed outcomes.
- Present dry-run route metrics as measured runtime results.
- Present bounded H100 subset evidence as complete workload measurement.
- Present provider samples as broad live route comparison.
- Present benchmark profiles as broad workload generality.
- Present dashboard or Studio artifacts as new experiments.
- Present the v0 draft as completed publication material.
- Present the evidence package as externally approved.

## 5. Evidence Traceability Notes

Traceability requirements:

- Provider metrics should cite `docs/reports/july-31-interim-result-report-draft.md` and provider evidence artifacts.
- 100K route metrics should cite `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`.
- Bounded H100 routed subset metrics should cite `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md`.
- Multi-profile statements should cite `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md`.
- 1M scale and saturation statements should cite `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md`.
- Dashboard and Studio statements should cite dashboard files, Studio planning reports, and demo package indexes.

## 6. Remaining Weak Areas

Remaining weak areas:

- Figure and table assets beyond Figure 1 and Table 1 are still planned.
- Dashboard and Studio capture artifacts remain pending.
- Sentence-level evidence traceability should be repeated for v0.1.
- Limitations should be reviewed again after final July 31 package decisions.
- Result captions need a future consistency pass once all figures and tables are drafted.

## 7. Required Evidence for Future Claim Upgrades

Future upgrades would require:

- More bounded provider samples if stronger provider path evidence is needed.
- Repeated bounded H100 routed subset measurements if stronger runtime confidence is needed.
- Measured complete baselines if complete-baseline claims are desired.
- Permissioned workload characterization if broader workload generality is desired.
- Reviewed dashboard and Studio captures if visual evidence package claims are desired.

## 8. Recommendation for v0.1

v0.1 should preserve the current claim boundaries, complete a sentence-level evidence traceability pass, align figure/table references, and keep limitations visible near the results.
