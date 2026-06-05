# KORA Champion GPU-004C H100 Routed Subset Measurement Report

## Executive Summary

GPU-004C H100 routed subset measurement completed. The source is the GPU-004B 100K mixed-realistic dry-run comparison. The KORA `local_gpu` routed subset from GPU-004B was measured with a bounded deterministic GPU workload.

No live provider call occurred. This is measured routed subset evidence, not production savings evidence.

## Source Routing Context

- Source comparison: `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json`
- Total requests: `100,000`
- KORA local GPU routed count from GPU-004B: `21,203`
- KORA local GPU route percentage from GPU-004B: `21.203%`
- KORA exact route accuracy from GPU-004B: `0.98477`
- KORA acceptable route rate from GPU-004B: `1.0`
- KORA unsafe misroute rate from GPU-004B: `0.0`
- KORA fallback rate from GPU-004B: `0.0909`
- Compute-weighted GPU reduction from GPU-004B: `31.496734%`

## H100 Measurement

Measured evidence:

- Evidence path: `docs/evidence/gpu-routed-subset-runs/20260605-124147937820Z-mixed_realistic_100k-kora-router-h100-subset.json`
- Claim level: `gpu_routed_subset_measured`
- H100 execution: `true`
- Live provider execution: `false`
- Measured subset count: `10,000`
- Measured subset limit: `10,000`
- Measured subset compute weight: `2,241,645.288123`
- Measured subset SHA-256: `87e6aad84996ea9aef9648dc3c0702badd72830caed2dabb94ecdc821cba2a46`
- Runtime seconds: `1.752106`
- Throughput requests/sec: `5707.417245`
- Throughput compute-weight/sec: `1279400.497529`
- GPU utilization avg/max: `15.444444` / `23.0`
- GPU memory MB avg/max: `600.0` / `717.0`
- Error count/rate: `0` / `0.0`
- Output digest: `c77db6eb26e4ff98bc6a21e0a5491fbd5512f671654dc5428ea0a88b2a7a8b62`

## Baseline Comparison

- Estimated all-GPU runtime seconds: `5.429518`
- Measured KORA routed subset runtime seconds: `1.752106`
- Estimated full KORA GPU subset runtime seconds: `3.719397`
- Estimated avoided GPU runtime seconds: `1.710121`
- Estimated runtime reduction percentage: `31.496734%`
- Baseline method: `compute_weight_scaled_from_measured_routed_subset`

The all-GPU runtime baseline is estimated by scaling measured routed subset runtime by compute weight. It is not a fully measured all-GPU execution.

## Interpretation

KORA moved from dry-run route comparison to measured H100 routed subset evidence. KORA connected oracle-labeled routing benchmark output to measured GPU execution and can report routed subset runtime, throughput, utilization, memory, and error rate.

This supports execution-path selectivity evidence. It is still not production cost-saving evidence.

## Claim Boundaries

Allowed:

- KORA measured H100 execution for the GPU-routed subset of a 100K benchmark.
- KORA can connect oracle-labeled routing benchmark output to measured GPU execution.
- KORA can report routed subset runtime, throughput, utilization, memory, and error rate.

Not allowed:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- 10x cost savings.
- Full provider/GPU live workload comparison.
- Final paper-ready result.

## Next Step

KORA-CHAMPION-GPU-005 Multi-Profile Routing Robustness Benchmark.
