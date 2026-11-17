# Decision log

This log records explicit repository decisions and their rationale. Add a new dated entry rather than silently rewriting historical decisions.

## 2026-11-17: Keep the project notebook-based
**Decision:** Document the current system as an exploratory Jupyter notebook, not as an application or API.

**Rationale:** The repository contains a notebook, CSV, and dependencies. It does not contain a serving application, database, trained model artifact, or supported inference endpoint.

**Consequence:** API, database, and deployment guides explain these boundaries and future requirements rather than inventing current capabilities.

## 2026-11-17: Do not claim early prediction
**Decision:** Describe the analysis as retrospective educational classification unless a valid prospective design is established.

**Rationale:** The target is `Dx:Cancer`, while selected predictors include screening and diagnosis fields. Feature availability timing is not documented.

**Consequence:** Feature leakage is prominently documented. Any future feature set must include a timing audit.

## 2026-11-17: Preserve a visible medical safety boundary
**Decision:** State that the project is not a diagnostic or screening tool.

**Rationale:** The current notebook is not clinically validated, and its evaluation design has material limitations.

**Consequence:** Public project documentation must not suggest individual use or clinical readiness.

## 2026-11-17: Keep patient-level values out of contribution workflows
**Decision:** Require synthetic or aggregate examples in issues and pull requests.

**Rationale:** The CSV and saved notebook outputs contain sensitive health-related information.

**Consequence:** Issue and PR templates include explicit privacy checks.

## Adding a decision
Include date, context, decision, alternatives considered, consequences, and a link to relevant evidence. Do not record patient-level information.
