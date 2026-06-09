# Commit And Push Rules

## End-Of-Hour Rule

At the end of every one-hour unit, Codex must:

1. Run validation.
2. Run `git status --short --branch`.
3. Commit relevant changes if files changed.
4. Push to `origin/main` if safe.
5. Report:
   - Changed files.
   - Validation commands.
   - Commit hash.
   - Whether push succeeded.
   - Next one-hour action.
6. Stop.

## Push Rule

If branch is ahead of `origin/main` and working tree is clean, push to `origin/main`.

If push fails, report the reason and stop.

Do not continue with additional work after push failure.

## Commit Rule

Commit only relevant `docs/ops/` or report files.

Do not commit unrelated local changes.

Use concise public-safe commit messages.

## Validation

Run:

- `git diff --check`
- `git diff --cached --check` before commit if files are staged
- `python3 scripts/run_smoke.py` if it remains the repo's lightweight smoke validation and is available

If additional lightweight markdown/report validation exists and is clearly relevant, run it.

Do not invent unavailable tooling.

## GitHub Push

After commit, push to `origin/main` if safe.
