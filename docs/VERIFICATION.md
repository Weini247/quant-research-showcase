# Verification: release 2.1

The public release checks cover file integrity, aggregate consistency and figure composition, not independent validation of the empirical forecasts.

- Thirteen FX aggregate/release tests and twelve unchanged synthetic accounting tests are executed locally; the fictional demonstration is also run.
- All twelve SVG/PNG figure files are regenerated twice in an isolated public-only directory and compared byte-for-byte in the documented environment.
- The public manifest verifies the exact release file set and SHA-256 values, excluding itself. Git metadata and generated Python caches are outside that file set.
- Landing and research pages are exercised at desktop, tablet and narrow mobile widths, including H1/H20 mouse/keyboard operation, image loading, local links and static fallback.
- F2 is inspected directly as an SVG and checked for its nine embedded PNG elements and vector text. No external image is required.
- Numerical aggregate values, figure files and the renderer are unchanged from the reviewed V2 measurements; only release metadata, scope and documentation are corrected.

Local results do not imply that GitHub CI or Pages deployment has completed. Those statuses must be checked separately for the public release commit. Rendering checks are not a comprehensive accessibility or device certification. Public figure reproduction is not private empirical inference or a new scientific sample.

See [reproduction](REPRODUCIBILITY.md), [methods](METHODS.md), [rights](DATA_LICENSING.md) and [publishing](PUBLISHING.md). No new open-source licence is assigned.
