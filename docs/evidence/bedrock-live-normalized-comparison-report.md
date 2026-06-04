# Bedrock Live Normalized Comparison Report

## Executive Summary

The first Bedrock live provider measurement has been normalized into the KORA evidence framework and paired with the existing synthetic baseline structure as a partial live-provider comparison.

This is measured provider evidence for one provider-routed request only. It is not full workload savings evidence.

## Input Live Evidence File

`docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json`

## Measured Provider Facts

- Provider: `bedrock`
- Model: `anthropic.claude-haiku-4-5-20251001-v1:0`
- Provider calls: 1
- Successful provider calls: 1
- Failed provider calls: 0
- Input tokens: 19
- Output tokens: 128
- Total tokens: 147
- Measured latency: 2187.0 ms
- Estimated provider cost: 0.000275
- Actual provider cost: null
- Claim level: `measured_provider`
- Real provider data: true
- Response text redacted: true

## Normalized Comparison Summary

Generated comparison type: `partial_live_provider`.

The comparison includes:

- synthetic all-provider baseline calls: 6
- KORA synthetic provider calls: 1
- measured provider calls: 1
- measured successful provider calls: 1
- measured failed provider calls: 0
- measured tokens: 147
- measured latency: 2187.0 ms
- comparison claim level: `measured_provider_partial`

Synthetic baseline fields remain clearly separated from measured provider fields.

## What This Proves

- The committed Bedrock live evidence is sanitized and measurable.
- KORA Core can normalize a bounded live provider measurement.
- The comparison framework can combine measured provider facts with synthetic workload context without making savings claims.

## What This Does Not Prove

- It does not prove cost reduction.
- It does not prove token reduction.
- It does not prove latency reduction.
- It does not prove GPU reduction.
- It does not prove infrastructure reduction.
- It does not prove production savings.

## Why It Matters For AI Champion

This creates the bridge from one measured provider call to a future full workload live micro-benchmark. It makes the claim boundary explicit before scaling live measurements.

## Next Step

Run a full workload Bedrock live micro-benchmark with strict call limits, sanitized evidence output, and baseline-vs-KORA measured comparison.
