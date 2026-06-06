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

## July 31 Readiness Checklist

- [ ] Core message appears in English.
- [ ] Core message appears in Korean.
- [ ] Evidence summary is readable without external context.
- [ ] Dashboard and Studio evidence surfaces are described as package assets.
- [ ] Limitations are explicit.
- [ ] Future work is claim-bounded.

## Publication Readiness Checklist

- [ ] Draft status remains visible.
- [ ] Claims have been reviewed by evidence owner.
- [ ] Figures and tables have been reviewed.
- [ ] Artifact index has been checked.
- [ ] Limitations section has been tightened.
- [ ] No external submission packaging is implied.

## Items To Review Before External Sharing

- [ ] Abstract wording.
- [ ] Results section metric labels.
- [ ] Claim boundary section.
- [ ] Limitations section.
- [ ] Figure captions.
- [ ] Table captions.
- [ ] Artifact index.
- [ ] Dashboard and Studio wording.
