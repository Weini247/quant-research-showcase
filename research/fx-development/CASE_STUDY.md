# Frozen FX development comparison

## Abstract

Five forecasting variants were compared on 98 registered development origins in 2018–2019 across eight ECB FX reference-rate series. H1 was primary and H20 secondary. Small point-loss advantages differed by horizon; all eight model-versus-no-change 95% moving-block intervals included zero. Grouped and ungrouped Chronos-2 produced lower descriptive weighted interval scores than static training quantiles. The latter is a limited, nonadaptive comparator; this does not isolate pretraining benefit. No independent generalization, trading validity or economic benefit is established.

## Scope and estimand

The eight rates are USD, GBP, JPY, CHF, CAD, AUD, SEK and NOK, expressed as currency units per EUR. Let P_i,t be the reference rate on actual common observation day t. Define z_i,t = 10,000 log(P_i,t / P_i,t−1). The horizon-h target is z_i,t+h: one future daily change, not a cumulative h-day return. Training-only scale a_i is mean_train |z_i,t| over 1999–2017. A model forecast is evaluated on its original raw-change scale and divided by a_i for equally weighted comparisons.

Five primary variants are no change, AR(1), AR(20)-Ridge, Chronos-2 grouped and Chronos-2 ungrouped. Preprocessing and model decisions were fixed before this run. No performance-based tuning occurred in this run. Chronos supplies its native median, not an expectation. The wider planned benchmark is incomplete; unexecuted model arms are not represented by substitutes. An auxiliary registered masking diagnostic is outside these five-variant public comparisons.

There are 490 completed primary origin jobs and 784 loss cells per model/horizon. Every origin contributes all eight currencies. The systematic five-observation-day origin grid reduces information relative to daily forecasting. Development observations were already exposed; three origins appeared in an earlier technical pilot.

## Loss and aggregation definitions

Point error e = forecast − target. Scaled absolute loss is |e|/a_i; raw MAE is mean |e| and raw MSE is mean e². The panel comparison first averages all eight jointly eligible currencies within an origin, then averages origins equally. The paired difference is model loss minus no-change loss; negative is lower loss. The grouped ablation is grouped loss minus ungrouped loss.

For quantile τ and value q, pinball loss is (τ − 1{y<q})(y−q). Mean pinball uses the native 0.1,...,0.9 grid. A central (1−α) interval [l,u] has interval score IS_α = (u−l) + (2/α)(l−y)1{y<l} + (2/α)(y−u)1{y>u}. With α in {0.2,0.4,0.6}, WIS = [0.5|y−median| + Σ_α (α/2)IS_α]/3.5. Pinball, WIS and widths are divided by a_i before aggregation. Coverage is mean 1{l≤y≤u}. The static training quantiles use linear empirical interpolation at τ(n−1). No calibration on development observations was performed.

Interval validity requires ordered, nested central intervals containing the median. Invalid interval scores would remain missing and explicitly counted, never repaired or silently selected away. All 784 cells were valid per shown model/horizon. There were zero native crossings in this real-data run; earlier synthetic crossings prevent a universal monotonicity claim. Finite-grid WIS is not exact CRPS.

## Stored uncertainty, not new inference

Figures use the stored 95% percentile endpoints from 2,000 moving-block resamples. The original calculation uses common daily-calendar blocks across models/currencies, retaining the forecast-origin and validity masks. The primary block length is 60 observation days; lengths 20 and 120 are fixed diagnostics, included in the public aggregate file. Sixty calendar observations correspond to approximately twelve sampled forecast origins, not sixty selected rows. Public plotting performs no resampling, p-value calculation, additional hypothesis test or model selection.

Currency dependence, overlapping contexts, systematic sampling, market changes and exposure limit interpretation. Diagnostic intervals are not independent validation or evidence of equivalence. No paired WIS significance claim is made.

## A complete, descriptive temporal landscape

Figure 2 partitions origins into all eight calendar quarters from 2018 Q1 through 2019 Q4. For each model/horizon/currency/quarter it averages the existing paired scaled absolute-loss differences. The figure includes all 512 cells; none is selected for its result. Counts range from 8 to 13 origins per cell, with a partial final quarter. The colour range is shared symmetrically across panels. The SVG combines vector text and axes with eight inline PNG heatmaps and one inline PNG colour bar. These are self-contained raster elements generated from the same aggregates; no external image is loaded. These views are descriptive aggregations, not independently tested subgroup findings. Quarterly values cannot reconstruct individual observations.

## Results and scientific interpretation

