# Reproducibility boundaries

Release 2.1 includes an independent aggregate figure renderer, the supplied aggregate file and an unchanged fictional accounting example. See the [FX reproduction instructions](../research/fx-development/README.md).

All six figures can be regenerated without private modules, private inputs, credentials, a model checkpoint or a research-data download. Byte equality is verified in the specified renderer/dependency environment; cross-platform font/rasterizer differences may change graphic bytes. The public manifest verifies the exact release file set and hashes, excluding itself to avoid self-reference.

Public figure reproduction does not verify original source observations, fitting, inference, private numerical cross-checks or independent validation. No entitlement to omitted objects is implied. Deterministic rescoring is not a new sample. These development observations must not be relabelled as an untouched holdout.

F2 uses nine inline PNG elements (eight heatmaps and one colour bar) inside an SVG with vector text and axes. It has no external image dependency. Other figure composition, all numerical aggregates and all twelve figure bytes remain unchanged from the reviewed V2 figures.
