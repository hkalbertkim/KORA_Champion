# KORA Studio Demo Capture Package

## Purpose

This directory is the public-safe assembly area for the July 31 KORA Studio demo evidence package. It is intended to organize reviewed screenshots, recording summaries, capture manifests, and evidence maps that explain execution-path selectivity through the Studio evidence surface and dashboard evidence view.

The package should help a reviewer understand:

- What was captured.
- What each capture shows.
- Which benchmark evidence backs each capture.
- Which claims are supported.
- Which claims are explicitly not supported.

## What Belongs Here

Allowed package files:

- Markdown package indexes.
- Markdown capture manifests.
- Markdown evidence maps.
- Markdown capture review summaries.
- Public-safe screenshot files after review.
- Public-safe small image files after review.
- Public-safe recording references or summaries.

Recommended subdirectories for future capture execution:

```text
docs/demo-capture/
  README.md
  capture-manifest.md
  evidence-map.md
  july31-package-index.md
  screenshots/
  recordings/
  notes/
```

## What Must Not Be Committed

Do not commit:

- Large binary video files unless explicitly approved.
- Raw screen recordings before review.
- Screenshots that show browser account UI, local usernames, terminal shells, machine details, service dashboards, secret strings, or non-public operational context.
- Files that expose private environment details.
- Unreviewed captures from local tools.
- Any capture that implies unsupported claims.

## Allowed File Types

Preferred:

- `.md` for package notes, manifests, summaries, and indexes.
- `.png` for reviewed screenshots.
- `.jpg` only when image size needs to be reduced and text remains readable.
- `.txt` only for reviewed public-safe capture notes.

Use video files only when explicitly approved for repository storage. Otherwise keep video outside the repository and document the public-safe filename, duration, and content summary.

## Disallowed File Types or Content

Avoid committing:

- `.mp4`, `.mov`, or other large video files unless explicitly approved.
- Raw capture exports.
- Browser profile exports.
- System logs.
- Service configuration dumps.
- Files with local machine identifiers.
- Files with private network details.
- Files with secret or account material.

## Expected Final Package Layout

```text
docs/demo-capture/
  README.md
  capture-manifest.md
  evidence-map.md
  july31-package-index.md
  screenshots/
    studio-route-decision-01.png
    studio-path-explanation-02.png
    studio-evidence-map-03.png
    dashboard-core-message-04.png
    dashboard-routing-selectivity-05.png
    dashboard-h100-measured-06.png
    dashboard-scale-saturation-07.png
    dashboard-claim-boundary-08.png
  recordings/
    kora-studio-two-minute-demo-summary.md
    kora-studio-five-minute-demo-summary.md
  notes/
    capture-review-summary.md
```

## Screenshot Naming Convention

Use lowercase, hyphen-separated names:

`{surface}-{section}-{sequence}.png`

Examples:

- `studio-route-decision-01.png`
- `studio-path-explanation-02.png`
- `studio-evidence-map-03.png`

## Video Naming Convention

If video files are explicitly approved for storage, use:

`{surface}-{duration}-demo.{extension}`

Examples:

- `kora-studio-two-minute-demo.mp4`
- `kora-studio-five-minute-demo.mp4`

If video files are not stored in the repository, use Markdown summaries:

- `kora-studio-two-minute-demo-summary.md`
- `kora-studio-five-minute-demo-summary.md`

## Dashboard Capture Naming Convention

Use:

`dashboard-{section}-{sequence}.png`

Required dashboard examples:

- `dashboard-core-message-04.png`
- `dashboard-routing-selectivity-05.png`
- `dashboard-h100-measured-06.png`
- `dashboard-scale-saturation-07.png`
- `dashboard-claim-boundary-08.png`

## Claim-Safe Usage Guidance

Use this package to support:

- Execution-path selectivity.
- Static dashboard evidence view readiness.
- KORA Studio as a demo evidence surface.
- Bounded live provider evidence.
- Measured H100 runtime evidence.
- Bounded H100 routed subset measurement.
- 1M dry-run scale stability evidence.
- Bounded 1M H100 saturation subset evidence.
- Compute-weighted GPU demand reduction in benchmark workloads.

Do not use this package to imply:

- Production cost reduction.
- Customer workload savings.
- Real infrastructure savings.
- Proven 10x savings.
- Full provider/GPU live workload comparison.
- Full 1M all-GPU measured execution.
- Production representativeness.
- Final paper-ready result.
- Formal government validation.
- Signed partner validation.
- Broad workload superiority proof.
- Energy reduction proof.

## Review Checklist Before Adding Future Capture

- [ ] Capture file name follows the naming convention.
- [ ] Capture is readable without zooming.
- [ ] Capture contains no private local details.
- [ ] Capture contains no secret or account material.
- [ ] Capture avoids unreviewed browser UI.
- [ ] Capture has a corresponding row in `capture-manifest.md`.
- [ ] Capture has a corresponding evidence mapping in `evidence-map.md`.
- [ ] Capture uses execution-path selectivity language.
- [ ] Capture distinguishes measured, dry-run, and estimated evidence where relevant.
- [ ] Capture does not imply production savings or official validation.
- [ ] Claim boundaries are visible in the final package.
