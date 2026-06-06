# KORA Technical Report v0.1 Review Checklist

## Evidence Traceability Checklist

- [ ] Every numeric result has a nearby source path.
- [ ] Every supported claim maps to one or more evidence artifacts.
- [ ] Every limitation maps to a known evidence boundary.
- [ ] Dashboard and Studio statements are identified as static or planned package assets.
- [ ] Figure and table references point to `docs/paper-assets/`.
- [ ] Appendix A includes primary evidence artifacts.

## Claim Boundary Checklist

- [ ] The report states that KORA benchmarks when H100 should be used.
- [ ] The report uses execution-path selectivity consistently.
- [ ] The report uses compute-weighted GPU demand reduction in benchmark workloads.
- [ ] The report uses bounded H100 routed subset measurement.
- [ ] The report includes "What This Report Does Not Claim."
- [ ] The report does not add new technical claims beyond existing evidence.

## Benchmark-Vs-Production Checklist

- [ ] Route metrics are framed as benchmark workload results.
- [ ] 100K and 1M routing results are labeled as dry-run evidence.
- [ ] H100 subset results are labeled as bounded measured evidence.
- [ ] Dashboard and Studio artifacts are described as evidence surfaces.
- [ ] Future claim upgrades are separated from current claims.

## Metric Interpretation Checklist

- [ ] Provider sample metrics are bounded.
- [ ] H100 micro benchmark metrics are runtime evidence, not route selectivity evidence by themselves.
- [ ] 100K route metrics are dry-run routing evidence.
- [ ] H100 routed subset metrics are bounded measured subset evidence.
- [ ] 1M route metrics separate dry-run scale from measured saturation subset.
- [ ] Estimated baseline language is not treated as measured unless separately measured.

## Figure/Table Consistency Checklist

- [ ] Figure 1 matches the six-path taxonomy.
- [ ] Table 1 evidence categories match the report.
- [ ] Planned figures are marked as planned.
- [ ] Planned tables are marked as planned.
- [ ] Figure captions retain claim boundary notes.
- [ ] Table captions retain claim boundary notes.

## July 31 Readiness Checklist

- [ ] Core message appears in English.
- [ ] Core message appears in Korean.
- [ ] Reader interpretation guide is visible.
- [ ] Evidence chain is readable without external context.
- [ ] Claim boundaries are easy to find.
- [ ] Missing capture and figure/table work is visible.

## External Sharing Checklist

- [ ] Draft status note remains at the top.
- [ ] Public-safety scan has passed.
- [ ] All paths are relative repository paths.
- [ ] No private or environment-specific details appear.
- [ ] Claim review has been incorporated.
- [ ] Remaining gaps are documented.

## Publication Readiness Checklist

- [ ] Report is still labeled as an early technical report.
- [ ] No submission packaging is implied.
- [ ] No external approval status is implied.
- [ ] Figure/table caption review is complete.
- [ ] Sentence-level evidence traceability review is complete.
- [ ] Limitation review is complete.

## Required Reviewer Signoff Items

- [ ] Evidence owner confirms metric-source mapping.
- [ ] Claim reviewer confirms wording boundaries.
- [ ] Figure/table reviewer confirms caption boundaries.
- [ ] Public-safety reviewer confirms no private details.
- [ ] July 31 package owner confirms packet linkage.
