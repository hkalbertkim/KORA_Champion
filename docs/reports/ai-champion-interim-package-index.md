# AI Champion Interim Package Index

KORA Champion has an interim evidence package showing provider path readiness, H100 runtime readiness, routing benchmark infrastructure, 100K execution-path selectivity evidence, measured H100 routed subset execution, multi-profile robustness, 1M dry-run scale stability, and bounded H100 saturation subset measurement. The strongest current claim is benchmark execution-path selectivity connected to bounded measured H100 routed subset execution. The package is not production savings evidence.

## Package Documents

| Document | Purpose |
| --- | --- |
| `docs/reports/ai-champion-interim-evidence-inventory.md` | Evidence inventory and claim boundary matrix |
| `docs/evidence/ai-champion-interim-evidence-index.json` | Machine-readable interim evidence index |
| `docs/reports/ai-champion-interim-evidence-package-report.md` | July 31 interim report basis |
| `docs/reports/ai-champion-github-evidence-table.md` | Public-facing GitHub evidence table |
| `docs/reports/ai-champion-demo-readiness-plan.md` | Demo video and dashboard readiness plan |

## Supporting Benchmark Reports

| Report | Purpose |
| --- | --- |
| `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md` | 100K source benchmark routed H100 subset measurement |
| `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md` | Multi-profile routing robustness |
| `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md` | 1M scale and H100 saturation subset evidence |

## Key Evidence JSON Files

| Evidence | Path |
| --- | --- |
| Provider live sample | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` |
| Provider normalized comparison | `docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json` |
| GPU micro benchmark | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` |
| 100K routing comparison | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` |
| 100K H100 routed subset | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` |
| Multi-profile aggregate | `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness.json` |
| 1M scale summary | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` |
| 1M H100 saturation subset | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` |

## Strongest Current Claim

KORA can benchmark execution-path selectivity across deterministic, cache, CPU, provider, GPU, and fallback paths; preserve acceptable route correctness in dry-run benchmarks; and measure bounded H100 execution for routed GPU subsets.

## Current Weakest Gaps

- Provider evidence is still partial-live sample evidence, not broad live-provider benchmarking.
- KORA Studio launch evidence is not yet included in this package.
- Demo video and dashboard evidence are planned but not recorded here.
- The 1M benchmark includes dry-run scale evidence and a bounded H100 subset, not full 1M all-GPU measured execution.
- The package is not final paper-ready.

## Claim Boundary Reminder

Allowed:

- Provider path readiness.
- H100 runtime readiness.
- Routing benchmark framework readiness.
- 100K execution-path selectivity evidence.
- Measured H100 routed subset execution.
- Multi-profile routing robustness.
- 1M scale routing stability.
- Bounded H100 saturation subset measurement.
- Estimated runtime from measured H100 calibration.

Prohibited:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- 10x cost savings as proven.
- Full provider/GPU live workload comparison.
- Full 1M all-GPU measured execution.
- Production representativeness.
- Final paper-ready result.

## Next Recommended Goal

KORA-CHAMPION-GPU-007B Dashboard Evidence View.

If the priority is external review rather than dashboard implementation, the next goal should be KORA-CHAMPION-GPU-007C Demo Video Capture Package.
