# KORA AI Champion Roadmap

Status: public-safe planning outline for KORA Core and AI Champion evidence.

## June Week 1: Measurement Infrastructure

- Initialize KORA Core repository structure.
- Add offline router, telemetry, placeholder cost model, synthetic smoke benchmark, and tests.
- Define public-safe evidence and artifact boundaries.
- Establish route accounting schema for deterministic, cache, CPU, local GPU, and provider API targets.
- KORA-CHAMPION-005 establishes the measurement-first evidence schema before live provider or GPU validation.
- KORA-CHAMPION-006 establishes baseline-vs-KORA synthetic comparison before live provider or GPU evidence.
- KORA-CHAMPION-007 establishes the provider dry-run adapter interface before live provider validation.
- KORA-CHAMPION-008 establishes the secret-safe live provider boundary before live provider validation.
- KORA-CHAMPION-009 establishes the dry-run-to-live provider harness switch before first live provider validation.
- KORA-CHAMPION-010 establishes the first bounded OpenAI live provider measurement path.
- KORA-CHAMPION-012 establishes the AI Champion Bedrock token-auth live provider adapter.
- KORA-CHAMPION-013 normalizes the first Bedrock live provider evidence into the comparison framework.
- KORA-CHAMPION-GPU-001 starts the GPU evidence track immediately because H100 x2 access ends on 2026-07-01.

## June Week 2: Provider And Runtime Integration

- Add integration boundaries for provider APIs and local runtimes.
- Keep all real credentials outside the repository.
- Add fail-closed adapters and dry-run validation before any live calls.
- Prepare runtime/provider smoke-test plans with explicit approval gates.

## June Week 3: Call Reduction Validation

- Run controlled workloads through direct baseline and KORA-routed paths.
- Measure provider calls avoided.
- Add token and latency counters where provider/runtime data is available.
- Preserve claim boundaries between synthetic, dry-run, and real measurements.

## June Week 4: GPU Reduction Validation

- Add local GPU route accounting.
- Compare provider/GPU route selection against direct execution baselines.
- Measure GPU workload changes only after approved runtime setup.
- Keep raw logs and sensitive artifacts out of public commits.

## July: Result Package

- Produce report-ready evidence tables and reproducibility commands.
- Build a public-safe demo/dashboard evidence surface.
- Draft technical report and Phase-2 roadmap.
- Prepare paper draft/submission materials.
- Prepare public KORA Core release evidence for the July 31 AI Champion result package.
