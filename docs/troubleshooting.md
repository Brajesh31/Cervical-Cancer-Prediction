# Troubleshooting

This guide covers the repository as it currently exists: one Jupyter notebook and a CSV data file. It does not describe a deployed application, API, database, or clinical system because none is included in the repository.

## The notebook cannot find the data file

The notebook refers to `data.csv`, while the tracked file is named `DATA _SET (1).csv`. From the repository root, either copy the dataset into a private local file named `data.csv`, or update the notebook's read path to the actual filename. Keep any private or locally renamed data file out of commits. See [installation](installation.md) for setup details.

## A Python package cannot be imported

Install the dependencies into the Python environment used by the notebook kernel. From the repository root, run `python -m pip install -r requirements.txt`, then select or restart a Jupyter kernel that uses that same interpreter. If the import still fails, compare `python -c "import sys; print(sys.executable)"` in the shell with the interpreter shown by the notebook kernel.

## A model rejects the data or reports strings where numbers are expected

The dataset uses `?` as a missing-value marker. The notebook has a replacement step commented out, while later `dropna()` calls remove null values, not necessarily the literal string `?`. Convert the marker to a proper missing value before filtering or imputing, and inspect column types after loading. Keep preprocessing fitted only on training data when evaluating a model.

## A train/test split or metric fails for a class

The notebook uses a random split without a fixed seed or stratification. A small class can be absent from one split, which can make class-specific metrics fail or become misleading. Inspect class counts first; use a reproducible, stratified split when class sizes permit, and specify the expected label set in reports. Explain any exclusions rather than silently changing the evaluation population.

## Results change between notebook runs

The split and estimators do not consistently set random seeds, so variation is expected. Record the dataset version, preprocessing choices, split seed, estimator settings, and library versions for each comparison. A stable number is not evidence that the model is valid or suitable for health decisions.

## SVC or logistic regression warns about convergence

These estimators are sensitive to feature scale. The current notebook does not put scaling into a fitted pipeline. For an exploratory comparison, use a scikit-learn pipeline that fits the scaler on training data only, then compare results on an untouched holdout set. Do not use the holdout set repeatedly to tune preprocessing or parameters.

## Notebook outputs look stale or show unexpected variables

Jupyter retains kernel state, and saved outputs can come from an earlier dataset or code version. Restart the kernel and run cells in order. Review outputs before sharing: they may contain rows or summaries of sensitive reproductive-health data. Clear outputs from a copy intended for publication when they are not needed.

## The notebook seems to predict a diagnosis from other diagnosis fields

The target is `Dx:Cancer`, and the feature list includes other diagnosis-related fields, including `Dx:HPV`, `Dx:CIN`, and biopsy-related variables. Their timing and availability are not established. This creates a serious risk of target leakage and means the notebook does not establish early prediction. Do not describe its metrics as evidence of screening or diagnosis performance.

## Security or privacy concern

Do not commit identifiable or sensitive health records, credentials, or private copies of datasets. For a suspected vulnerability, follow [SECURITY.md](../SECURITY.md) and avoid publishing sensitive details in a public issue. This repository is not approved for handling patient records.

## Check the documented project boundaries

The [architecture guide](architecture.md), [API guide](api.md), and [database guide](database.md) describe the repository's current scope. There is no prediction service, API, database, or deployment configuration to troubleshoot.

## Check the working directory and launch location

Run Jupyter from the repository root so relative paths resolve predictably. If you launch the notebook from another directory, either return to the root or change the data path explicitly. Avoid keeping multiple copies of the CSV with ambiguous names.

## Confirm the notebook's actual columns

Before changing the feature list, compare the loaded column names with the CSV header and check for whitespace, spelling, or encoding differences. A `KeyError` often means a column name does not match exactly. Keep the target column separate from the input columns and document every feature removed or transformed.

## Resolve inconsistent or missing-value handling

Inspect missing values both before and after replacing the literal `?` marker. Decide whether rows or columns are excluded or whether an imputation method is appropriate, and report that decision. Do not calculate preprocessing values across the full dataset before splitting; that can leak information from the evaluation set.
