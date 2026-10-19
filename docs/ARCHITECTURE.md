# Architecture · Public Overview

The goal is to separate the *research computation* from the *research user interface*.

```mermaid
flowchart TB
    user[Researcher] --> ui[ENNEAD Research Workbench\nplanned GUI integration]
    ui --> controller[Experiment & Artifact Interface\nplanned]
    controller --> py[Standalone Python Quant Core\nplanned]
    py --> measure[Measurement & Data Validation]
    py --> accounting[Accounting & Cost Checks]
    py --> models[Statistical / ML Models]
    py --> validation[Research Validation]
    measure --> store[(Permitted data & run artifacts)]
    accounting --> store
    models --> store
    validation --> store
```

This is **target architecture, not a diagram of shipped software**.

## Architectural principles

- **Independence:** numerical code should run, test and reproduce without the graphical application.
- **Explicit evidence:** data provenance, experiment configuration and evaluation boundaries must be inspectable.
- **Proportional complexity:** avoid building production/live infrastructure for a measurement pilot.
- **Modular trust boundary:** confidential datasets, internal hypotheses, keys and potentially proprietary models are never imported into this public repository.
- **Stage discipline:** exploratory diagnostics are not confirmatory evidence of economic value.

## ENNEAD relationship

ENNEAD is envisioned as a wider personal research/workspace environment. The trading integration is **planned**; the private ENNEAD application's complete code is not part of this showcase. The public site may eventually feature real sanitized screenshots when the corresponding features exist.
