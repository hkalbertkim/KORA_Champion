# July 31 Reviewer Q&A Notes

## What exactly does KORA prove today?

KORA has benchmark evidence for execution-path selectivity. It shows that benchmark requests can be routed across deterministic, cache, CPU, provider, GPU, and fallback paths, and it connects dry-run routing evidence to bounded H100 routed subset measurement.

## What does KORA not prove yet?

KORA does not yet prove production outcomes, customer workload outcomes, broad workload generality, complete live comparison across all routes, GPU execution measurement for every request in the million-request benchmark, external approval status, or final publication readiness.

## What is execution-path selectivity?

Execution-path selectivity is the task of selecting the appropriate execution path for a request instead of treating GPU execution as the default. In KORA, the paths are deterministic, cache, CPU, provider, GPU, and fallback.

## Why is H100 evidence bounded?

The current measured H100 evidence is tied to specific benchmark settings and routed subsets. Bounded H100 routed subset measurement is useful because it connects GPU-routed benchmark requests to measured H100 execution, but it does not measure every request in the source benchmark under GPU execution.

## Is this production cost reduction?

No. The safe metric is compute-weighted GPU demand reduction in benchmark workloads. It is a benchmark demand metric, not a production or customer workload outcome.

## Why is all-GPU full measurement not claimed?

The current evidence includes measured H100 runtime evidence, bounded H100 routed subset measurement, and bounded saturation subset evidence. It does not include measured GPU execution for every request in the million-request benchmark under the same comparison protocol.

## What does compute-weighted GPU demand reduction mean?

It is a benchmark metric that estimates how much GPU demand remains after KORA routes benchmark requests across available execution paths. It should be interpreted only within the benchmark workload context.

## How should the dashboard be interpreted?

The dashboard is a static dashboard evidence view. It packages existing reports, evidence metrics, and claim boundaries for inspection. It does not create new runtime evidence.

## How should KORA Studio be interpreted?

KORA Studio should be interpreted as a Studio evidence surface for explaining route decisions and linking them to existing evidence. It is not measured workload evidence by itself.

## What evidence is needed next?

Next evidence needs include reviewed dashboard screenshots, reviewed Studio screenshots, a demo recording summary or documented deferral, remaining figure/table drafts, and sentence-level evidence traceability review.

## What is ready for July 31?

The evidence package, technical report v0.1, packet index, reviewer guide, evidence traceability map, claim boundary sheet, readiness report, dashboard evidence view, and Studio demo package plan are ready for internal review.

## What remains missing?

Final dashboard captures, final Studio captures, demo recording summary, remaining figure/table drafts, packet issue resolution, and external sharing signoff remain missing.
