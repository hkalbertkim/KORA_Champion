# AI Champion GitHub Evidence Table

This table is a public-facing reviewer map for the interim evidence package. It separates measured, dry-run, and estimated evidence so claims remain bounded.

| Evidence category | Artifact path | What it proves | What it does not prove | Evidence type | Reviewer note |
| --- | --- | --- | --- | --- | --- |
| Provider path readiness | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` | A bounded live provider call completed successfully with measured tokens and latency | Provider cost reduction or full live provider comparison | Measured partial provider sample | Use as provider path readiness only |
| Provider normalized comparison | `docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json` | Partial live provider evidence can be normalized into a comparison artifact | Full provider/GPU live workload comparison | Partial live comparison | Keep sample-size caveat visible |
| H100 runtime readiness | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` | H100 runtime was visible and executed a 10K measured workload | Route-aware GPU selectivity | Measured micro benchmark | Shows runtime readiness, not routing |
| Routing benchmark framework | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` | KORA has schema, workload generation, oracle labels, routers, and metrics for routing benchmarks | Runtime performance | Framework/report | Foundation for later evidence |
| 100K routing selectivity | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | KORA can compare routing policies at 100K dry-run scale with acceptable route rate 1.0 and unsafe misroute rate 0.0 | Measured GPU runtime reduction | Dry-run routing benchmark | Core execution-path selectivity evidence |
| H100 routed subset measurement | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | KORA connected GPU-routed requests to measured H100 execution for 10K routed requests | Full 100K all-GPU measurement or production savings | Measured routed subset | Strongest route-aware measured GPU evidence |
| Multi-profile robustness | `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness.json` | KORA route behavior was compared across mixed, GPU-heavy, cache-heavy, adversarial, and service-replay profiles | Production representativeness | Dry-run robustness benchmark | Shows profile robustness and adversarial fallback behavior |
| 1M dry-run scale | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` | KORA ran a deterministic 1M dry-run routing benchmark with acceptable route rate 1.0 and unsafe misroute rate 0.0 | Full 1M measured GPU execution | Dry-run scale benchmark with estimated runtime | Shows route stability at scale |
| 50K H100 saturation subset | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | KORA measured a 50K H100 subset from the 1M GPU-routed workload | Full 1M all-GPU execution or production cost reduction | Measured saturation subset | Extends routed subset measurement beyond 10K |
| Interim evidence inventory | `docs/reports/ai-champion-interim-evidence-inventory.md` | Evidence is mapped to claim levels, allowed claims, caveats, and recommended usage | New runtime evidence | Report/index | Use as reviewer navigation |
| Interim evidence package report | `docs/reports/ai-champion-interim-evidence-package-report.md` | Evidence chain is summarized for July 31 readiness | Final paper-ready result | Report | Use as current package narrative |

## Reviewer Summary

The strongest current claim is:

KORA can benchmark execution-path selectivity across deterministic, cache, CPU, provider, GPU, and fallback paths; preserve route correctness in dry-run benchmarks; and measure bounded H100 execution for routed GPU subsets.

The current package should not be read as production savings evidence, real customer workload evidence, or full provider/GPU live workload comparison evidence.
