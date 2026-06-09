# Deviation Guardrails

## North Star Precedence Rule

If any instruction conflicts with `NORTH_STAR.md`, follow `NORTH_STAR.md`.

## Allowed Direction

KORA AI Champion evidence/report/demo package preparation and closure only.

## Forbidden Direction

- Product feature development.
- Runtime changes.
- Benchmark expansion.
- Dashboard expansion.
- Provider expansion.
- Architecture expansion.
- Paper drafting.
- Marketing rewrite.
- Repo restructuring.
- Unsupported claims.
- Private server detail exposure.

## Evidence Claim Rules

- Do not claim demo/capture evidence exists unless verified in the repo or via bounded H100 verification.
- If evidence is missing, create or recommend a defer log.
- Prefer precise evidence status over optimistic wording.
- Do not claim production savings, customer savings, or 10x savings unless explicitly backed by approved evidence.

## Stop Conditions

- Stop if the next action requires product development.
- Stop if the next action requires a new benchmark.
- Stop if the next action requires dashboard feature work.
- Stop if H100 verification would require long-running experiments or server environment changes.
- Stop if push fails.
- Stop if unexpected unrelated file changes are present.

## Self-Check

- [ ] Did I stay inside the north star?
- [ ] Did I complete only one focused one-hour package?
- [ ] Did I avoid product development?
- [ ] Did I avoid unsupported claims?
- [ ] Did I avoid private server details?
- [ ] Did I touch only relevant files?
- [ ] Did I validate?
- [ ] Did I commit?
- [ ] Did I push if safe?
