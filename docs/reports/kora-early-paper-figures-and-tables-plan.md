# KORA Early Paper Figures and Tables Plan

## 1. Purpose

This plan defines figure and table candidates for an early KORA technical report. The assets should explain execution-path selectivity, the evidence chain, and claim boundaries without implying unsupported production or validation claims.

## 2. Figure Plan

| Asset | Purpose | Source evidence | Expected caption | Claim boundary note | Status |
| --- | --- | --- | --- | --- | --- |
| Figure 1: System overview / execution-path selectivity | Show KORA as a route-aware benchmark system | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md`; `docs/reports/kora-studio-launch-evidence-plan.md` | "KORA frames AI workload routing as execution-path selectivity across deterministic, cache, CPU, provider, GPU, and fallback paths." | This figure explains the system frame; it is not runtime evidence | Must be created later |
| Figure 2: Routing paths | Show the six execution paths and their roles | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md`; `docs/reports/kora-studio-demo-narration-script.md` | "Benchmark route taxonomy used to evaluate when H100 should be used." | Do not imply every path was live-executed at full scale | Must be created later |
| Figure 3: Evidence chain | Show GPU-004A through GPU-006 plus July 31 packaging | `docs/reports/ai-champion-interim-package-index.md`; `docs/reports/july-31-interim-result-report-evidence-table.md` | "KORA evidence chain from routing framework to bounded H100 routed subset measurement and 1M scale evidence." | Keep measured, dry-run, estimated, and static package evidence visually distinct | Must be created later |
| Figure 4: Dashboard / Studio evidence surface | Show how Studio and dashboard package the evidence for review | `docs/dashboard/index.html`; `docs/demo-capture/july31-package-index.md`; `docs/reports/kora-studio-july31-package-assembly-report.md` | "Studio explains the route decision; the dashboard evidence view links to committed benchmark artifacts." | Dashboard and Studio package evidence; they do not create new runtime results | Must be created later |

## 3. Table Plan

| Asset | Purpose | Source evidence | Expected caption | Claim boundary note | Status |
| --- | --- | --- | --- | --- | --- |
| Table 1: Benchmark evidence summary | Summarize provider, GPU, routing, routed subset, robustness, scale, and saturation evidence | `docs/reports/july-31-interim-result-report-evidence-table.md` | "Summary of KORA Champion evidence artifacts and supported benchmark claims." | Each row must include evidence type and non-claim boundary | Source exists; table draft needed |
| Table 2: Claim boundary table | Separate supported claims from unsupported claims | `docs/reports/july-31-interim-result-report-claim-boundary.md` | "Claim boundaries for the early KORA technical report." | Avoid phrasing that upgrades interim evidence into deployment claims | Source exists; table draft needed |
| Table 3: Workload/profile comparison | Compare mixed, GPU-heavy, cache-heavy, adversarial, and service replay benchmark profiles | `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md`; `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json` | "Execution-path selectivity across benchmark profile distributions." | Do not describe profiles as deployed-workload representative | Source exists; table draft needed |
| Appendix table: Artifact index | Provide relative paths for reports, JSON files, dashboard, Studio, and capture package artifacts | `docs/reports/ai-champion-interim-package-index.md`; `docs/demo-capture/evidence-map.md` | "Public evidence artifact index for the early technical report." | Artifact presence does not imply new measurements | Source exists; table draft needed |

## 4. Visual Asset Requirements

Future figure drafts should:

- Use execution-path selectivity as the central frame.
- Show GPU as one route, not the default route.
- Separate measured, dry-run, estimated, and static package evidence.
- Use relative repository paths in figure source notes.
- Avoid deployment, savings, or validation language.
- Include claim boundary notes in captions where needed.

## 5. Priority Order

1. Figure 1: System overview / execution-path selectivity.
2. Table 1: Benchmark evidence summary.
3. Figure 3: Evidence chain.
4. Table 2: Claim boundary table.
5. Figure 2: Routing paths.
6. Table 3: Workload/profile comparison.
7. Figure 4: Dashboard / Studio evidence surface.
8. Appendix table: Artifact index.
