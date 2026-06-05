# KORA Champion GPU-004C H100 Routed Subset Measurement Report

## Executive Summary

GPU-004C implementation added the routed subset measurement harness. The source is the GPU-004B 100K mixed-realistic dry-run comparison. The harness identifies the KORA `local_gpu` routed subset, creates a bounded deterministic GPU workload, and writes sanitized evidence.

No live provider call occurred. This is routed subset measurement infrastructure and local validation evidence until the script is executed on an H100 runtime.

## Source Routing Context

- Source comparison: `docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json`
- Total requests: `100,000`
- KORA local GPU route percentage from GPU-004B: `21.203%`
- KORA acceptable route rate from GPU-004B: `1.0`
- KORA unsafe misroute rate from GPU-004B: `0.0`
- Compute-weighted GPU reduction from GPU-004B: `31.496734%`

## H100 Measurement

H100 execution was not completed in the local workspace because CUDA was not available. The harness supports the required command shape:

`python3 scripts/run_gpu_routed_subset_benchmark.py --comparison-run docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json --router kora_router_adapter --limit 10000`

Local validation evidence can be produced with:

`python3 scripts/run_gpu_routed_subset_benchmark.py --comparison-run docs/evidence/routing-benchmark-runs/20260605-101501-mixed_realistic_100k-100000.json --router kora_router_adapter --limit 100 --local-validation-only`

Local validation evidence produced in this workspace:

- `docs/evidence/gpu-routed-subset-runs/20260605-102732580852Z-mixed_realistic_100k-kora-router-h100-subset.json`
- Claim level: `local_validation_only`
- H100 execution: `false`
- Measured subset count for schema validation: `100`

## Baseline Comparison

The harness estimates all-GPU runtime by scaling measured routed subset runtime by compute weight. This baseline is estimated, not a fully measured all-GPU execution, unless the all-GPU path is separately executed.

## Interpretation

KORA can now connect oracle-labeled routing benchmark output to a bounded GPU measurement harness. Once run on H100, the evidence can report routed subset runtime, throughput, utilization, and memory. This supports execution-path selectivity evidence and does not prove production cost savings.

## Claim Boundaries

Allowed after an H100 run:

- KORA measured H100 execution for the GPU-routed subset of a 100K benchmark.
- KORA can connect oracle-labeled routing benchmark output to measured GPU execution.
- KORA can report routed subset runtime, throughput, utilization, and memory.

Not allowed:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- 10x cost savings.
- Full provider/GPU live workload comparison.
- Final paper-ready result.

## Next Step

KORA-CHAMPION-GPU-005 Multi-Profile Routing Robustness Benchmark.
