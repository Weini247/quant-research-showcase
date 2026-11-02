# Sources, software and figure attribution

Checked on 2 November 2026. No new rights are asserted on behalf of third parties.

| Component | Role | Rights / distribution boundary |
|---|---|---|
| European Central Bank EXR | Underlying reference-rate source | Accurate attribution and explicit transformation notice under ECB reuse conditions; selected derived aggregates only, no source series or ECB logo |
| Amazon Chronos-2 | Model used in the private measured run | Official fixed model card identifies Apache-2.0; no code, weights or configuration redistributed |
| chronos-forecasting | Official model implementation used privately | Official code licence Apache-2.0; not imported or bundled by the public renderer |
| Matplotlib 3.11.2 | Produces the six original figures | Matplotlib licence is PSF-based/BSD-compatible; dependency, not vendored code |
| Pillow 12.3.0 | PNG backend dependency | MIT-CMU/HPND licence family as documented by Pillow; dependency, not vendored code |
| DejaVu Sans | Matplotlib figure typography | DejaVu/Bitstream Vera terms; no font files embedded in SVG or distributed |
| Browser system fonts and Georgia fallback | Website typography | Uses installed fonts only; no remote font download or redistributed font file |
| Existing synthetic demo, favicon and design | Retained public showcase material | Existing rights position preserved; no new open-source licence invented |

All six diagrams/plots are newly rendered by this project from the selected aggregates or an original conceptual layout. No external illustration, stock image, chart screenshot or third-party logo is copied. SVG retains text and references locally available font families; F2 additionally embeds eight PNG heatmaps and one PNG colour bar as data URIs. Its axes and text remain vector elements. No external image is loaded. PNG figure files rasterize the complete figure. CSS, JavaScript and the public aggregate renderer are newly authored presentation code, not copies of private core implementations.

Official references: [ECB reuse](https://www.ecb.europa.eu/services/using-our-site/disclaimer/html/index.en.html), [Chronos-2 model card](https://huggingface.co/amazon/chronos-2), [Chronos code licence](https://github.com/amazon-science/chronos-forecasting/blob/main/LICENSE), [Matplotlib licence](https://matplotlib.org/stable/project/license.html), [Pillow licence](https://pillow.readthedocs.io/en/stable/about.html#license), [Matplotlib fonts](https://matplotlib.org/stable/users/explain/text/fonts.html).

The case study cites Bracher et al. (2021), Evaluating epidemic forecasts in an interval format, PLOS Computational Biology 17(2): e1008618, [doi:10.1371/journal.pcbi.1008618](https://doi.org/10.1371/journal.pcbi.1008618). Definitions are specified explicitly; no article figure or substantial passage is reproduced.
