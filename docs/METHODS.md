# Methods: FX development evidence

The [research note](../research/fx-development/CASE_STUDY.md) gives the exact target, training-only scales, loss formulas, aggregation and uncertainty definitions. The target is a single future daily log change in ECB reference rates; H20 is not a cumulative return.

The benchmark comprises no change, AR(1), AR(20)-Ridge and grouped/ungrouped Chronos-2. H1 is the primary horizon and H20 secondary. Four model-versus-no-change contrasts are shown per horizon. The eight displayed contrasts are not eight primary tests. Stored paired intervals and fixed block-length diagnostics are reported; the public renderer performs no resampling or additional hypothesis test.

WIS uses the specified finite quantile grid, not exact CRPS. Static training quantiles are a nonadaptive comparator and do not isolate pretraining benefit. Ordered intervals alone do not establish calibration. Forecast losses are not investment utility or trading returns.

Development exposure, common EUR/market dependence, latest-vintage inputs and unknown pretraining overlap limit interpretation. Public aggregate figure reproduction is narrower than empirical replication. No later reserved transfer data were evaluated by this release.
