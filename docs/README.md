# 📚 Documentation Hub

This hub indexes the current implementation and the supporting research, privacy, and contributor guidance. Start with the [root README](../README.md), then work through setup, architecture, data provenance, feature availability, and evaluation before interpreting notebook results.

## 🧭 Core project guides

| Topic | Document |
|---|---|
| Project overview | [README](../README.md), [notebook walkthrough](notebook-walkthrough.md) |
| Architecture and data flow | [Architecture](architecture.md), [data flow](data-flow.md), [diagrams](diagrams/README.md) |
| Installation and development | [Installation](installation.md), [development](development.md), [support matrix](support-matrix.md) |
| Dataset provenance | [Dataset card](dataset-card.md), [data dictionary](data-dictionary.md), [database and licensing](database.md), [references](references.md) |
| Data quality | [Data quality](data-quality.md), [preparation](data-preparation.md), [privacy](privacy.md) |
| Feature and model | [Feature audit](feature-audit.md), [model card](model-card.md), [methodology](methodology.md), [model governance](model-governance.md) |
| Evaluation | [Evaluation protocol](evaluation-protocol.md), [validation strategy](validation-strategy.md), [metric glossary](metric-glossary.md) |
| Reproducibility | [Reproducibility](reproducibility.md), [experiment tracking](experiment-tracking.md), [research reporting](research-reporting.md) |
| Ethics and safety | [Ethics and governance](ethics-and-governance.md), [ethics checklist](research-ethics-checklist.md), [clinical-use boundary](clinical-use-boundary.md) |
| Sharing and release | [Publication checklist](publication-checklist.md), [release process](release-process.md) |
| Maintenance | [Known issues](known-issues.md), [technical debt](technical-debt.md), [decision log](decision-log.md) |
| Support | [FAQ](faq.md), [troubleshooting](troubleshooting.md), [API status](api.md), [deployment boundary](deployment.md) |
| Accessibility | [Accessibility guide](accessibility.md) |
| Operations | [Runbooks](runbooks/README.md), [templates](templates/README.md) |

## 🧰 Repository utilities

- [Local maintenance scripts](../scripts/README.md)
- [Test suite guide](../tests/README.md)
- [Repository validator](../scripts/validate_project.py)
- [Aggregate dataset schema audit](../scripts/audit_dataset_schema.py), runs locally and must only be used in an approved environment.

## 🎨 Visual assets

- [Project banner](assets/project-banner.svg)
- [Research workflow](assets/research-workflow.svg)
- [Privacy boundary](assets/privacy-boundary.svg)
- [Evaluation gates](assets/evaluation-gates.svg)

## Important boundaries

These documents describe a notebook-based educational analysis. The repository has no supported API, app, database, model-serving service, or clinically validated model. Never publish patient-level records, including saved notebook output. Use synthetic or carefully reviewed aggregate examples in public issues and pull requests.

A documentation page about a possible future capability does not mean that capability is implemented.
