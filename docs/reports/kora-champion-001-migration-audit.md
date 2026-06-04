# KORA Champion 001 Migration Audit

Date: 2026-06-04
Task: KORA-CHAMPION-001
Scope: repository and migration audit only

## Executive Summary

The old KORA Project directory and the new KORA Champion directory are separate local workspaces. The old track contains the active KORA OSS/Studio repository under `repo/KORA`, an `internals` repository, local reports, generated paper outputs, and many old worktrees. The new Champion track is not a git repository and currently contains only AI Champion workspace scaffolding: `docs/`, `envs/`, `private/`, `repos/`, and `.gitignore`.

The best reusable material for KORA Core v0.1 is in the active old repo path `repo/KORA`, not in old worktrees. The strongest candidates are the task graph IR, deterministic scheduler/executor primitives, deterministic-heavy benchmark workload and runner, runtime-integrated benchmark example, provider-routing dry-run harness, model-call measurement primitives, telemetry summarization, cost model, and focused tests. Studio UI/server code should not be copied into the Champion track. Studio dashboard/report viewer pieces may be used only as reference for later evidence display requirements.

No source files were copied. No old Project files were modified. The only created/changed Champion file is this audit report.

## Directory Separation Summary

| Workspace | Path | Role | Git state |
|---|---|---|---|
| Old KORA Project root | `/Users/albertkim/02_PROJECTS/05_KORA_Project` | Studio development, Studio release, existing OSS work, consumer-facing app work, historical worktrees, local reports | Root is not a git repo |
| Old active public KORA repo | `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA` | Current KORA OSS/Studio code and docs | Git repo on `main`, dirty with Studio-focused modifications |
| Old internals repo | `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals` | Private/internal project material | Git repo on `main`, clean |
| New KORA Champion root | `/Users/albertkim/02_PROJECTS/05_KORA_Champion` | KORA Core, AI Champion Phase-1 evidence, runtime measurement, benchmarking, routing evidence, future paper artifacts | Root is not a git repo |

Important boundary: AI Champion work should start from a clean KORA Core repository structure and migrate only the runtime/evidence primitives needed for measurement. It should not absorb KORA Studio implementation work or old private operational notes.

## Preflight Results

Current working directory during audit:

```text
/Users/albertkim/02_PROJECTS/05_KORA_Champion
```

Old Project root:

- `/Users/albertkim/02_PROJECTS/05_KORA_Project` is not itself a git repository.
- Top-level entries observed: local README, archives, extraction utility, local-only material, repo clones, and worktrees.
- Nested git repos found:
  - `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/.git`
  - `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals/.git`

Old active KORA repo:

- Path: `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA`
- Branch: `main`
- Latest commit: `c245864 docs: consolidate kora studio browser smoke guidance`
- Remote: `origin git@github.com:Krako-Labs/KORA.git`
- Status: dirty, mostly Studio-focused changes:
  - Modified: `README.md`, `docs/kora-studio/kora-studio-implementation-breakdown.md`, multiple `kora/studio_*` files, `kora/studio_assets/studio.css`, `kora/studio_assets/studio.js`, Studio preview script/tests.
  - Untracked: several `docs/kora-studio/kora-studio-v4-*` and `v5-*` Studio reports.

Old internals repo:

- Path: `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals`
- Branch: `main`
- Latest commit: `641f7a6 Add KORA India contributor onboarding packet`
- Remote: `origin https://github.com/Krako-Labs/internals.git`
- Status: clean.

New Champion root:

- `/Users/albertkim/02_PROJECTS/05_KORA_Champion` is not a git repository.
- No nested `.git` directory was found under the inspected depth.
- Top-level entries observed: `.gitignore`, `docs/`, `envs/`, `private/`, `repos/`.
- Existing tracked-style local docs before this task:
  - `docs/handoffs/task525-ai-champion-workspace-status.md`
- Existing ignored/private workspace pattern:
  - `private/`, `envs/`, `repos/` are ignored.
  - secrets, logs, traces, profiler files, model files, databases, parquet, and caches are ignored.

## Old KORA Project Inventory

### Active KORA Repo Structure

Useful active tree under `repo/KORA`:

