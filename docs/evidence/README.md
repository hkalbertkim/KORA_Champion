# KORA Core Evidence

This directory is for public-safe evidence documentation and reviewed summaries for KORA Core.

Schema reference:

- [Evidence Schema v0.1](evidence-schema-v0.1.md)

Expected evidence types:

- workload definitions and versions
- route decision summaries
- provider-call reduction summaries
- token reduction summaries
- latency reduction summaries
- cost reduction summaries
- GPU workload reduction summaries
- infrastructure reduction summaries
- reproducibility commands
- claim boundary notes

## Synthetic Fixture Evidence

Synthetic fixture evidence belongs in reviewed docs or test fixtures. It may include public-safe request shapes, expected route decisions, cache hit/miss behavior, and local smoke-test summaries. It must not include real user data.

## Runtime Telemetry Evidence

Runtime telemetry evidence should include route counts, provider-call avoided flags, token counters, latency counters, placeholder or real cost fields, and the source of each measurement. Synthetic placeholder telemetry must be labeled as synthetic/offline.

## Provider Evidence

Provider evidence must identify the provider family, model or runtime identifier, call count, token accounting source, latency method, cost source, and whether a real call was attempted. Credentials and raw provider responses with sensitive material must not be committed.

## GPU Evidence

GPU evidence must identify only public-safe runtime configuration and aggregate measurements suitable for release. Private server details, credentials, raw logs, and operational access notes must stay in ignored private storage.

## Dashboard Screenshots

Dashboard screenshots may be committed only after review for secrets, private hostnames, account identifiers, raw logs, and unreleased claims. Prefer synthetic or sanitized screenshots until real evidence is approved.

## Safety Rules For Evidence Artifacts

Commit only reviewed, public-safe summaries. Keep raw or sensitive artifacts in ignored local directories. Do not commit private logs, credential paths, API keys, SSH material, private provider responses, or local-only operational notes.

## Evidence Runs

`docs/evidence/runs/` stores reviewed public-safe run records. Current committed run records are synthetic unless explicitly labeled otherwise.

Generate a synthetic evidence record:

```bash
python3 scripts/record_synthetic_evidence.py
```

The current script runs the local synthetic fixture harness, writes a JSON record under `docs/evidence/runs/`, and prints total requests, routing distribution, avoided provider calls, claim level, and warnings.

Synthetic evidence is not real runtime savings. It validates schema, local routing behavior, and evidence serialization only.

## Comparison Evidence

`docs/evidence/comparisons/` stores reviewed public-safe baseline-vs-KORA comparison records.

Generate a synthetic baseline comparison:

```bash
python3 scripts/compare_synthetic_baseline.py
```

The current comparison uses `all_provider_api` as the synthetic baseline and compares it with KORA Core's classifier/router/harness path. Interpret the output as measurement scaffolding only. It does not prove real provider, GPU, token, latency, cost, or infrastructure savings.

Human-readable synthetic comparison:

- [Baseline vs KORA Synthetic Report](baseline-vs-kora-synthetic-report.md)

## Provider Dry-Run Evidence

`docs/evidence/provider-dry-runs/` stores reviewed provider-shaped dry-run records. These records validate adapter shape and accounting fields without external calls.

Generate provider dry-run evidence:

```bash
python3 scripts/provider_dry_run.py
```

Default provider label: `local_mock`.

Interpretation guide:

- Provider dry-run evidence can show request shape, placeholder token counts, placeholder costs, and dry-run warnings.
- Provider dry-run evidence is not real provider evidence.
- `actual_provider_cost` must remain `null`.
- `has_real_provider_data` must remain `false`.

## Provider Harness Evidence

`docs/evidence/provider-harness/` stores reviewed provider harness records. This is the canonical dry-run-to-live provider evidence entrypoint.

Run the canonical provider harness:

```bash
python3 scripts/run_provider_harness.py
```

Dry-run output with `evidence_status: dry_run_complete` validates the provider harness path, provider-routed fixture selection, placeholder token/cost fields, warnings, and JSON evidence shape.

Live output with `evidence_status: live_config_error` means live mode was requested but required config was missing. This is a safe failure and not provider evidence.

Live output with `evidence_status: live_boundary_not_implemented` means config passed the boundary, but no concrete live adapter exists yet. This is also not measured provider evidence.

Dry-run and live-boundary evidence must not be interpreted as real provider evidence.

## Live Provider Evidence Boundary

Live provider evidence requires explicit live mode:

```bash
KORA_PROVIDER_MODE=live
```

Check local provider config without network calls:

```bash
python3 scripts/check_provider_config.py
```

The config check prints redacted summaries only. It does not load `.env` automatically and does not print credential values.

Dry-run evidence is not real provider evidence. Live evidence must be generated only after provider-specific adapters, request scrubbing, token accounting, latency timing, cost metadata, and claim review are implemented.

Secrets must never be committed. Keep local provider config in ignored local files or shell environment state.

## Provider Live Runs

`docs/evidence/provider-live-runs/` is reserved for sanitized live provider evidence.

Live evidence safety rules:

- Do not commit unsanitized live evidence.
- Do not commit API keys, account identifiers, private inputs, private responses, or raw provider payloads.
- Response text should be redacted by default.
- Input text should be synthetic fixture text or redacted.
- `actual_provider_cost` remains `null` unless a reviewed cost source is added.
- A single live provider measurement is not cost-reduction evidence by itself.

Example bounded live command:

```bash
KORA_PROVIDER_MODE=live KORA_LIVE_PROVIDER=openai KORA_OPENAI_API_KEY=replace-with-your-key python3 scripts/run_provider_harness.py --mode live --provider openai --model gpt-4o-mini --allow-live --max-live-calls 1
```

AI Champion Bedrock live command:

```bash
export KORA_PROVIDER_MODE=live
export KORA_LIVE_PROVIDER=bedrock
export KORA_BEDROCK_API_KEY="replace-with-your-token"
export KORA_AWS_REGION="us-east-1"
export KORA_BEDROCK_MODEL_ID="anthropic.claude-haiku-4-5-20251001-v1:0"

python3 scripts/run_provider_harness.py --mode live --provider bedrock --allow-live --max-live-calls 1
```

Bedrock live evidence is measured provider evidence only when a real call succeeds. It is not cost-reduction evidence, baseline-vs-live comparison evidence, or GPU evidence.

## Live Comparisons

`docs/evidence/live-comparisons/` stores reviewed normalized live comparison records.

Current normalized Bedrock live comparison:

- input evidence: `docs/evidence/provider-live-runs/20260604-112641-provider-live-bedrock.json`
- comparison type: `partial_live_provider`
- claim level: `measured_provider_partial`
- interpretation: one measured provider-routed request normalized into the existing comparison framework

This is not full workload live comparison evidence. It is not cost-reduction, token-reduction, latency-reduction, GPU-reduction, or infrastructure-reduction evidence.

Human-readable normalized comparison:

- [Bedrock Live Normalized Comparison Report](bedrock-live-normalized-comparison-report.md)

## Future Live Evidence Plan

Future live evidence should add separate records for provider dry runs, provider live runs, GPU dry runs, GPU live runs, and hybrid live runs. Each live record must include source metadata for tokens, latency, cost, runtime, and claim boundaries.

Do not commit raw secrets, API keys, provider credentials, SSH details, GPU credentials, private server logs, sensitive raw benchmark dumps, or private operational transcripts.

Use ignored local directories such as `private/artifacts/`, `private/logs/`, and `private/reports/` for sensitive or unreviewed material.
