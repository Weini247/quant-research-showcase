# Research Roadmap · October 2026

> All statuses are **project-specific**, not measures of algorithmic profitability. Design completion does not establish empirical success.

| Phase | Status | Exit evidence |
|---|---|---|
| **01. Research foundation** | Design documented | Working research architecture, falsification and experiment principles |
| **02. First pilot design** | **Conditionally specified** | Bounded AAPL/MSFT 2020 measurement contract with identified activation gaps |
| **03. Data & accounting core** | **Next / not yet implemented** | Offline correctness tests, scoped ingestion and authorized measurement pilot |
| **04. ENNEAD research workbench** | Planned | GUI can configure and inspect standalone research runs |
| **05. ML experimentation** | Planned | Simple reproducible baselines, then justified complexity increases |
| **06. Strategy research** | Planned | Predefined claims, candidate identification, baselines, portfolio policies |
| **07. Scientific validation** | Planned | Out-of-sample and net-cost analysis with search governance |
| **08. Paper operation** | Conditional | Monitoring, paper execution, operational reliability |
| **Northstar** | Long-term vision | Evolvable and independently reproducible quantitative research capability |

### Current constraints

- **P1 not activated**: data rights/access, historical closing-price and instrument semantics, retention/replay rules and explicit execution authorization remain open.
- **No real-data experiment** has been run under this project.
- **No ML model** has been trained or evaluated for trading.
- **No profitability claim** exists.
- The public synthetic demonstrator is an independent minimal example, not the implementation of the contracted pilot.

### Milestone update rule

Move a phase from *planned* to *implemented* only after code and an executable demonstration exist. Move from *implemented* to *validated* only after applicable tests and checks have actually run. Keep the research claims separate from engineering readiness.

### Why this sequence?

It distinguishes three fundamentally different questions: (1) does the data and accounting work, (2) do models predict anything on unseen data, and (3) is any prediction economically useful under real-world constraints? Each question has different evidence requirements.
