# July 31 Interim Result Report Claim Boundary Appendix

This appendix defines claim-safe wording for the July 31 interim result report draft.

## 1. Safe Claim List

- KORA has bounded live provider evidence.
- KORA has measured H100 runtime evidence.
- KORA has routing framework evidence.
- KORA has 100K routing selectivity evidence.
- KORA has measured H100 routed subset evidence.
- KORA has multi-profile routing robustness evidence.
- KORA has 1M dry-run scale stability evidence.
- KORA has bounded 1M H100 saturation subset evidence.
- KORA has a static dashboard evidence view.
- KORA can show compute-weighted GPU demand reduction in benchmark workloads.
- KORA can estimate routed GPU runtime from measured H100 calibration.

## 2. Unsafe Claim List

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- Proven 10x savings.
- Full provider/GPU live workload comparison.
- Full 1M all-GPU measured execution.
- Production representativeness.
- Final paper-ready result.
- Full KORA Studio launch evidence.
- Real pilot workload results unless separately collected and documented.

## 3. Measured vs Dry-Run vs Estimated Definitions

Measured evidence:

- A bounded provider call, GPU micro workload, routed H100 subset, or saturation subset was actually executed and recorded.
- Examples: provider live sample, GPU micro benchmark, GPU-004C routed subset, GPU-006 saturation subset.

Dry-run benchmark evidence:

- Router behavior and benchmark metrics were computed without live provider calls or H100 execution.
- Examples: GPU-004B 100K routing comparison, GPU-005 multi-profile robustness, GPU-006 1M scale routing summary.

Estimated runtime evidence:

- Runtime values are computed from benchmark compute weight and measured H100 throughput calibration.
- Examples: GPU-004C estimated all_gpu runtime, GPU-006 estimated all_gpu runtime, estimated KORA GPU-routed runtime, estimated avoided GPU runtime.

Planned/future evidence:

- Evidence that has not yet been collected but is included in the roadmap.
- Examples: KORA Studio launch evidence, recorded demo video, broader provider sample, paper/arXiv draft.

## 4. Reviewer-Facing Caveats

- Provider evidence is partial-live and bounded.
- Dry-run routing benchmarks do not execute live provider or H100 workloads.
- H100 routed subset evidence is measured, but bounded to selected benchmark subsets.
- The 1M benchmark includes dry-run scale evidence and a measured 50K saturation subset, not full 1M all-GPU execution.
- Runtime comparisons that use all_gpu baselines are estimates unless explicitly measured.
- Benchmark workloads do not prove production representativeness.

## 5. Suggested Wording

Use:

- "benchmark evidence"
- "measured routed subset evidence"
- "bounded H100 saturation subset"
- "estimated runtime based on measured H100 calibration"
- "directional compute-weighted GPU demand reduction"
- "execution-path selectivity evidence"
- "dry-run routing benchmark"
- "provider path readiness"
- "public evidence package"

Example:

"KORA demonstrates execution-path selectivity in benchmark workloads and connects GPU-routed subsets to measured H100 execution."

Example:

"The 1M benchmark shows dry-run route stability and estimated runtime based on measured H100 calibration; it is not a full 1M all-GPU execution."

## 6. Wording To Avoid

Avoid:

- "production savings proven"
- "real customer savings"
- "10x proven"
- "production infrastructure reduction"
- "full provider/GPU live comparison"
- "final paper result"
- "production representative benchmark"
- "full 1M measured all-GPU result"

Replacement examples:

| Avoid | Use instead |
| --- | --- |
| production savings proven | benchmark compute-weighted GPU demand reduction |
| real customer savings | benchmark workload evidence |
| 10x proven | directional improvement target for future validation |
| production infrastructure reduction | estimated avoided runtime in benchmark setting |
| final paper result | interim evidence package |
| production representative | benchmark profile coverage |
