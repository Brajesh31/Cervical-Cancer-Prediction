# Development

## Project structure

The repository is a notebook analysis, not a Python package. The main source
is cervical-cancer-risk-data.ipynb; the data file is DATA _SET (1).csv.
Notebook execution currently expects a local data.csv copy in the root.
README.md and the other docs describe the workflow and its limits.

## Set up a development environment

Follow docs/installation.md to create a virtual environment, install
requirements.txt, prepare the expected local data filename, and open the
notebook from the repository root. The dependency versions and Python runtime
are not pinned.

## Current checks

There is no automated test suite, lint configuration, notebook execution
workflow, or continuous integration in the repository. No test command is
defined. Running all notebook cells may produce outputs derived from
patient-level health records, so only execute them in an environment approved
to handle that data.

## Focused development workflow

1. Identify the affected notebook cell, data-loading behavior, or guide.
2. Define the expected behavior with synthetic or aggregate examples.
3. Make one focused change and preserve source data attribution.
4. Inspect notebook JSON and outputs before staging.
5. Review missing-value handling, feature timing, split strategy, and metrics.
6. Record the Python and package versions and checks actually performed.
7. Update README.md and affected docs when behavior changes.

## Analysis quality

Document the prediction target and the time at which each feature would be
available. The current feature set includes diagnosis/screening fields beside
Dx:Cancer, so a prospective early-prediction claim is not established. Keep
preprocessing inside training folds and separate model selection from final
evaluation.

## Data and privacy

Treat the CSV and saved notebook output as patient-level health information.
Do not copy rows into issues, commit additional data, or upload records to
unreviewed services. Preserve CC BY 4.0 attribution if reusing material
derived from the likely UCI source dataset.
## Fixing the file path

The notebook asks for data.csv, while the tracked file has another name.
A robust code fix should use an explicit repository-relative path or provide a
clear data configuration, then work from a clean checkout without an
untracked duplicate.
