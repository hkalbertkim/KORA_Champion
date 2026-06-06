# July 31 Interim Result Report Evidence Table

This table maps the interim result report draft to public evidence artifacts and claim-safe usage.

| Evidence category | Artifact path | Metric | Evidence type | Claim supported | Claim not supported | July 31 readiness usage |
| --- | --- | --- | --- | --- | --- | --- |
| Provider path | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` | 1 successful call, 0 failed calls, 147 tokens, 2,187.0 ms latency | Measured partial | KORA has bounded live provider evidence | Full provider/GPU live workload comparison | Provider path readiness section |
| Provider normalized comparison | `docs/evidence/live-comparisons/20260604-114009-bedrock-live-normalized-comparison.json` | Partial live sample normalized into comparison artifact | Measured partial comparison | KORA can package partial provider evidence into a comparison artifact | Production provider reduction | Provider evidence caveat |
| GPU micro benchmark | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` | 10,000 units, 0.836763s, 11,950.815225 units/sec | Measured | H100 runtime evidence exists | Route-aware selectivity | H100 runtime readiness |
| Routing framework | `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md` | Schema, workloads, oracle labels, routers, metrics | Framework/report | KORA has routing benchmark infrastructure | Measured runtime impact | KORA Core evidence status |
| 100K routing comparison | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | local_gpu 21.203%, acceptable 1.0, unsafe 0.0, demand reduction 31.496734% | Dry-run | KORA has 100K execution-path selectivity evidence | Measured GPU reduction | Main routing result |
| H100 routed subset | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | 10,000 requests, 1.752106s, 5,707.417245 req/sec, error rate 0.0 | Measured | KORA measured H100 execution for a routed GPU subset | Full 100K all-GPU execution | Strongest route-aware measured GPU evidence |
| Multi-profile robustness | `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness-summary.json` | 5 profiles, acceptable 1.0 and unsafe 0.0 across profiles | Dry-run | KORA can compare robustness across profile distributions | Production representativeness | Robustness section |
| 1M scale summary | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` | 1,000,000 requests, acceptable 1.0, unsafe 0.0, demand reduction 31.564469% | Dry-run with estimated runtime | KORA has 1M dry-run scale stability evidence | Full 1M measured GPU execution | Scale section |
| 1M saturation subset | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | 50,000 requests, 7.471771s, 6,691.853913 req/sec, error rate 0.0 | Measured | KORA measured a bounded H100 saturation subset | Full 1M all-GPU execution | Saturation section |
| Dashboard evidence view | `docs/dashboard/index.html` | Static evidence view with KPI cards, tables, links, boundaries | Static package | KORA has a local reviewer dashboard | New runtime evidence | Demo and reviewer navigation |
| Interim package index | `docs/reports/ai-champion-interim-package-index.md` | Evidence map and claim boundary summary | Report | Evidence package is organized for review | Final submission package | Reviewer entry point |

## Evidence-Type Summary

| Evidence type | Meaning | Example |
| --- | --- | --- |
| Measured | Runtime or provider behavior was actually executed and recorded in a bounded benchmark or sample | H100 routed subset measurement |
| Measured partial | A bounded live path sample was executed, but sample scale is intentionally limited | Provider live evidence |
| Dry-run | Routing decisions and benchmark metrics were computed without live provider calls or H100 execution | 100K routing comparison |
| Dry-run with estimated runtime | Dry-run routing demand was converted to runtime estimates using measured H100 calibration | 1M scale summary |
| Static package | Documentation or dashboard artifact that packages existing evidence | Dashboard evidence view |

## July 31 Usage Priority

1. Use measured routed subset and saturation subset evidence for H100 benchmark credibility.
2. Use 100K, multi-profile, and 1M dry-run evidence for execution-path selectivity.
3. Use provider evidence only as bounded provider path readiness.
4. Use dashboard evidence view for reviewer navigation and demo capture.
5. Keep runtime estimates visibly labeled as estimates based on measured calibration.
