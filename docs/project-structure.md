# Project structure and file guide

This repository is a notebook-based analysis, not a packaged application. The tree below describes the purpose of the important tracked files and folders.

## Root files

| Path | Purpose |
|---|---|
| `README.md` | Project overview, medical safety statement, setup, limitations, and navigation |
| `cervical-cancer-risk-data.ipynb` | Primary exploratory analysis notebook |
| `DATA _SET (1).csv` | Tracked patient-level dataset copy; handle as sensitive data |
| `requirements.txt` | Runtime dependencies used by the notebook |
| `requirements-dev.txt` | Optional test and lint tools |
| `pyproject.toml` | pytest and Ruff configuration |
| `Makefile` | Convenience commands for setup, validation, tests, and local schema audit |
| `LICENSE` | MIT notice for original project work plus separate dataset license notes |
| `CITATION.cff` | Citation metadata for the software repository |
| `ACKNOWLEDGMENTS.md` | Dataset and dependency attribution notes |
| `GOVERNANCE.md` | Project decisions, review responsibilities, and contribution boundaries |
| `CONTRIBUTING.md` | Contributor setup and review requirements |
| `CODE_OF_CONDUCT.md` | Expected behavior and reporting |
| `SECURITY.md` | Private vulnerability reporting and safe handling |
| `SUPPORT.md` | Technical help and support boundaries |
| `CHANGELOG.md` | Verified changes grouped by release status |
| `ROADMAP.md` | Possible future work, not a delivery promise |
| `CODEOWNERS` | Default ownership and review routing |
| `.editorconfig` | Consistent editor behavior |
| `.gitattributes` | Text and line-ending normalization |
| `.gitignore` | Excludes virtual environments, local data copies, caches, and generated artifacts |
| `.env.example` | Existing environment example; the current notebook does not require an application API |

## GitHub automation

| Path | Purpose |
|---|---|
| `.github/workflows/quality-checks.yml` | Linting, tests, notebook JSON, YAML, and repository validation |
| `.github/workflows/update-readme.yml` | Existing README timestamp automation |
| `.github/dependabot.yml` | Monthly dependency and GitHub Actions update proposals |
| `.github/ISSUE_TEMPLATE/` | Bug, feature, dataset, documentation, research, and model-evaluation issue forms |
| `.github/DISCUSSION_TEMPLATE/` | Question and idea discussion forms |
| `.github/pull_request_template.md` | Contribution and safety review checklist |

## Documentation

The `docs/` folder contains architecture, setup, notebook walkthrough, dataset/model cards, data dictionary, quality, methodology, feature audit, evaluation, validation, metric definitions, privacy, ethics, governance, reporting, release, troubleshooting, and support guidance.

- `docs/assets/`: accessible SVG illustrations.
- `docs/diagrams/`: editable Mermaid source diagrams.
- `docs/runbooks/`: operational procedures.
- `docs/templates/`: reusable research and review documents.

## Scripts and tests

- `scripts/validate_project.py`: checks documentation paths, local links, and notebook JSON without reading the CSV.
- `scripts/audit_dataset_schema.py`: locally inspects aggregate CSV shape and required headers without printing data rows.
- `tests/test_repository_contract.py`: verifies project files, notebook JSON, README safety language, and local links.
- `tests/test_dataset_audit.py`: tests CSV schema-audit behavior using synthetic temporary files.

## What is deliberately absent

There is no web application, backend, REST API, database, authentication, saved trained model, model registry, hosted inference service, or clinical deployment. Documentation about these boundaries must not be interpreted as evidence that such features exist.
