# KORA Core v0.1 Architecture

KORA Core is a workload execution router for AI services. Its role is to choose an execution target before a request defaults to a provider model call.

## Role

KORA Core sits above deterministic execution, cache, CPU execution, local GPU runtimes, and provider APIs. It is not a model runtime and does not replace provider models or serving systems.

Primary message: run AI services with less infrastructure.

## Execution Target Model

The v0.1 skeleton defines five initial execution targets:

- `deterministic`: code can answer without inference.
- `cache`: a replay-safe cached result is available.
- `cpu`: local CPU execution is sufficient.
- `local_gpu`: a local GPU route is required or preferred.
- `provider_api`: a remote model provider is required.

The initial router uses explicit request fields and makes no external calls.

## Measurement-First Design

The skeleton records local telemetry for:

- total requests
- target counts
- avoided provider calls
- estimated cost

Current cost values are configurable placeholders. They are not provider pricing claims.

## Non-Goals

KORA Core v0.1 is not:

- a GPT replacement
- a Claude replacement
- a Gemini replacement
- a vLLM replacement
- a production inference system
- a benchmark claim for real provider, GPU, latency, token, or cost reduction

## Future Integrations

Planned provider and runtime integration surfaces include:

- vLLM
- Bedrock
- Claude
- GPT
- Gemini

Future integrations must preserve explicit route accounting, provider-call flags, latency counters, token counters, cost-source metadata, and public-safety boundaries.

## AI Champion Evidence Support

This architecture supports the AI Champion evidence path by creating a clean place to measure:

- call reduction
- token reduction
- latency reduction
- provider cost reduction
- GPU workload reduction
- infrastructure reduction

The v0.1 skeleton is only the measurement foundation. Real evidence requires later tasks with approved workloads, provider/runtime configuration, artifact policy, and reproducibility checks.
