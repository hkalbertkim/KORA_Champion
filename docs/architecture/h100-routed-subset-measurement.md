# H100 Routed Subset Measurement

GPU-004C connects the 100K routing benchmark output to measured GPU execution for the KORA `local_gpu` routed subset.

The measurement flow is:

1. Load the GPU-004B 100K comparison run.
2. Reconstruct the deterministic workload from profile, count, and seed.
3. Rerun the selected router on router-visible metadata.
4. Select the first bounded set of `local_gpu` routed requests.
5. Execute deterministic synthetic CUDA operations derived from workload class, input size, batch size, and compute weight.
6. Store sanitized evidence with aggregate runtime, throughput, utilization, memory, and claim boundaries.

The measured GPU operation is not model inference. It is a deterministic measurement harness designed to provide routed subset runtime evidence without storing raw tensors or large arrays.

Claim boundary:

- Measured routed subset runtime is allowed when CUDA execution occurs.
- Production cost reduction, customer workload savings, full production representativeness, and provider cost claims are not allowed from this evidence alone.
