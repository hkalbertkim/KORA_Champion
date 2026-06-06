# AI Champion Demo Readiness Plan

## Demo Video Objective

Show that KORA has a public evidence chain for execution-path selectivity: provider path readiness, H100 runtime readiness, routing benchmarks, measured H100 routed subset execution, multi-profile robustness, and 1M scale evidence.

The demo should focus on evidence files, benchmark outputs, and claim boundaries. It should not present production savings claims.

## Required Demo Scenes

| Scene | Evidence to show | Main point |
| --- | --- | --- |
| Provider path evidence | `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json` | A bounded live provider call succeeded |
| H100 runtime evidence | `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json` | H100 runtime produced measured throughput, utilization, and memory evidence |
| 100K routing selectivity table | `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json` | KORA routes requests across execution paths with acceptable route rate 1.0 and unsafe misroute rate 0.0 |
| H100 routed subset measurement | `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json` | GPU-routed subset execution was measured on H100 |
| Multi-profile robustness table | `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness.json` | KORA stays within safety boundaries across workload profiles |
| 1M scale summary | `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json` | KORA can run 1M dry-run routing scale evaluation |
| Saturation subset measurement | `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json` | 50K routed H100 subset was measured |
| Final evidence dashboard | `docs/reports/ai-champion-interim-evidence-package-report.md` | The evidence chain is ready for interim review with explicit boundaries |

## Dashboard Metrics To Show

- Provider measured calls, failed calls, tokens, and latency.
- GPU micro benchmark runtime, throughput, utilization, and memory.
- 100K KORA route distribution.
- 100K acceptable route rate and unsafe misroute rate.
- 100K compute-weighted GPU demand reduction in benchmark workload.
- 10K H100 routed subset runtime, throughput, utilization, memory, and error rate.
- Multi-profile local_gpu, cache, provider, fallback, acceptable route rate, unsafe misroute rate, and compute-weighted GPU demand reduction.
- 1M dry-run local_gpu, cache, provider, fallback, acceptable route rate, unsafe misroute rate, and estimated runtime.
- 50K H100 saturation subset runtime, throughput, utilization, memory, and error rate.

## Suggested Screen Capture Sequence

1. Open the interim package index and show the document map.
2. Open the GitHub evidence table and highlight measured, dry-run, and estimated evidence types.
3. Show the provider live evidence JSON summary.
4. Show the GPU micro benchmark evidence JSON summary.
5. Show the 100K routing comparison and KORA route distribution.
6. Show the 10K H100 routed subset measurement.
7. Show the multi-profile robustness report or aggregate JSON.
8. Show the 1M scale summary.
9. Show the 50K saturation subset measurement.
10. End on the claim boundary section.

## Evidence Files To Reference

- `docs/reports/ai-champion-interim-package-index.md`
- `docs/reports/ai-champion-github-evidence-table.md`
- `docs/reports/ai-champion-interim-evidence-package-report.md`
- `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json`
- `docs/evidence/gpu-runs/20260605-070531-gpu-micro-benchmark.json`
- `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json`
- `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json`
- `docs/evidence/routing-benchmark-multi-profile/20260605-132228-multi-profile-routing-robustness.json`
- `docs/evidence/routing-benchmark-scale/20260606-052807-gpu-006-scale-summary.json`
- `docs/evidence/gpu-saturation-runs/20260606-053159-mixed_realistic_1m-kora-router-h100-saturation-subset.json`

## Narration Outline

1. KORA measures execution-path selectivity, not raw H100 usage.
2. The provider path has bounded live evidence.
3. The H100 path has measured runtime evidence.
4. The routing benchmark compares routers over oracle-labeled workloads without using oracle labels inside router decisions.
5. The KORA adapter preserves acceptable route correctness and avoids unsafe misroutes in the 100K dry-run.
6. GPU-routed subsets are connected to measured H100 execution.
7. Multi-profile benchmarks show robustness across different workload distributions.
8. The 1M benchmark shows dry-run scale stability.
9. The 50K saturation subset shows a larger bounded H100 measurement.
10. The current package supports benchmark evidence, not production savings.

## Claim Boundary Overlay Text

Use these short overlays:

- "Execution-path selectivity benchmark."
- "Measured routed subset, not full production workload."
- "Dry-run routing comparison, no live provider calls."
- "Estimated runtime uses measured H100 calibration."
- "Not production savings evidence."

## What Should Not Be Said In The Video

- Do not say KORA has proven production cost reduction.
- Do not say KORA has proven real customer workload savings.
- Do not say KORA has proven real infrastructure savings.
- Do not say KORA has proven 10x savings.
- Do not say KORA has completed a full provider/GPU live workload comparison.
- Do not say the evidence is final paper-ready.
- Do not imply the full 1M workload was measured on H100.
- Do not imply production representativeness.
