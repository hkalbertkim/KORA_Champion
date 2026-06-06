# KORA Studio Evidence Checklist

## 1. Screenshot Checklist

- [ ] Studio route decision view captured.
- [ ] Studio path explanation panel captured.
- [ ] Studio evidence mapping panel captured.
- [ ] Studio claim boundary panel captured.
- [ ] Deterministic path example captured if available.
- [ ] Cache path example captured if available.
- [ ] CPU path example captured if available.
- [ ] Provider path example captured if available.
- [ ] GPU path example captured if available.
- [ ] Fallback path example captured if available.
- [ ] Screenshots use public-safe labels.
- [ ] Screenshots avoid exposing non-public operational details.

## 2. Screen Recording Checklist

- [ ] Two-minute Studio plus dashboard walkthrough recorded.
- [ ] Five-minute extended walkthrough recorded if time allows.
- [ ] Opening message states that KORA benchmarks when H100 should be used.
- [ ] Demo uses "execution-path selectivity" consistently.
- [ ] Demo uses "compute-weighted GPU demand reduction in benchmark workloads" where needed.
- [ ] Demo uses "bounded H100 routed subset measurement" where needed.
- [ ] Demo does not imply production savings.
- [ ] Demo does not imply official validation.
- [ ] Demo ends with explicit non-claims.

## 3. Dashboard Capture Checklist

- [ ] Dashboard core message captured.
- [ ] KPI cards captured.
- [ ] Evidence chain timeline captured.
- [ ] 100K execution-path selectivity table captured.
- [ ] H100 measured execution table captured.
- [ ] Multi-profile robustness table captured.
- [ ] 1M scale and saturation table captured.
- [ ] Evidence links section captured.
- [ ] Claim boundary section captured.
- [ ] Dashboard capture files are referenced from the final package index.

## 4. Benchmark Evidence Link Checklist

- [ ] `docs/reports/kora-champion-gpu-004a-routing-benchmark-framework-report.md`
- [ ] `docs/reports/kora-champion-gpu-004b-100k-dry-run-routing-comparison-report.md`
- [ ] `docs/reports/kora-champion-gpu-004c-h100-routed-subset-measurement-report.md`
- [ ] `docs/reports/kora-champion-gpu-005-multi-profile-routing-robustness-report.md`
- [ ] `docs/reports/kora-champion-gpu-006-1m-scale-saturation-benchmark-report.md`
- [ ] `docs/reports/july-31-interim-result-report-draft.md`
- [ ] `docs/reports/july-31-interim-result-report-evidence-table.md`
- [ ] `docs/reports/july-31-interim-result-report-claim-boundary.md`
- [ ] `docs/reports/july-31-interim-result-report-executive-summary.md`
- [ ] `docs/dashboard/index.html`
- [ ] `docs/dashboard/dashboard-data.json`

## 5. Local Validation Output Checklist

- [ ] `git status --short --branch` recorded before work.
- [ ] `git log --oneline -5` recorded before work.
- [ ] Git author name verified.
- [ ] Git author email verified.
- [ ] `git diff --check` passes.
- [ ] `find docs/reports -maxdepth 1 -type f | sort` reviewed.
- [ ] Safety scan over changed public files passes.
- [ ] Lightweight validation command run if reasonably discoverable.
- [ ] Documentation-only scope noted if no additional test suite is run.

## 6. Repository Evidence Checklist

- [ ] Commit contains only public-safe evidence planning documents.
- [ ] Commit message is `Add KORA Studio launch evidence plan`.
- [ ] Branch is pushed according to the current repository workflow.
- [ ] Final working tree is clean.
- [ ] Final package references the commit after push.
- [ ] No unrelated local changes are included.

## 7. Demo Readiness Checklist

- [ ] Demo can be completed in two minutes.
- [ ] Extended five-minute version is available.
- [ ] Viewer can identify the selected execution path.
- [ ] Viewer can identify the evidence backing the selected path.
- [ ] Viewer can distinguish measured, dry-run, and estimated evidence.
- [ ] Viewer can find the dashboard evidence view.
- [ ] Viewer can identify explicit non-claims.

## 8. Claim Boundary Review Checklist

- [ ] No production cost reduction claim.
- [ ] No customer workload savings claim.
- [ ] No real infrastructure savings claim.
- [ ] No proven 10x savings claim.
- [ ] No full provider/GPU live workload comparison claim.
- [ ] No full 1M all-GPU measured execution claim.
- [ ] No production representativeness claim.
- [ ] No final paper-ready result claim.
- [ ] No formal government validation claim.
- [ ] No signed partner validation claim.
- [ ] No broad workload superiority proof claim.
- [ ] No energy reduction proof claim.

## 9. Public Safety Scan Checklist

- [ ] Changed files avoid non-public workflow details.
- [ ] Changed files avoid access details.
- [ ] Changed files avoid non-public host or machine labels.
- [ ] Changed files avoid credential-like strings.
- [ ] Changed files avoid raw service output dumps.
- [ ] Changed files use public-safe wording such as measurement harness, routing benchmark, execution-path selectivity, evidence package, dashboard evidence view, interim result report, demo evidence package, and Studio evidence surface.

## 10. Final July 31 Package Readiness

- [ ] Studio evidence plan complete.
- [ ] Studio demo script complete.
- [ ] Studio evidence checklist complete.
- [ ] Studio gap analysis complete.
- [ ] Dashboard capture package complete.
- [ ] Studio screenshot package complete.
- [ ] Demo recording complete or clearly listed as remaining work.
- [ ] Package index updated.
- [ ] Final claim boundary review complete.
- [ ] Final repository state clean and pushed.
