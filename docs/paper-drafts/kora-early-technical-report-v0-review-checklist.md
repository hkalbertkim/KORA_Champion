# KORA Early Technical Report v0 Review Checklist

## Technical Accuracy Checklist

- [ ] Every metric is traceable to a source report or evidence file.
- [ ] Measured evidence is labeled separately from dry-run evidence.
- [ ] Estimated runtime language is clearly marked where used.
- [ ] Bounded H100 routed subset measurement is not described as complete workload measurement.
- [ ] The route taxonomy matches deterministic, cache, CPU, provider, GPU, and fallback paths.
- [ ] The report uses execution-path selectivity consistently.

## Evidence Traceability Checklist

- [ ] Provider evidence links to committed provider artifacts.
- [ ] H100 runtime evidence links to committed GPU artifacts.
- [ ] 100K routing evidence links to committed routing benchmark artifacts.
- [ ] Multi-profile robustness links to committed summary artifacts.
- [ ] 1M scale and saturation evidence links to committed scale and saturation artifacts.
- [ ] Dashboard evidence links to dashboard files and reports.
- [ ] Studio evidence links to Studio planning and capture package files.
- [ ] Paper figure and table references link to `docs/paper-assets/`.

## Claim Boundary Checklist

- [ ] The draft states that KORA benchmarks when H100 should be used.
- [ ] The draft uses compute-weighted GPU demand reduction in benchmark workloads.
- [ ] The draft uses bounded H100 routed subset measurement.
- [ ] The draft does not claim deployed savings.
- [ ] The draft does not claim customer workload outcomes.
- [ ] The draft does not claim broad workload generality.
- [ ] The draft does not claim complete live comparison across all paths.
- [ ] The draft does not claim complete million-request GPU-only measurement.
- [ ] The draft does not claim external approval status.
- [ ] The draft does not claim finished publication readiness.

## Unsupported Claim Detection Checklist

- [ ] No sentence describes benchmark demand reduction as a deployed outcome.
- [ ] No sentence treats dry-run routing evidence as measured runtime evidence.
- [ ] No sentence treats dashboard or Studio assets as new experiments.
- [ ] No sentence describes bounded provider evidence as broad live route comparison.
- [ ] No sentence describes benchmark profiles as deployed-workload generality.
- [ ] No sentence treats estimated runtime values as directly measured baselines.

## Evidence-To-Sentence Traceability Checklist

- [ ] Every numeric result has a source path nearby.
- [ ] Every supported claim maps to one or more artifact paths.
- [ ] Every limitation maps to a known evidence boundary.
- [ ] Every dashboard or Studio statement identifies whether it is a static package or planned package asset.
- [ ] Every figure/table reference points to `docs/paper-assets/`.

## Benchmark-Vs-Deployed Language Checklist

- [ ] Benchmark workload language is used for route metrics.
- [ ] Dry-run language is used for 100K and 1M route metrics.
- [ ] Bounded measured language is used for provider and H100 subset evidence.
- [ ] Static package language is used for dashboard and Studio assets.
- [ ] Deployed-outcome wording is avoided unless stated as future evidence needed.

## Public/Private Safety Checklist

- [ ] All paths are relative repository paths.
- [ ] No local absolute paths appear.
- [ ] No account material appears.
- [ ] No secret material appears.
- [ ] No environment-specific host details appear.
- [ ] No raw service dumps appear.
- [ ] No unreviewed screenshots or media are referenced as existing.

## Figure/Table Readiness Checklist

- [ ] Figure 1 is referenced as a draft asset.
- [ ] Table 1 is referenced as a draft asset.
- [ ] Planned figures are marked as planned, not complete.
- [ ] Planned tables are marked as planned, not complete.
- [ ] Every figure/table caption includes or implies a claim boundary.
- [ ] Figure and table source files are relative paths.

## Figure/Table Consistency Checklist

- [ ] Figure 1 matches the six-path taxonomy in the report.
- [ ] Table 1 uses the same evidence categories as the report.
- [ ] Planned figures are not described as completed assets.
- [ ] Planned tables are not described as completed assets.
- [ ] Captions avoid broad deployment or approval language.

## July 31 Readiness Checklist

- [ ] Core message appears in English.
- [ ] Core message appears in Korean.
- [ ] Evidence summary is readable without external context.
- [ ] Dashboard and Studio evidence surfaces are described as package assets.
- [ ] Limitations are explicit.
- [ ] Future work is claim-bounded.

## July 31 Reviewer Readiness Checklist

- [ ] Reader interpretation guide is present.
- [ ] Claim boundaries are easy to find.
- [ ] Results sections state both support and interpretation boundary.
- [ ] Artifact index includes primary evidence files.
- [ ] Missing capture and figure/table work is not hidden.

## Publication Readiness Checklist

- [ ] Draft status remains visible.
- [ ] Claims have been reviewed by evidence owner.
- [ ] Figures and tables have been reviewed.
- [ ] Artifact index has been checked.
- [ ] Limitations section has been tightened.
- [ ] No external submission packaging is implied.

## External Sharing Readiness Checklist

- [ ] Draft status note remains at the top.
- [ ] Claim review report has been completed.
- [ ] Evidence traceability review has been completed.
- [ ] Public-safety scan has passed.
- [ ] Figure and table captions have been checked.
- [ ] Remaining gaps are documented.

## Items To Review Before External Sharing

- [ ] Abstract wording.
- [ ] Results section metric labels.
- [ ] Claim boundary section.
- [ ] Limitations section.
- [ ] Figure captions.
- [ ] Table captions.
- [ ] Artifact index.
- [ ] Dashboard and Studio wording.
