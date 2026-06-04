# KORA Core Runtime Primitives

Status: v0.1 public-safe runtime primitive migration.

## Migrated Primitive Categories

KORA Core now has local, dependency-light primitives for:

- request classification
- deterministic availability flags
- cache eligibility and cache hit handling
- execution target routing
- in-memory cache behavior
- token, latency, cost, and provider-call metric placeholders
- offline harness execution over synthetic request fixtures
- telemetry summaries for route counts and provider-call avoidance

## Copy, Adapt, Reference Decisions

No old source file was copied directly in this task. The old KORA Project runtime and benchmark code was used as design reference, then clean-room primitives were implemented in the Champion repo.

Adapted clean-room:

- `src/kora_core/classifier.py`
- `src/kora_core/cache.py`
- `src/kora_core/metrics.py`
- `src/kora_core/harness.py`
- updates to `router.py`, `telemetry.py`, `benchmark.py`, and `scripts/run_smoke.py`

Reference only:

- old retrieval/cache helper
- old model-call measurement structures
- old benchmark runner patterns
- old runtime-integrated benchmark tests
- old provider-routing dry-run safety tests
- old benchmark and telemetry docs

## Why Studio Coupling Was Avoided

The old project contains active dirty Studio work and Studio-specific rendering, server, browser, and report-viewer files. Those files are not part of KORA Core runtime routing. Pulling them into this repo would mix tracks and increase public-safety risk.

The migrated primitives are intentionally UI-free and do not depend on browser app state, Studio assets, old handoff material, private prompts, or generated paper artifacts.

## AI Champion Evidence Support

These primitives support the evidence path by making every synthetic request produce:

- a classification record
- a route decision
- cache hit/miss metadata
- provider-call avoided flag
- placeholder token counters
- placeholder latency counters
- placeholder cost counters
- aggregate telemetry

This creates the foundation for later measurement-first evidence without claiming real savings yet.

## Still Synthetic And Offline

Current behavior is synthetic and offline:

- no external network calls
- no provider API calls
- no GPU access
- no model runtime execution
- no real provider pricing
- no production latency measurement

The current metrics are placeholders for schema and harness validation only.

## Later Requirements For Real Evidence

Future real provider/GPU evidence must add:

- fail-closed provider/runtime adapters
- explicit provider and model identifiers
- approved credential handling outside git
- real token accounting source
- real latency measurement method
- real cost calculation source and date
- GPU route and workload counters
- raw artifact policy
- public claim boundary review
