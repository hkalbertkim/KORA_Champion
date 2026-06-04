# Provider Live Boundary

Status: secret-safe boundary for future live provider adapters.

## Why This Boundary Exists

KORA Core is a public repository. Live provider validation needs a clear boundary before any provider SDK, endpoint, or credential path is added. This boundary defines how live mode is selected, how required configuration is checked, and how missing configuration fails safely.

This task does not implement live provider calls.

## Dry-Run vs Live Mode

Dry-run mode is the default:

```bash
KORA_PROVIDER_MODE=dry_run
```

Live mode must be enabled explicitly:

```bash
KORA_PROVIDER_MODE=live
```

When live mode is requested, KORA Core validates the selected provider config before returning a live adapter boundary. The current boundary returns non-measured boundary output and does not call a provider.

## Supported KORA Env Vars

KORA Core uses KORA-specific environment variable names:

- `KORA_PROVIDER_MODE`
- `KORA_LIVE_PROVIDER`
- `KORA_OPENAI_API_KEY`
- `KORA_ANTHROPIC_API_KEY`
- `KORA_GEMINI_API_KEY`
- `KORA_AWS_REGION`
- `KORA_AWS_PROFILE`
- `KORA_VLLM_BASE_URL`

Provider identifiers:

- `openai`
- `anthropic`
- `gemini`
- `bedrock`
- `vllm`
- `local_mock`

## Secret Handling Rules

Configuration is loaded from environment variables only. KORA Core does not automatically read `.env` files. Local tools may choose to load `.env`, but that must happen outside the public core package.

Config summaries are redacted. They show whether a field is `present` or `missing`; they do not expose values.

## Required Fields

Live-mode checks require:

- `openai`: `KORA_OPENAI_API_KEY`
- `anthropic`: `KORA_ANTHROPIC_API_KEY`
- `gemini`: `KORA_GEMINI_API_KEY`
- `bedrock`: `KORA_AWS_REGION`
- `vllm`: `KORA_VLLM_BASE_URL`
- `local_mock`: no required credential field

## No Network Calls

The live boundary does not import provider SDKs, HTTP clients, or cloud SDKs. It does not make network calls. It does not attempt provider execution.

## Config Check

Run:

```bash
python3 scripts/check_provider_config.py
```

Dry-run mode exits successfully even with no credentials. Live mode exits nonzero when required provider config is missing.

## Provider Harness Use

`scripts/run_provider_harness.py` uses this live boundary when live mode is requested. The harness validates config and records a boundary status, but it still does not call providers in Task 009.

## Future Live Provider Plan

Future live-provider work should add provider-specific adapters behind this boundary, including:

- explicit live execution flags
- provider SDK or endpoint review
- request and response scrubbing
- token accounting source
- latency timing method
- cost source metadata
- error and fallback accounting
- evidence claim review before publication
