# Notebook walkthrough

## Before opening
Read the [medical safety notice](clinical-use-boundary.md), [installation guide](installation.md), and [dataset card](dataset-card.md). Use only an approved local environment.

## Notebook sections
The committed notebook is the source of truth for the exact cell order. At a high level it:
1. Imports Python data and plotting libraries.
2. Loads the CSV using the relative path `data.csv`.
3. Inspects sample rows, shape, missing values, duplicates, and columns.
4. Selects a group of demographic, screening, and diagnosis-related variables.
5. Uses `Dx:Cancer` as the target.
6. Creates one train/test split.
7. Fits Random Forest, SVC, and Logistic Regression.
8. Displays selected metrics and a model-accuracy plot.

## Important execution detail
The tracked data file is `DATA _SET (1).csv`, but the notebook asks for `data.csv`. Follow the local-copy workaround in the root README until the notebook path is corrected.

## How to read outputs
Treat them as exploratory outputs from one run. The split is unseeded, missing-marker handling is incomplete, and feature leakage is possible. Saved outputs can be stale or data-derived. Do not use a metric from this notebook as evidence of individual-level medical risk.

## Suggested study questions
- How many question-mark missing markers exist in each field?
- Does the target class distribution make accuracy misleading?
- Which features are genuinely available before a proposed prediction moment?
- How do stratified and unstratified splits differ on synthetic data?
- How should scaling be fitted inside a training pipeline?

Use synthetic data for demonstrations and public questions.
