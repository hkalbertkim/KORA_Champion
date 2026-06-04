# OpenAI Live Provider Adapter

Status: first bounded live provider measurement adapter for KORA Core.

## Purpose

The OpenAI live adapter proves that KORA Core can execute one tightly gated provider measurement path and record provider-shaped evidence with real usage and locally measured latency.

This adapter is not a cost-reduction, token-reduction, latency-reduction, GPU-reduction, or infrastructure-reduction proof.

## Why OpenAI First

OpenAI is the first live provider path because it has the smallest adapter surface for this repository: one KORA-specific credential, one provider identifier, and one standard HTTPS request path.

No Claude, Gemini, Bedrock, vLLM, or GPU path is added in this task.

## Required Env Vars

Live OpenAI execution requires:

- `KORA_PROVIDER_MODE=live`
- `KORA_LIVE_PROVIDER=openai`
- `KORA_OPENAI_API_KEY` present in the environment

KORA Core does not automatically read `.env` files and does not use the non-KORA-prefixed OpenAI key name as the preferred variable.

## Explicit Live Flag

Live execution also requires:

```bash
--allow-live
```

Without `--allow-live`, the harness fails before any network-capable adapter can run.

## Max Live Calls

The canonical harness defaults to:

```bash
--max-live-calls 1
```

The default live model is `gpt-4o-mini` unless another model is supplied.

## Response Redaction

Committed live evidence must not include full model response text by default. The adapter stores:

- `response_text_redacted: true`
- redacted response text marker
- token usage if returned by the provider
- measured local latency
- response metadata flags that avoid account identifiers

## Evidence Fields

Live OpenAI evidence includes:

- provider
- model
- provider calls
- successful provider calls
- failed provider calls
- input tokens
- output tokens
- total tokens
- measured latency
- estimated provider cost using placeholder cost model
- actual provider cost as `null`
- real provider data status
- claim level
- warnings
- errors

## What This Proves

This proves that KORA Core has a bounded, secret-safe live measurement path for one OpenAI-compatible provider call.

## What This Does Not Prove

This does not prove real provider cost reduction, token reduction, latency reduction, GPU workload reduction, or infrastructure reduction.

## Future Providers

Future providers must be added one at a time behind the same harness gates, with provider-specific request scrubbing, token accounting, latency measurement, error handling, and evidence review.
