# Codex Execution Order

## Required Order

1. Read `NORTH_STAR.md` first.
2. Read `TODAY_MANDATE.md`.
3. Read `DEVIATION_GUARDRAILS.md`.
4. Read `TODAY_QUEUE.md`.
5. Read `NEXT_ACTION.md`.
6. Read `H100_BOUNDARY.md`.
7. Read `COMMIT_AND_PUSH_RULES.md`.
8. Read the current HOUR plan.
9. Confirm git status and branch.
10. Execute only the current one-hour unit.
11. Touch only allowed files.
12. Run validation.
13. Commit.
14. Push to `origin/main` if safe.
15. Update `NEXT_ACTION.md`.
16. Report changed files, validation, commit hash, pushed status, and next one-hour unit.
17. Stop.

## Allowed File Scope

- `docs/ops/**`
- `docs/reports/**`
- `docs/july31-review-packet/**` only if directly relevant
- `docs/demo-capture/**` only if directly relevant
- Existing review/index docs if directly relevant
- `scripts/kora_today.sh` only if useful and lightweight

## Forbidden File Scope Unless Explicitly Required

- `src/**`
- `tests/**`
- Provider adapters.
- Benchmark logic.
- Dashboard feature code.
- KORA Studio runtime/product code.
- Server environment files.
- Dependency files.
