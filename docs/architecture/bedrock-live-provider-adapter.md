# Bedrock Live Provider Adapter

Status: AI Champion Bedrock bearer-token live provider adapter.

## Purpose

The Bedrock live adapter gives KORA Core a bounded AI Champion provider measurement path using the Bedrock Runtime Converse API with bearer-token authentication.

This adapter proves only the live measurement path. It is not cost-reduction, token-reduction, latency-reduction, GPU-reduction, or infrastructure-reduction evidence by itself.

## Required Env Vars

Required local environment:

- `KORA_PROVIDER_MODE=live`
- `KORA_LIVE_PROVIDER=bedrock`
- `KORA_BEDROCK_API_KEY`
- `KORA_AWS_REGION`
- `KORA_BEDROCK_MODEL_ID`

The token value must never be printed, stored, or committed.

## Bearer-Token Flow

The adapter sends:

- `Authorization: Bearer <token>`
- `Content-Type: application/json`

It uses the standard library only and does not add an SDK dependency.

## Model Prefix Rule

Bedrock Converse model paths require a `us.` prefix before the model ID for this AI Champion path.

If `KORA_BEDROCK_MODEL_ID` is:

```text
anthropic.claude-haiku-4-5-20251001-v1:0
```

the request path uses:

```text
us.anthropic.claude-haiku-4-5-20251001-v1:0
```

If the model ID already starts with `us.`, the adapter does not duplicate the prefix.

## Live Gate

Live execution requires:

```bash
--allow-live --max-live-calls 1
```

Without `--allow-live`, the adapter fails before a network-capable call can run.

## Request Shape

The adapter sends one Converse request per provider-routed request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": [{"text": "..."}]
    }
  ],
  "inferenceConfig": {
    "maxTokens": 128,
    "temperature": 0.2
  }
}
```

## Response Redaction

Response text is redacted by default. Evidence records include `response_text_redacted: true` and do not commit full model responses.

## Evidence Fields

Bedrock live evidence records:

- provider
- model
- provider calls
- successful provider calls
- failed provider calls
- input tokens
- output tokens
- total tokens
- measured latency
- estimated provider cost as placeholder
- actual provider cost as `null`
- claim level
- warnings
- errors
- response text redaction status

## What This Proves

This proves KORA Core can support a bounded Bedrock bearer-token measurement path when local credentials are present and explicit live gates are enabled.

## What This Does Not Prove

This does not prove real provider cost reduction, token reduction, latency reduction, GPU workload reduction, or infrastructure reduction.
