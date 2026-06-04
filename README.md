# KORA Core

Run AI services with less infrastructure.

KORA Core is a workload execution router for AI systems. It sits above deterministic execution, cache, CPU execution, local GPU runtimes, and provider APIs so applications can decide where work should run before defaulting to an external model call.

KORA Core is measurement-first. The v0.1 skeleton focuses on routing decisions, telemetry counters, cost-estimation placeholders, and synthetic benchmarks that can later be replaced with real provider and GPU measurements.

## What KORA Core Is

- A routing layer for AI workloads.
- A way to prefer deterministic and cached execution before model inference.
- A measurement surface for calls, tokens, latency, cost, GPU workload, and infrastructure pressure.
- A foundation for comparing direct provider-first execution against controlled execution paths.

## What KORA Core Is Not

- Not a GPT replacement.
- Not a Claude replacement.
- Not a Gemini replacement.
- Not a vLLM replacement.
- Not yet a production system.

KORA Core routes work above runtimes and providers. It can integrate with systems such as vLLM, Bedrock, Claude, GPT, and Gemini, but it does not replace them.

## Why Workload Routing Matters

AI services often send every request to a model, even when deterministic code, cache reuse, CPU execution, or a local runtime would be enough. That default increases provider calls, tokens, latency, cost, GPU load, and infrastructure requirements.

KORA Core makes the execution target explicit before inference. The initial routing model supports:

- deterministic
- cache
- CPU
- local GPU
- provider API

Planned provider and runtime integrations include:

- vLLM
- Bedrock
- Claude
- GPT
- Gemini

## AI Champion Phase-1 Evidence Goals

The Phase-1 evidence path is designed to measure:

- call reduction
- token reduction
- latency reduction
- cost reduction
- GPU workload reduction
- infrastructure reduction

Current status:

- v0.1 skeleton
- measurement-first
- local synthetic benchmark only
- no external network calls
- not yet a production system

## Public-Safety Note

This repository must not contain secrets, private provider credentials, GPU credentials, SSH credentials, raw private logs, or private infrastructure details. Use ignored local/private directories for sensitive operational artifacts.
