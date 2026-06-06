# KORA Paper Figure Specs

## Figure 1: KORA Execution-Path Selectivity Overview

Status: draft.

Purpose: show KORA as a routing and control layer that selects among deterministic, cache, CPU, provider, GPU, and fallback execution paths.

Proposed visual structure:

- Request enters KORA routing/control.
- KORA evaluates route features and policy.
- Six execution paths branch from the routing layer.
- Output and evidence logging converge after execution.

Source evidence files:

- `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md`
- `docs/reports/kora-studio-launch-evidence-plan.md`
- `docs/reports/kora-early-paper-outline.md`

Draft caption:

"KORA frames AI workload execution as execution-path selectivity. A request is routed to deterministic, cache, CPU, provider, GPU, or fallback execution, and the route decision is logged for benchmark evidence review."

Claim-safe interpretation: KORA evaluates when H100 should be used as one route among several benchmark execution paths.

Explicit non-claims: this figure is conceptual and does not present a new runtime measurement or deployed outcome.

## Figure 2: Routing Benchmark Evidence Chain

Status: planned.

Purpose: show the benchmark progression from framework design to route selectivity, measured routed subset execution, robustness, scale, and evidence packaging.

Proposed visual structure:

- GPU-004A routing framework.
- GPU-004B 100K routing selectivity.
- GPU-004C bounded H100 routed subset measurement.
- GPU-005 multi-profile robustness.
- GPU-006 1M dry-run scale and bounded saturation evidence.
- Dashboard and Studio evidence packaging.

Source evidence files:

- `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md`
- `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`
- `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md`
- `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md`
- `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md`
- `docs/reports/ai-champion-dashboard-evidence-view-report.md`

Draft caption:

"KORA Champion evidence chain from routing benchmark framework to 100K execution-path selectivity, bounded H100 routed subset measurement, multi-profile robustness, 1M dry-run scale stability, bounded saturation evidence, and reviewer-facing evidence packaging."

Claim-safe interpretation: the chain organizes existing measured, dry-run, estimated, and static package evidence.

Explicit non-claims: the chain is not a complete live comparison of every execution path and does not upgrade benchmark evidence into deployed-workload evidence.

## Figure 3: Compute-Weighted GPU Demand Reduction Framing

Status: planned.

Purpose: explain how compute-weighted GPU demand reduction in benchmark workloads should be interpreted without implying deployed savings.

Proposed visual structure:

- Baseline benchmark demand.
- KORA route selection.
- GPU-routed subset remains.
- Non-GPU routed work is separated into deterministic, cache, CPU, provider, and fallback paths.
- Metric label: compute-weighted GPU demand reduction in benchmark workloads.

Source evidence files:

- `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`
- `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md`
- `docs/reports/july-31-interim-result-report-claim-boundary.md`

Draft caption:

"Compute-weighted GPU demand reduction in benchmark workloads measures how route selection changes benchmark GPU demand after separating non-GPU execution paths."

Claim-safe interpretation: this is a benchmark demand metric derived from route distribution and compute weights.

Explicit non-claims: this figure must not be read as deployed cost, customer workload, or infrastructure outcome evidence.

## Figure 4: Dashboard and Studio Evidence Surface

Status: planned.

Purpose: show how the static dashboard evidence view and Studio evidence surface communicate the benchmark evidence chain.

Proposed visual structure:

- Studio explains route decision.
- Dashboard summarizes evidence metrics and links.
- Reports and evidence files form the backing artifact layer.
- Claim boundaries remain visible.

Source evidence files:

- `docs/dashboard/index.html`
- `docs/dashboard/dashboard-data.json`
- `docs/reports/kora-studio-launch-evidence-plan.md`
- `docs/demo-capture/july31-package-index.md`
- `docs/reports/kora-studio-july31-package-assembly-report.md`

Draft caption:

"KORA Studio explains route decisions while the dashboard evidence view links the explanation to committed benchmark reports and evidence artifacts."

Claim-safe interpretation: Studio and dashboard assets package existing evidence for reviewer inspection.

Explicit non-claims: these surfaces are not new benchmark runs and do not prove deployed behavior.
