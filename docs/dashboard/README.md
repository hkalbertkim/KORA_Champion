# KORA Champion Dashboard Evidence View

## Purpose

This dashboard is a static evidence view for KORA Champion reviewers. It summarizes the provider, GPU, routing, routed subset, multi-profile, 1M scale, and saturation benchmark evidence chain in one local page.

The dashboard is designed for:

- AI Champion reviewer inspection.
- GitHub evidence navigation.
- Demo video capture.
- July 31 interim result report preparation.

## How To Open Locally

Open:

`docs/dashboard/index.html`

The page is static HTML with embedded CSS and JavaScript. It can be opened directly in a browser from the local repository checkout.

## Data Source

The structured dashboard data model is:

`docs/dashboard/dashboard-data.json`

The HTML includes a compact embedded copy of the key display metrics so it works from a local file without a server.

## Static Runtime Boundary

The dashboard:

- Does not require a backend.
- Does not make live provider calls.
- Does not require H100 runtime access.
- Does not load external tracking scripts.
- Does not require secrets or account material.

## Claim Boundaries

Allowed claims:

- KORA has bounded live provider evidence.
- KORA has measured H100 runtime evidence.
- KORA has routing framework evidence.
- KORA has 100K routing selectivity evidence.
- KORA has measured H100 routed subset evidence.
- KORA has multi-profile routing robustness evidence.
- KORA has 1M dry-run scale stability evidence.
- KORA has bounded 1M H100 saturation subset evidence.
- KORA can show compute-weighted GPU demand reduction in benchmark workloads.

Prohibited claims:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- Proven 10x savings.
- Full provider/GPU live workload comparison.
- Full 1M all-GPU measured execution.
- Production representativeness.
- Final paper-ready result.

## Demo Capture Usage

Recommended screen sequence:

1. Hero/core message.
2. KPI cards.
3. Evidence chain timeline.
4. Routing selectivity section.
5. Multi-profile robustness table.
6. H100 measured execution section.
7. Evidence links.
8. Claim boundaries.
9. Demo capture mode section.

Suggested overlay text:

`Benchmark evidence for execution-path selectivity. Not production savings evidence.`

## Related Reports

- `docs/reports/ai-champion-interim-evidence-package-report.md`
- `docs/reports/ai-champion-github-evidence-table.md`
- `docs/reports/ai-champion-demo-readiness-plan.md`
- `docs/reports/ai-champion-interim-package-index.md`
