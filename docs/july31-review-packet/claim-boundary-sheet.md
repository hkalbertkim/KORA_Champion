# July 31 Claim Boundary Sheet

This is the controlling packet-level claim sheet for the July 31 review packet. If another packet document is less specific, use this sheet to resolve wording.

## Approved One-Liners

Use:

- KORA benchmarks when H100 should be used.
- KORA is an execution-path selectivity system for benchmark workloads.
- KORA evaluates routing across deterministic, cache, CPU, provider, GPU, and fallback paths.
- KORA can show compute-weighted GPU demand reduction in benchmark workloads.
- KORA has bounded H100 routed subset measurement.
- KORA has 100K dry-run routing selectivity evidence.
- KORA has 1M dry-run scale stability evidence.
- KORA has bounded 1M H100 saturation subset evidence.
- The dashboard evidence view packages committed benchmark evidence for review.
- KORA Studio is a Studio evidence surface for explaining route decisions when backed by existing evidence artifacts.
- The July 31 packet is ready for internal review, with broader sharing gated by remaining review and capture requirements.

## Phrases To Avoid

Avoid language that states or implies:

- Deployed financial outcomes.
- Customer workload outcomes.
- Broad workload generality.
- Complete live comparison across all routes.
- GPU execution measurement for every request in the million-request benchmark.
- External approval status.
- Finished publication readiness.
- Completed capture artifacts before screenshots or recordings are committed and reviewed.

## Unsafe Inference Patterns

Avoid patterns that:

- Convert benchmark demand metrics into deployed outcomes.
- Treat dry-run route metrics as measured runtime results.
- Treat bounded H100 routed subset evidence as complete workload measurement.
- Treat provider samples as broad live route comparison.
- Treat benchmark profiles as broad workload generality.
- Treat dashboard or Studio artifacts as new experiments.
- Treat internal review readiness as broader sharing readiness.

## Benchmark-Vs-Production Wording Rules

Use "benchmark workloads" when discussing route distribution, demand reduction, and profile behavior.

Use "bounded measured evidence" when discussing provider samples or H100 subset execution.

Use "static package," "planned capture package," or "evidence surface" when discussing dashboard and Studio assets.

Do not use wording that turns benchmark behavior into deployed behavior.

## GPU Demand Wording Rules

Use:

- Compute-weighted GPU demand reduction in benchmark workloads.
- Benchmark demand metric.
- Route-aware benchmark demand.

Do not use realized outcome wording unless future evidence separately supports it.

## H100 Measurement Wording Rules

Use:

- Bounded H100 routed subset measurement.
- Measured H100 runtime evidence.
- Bounded 1M H100 saturation subset evidence.

Do not describe bounded subset evidence as complete workload measurement.

Do not describe H100 as the benchmark target by itself. The framing is when H100 should be used, not raw accelerator comparison.

## Provider Evidence Wording Rules

Use:

- Bounded live provider evidence.
- Provider path readiness in a bounded sample.

Do not describe provider samples as broad live route comparison.

## Dashboard And Studio Wording Rules

Use:

- Static dashboard evidence view.
- Studio evidence surface.
- Demo evidence package.
- Evidence packaging for review.
- Public-safe capture artifacts remain pending until committed and reviewed.

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
| Broader sharing readiness | Sentence-level traceability review, figure/table caption review, missing capture disposition, public-safety review, and reviewer signoff |
