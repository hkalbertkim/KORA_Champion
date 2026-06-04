# Provider Harness Switch

Status: canonical dry-run-to-live provider harness switch for KORA Core v0.1.

## Purpose

The provider harness gives KORA Core one entrypoint for provider-shaped evidence runs. It runs dry-run provider evidence by default and gates live intent through the secret-safe live provider boundary.

This task does not add live provider API calls.

## Dry-Run Default

Default command:

```bash
python3 scripts/run_provider_harness.py
```

Dry-run behavior:

- uses `DryRunProviderAdapter`
- runs only requests routed to `provider_api`
- makes no external calls
- requires no credentials
- sets `claim_level: dry_run`
- sets `has_real_provider_data: false`
- keeps `actual_provider_cost: null`

## Live Mode Gate

Live intent must be explicit:

```bash
KORA_PROVIDER_MODE=live KORA_LIVE_PROVIDER=openai python3 scripts/run_provider_harness.py --mode live --provider openai
```

If required provider config is missing, the harness exits nonzero and records a safe `live_config_error` result. It prints only missing KORA-specific field names, not values.

If config is valid but no concrete live adapter exists, the harness returns `live_boundary_not_implemented`. That result still has:

- `has_real_provider_data: false`
- `claim_level` not equal to measured provider
- zero real provider calls
- warnings explaining the boundary status

## Live OpenAI Path

The first concrete live path is OpenAI-only. It requires:

```bash
KORA_PROVIDER_MODE=live KORA_LIVE_PROVIDER=openai KORA_OPENAI_API_KEY=... python3 scripts/run_provider_harness.py --mode live --provider openai --model gpt-4o-mini --allow-live --max-live-calls 1
```

`--allow-live` is mandatory. Without it, the harness fails before any network-capable adapter can run.

`--max-live-calls` defaults to `1` and should remain low during initial validation.

## Config Loading

The harness uses `src/kora_core/config.py` and loads provider config from environment variables only. It does not automatically read `.env` files.

## Evidence Fields

Provider harness evidence includes:

- mode
- selected provider
- selected model
- provider calls
- input tokens
- output tokens
- total tokens
- estimated provider cost
- actual provider cost
- real provider data status
- claim level
- warnings
- errors
- evidence status

## Failure Behavior

Unsupported provider identifiers fail clearly. Live mode with missing required config fails before adapter invocation and before any external call can be attempted.

## Why No External Calls Are Made

Task 009 is a harness switch only. It intentionally avoids provider SDKs, HTTP clients, network calls, real provider credentials, and real provider measurements.

Task 010 adds the first OpenAI live measurement adapter behind the same harness switch. Dry-run remains the default.

## Task 010 Path

Task 010 can add one live provider adapter behind this harness by implementing provider-specific invocation after:

- explicit live mode
- validated provider config
- request scrubbing
- token accounting source
- latency timing source
- cost metadata source
- public claim review
