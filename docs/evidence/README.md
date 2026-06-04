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

Provider evidence must identify the provider family, model or runtime identifier, call count, token accounting source, latency method, cost source, and whether a real call was attempted. Credentials and raw provider responses with sensitive content must not be committed.

## GPU Evidence

GPU evidence must identify only public-safe runtime configuration and aggregate measurements suitable for release. Private server details, credentials, raw logs, and operational access notes must stay in ignored private storage.

## Dashboard Screenshots

Dashboard screenshots may be committed only after review for secrets, private hostnames, account identifiers, raw logs, and unreleased claims. Prefer synthetic or sanitized screenshots until real evidence is approved.

## Safety Rules For Evidence Artifacts

Commit only reviewed, public-safe summaries. Keep raw or sensitive artifacts in ignored local directories. Do not commit private logs, credential paths, API keys, SSH material, private provider responses, or local-only handoff notes.

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

## Future Live Evidence Plan

Future live evidence should add separate records for provider dry runs, provider live runs, GPU dry runs, GPU live runs, and hybrid live runs. Each live record must include source metadata for tokens, latency, cost, runtime, and claim boundaries.

Do not commit raw secrets, API keys, provider credentials, SSH details, GPU credentials, private server logs, sensitive raw benchmark dumps, or private operational transcripts.

Use ignored local directories such as `private/artifacts/`, `private/logs/`, and `private/reports/` for sensitive or unreviewed material.