- `kora/`: Python runtime package.
- `kora/adapters/`: adapter abstractions and mock/OpenAI adapters.
- `experiments/`: deterministic workload generation and benchmark modes.
- `experiments/provider_routing/`: AI Champion provider routing dry-run harness.
- `examples/runtime_integrated_benchmark/`: offline runtime-path benchmark evidence harness.
- `examples/real_model_call_validation_fake/`: local no-network model-call validation example.
- `examples/customer_support_triage_fake_validation/`: local validation workload example.
- `scripts/metrics/`: metrics aggregation and harness scripts.
- `tests/`: focused unit and integration tests for runtime, benchmark, provider routing, validation, Studio server pieces, and harnesses.
- `docs/benchmarks/`: benchmark results, provider-routing docs, validation roadmap, claim boundaries, local/real provider designs.
- `docs/reports/`: release/evidence reports and benchmark artifact policy.
- `docs/paper/` and `local/paper_outputs/`: prior paper preparation material and generated manuscripts.
- `studio/`, `kora/studio_*`, `kora/studio_assets/`: Studio implementation and report/dashboard surfaces. Reference only for Champion.

### Reusable Runtime And Evidence Assets

The most relevant code/docs are:

- `kora/task_ir.py`: Pydantic task graph schema, budgets, deterministic/LLM run specs, adaptive routing policy schema, normalization, and validation.
- `kora/scheduler.py`: deterministic DAG helpers and topological sort.
- `kora/executor.py`: task graph executor with deterministic handlers, LLM adapter routing, adaptive metadata, retrieval gate hooks, and event emission.
- `kora/model_call.py`: provider-neutral request/response dataclasses, deterministic local validation adapters, local runtime stub, blocked adapters, token estimates, and aggregate counters.
- `kora/telemetry.py`: summary extraction for total time, LLM calls, tokens, events, skipped events, stage counts, budget breaches, escalation, and estimated cost.
- `kora/cost_model.py`: simple provider-cost estimation and savings calculation.
- `kora/retrieval.py`: in-memory retrieval/cache-like support for deterministic gate reuse.
- `experiments/run_benchmark.py`: deterministic-heavy benchmark runner with `dry-run`, `direct-baseline`, and `kora-controlled` modes.
- `experiments/generate_workload.py`: reproducible workload generation.
- `experiments/workloads/deterministic_heavy_v1_100.json`: 100-task deterministic-heavy workload with 80 no-model tasks and 20 fallback/model-candidate tasks.
- `examples/runtime_integrated_benchmark/run.py`: offline runtime-path harness showing 80 avoided simulated model invocations through executor events.
- `examples/runtime_integrated_benchmark/report.py`: Markdown evidence packet generation.
- `experiments/provider_routing/run_dry_run.py`: synthetic provider route validation across deterministic, cache, local CPU/small model, local GPU, cloud, and API provider families.
- `experiments/provider_routing/config.example.yaml`: placeholder-only JSON-compatible route config.
- `tests/test_runtime_integrated_benchmark.py`: assertions for 100 tasks, 80 deterministic routes, 20 model-candidate routes, 80% avoided simulated invocations, generated JSON, and evidence packet boundaries.
- `tests/test_provider_routing_dry_run.py`: safety checks that no active endpoints, credentials, GPU calls, or network calls are present in provider routing dry run.
- `docs/benchmarks/kora_benchmark_result_v1_100.md`: prior 100-task benchmark result and command record.
- `docs/benchmarks/ai-champion-provider-routing-matrix.md`: route matrix and required accounting fields for future real runs.
- `docs/benchmarks/ai-champion-claim-boundaries.md`: public wording and forbidden claim guardrails.
- `docs/benchmarks/ai-champion-gpu-api-test-plan.md`: planning reference for real GPU/API route activation.
- `docs/reports/benchmark_artifact_policy.md`: artifact handling policy.
- `docs/reports/v0.3.0-alpha-runtime-evidence-reviewer-guide.md`: reviewer-facing runtime evidence path.
- `docs/README.md` and `README.md`: KORA positioning, setup, evidence links, and claim wording.

### Local/Private Old Artifacts

The old Project directory also contains local-only reports, generated paper outputs, and local assistant context. These are useful for private planning context but should not be copied into a public KORA Core repository. Some contain private infrastructure details, server facts, or non-public operational history.

## New KORA Champion Inventory

The new Champion workspace is initialized as a local workspace, not as an application/package repository.

Existing structure:

```text
/Users/albertkim/02_PROJECTS/05_KORA_Champion
  .gitignore
  docs/
    handoffs/
      task525-ai-champion-workspace-status.md
    reports/
      kora-champion-001-migration-audit.md
  envs/
  private/
    artifacts/
    logs/
    models/
    reports/
    tmp/
  repos/
```

Existing files to preserve:

