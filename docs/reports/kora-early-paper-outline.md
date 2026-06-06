# KORA Early Paper Outline

## 1. Working Title Candidates

- KORA: Benchmarking When H100 Should Be Used Through Execution-Path Selectivity
- Execution-Path Selectivity for AI Workload Routing: An Early KORA Champion Evidence Report
- Measuring Route-Aware GPU Demand in Benchmark Workloads
- KORA Champion: A Benchmark Evidence Chain for Selective AI Execution Paths

## 2. Recommended Title

KORA: Benchmarking When H100 Should Be Used Through Execution-Path Selectivity

## 3. Paper/Report Thesis

KORA evaluates AI workload routing as an execution-path selectivity problem. Instead of measuring H100 as a raw accelerator used for every request, KORA benchmarks whether a request should use deterministic handling, cache, CPU, provider, GPU, or fallback execution. The current evidence package supports compute-weighted GPU demand reduction in benchmark workloads and connects dry-run routing evidence to bounded H100 routed subset measurement.

Core message:

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

## 4. Abstract Outline

The abstract should:

- State the execution-path selectivity problem.
- Describe KORA as a route-aware benchmark and measurement harness.
- Name the six execution paths: deterministic, cache, CPU, provider, GPU, and fallback.
- Summarize the evidence chain: bounded provider evidence, H100 runtime evidence, 100K routing selectivity, bounded H100 routed subset measurement, multi-profile robustness, 1M dry-run scale stability, and bounded saturation evidence.
- Use compute-weighted GPU demand reduction in benchmark workloads as the safe benchmark metric.
- State that the current package is an early technical report outline, not a deployment result.

## 5. Introduction Outline

1. Motivation: AI execution decisions are often framed as accelerator performance questions.
2. Reframing: KORA asks when H100 should be used.
3. Problem: requests differ in whether they require deterministic handling, cache, CPU, provider, GPU, or fallback execution.
4. Contribution: an evidence chain for execution-path selectivity in benchmark workloads.
5. Current status: interim evidence, bounded measurements, and public-safe package preparation.

## 6. Problem Statement

The problem is to evaluate route selection across heterogeneous execution paths without assuming that every request should use GPU execution. A benchmark should measure whether a route decision is acceptable, whether unsafe misroutes are avoided, and how much compute-weighted GPU demand remains after routing benchmark workloads through the KORA policy.

This problem differs from raw accelerator benchmarking because the target is not maximum GPU throughput alone. The target is correct and bounded selection of the execution path.

## 7. System Framing

KORA should be framed as:

- A route-aware benchmark and measurement harness.
- A system that separates deterministic, cache, CPU, provider, GPU, and fallback execution.
- A framework for comparing routing strategies over oracle-labeled benchmark workloads.
- A bridge between dry-run routing evidence and measured H100 routed subset evidence.

KORA Studio should be framed separately as a Studio evidence surface that explains the route decisions and links to the evidence package.

## 8. Methodology Section Plan

The methodology section should cover:

- Workload generation and benchmark profiles.
- Oracle labels and route correctness boundaries.
- Router policies and KORA adapter behavior.
- Path taxonomy: deterministic, cache, CPU, provider, GPU, fallback.
- Metrics: acceptable route rate, unsafe misroute rate, route distribution, compute-weighted GPU demand reduction in benchmark workloads.
- Evidence types: measured, bounded measured, dry-run, dry-run with estimated runtime, static package.
- How H100 routed subset measurement calibrates a subset of the GPU path.

## 9. Benchmark Setup Section Plan

The benchmark setup section should include:

- Provider path boundary and bounded live sample evidence.
- H100 micro benchmark setup and measured runtime metrics.
- 100K routing selectivity benchmark setup.
- Multi-profile routing robustness setup.
- 1M dry-run scale setup.
- Bounded H100 saturation subset setup.
- Public evidence package and dashboard evidence view setup.

Each subsection should identify the artifact path, evidence type, and claim boundary.

## 10. Results Section Plan

The results section should be organized by evidence strength:

1. Provider path readiness.
2. H100 runtime readiness.
3. 100K execution-path selectivity.
4. Bounded H100 routed subset measurement.
5. Multi-profile routing robustness.
6. 1M dry-run scale stability.
7. Bounded 1M H100 saturation subset evidence.
8. Dashboard and Studio evidence packaging.

The results section should keep measured values separate from dry-run metrics and estimated runtime values.

## 11. Discussion Section Plan

The discussion should explain:

- Why execution-path selectivity is a different benchmark target from raw GPU throughput.
- Why non-GPU paths matter in benchmark workloads.
- Why bounded H100 routed subset measurement strengthens the dry-run routing evidence.
- How the dashboard evidence view and Studio evidence surface support reviewer inspection.
- Which claims remain outside the current evidence package.

## 12. Limitations Section Plan

The limitations section should state:

- Provider evidence is bounded.
- H100 execution evidence is measured for bounded benchmark subsets.
- Dry-run routing evidence does not execute every provider or GPU path live.
- Complete million-request GPU-only measurement has not been performed.
- Current benchmark profiles do not establish deployed-workload generality.
- Studio and dashboard artifacts package evidence but do not create new runtime measurements.

## 13. Claim Boundary Section Plan

The claim boundary section should include:

- Supported claims.
- Unsupported claims.
- Definitions of measured, dry-run, estimated, and static package evidence.
- Approved wording for compute-weighted GPU demand reduction in benchmark workloads.
- Approved wording for bounded H100 routed subset measurement.

## 14. Future Work Section Plan

Future work should include:

- Additional bounded provider sampling.
- Repeated H100 routed subset measurements.
- Larger measured GPU-routed subsets if needed.
- Additional benchmark workload profiles.
- Public-safe demo capture execution.
- Paper figures and tables.
- Optional external review only after evidence boundaries are upgraded.

## 15. Appendix Plan

Appendices should include:

- Artifact index.
- Evidence type definitions.
- Claim boundary table.
- Benchmark profile summary.
- Route taxonomy.
- Figure and table source map.
- Dashboard and Studio package references.