H1 scaled MAE is 0.731174 for no change, 0.732169 for AR(1), 0.730850 for Ridge, 0.734064 for grouped Chronos-2 and 0.733566 for ungrouped Chronos-2. H20 values are 0.743374, 0.743202, 0.743609, 0.741595 and 0.742463 respectively. All eight model-versus-no-change intervals and both grouping intervals include zero. Four no-change contrasts concern the primary H1 horizon; four concern the secondary H20 horizon. They are not eight primary tests. Direction and magnitude provide no clear point-forecast or grouping advantage.

H1 scaled WIS is 0.547018 for static quantiles, 0.529591 for grouped Chronos-2 and 0.528659 for ungrouped Chronos-2. H20 values are 0.559040, 0.548394 and 0.547979. Chronos intervals are narrower, and observed 80% coverage is closer to nominal. This is a qualified descriptive result against a static baseline, not proof that pretraining beats simpler adaptive distributional forecasts. Those were not evaluated here.

## Reproduction and engineering evidence

The public figures and tables require only supplied aggregates and the independent renderer. The private study reports independent reconstruction of inputs, statistical fits, losses and interval calculations, plus deterministic rescoring. Those checks are not publicly rerun here and do not establish a new scientific sample. One integrated synthetic interruption/resume check was conducted after the real run; it should not be described as a completed pre-inference integration prerequisite.

Figure 5 uses measured full-component fit-plus-run walltime and sampled worker RSS, not estimates. Loading, I/O and scheduling affect elapsed time. The host was shared, execution serial and CPU-based; the chart is not an exclusive hardware benchmark. CPU accounting reserves, auxiliary runs and verification costs are outside this five-variant figure.

## Limitations and disclosure

Latest-vintage data are not historical release vintages; actual historical availability is not certified. Foundation-model training overlap is unknown. Rates share a common EUR denominator and market history. No executable prices, implementation costs, portfolio results or trading validation are supplied. The later reserved transfer period was not evaluated. The formal P1 diagnostic is not activated.

Source: European Central Bank. All transformations and derived results are project calculations; no ECB or model-provider endorsement is implied. No EODHD-derived case study, results or figures are included in this release. No private research report, implementation, forecast series, parameter configuration or review is distributed. Development and presentation used AI assistance; scientific and publication responsibility remains with the human owner.

## Figure captions
**Figure 1. Point forecasts against no change.** Paired mean differences in scaled absolute loss; negative values favour the model. H1 is primary; H20 is secondary. Stored 95% percentile intervals use 60-observation-day moving blocks with the original sampling mask and common indices across currencies. Each comparison includes 98 origins and eight currencies. All eight intervals include zero: four H1 contrasts at the primary horizon and four H20 contrasts at the secondary horizon.

**Figure 2. A complete failure landscape.** Mean paired scaled absolute-loss differences, partitioned by forecast-origin calendar quarter. Every quarter from 2018 Q1 through 2019 Q4, all eight currencies and all four nonzero models are included. Cell counts are shown; 2019 Q4 is partial. A single symmetric colour scale is shared by every panel. This is descriptive aggregation, not subgroup testing. The SVG is hybrid, with eight inline PNG heatmaps and one inline PNG colour bar beneath vector text and axes.

**Figure 3. Distribution quality against a limited reference.** Scaled weighted interval score (WIS), observed coverage and scaled width for nominal 40%, 60% and 80% central intervals. There are 784 valid cells per model and horizon. Static training quantiles are an unconditional, nonadaptive comparator. Native quantiles are unmodified. No paired WIS significance claim is made; public tables include the stored coverage and width intervals.

**Figure 4. Cross-asset grouping.** Grouped minus ungrouped Chronos-2 scaled absolute loss, using identical origins, checkpoint, transformations and inputs. Both stored 60-day-block uncertainty intervals include zero. Grouping is not consistently advantageous in this development sample. Marginal forecast quantiles do not specify a joint cross-asset distribution.

**Figure 5. The measured cost of complexity.** Complete fit-plus-run component walltime, sampled worker peak RSS and completed origin jobs for the five primary variants. All completed 98 jobs without failures. Measurements include model loading and I/O; the host was not exclusive. CPU budget reservations and estimated quantities are not plotted as measured CPU time. Auxiliary and verification costs are outside this five-variant chart.

**Figure 6. From provenance to a bounded claim.** An original conceptual rendering of the privately audited evidence chain. Public reproduction begins at curated aggregates and regenerates charts; it cannot verify private source bytes, refit models or recreate forecasts. Repeated scoring of frozen predictions is not a new test sample or independent empirical validation.

## References

See the [case-study bibliography](../../fx-development.html#reproduction), [data notice](../../docs/DATA_LICENSING.md) and [third-party notices](../../docs/THIRD_PARTY_NOTICES.md).