- `.gitignore`: important safety guardrail for private material, model files, logs, and local repos.
- `docs/handoffs/task525-ai-champion-workspace-status.md`: establishes the track separation, private/public boundaries, and next-task guidance.
- `private/`, `envs/`, `repos/`: local ignored directories for future private reports, environments, and clones/worktrees.

Missing repository structure:

- No `pyproject.toml`.
- No `README.md`.
- No `src/` or `kora_core/` package.
- No benchmark scripts under the Champion root.
- No tests.
- No committed sample fixtures.
- No git repository at the Champion root.

## Reusable Assets Table

| Source path | Asset type | Why it matters | Recommended action | Risk level |
|---|---|---|---|---|
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/task_ir.py` | Core runtime schema | Defines task graph, budgets, run specs, validation, and adaptive routing schema needed for KORA Core v0.1 | copy | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/scheduler.py` | DAG scheduler | Small deterministic dependency ordering primitive, low coupling | copy | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/executor.py` | Runtime executor | Main runtime path for deterministic-first execution, adapter invocation, telemetry events, and skip/escalation behavior | copy after pruning Studio/legacy coupling | High |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/adapters/base.py` | Adapter interface | Needed to preserve provider abstraction | copy | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/adapters/mock.py` | Mock adapter | Needed for offline deterministic validation and tests | copy | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/adapters/openai_adapter.py` | Provider adapter | Useful later for provider evidence, but live API behavior and dependencies need fresh review | reference only initially | High |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/model_call.py` | Measurement primitive | Provider-neutral requests/responses, local validation adapters, token and latency counters | copy | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/telemetry.py` | Measurement/report primitive | Aggregates LLM calls, tokens, latency, skipped events, stage counts, and estimated cost | copy | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/cost_model.py` | Cost accounting | Starting point for provider-cost reduction evidence | copy, then expand pricing source/versioning | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/retrieval.py` | Cache/retrieval primitive | Supports replay/gate cache patterns, useful for cache-routing evidence | copy with renamed cache semantics if appropriate | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/budget.py` | Budget primitive | Useful for runtime budget and escalation accounting | copy if executor dependencies require it | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/validation_report.py` | Report generation | Reviewer-facing local validation reports | reference first, copy after schema decision | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/experiments/run_benchmark.py` | Benchmark runner | Implements dry-run, direct baseline, and KORA-controlled simulated invocation accounting | copy | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/experiments/generate_workload.py` | Workload generator | Reproducible deterministic-heavy workload generation | copy | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/experiments/workloads/deterministic_heavy_v1_100.json` | Benchmark fixture | Prior 100-task benchmark fixture | copy as fixture with provenance note | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/examples/runtime_integrated_benchmark/run.py` | Runtime evidence harness | Bridges benchmark workload to actual executor events | copy after package path adjustment | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/examples/runtime_integrated_benchmark/report.py` | Evidence packet renderer | Produces reviewer-facing Markdown from structured JSON | copy | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/experiments/provider_routing/run_dry_run.py` | Provider routing dry run | Covers deterministic/cache/CPU/GPU/provider route families with no real calls | copy | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/experiments/provider_routing/config.example.yaml` | Provider route fixture | Placeholder-only route config for safe synthetic evidence | copy with secret scan | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/tests/test_runtime_integrated_benchmark.py` | Test pattern | Locks core 100-task evidence counters and report boundaries | copy/adapt | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/tests/test_provider_routing_dry_run.py` | Safety tests | Ensures provider routing stays placeholder-only and does not attempt real calls | copy/adapt | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/tests/test_benchmark_runner.py` | Benchmark tests | Useful baseline for workload/runner correctness | copy/adapt | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/tests/test_model_call.py` | Measurement tests | Useful for local validation counters and fail-closed adapters | copy/adapt | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs/benchmarks/kora_benchmark_result_v1_100.md` | Benchmark result doc | Documents prior 100-task methodology and limitations | reference only, then recreate Champion-native summary | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs/benchmarks/ai-champion-provider-routing-matrix.md` | Route matrix doc | Strong starting point for Champion route taxonomy and accounting fields | reference only initially | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs/benchmarks/ai-champion-claim-boundaries.md` | Claim guardrail | Prevents overstating simulated/dry-run evidence | copy or reference in docs | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs/reports/benchmark_artifact_policy.md` | Artifact policy | Needed to separate reproducible public artifacts from raw/private evidence | reference only, then draft Champion policy | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs/README.md` | Docs index and positioning | Useful KORA Core positioning and evidence navigation | reference only | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/README.md` | Public positioning | Useful phrasing for KORA Core README, but contains Studio/OSS context | reference only | Low |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/studio/frontend/src/App.tsx` | Studio UI | Not relevant to KORA Core v0.1 implementation; future dashboard reference only | reference only | High |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/studio_report_viewer.py` | Studio report viewer | Could inform later evidence display but is Studio-coupled | reference only | High |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/studio_harness_*` | Studio harness display/request/run helpers | Some data contracts may be useful, but implementation is Studio-specific | reference only | High |
| Old Project local-only report directories | Private operational reports | Contains server planning and private operational context | reference locally only, do not copy | High |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/local/paper_outputs/` | Paper artifacts | Useful prior manuscript/evidence context, but generated/private review material | reference only | Medium |
| `/Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/` | Historical worktrees | Duplicate and stale branches; high confusion risk | ignore except named Task 524 handoff reference | High |

## Files That Must NOT Be Copied

Do not copy these into KORA Champion source/release scope:

- Any dirty Studio implementation files from `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/studio_*`.
- Any dirty Studio assets from `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/studio_assets/`.
- Any Studio frontend/backend source under `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/studio/`.
- Any Studio planning/review docs under `/Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs/kora-studio/`, except as reference for later dashboard requirements.
- Any `.envrc`, `.env`, credential, key, token, local config, or shell history.
- Any `.DS_Store`, `__pycache__/`, `.pytest_cache/`, local build outputs, or generated caches.
- Any old raw benchmark outputs unless explicitly selected and sanitized in a later artifact-policy task.
- Any local GPU/server reports from old Project local-only report directories.
- Any exact private host/IP/user/credential/server connection details.
- Any generated paper `.docx` or local review packet from `local/paper_outputs/` or `local/generated_paper_outputs/`.
- Any old worktree wholesale from `/Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/`.
- Any `repo/internals` material unless a later private-only task explicitly requests it.

## Recommended Initial KORA Core v0.1 Repository Structure

Recommended structure under `/Users/albertkim/02_PROJECTS/05_KORA_Champion/repos/kora-core` or a future Champion-root git repo:

```text
README.md
pyproject.toml
LICENSE
docs/
  benchmarks/
  reports/
  architecture/
  claims/
