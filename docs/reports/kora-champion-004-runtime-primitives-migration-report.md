# KORA Champion 004 Runtime Primitives Migration Report

Date: 2026-06-04
Task: KORA-CHAMPION-004
Scope: migrate low-coupling KORA Core runtime primitives

## Summary

Implemented public-safe KORA Core runtime primitives using clean-room adaptation from the old KORA Project design patterns. No old source file was copied directly. No Studio UI, dirty Studio code, private handoffs, provider credentials, real provider integrations, or old private operational artifacts were migrated.

The new Champion repo now includes request classification, cache key/store primitives, metric placeholder schemas, an offline harness over synthetic request fixtures, expanded telemetry, and fixture-driven tests.

## Source Directories Inspected

- `/Users/albertkim/02_PROJECTS/05_KORA_Project`
- `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA`
- `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora`
- `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/experiments`
- `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/examples`
- `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/tests`
- `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs`

The old Project root is not a git repo. The nested active KORA repo was dirty with Studio-focused changes, so Studio paths were excluded.

## Old Project Candidate Files Reviewed

| Source path | Decision | Destination path | Reason | Safety notes |
|---|---|---|---|---|
| `repo/KORA/kora/retrieval.py` | adapt clean-room | `src/kora_core/cache.py` | Stable key and in-memory cache concepts are useful, but Champion needed smaller cache-specific naming | No private strings copied |
| `repo/KORA/kora/model_call.py` | adapt clean-room | `src/kora_core/metrics.py`, `src/kora_core/telemetry.py` | Request metric and token/latency/cost schema ideas are useful, but provider adapter classes are out of scope | No provider integration copied |
| `repo/KORA/kora/telemetry.py` | adapt clean-room | `src/kora_core/telemetry.py` | Aggregate counters informed telemetry fields | Old report renderer and broad event parsing not copied |
| `repo/KORA/kora/cost_model.py` | reference only | `src/kora_core/cost_model.py` already existed | Existing Champion cost model was sufficient for placeholders | No pricing claims added |
| `repo/KORA/experiments/run_benchmark.py` | adapt clean-room | `src/kora_core/harness.py`, `src/kora_core/benchmark.py` | Harness pattern informed fixture execution and summary shape | Old simulated benchmark framing not copied |
| `repo/KORA/experiments/workloads/deterministic_heavy_v1_100.json` | reference only | `tests/fixtures/sample_requests.json` | Champion needed smaller synthetic fixture, not the old 100-task artifact | No real user data copied |
| `repo/KORA/tests/test_benchmark_runner.py` | reference only | `tests/test_harness.py` | Test shape informed harness assertions | Tests rewritten for Champion APIs |
| `repo/KORA/tests/test_runtime_integrated_benchmark.py` | reference only | `tests/test_harness.py` | Useful evidence-boundary pattern, but old runtime integration is broader | No old evidence claims copied |
| `repo/KORA/tests/test_provider_routing_dry_run.py` | reference only | future task | Useful safety-test model for provider routes | Provider routing integration not added in this task |
| `repo/KORA/docs/telemetry-and-observability.md` | reference only | `docs/architecture/kora-core-runtime-primitives.md` | Useful measurement vocabulary | New doc avoids old release framing |
| `repo/KORA/docs/benchmark.md` | reference only | `docs/evidence/README.md` | Useful artifact/evidence categories | New doc labels current evidence synthetic/offline |
| `repo/KORA/kora/studio_*` and `repo/KORA/studio/` | ignore | none | Studio code is outside KORA Core scope | Dirty Studio files not copied |
| old local-only report and handoff directories | ignore | none | Private operational context is outside public repo scope | Not inspected beyond preflight listing |

## Files Created

- `src/kora_core/classifier.py`
- `src/kora_core/cache.py`
- `src/kora_core/metrics.py`
- `src/kora_core/harness.py`
- `tests/fixtures/sample_requests.json`
- `tests/test_classifier.py`
- `tests/test_cache.py`
- `tests/test_harness.py`
- `docs/architecture/kora-core-runtime-primitives.md`
- `docs/reports/kora-champion-004-runtime-primitives-migration-report.md`

## Files Changed

- `src/kora_core/__init__.py`
- `src/kora_core/router.py`
- `src/kora_core/telemetry.py`
- `src/kora_core/benchmark.py`
- `scripts/run_smoke.py`
- `docs/evidence/README.md`

## Validation Results

Pre-migration baseline:

- `python3 scripts/run_smoke.py`: passed
- `python3 -m unittest discover -s tests`: passed, 6 tests

Post-migration validation:

- `python3 -m py_compile src/kora_core/*.py scripts/run_smoke.py`: passed
- `python3 scripts/run_smoke.py`: passed; fixture smoke produced 6 records, 5 avoided provider calls, 1 provider-call placeholder, and no external calls
- `python3 -m unittest discover -s tests`: passed, 17 tests
- `git diff --check`: run before commit
- `git status --short --branch`: run before and after commit

## Public-Safety Scan Result

A lightweight scan was run over tracked/staged public files for common API-key, provider-secret, SSH-key, secret phrase, private host, and account patterns.

Result:

- No API keys found.
- No SSH key material found.
- No private provider credentials found.
- No private host/account patterns from the required scan list found.
- Planned public provider/runtime words, if present elsewhere in docs, are treated as public integration references rather than credentials.

## Git Commit And Push Result

Commit and push are performed after this report is written and validation passes. The final task response records the commit hash and push result.

## Remaining Blockers

- Current harness evidence is synthetic/offline only.
- No real provider adapter exists yet.
- No real GPU/runtime integration exists yet.
- No real token, latency, provider cost, GPU workload, or infrastructure reduction claim is supported yet.
- Provider route safety tests should be added before real integrations.

## Recommended Next Task

`KORA-CHAMPION-005 Measurement-First Telemetry Evidence Schema`

Recommended scope:

- Define stable evidence schemas for route decisions, token counters, latency counters, cost counters, GPU workload counters, and infrastructure counters.
- Add JSON schema or dataclass validation for evidence artifacts.
- Keep all provider/GPU runs fail-closed until explicit approval gates exist.
