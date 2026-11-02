# Frozen FX development study: public aggregate reproduction

Release **2.1**. Public scope: the supplied ECB-derived FX development aggregates and figures.

These are measured 2018–2019 development results: 98 registered origins, eight ECB FX reference-rate series, five primary variants, H1 primary and H20 secondary. Public scope is aggregate figures and numerical tables only. There is no new inference, training or hypothesis test.

## Recreate the six figures

Use Python 3.12 and an isolated environment with the versions in `requirements.txt`. Existing compatible installations can be used without installation. After separately installing dependencies when needed:

```sh
python research/fx-development/render_figures.py
python -m unittest discover -s research/fx-development -p 'test_*.py' -v
```

The renderer reads only the adjacent `aggregates.json`, never private modules, raw histories, forecasts, credentials, a model checkpoint or a network endpoint. SVG and PNG are written to `figures/`; `--output <directory>` selects an independent directory. No private absolute path is required. A browser can open the repository-root `index.html` directly; no server or build is needed.

Byte equality is verified on the reviewed Python/Matplotlib/Pillow/font environment. SVG IDs and metadata are fixed, PNG metadata contain no run timestamp. Cross-platform font/rasterizer differences can change bytes without changing the input numbers; exact aggregate and script hashes are in `PUBLIC_FILE_MANIFEST.json` at the repository root.

## What is reproducible

All six aggregate graphics, the H1/H20 presentation and supplied CSV projections are publicly inspectable. This is figure reproduction, not independent reconstruction of the empirical inference. Underlying snapshots, predictions, model-fitting code, parameter configurations and private reviews are deliberately absent. No publication right to omitted objects is implied.

`CASE_STUDY.md` defines the target, scorers, quarter aggregation, stored uncertainty and limitations. All public prose, labels, comments and captions use English. Values are stored at twelve decimal places; display rounding never selects models or changes the stored uncertainty intervals.

## Source and attribution

Source: European Central Bank, EXR reference rates. The project computed log changes, scaling, forecasts and derived statistics; these are not ECB statistics or an ECB endorsement. See the repository's data/licensing and third-party notices. No Chronos code, weights, Matplotlib/Pillow distribution or font file is bundled.

## Numerical serialization

Public floating-point values use Python binary64 `round(value, 12)` before JSON serialization (nearest rounding, half-even for representable ties). Display tables use six decimal places for MAE/effects; plots use labelled axis precision and coverage percentages as appropriate. Full private measurements were scored before this presentation rounding. Stored bootstrap endpoints are rounded only for export; no bootstrap is recomputed by the public renderer.

## SVG composition

F2 is a self-contained hybrid SVG. Its text and axes are vector elements; eight heatmap panels and the colour bar are embedded as nine inline PNG data URIs. This is not an entirely vector heatmap. The same fixed renderer regenerates those embedded rasters; their presence does not introduce external images or change any measurement. The other SVGs retain their original composition.
