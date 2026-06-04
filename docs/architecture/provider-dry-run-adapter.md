# Provider Dry-Run Adapter

Status: dry-run adapter interface for KORA Core v0.1.

## Purpose

The provider dry-run adapter gives KORA Core a provider-shaped interface before live provider validation. It records request, token, latency, cost, and warning fields without making external calls or requiring credentials.

## Adapter Interface

The adapter module defines:

- `ProviderRequest`
- `ProviderResponse`
- `ProviderUsage`
- `ProviderLatency`
- `ProviderCost`
- `ProviderAdapterResult`
- `ProviderAdapter`
- `DryRunProviderAdapter`

The dry-run adapter returns deterministic placeholder responses and provider-shaped metrics.

## Dry-Run vs Live Provider Boundary

Dry-run behavior:

- no external API calls
- no SDK imports
- no provider credentials
- no environment variables
- deterministic placeholder response
- local token heuristic
- configurable placeholder cost rates
- placeholder latency

Live provider behavior is not implemented. Future live adapters must be added behind explicit approval gates and secret-safe configuration.

## Provider Identifiers

Supported identifiers:

- `openai`
- `anthropic`
- `gemini`
- `bedrock`
- `vllm`
- `local_mock`

These identifiers are labels only in the dry-run path.

## Evidence Fields Populated

Provider dry-run evidence populates:

- provider name
- model name
- provider calls
- input tokens
- output tokens
- total tokens
- estimated provider cost
- actual provider cost as `null`
- placeholder latency
- claim level as `dry_run`
- warnings
- `has_real_provider_data: false`

## Safety Guarantees

The dry-run adapter does not import provider SDKs or HTTP clients. It does not read API keys and does not call any external service.

## Future Live Provider Plan

Future live provider adapters must add:

- explicit secret-safe config
- fail-closed defaults
- provider SDK or HTTP boundary review
- token accounting source
- cost source and date
- retry/error accounting
- public claim review before publication
