# KORA Early Paper Limitations and Next Work

## 1. Current Limitations

The current KORA Champion evidence package is strong enough for an early technical report outline, but it remains bounded benchmark evidence.

Current limitations:

- Provider evidence is bounded and limited in scale.
- H100 runtime evidence exists for bounded benchmark settings.
- Bounded H100 routed subset measurement does not cover every request in the benchmark as a measured GPU execution.
- 100K and 1M routing results are dry-run routing benchmarks.
- Runtime estimates depend on measured H100 calibration and benchmark compute weight.
- Multi-profile benchmark coverage does not establish deployed-workload generality.
- Dashboard and Studio artifacts package evidence for review but do not create new runtime measurements.
- Actual Studio and dashboard capture artifacts are still pending.

## 2. Why Deployment Savings Are Not Yet Claimed

The current evidence package measures benchmark behavior, not deployed infrastructure behavior. It can support compute-weighted GPU demand reduction in benchmark workloads because the benchmark route distribution and compute weights are recorded. It cannot yet support claims about realized savings in a deployed setting because those would require measured workload traces, deployment context, billing or resource allocation data, and a documented comparison protocol.

## 3. Why Complete GPU-Only Measurement Is Not Yet Claimed

The current package includes measured H100 runtime evidence, bounded H100 routed subset measurement, and bounded saturation subset evidence. It does not include measured GPU execution for every request in the complete million-request benchmark. Runtime values that compare against a complete GPU-only baseline should remain labeled as estimates unless that baseline is actually measured.

## 4. Why Deployed-Workload Generality Remains Unproven

The benchmark profiles are useful for testing execution-path selectivity under different workload distributions. They do not prove that the same route distribution or demand reduction would occur in a deployed workload. Upgrading this claim would require documented workload sampling, permissioned trace characterization, profile matching, and repeated measurements with the same claim boundaries.

## 5. Evidence Needed To Upgrade Claims

| Claim upgrade area | Evidence needed |
| --- | --- |
| Broader provider path evidence | Additional bounded provider samples with clear scale, success, latency, and path metrics |
| Stronger H100 measurement confidence | Repeated bounded H100 routed subset measurements and larger routed subsets if needed |
| Complete GPU-only baseline | Measured GPU execution for the full comparison workload under the same benchmark protocol |
| Deployed-workload generality | Permissioned workload characterization, benchmark-to-workload mapping, and repeated route measurement |
| Demo evidence readiness | Public-safe Studio and dashboard screenshots, recording summaries, and capture review notes |
| Report readiness | Figure drafts, table drafts, limitations, and artifact appendix |

## 6. Recommended Next Work

Immediate next work should focus on paper figures and tables because the evidence chain is already organized and the capture package structure is prepared.

Recommended work:

- Draft Figure 1: execution-path selectivity overview.
- Draft Figure 3: evidence chain.
- Draft Table 1: benchmark evidence summary.
- Draft Table 2: claim boundary table.
- Draft Table 3: workload/profile comparison.
- Draft appendix artifact index.

This work is higher leverage than running new measurements because the early report still needs clear visual structure before any claim upgrade is considered.

## 7. Recommended Goal 014

Goal 014

Title: Paper Figure and Table Draft Package

Rationale: Goal 013 creates the early technical report outline and maps evidence to possible sections. The next useful step is to draft the figures and tables that will make execution-path selectivity, evidence types, and claim boundaries clear for July 31 and later report work.