src/
  kora_core/
    __init__.py
    task_ir.py
    scheduler.py
    executor.py
    adapters/
      __init__.py
      base.py
      mock.py
    measurement/
      __init__.py
      model_call.py
      telemetry.py
      cost_model.py
    routing/
      __init__.py
      provider_matrix.py
      cache.py
benchmarks/
  workloads/
    deterministic_heavy_v1_100.json
  run_benchmark.py
  runtime_integrated/
    run.py
    report.py
  provider_routing/
    config.example.json
    run_dry_run.py
tests/
  test_task_ir.py
  test_scheduler.py
  test_executor.py
  test_benchmark_runner.py
  test_runtime_integrated_benchmark.py
  test_provider_routing_dry_run.py
  test_model_call.py
  test_telemetry.py
```

Keep private raw evidence outside the repo or under ignored Champion paths:

```text
/Users/albertkim/02_PROJECTS/05_KORA_Champion/private/artifacts/
/Users/albertkim/02_PROJECTS/05_KORA_Champion/private/logs/
/Users/albertkim/02_PROJECTS/05_KORA_Champion/private/reports/
```

## Recommended First Implementation Sequence

1. Create a KORA Core repo skeleton in the Champion track with Python 3.11+, `src/` layout, pytest, and no Studio dependencies.
2. Migrate only low-coupling core primitives first: `task_ir.py`, `scheduler.py`, adapter base/mock, `model_call.py`, `telemetry.py`, `cost_model.py`.
3. Port focused tests for task IR, scheduler, model-call counters, telemetry, and cost model.
4. Migrate deterministic workload generator, 100-task fixture, and benchmark runner.
5. Port benchmark tests and validate the 100-task simulated evidence still reproduces 80 avoided simulated invocations.
6. Migrate runtime-integrated benchmark harness and report generator, adjusting imports to `kora_core`.
7. Migrate provider routing dry-run harness and placeholder config, preserving tests that forbid active endpoints and credentials.
8. Add a Champion-native claim boundary doc and artifact policy before any real provider/GPU runs.
9. Add route accounting schema for deterministic/cache/CPU/GPU/provider execution with required fields for tokens, latency, cost, provider family, model ID, cache hit/miss, GPU route, and real-call attempted flag.
10. Only after the offline/dry-run suite is stable, plan separate approved tasks for GPU live verification, local model smoke tests, provider API smoke tests, and dashboard/report evidence.

## Validation Commands Run

Read-only or safe commands run during this audit:

```bash
pwd
ls /Users/albertkim/02_PROJECTS/05_KORA_Project
ls /Users/albertkim/02_PROJECTS/05_KORA_Champion
git -C /Users/albertkim/02_PROJECTS/05_KORA_Project rev-parse --is-inside-work-tree
git -C /Users/albertkim/02_PROJECTS/05_KORA_Champion rev-parse --is-inside-work-tree
find /Users/albertkim/02_PROJECTS/05_KORA_Project -maxdepth 3 -type d -name .git -print
find /Users/albertkim/02_PROJECTS/05_KORA_Champion -maxdepth 5 -type d -name .git -print
git -C /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA status --short --branch
git -C /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA branch --show-current
git -C /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA log -1 --oneline
git -C /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA remote -v
git -C /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals status --short --branch
git -C /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals branch --show-current
git -C /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals log -1 --oneline
git -C /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/internals remote -v
find /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA -maxdepth 2 -type d -name .git -prune -o -maxdepth 2 -print
find /Users/albertkim/02_PROJECTS/05_KORA_Champion -maxdepth 4 -type d -name .git -prune -o -maxdepth 4 -print
find /Users/albertkim/02_PROJECTS/05_KORA_Champion -maxdepth 3 -type f | sort
rg --files /Users/albertkim/02_PROJECTS/05_KORA_Project | rg -i '(bench|benchmark|route|router|routing|cache|telemetry|metric|latency|token|cost|dashboard|report|paper|readme|test|harness|eval|provider|gpu|cpu|llm)'
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Champion/docs/handoffs/task525-ai-champion-workspace-status.md
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/model_call.py
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/telemetry.py
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/cost_model.py
sed -n '1,260p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/kora/task_ir.py
sed -n '1,240p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/experiments/run_benchmark.py
sed -n '240,520p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/experiments/run_benchmark.py
sed -n '1,260p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/examples/runtime_integrated_benchmark/run.py
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/experiments/provider_routing/run_dry_run.py
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/tests/test_runtime_integrated_benchmark.py
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/tests/test_provider_routing_dry_run.py
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs/benchmarks/kora_benchmark_result_v1_100.md
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs/benchmarks/ai-champion-provider-routing-matrix.md
sed -n '1,220p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/docs/benchmarks/ai-champion-claim-boundaries.md
sed -n '1,180p' /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA/pyproject.toml
sed -n '1,200p' /Users/albertkim/02_PROJECTS/05_KORA_Champion/.gitignore
```

One exploratory read attempted a non-existent local-only report path under the old active repo; the correct local-only report directory is outside that repo.

Write command run for this audit:

```bash
mkdir -p /Users/albertkim/02_PROJECTS/05_KORA_Champion/docs/reports
```

## Current Blockers

- The Champion root is not a git repository, so this task did not commit.
- The active old `repo/KORA` git repo is dirty with Studio-focused work. Migration should not use dirty Studio files as source of truth.
- Existing runtime/evidence code is coupled to package name `kora`; Champion Core should likely use `kora_core` or a clearly separated package name, requiring import and CLI adjustments.
- Existing executor includes accumulated alpha behavior and adapter imports; it should be pruned and tested during migration rather than copied blindly.
- Current public evidence is still simulated/offline for model-call reduction. It does not yet prove real token, latency, provider cost, GPU workload, or infrastructure reduction.
- GPU/server operational reports contain private details and should remain local/private.
- No Champion-native README, package metadata, test suite, or claim registry exists yet.

## Next Codex Task Recommendation

Recommended next task: `KORA-CHAMPION-002 Initialize KORA Core v0.1 Repository Skeleton`.

Scope:

- Create a clean Champion-owned repo skeleton, preferably under `/Users/albertkim/02_PROJECTS/05_KORA_Champion/repos/kora-core` unless the user explicitly wants the Champion root initialized as git.
- Add `README.md`, `pyproject.toml`, `src/kora_core/`, `tests/`, `benchmarks/`, and `docs/claims/`.
- Do not migrate old source yet except minimal empty package/test scaffolding.
- Preserve `.gitignore` safety patterns.
- Add an explicit migration plan checklist referencing this audit.
- Keep Studio code, private reports, and old worktrees out of scope.

After that, run `KORA-CHAMPION-003` to migrate the low-coupling core primitives and their tests.
