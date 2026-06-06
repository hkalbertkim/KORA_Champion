# KORA Early Paper Abstract Draft

## 1. Conservative Technical Report Version

KORA Champion evaluates AI workload routing as an execution-path selectivity problem. Rather than benchmarking H100 as a raw accelerator for every request, KORA benchmarks when H100 should be used. The current evidence package routes benchmark workloads across deterministic, cache, CPU, provider, GPU, and fallback paths, then reports route correctness, path distribution, and compute-weighted GPU demand reduction in benchmark workloads. The package includes bounded live provider evidence, measured H100 runtime evidence, 100K routing selectivity evidence, bounded H100 routed subset measurement, multi-profile routing robustness evidence, 1M dry-run scale stability evidence, and bounded 1M H100 saturation subset evidence. The current results support an interim benchmark evidence claim for execution-path selectivity. They do not establish deployed-workload savings, complete live path comparison, or broad workload generality.

## 2. Research-Paper Style Version

Accelerator benchmarks often focus on raw throughput, but many AI workloads contain requests that should be handled by deterministic logic, cache, CPU, provider execution, GPU execution, or fallback. KORA reframes the benchmark target as execution-path selectivity: deciding when H100 should be used rather than assuming H100 should handle every request. We outline a route-aware benchmark framework with oracle-labeled workloads, route correctness metrics, compute-weighted demand metrics, dry-run scale tests, and bounded H100 routed subset measurement. Initial evidence includes 100K routing selectivity, multi-profile robustness, 1M dry-run scale stability, and bounded measured H100 execution for routed subsets. The early evidence supports benchmark workload analysis of compute-weighted GPU demand reduction while preserving clear boundaries between measured, dry-run, estimated, and static package evidence.

## 3. July 31 Interim Report Version

KORA Champion has an interim evidence package showing execution-path selectivity across deterministic, cache, CPU, provider, GPU, and fallback paths. KORA is not benchmarking H100 as a raw accelerator; it benchmarks when H100 should be used. The current package includes routing framework evidence, bounded live provider evidence, measured H100 runtime evidence, 100K routing selectivity evidence, bounded H100 routed subset measurement, multi-profile routing robustness, 1M dry-run scale stability, bounded 1M H100 saturation subset evidence, a static dashboard evidence view, and a KORA Studio demo evidence plan. The safe July 31 claim is compute-weighted GPU demand reduction in benchmark workloads. The package is an interim technical evidence report and should not be read as deployment proof or complete live workload validation.

## 4. Safest Abstract for July 31

The conservative technical report version is safest for July 31 because it explicitly frames the work as an interim benchmark evidence package, separates supported evidence from non-claims, and avoids language that could be read as deployment validation.
