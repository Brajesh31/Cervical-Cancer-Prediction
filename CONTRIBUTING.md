# Contributing

Thank you for considering a contribution. This repository contains an
exploratory notebook using patient-level health data, so changes need careful
attention to data attribution, privacy, reproducibility, and medical claims.

## Before proposing a change

- Read README.md, LICENSE, and the relevant guide in docs/.
- Keep the UCI dataset attribution and applicable CC BY 4.0 terms with
  dataset-derived material.
- Use synthetic examples in issues, screenshots, and pull requests.
- Do not add identifiable, confidential, or newly collected health data.
- Do not claim that the notebook diagnoses cancer or predicts clinical risk.
- Open an issue first for large changes to the data, target, or analysis.

## Development setup

Use an isolated Python environment and install the packages in
requirements.txt. The notebook expects data.csv in the repository root, but
the tracked CSV is named DATA _SET (1).csv. Make a local copy with the
expected name; .gitignore excludes that working copy.

A local copy can be created in PowerShell with:

    Copy-Item "DATA _SET (1).csv" data.csv

Then open cervical-cancer-risk-data.ipynb in Jupyter. Do not commit the
temporary duplicate or generated outputs without reviewing their contents.

## Good contributions

- Fix the dataset path and document the corrected workflow.
- Handle question-mark missing-value markers before dropping incomplete rows.
- Make the split reproducible and stratified where appropriate.
- Evaluate class imbalance and report metrics with uncertainty.
- Audit whether predictors are available at the intended prediction time.
- Add appropriate tests and explain their limits.
- Improve documentation, accessibility, and dependency reproducibility.

## Analysis and review

For data or model changes, state the target, prediction time, feature set,
split strategy, preprocessing, metrics, and limitations. Keep training and
evaluation separate. Do not use the same records to select and evaluate a
model without explaining the resulting optimistic bias.

Before submitting:

1. Review the diff for patient-level rows and notebook outputs.
2. Confirm that attribution is preserved for source data and derivatives.
3. Describe the expected and observed behavior.
4. List the environment and checks actually used.
5. State clearly if the notebook could not be executed.

There is no automated test suite or model validation pipeline in this
repository today. A successful notebook run does not establish clinical
validity or safety.
## Dataset changes

Do not replace or augment the committed data without documenting its source,
license, transformation history, missingness, and permission for
redistribution. Preserve the dataset's CC BY 4.0 attribution if it is derived
from the UCI record.
