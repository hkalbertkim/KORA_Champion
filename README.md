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

## Current Evidence Status

KORA Core has a measurement-first evidence schema and a baseline-vs-KORA synthetic comparison over public-safe fixtures. The current comparison is offline and synthetic: it demonstrates route accounting and provider-call avoidance measurement, but it does not prove real provider cost reduction, token reduction, latency reduction, GPU workload reduction, or infrastructure reduction.

Provider dry-run support now records provider-shaped request, token, cost, latency, and warning fields without external calls or credentials. Dry-run evidence is not measured provider evidence.

## Provider Config

KORA Core defaults to dry-run provider mode:

```bash
python3 scripts/check_provider_config.py
```

Use `.env.example` as a local reference for KORA-specific environment variable names. The core library reads environment variables only and does not automatically load `.env` files.

Live mode must be explicit:

```bash
KORA_PROVIDER_MODE=live KORA_LIVE_PROVIDER=local_mock python3 scripts/check_provider_config.py
```

The current live adapter is a boundary only. It validates config and refuses missing live requirements, but it does not call provider APIs and does not produce measured provider evidence.

## Provider Harness

Run the canonical provider harness in dry-run mode:

```bash
python3 scripts/run_provider_harness.py
```

The harness runs only provider-routed fixture requests, writes JSON under `docs/evidence/provider-harness/`, and defaults to `dry_run`.

Live mode is gated and still boundary-only:

```bash
KORA_PROVIDER_MODE=live KORA_LIVE_PROVIDER=openai python3 scripts/run_provider_harness.py --mode live --provider openai
```

Without required config, live mode fails safely. With valid config, the current boundary still does not call provider APIs or produce measured provider evidence.

## Public-Safety Note

This repository must not contain secrets, private provider credentials, GPU credentials, SSH credentials, raw private logs, or private infrastructure details. Use ignored local/private directories for sensitive operational artifacts.
