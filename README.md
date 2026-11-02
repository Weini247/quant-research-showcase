# Quant Research Lab

**Evidence before advantage.** Release 2.1 presents a measured FX development comparison, its limitations and a bounded public reproduction path.

[Research website](index.html) · [FX development study](fx-development.html) · [Research note](research/fx-development/CASE_STUDY.md) · [Reproduction](research/fx-development/README.md) · [Data rights](docs/DATA_LICENSING.md)

Five benchmark variants were evaluated at 98 registered 2018–2019 development origins across eight ECB FX reference-rate series. H1 is the primary horizon; H20 is secondary. All eight model-versus-no-change block intervals include zero: four at H1 and four at H20. They are not eight primary tests. No clear point-forecast improvement or consistent grouping advantage is established. Chronos-2 has a descriptive WIS advantage against static training quantiles, a limited nonadaptive comparator.

This is development evidence, not independent validation, economic benefit, alpha or profitability. No new experiments are performed by this public package. P1 remains not activated. No qualitative or quantitative EODHD-derived case study, results or empirical figures are included.

## Explore and reproduce

Open `index.html` directly. The static website uses local assets and system fonts, with no tracking or live data connection. Six original figures, numerical tables, an H1/H20 comparison, methods and references are included. All public research prose and labels use English.

```sh
python verify_public_manifest.py
python research/fx-development/render_figures.py
python -m unittest discover -s research/fx-development -p 'test_*.py' -v
python examples/synthetic_accounting/demo.py
python -m unittest discover -s examples/synthetic_accounting -p 'test_*.py' -v
```

The renderer uses the documented dependencies and the supplied aggregates only. The unchanged fictional accounting demo needs only Python's standard library. Public figure reproduction does not reconstruct private inference or certify independent empirical replication. F2 is a hybrid SVG with inline raster heatmaps and a raster colour bar, alongside vector text and axes.

## Disclosure and rights

Source: European Central Bank. Log transformations, scaling, forecasts and derived statistics are project calculations; no ECB endorsement is implied. No raw history, individual measurement, forecast series, fitted weight, private configuration, private Git history or internal review is distributed. No new open-source licence is assigned. Existing software rights and third-party notices remain separate from data reuse conditions.

AI assistance is disclosed; scientific responsibility remains human. An adaptive research capability is a long-term aspiration, not a delivered trading system. See [verification](docs/VERIFICATION.md), [publishing](docs/PUBLISHING.md), [disclosure](docs/PUBLIC_DISCLOSURE.md) and [third-party notices](docs/THIRD_PARTY_NOTICES.md).
