# July 31 Claim Boundary Sheet

## Approved Claim Language

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

## Phrases To Avoid

Avoid language that states or implies:

- Deployed financial outcomes.
- Customer workload outcomes.
- Broad workload generality.
- Complete live comparison across all routes.
- GPU execution measurement for every request in the million-request benchmark.
- External approval status.
- Finished publication readiness.

## Unsafe Inference Patterns

Avoid patterns that:

- Convert benchmark demand metrics into deployed outcomes.
- Treat dry-run route metrics as measured runtime results.
- Treat bounded H100 subset evidence as complete workload measurement.
- Treat provider samples as broad live route comparison.
- Treat benchmark profiles as broad workload generality.
- Treat dashboard or Studio artifacts as new experiments.

## Benchmark-Vs-Production Wording Rules

Use "benchmark workloads" when discussing route distribution, demand reduction, and profile behavior.

Use "bounded measured evidence" when discussing provider samples or H100 subset execution.

Use "static package" or "evidence surface" when discussing dashboard and Studio assets.

## GPU Demand Vs Cost Wording Rules

Use:

- Compute-weighted GPU demand reduction in benchmark workloads.
- Benchmark demand metric.
- Route-aware benchmark demand.

Avoid cost or realized savings wording unless future evidence separately supports it.

## H100 Measurement Wording Rules

Use:

- Bounded H100 routed subset measurement.
- Measured H100 runtime evidence.
- Bounded 1M H100 saturation subset evidence.

Do not describe bounded subset evidence as complete workload measurement.

## Provider Evidence Wording Rules

Use:

- Bounded live provider evidence.
- Provider path readiness in a bounded sample.

Do not describe provider samples as broad live route comparison.

## Studio/Dashboard Wording Rules

Use:

- Static dashboard evidence view.
- Studio evidence surface.
- Demo evidence package.
- Evidence packaging for review.

Do not describe dashboard or Studio assets as new runtime experiments.

## Claim Upgrade Requirements

Future claim upgrades require additional evidence:

| Upgrade area | Required evidence |
| --- | --- |
| Stronger provider path evidence | Additional bounded provider samples with documented scale and metrics |
| Stronger H100 runtime confidence | Repeated bounded H100 routed subset measurements |
| Complete baseline measurement | Measured complete baseline under the same benchmark protocol |
| Broader workload generality | Permissioned workload characterization and benchmark-to-workload mapping |
| Visual evidence package | Reviewed dashboard and Studio capture artifacts |
| Later report readiness | Sentence-level traceability review, figure/table caption review, and final limitation review |
