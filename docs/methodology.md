# Methodology and analysis workflow

## Current implementation
The notebook performs exploratory tabular classification. It reads a CSV, inspects data, selects a subset of fields, creates one train/test split, fits three classifiers, prints selected metrics, and plots an accuracy comparison.

## Notebook stages
1. Load the dataset into pandas.
2. Inspect dimensions, types, missing values, duplicates, and selected columns.
3. Select a feature matrix and `Dx:Cancer` target.
4. Split data into training and test sets.
5. Fit Random Forest, SVC, and Logistic Regression.
6. Produce predictions and selected evaluation output.

This sequence summarizes the checked-in notebook and does not endorse the correctness of its current preprocessing or feature set.

## Issues to resolve
- The notebook reads `data.csv`, but the tracked CSV is named `DATA _SET (1).csv`.
- Question-mark replacement is commented out before missing-value removal.
- The selected features include diagnosis/screening fields that may leak the target.
- The prediction moment and intended population are not defined.
- The split is not fixed by a seed or stratified.
- There is no documented tuning strategy or independent validation.
- Accuracy and mean squared error do not sufficiently describe class-imbalanced screening-related tasks.

## Recommended future protocol
Define a precise research question and prediction time. Verify source data provenance. Audit feature availability. Parse missing-value sentinels explicitly. Use a leakage-safe pipeline with preprocessing fitted within training folds. Record seeds and package versions. Report class-aware metrics and uncertainty. Keep the final test set untouched until evaluation. Seek external validation before making broader claims.

## Interpretation boundary
This is an educational historical-data analysis. Do not describe it as an early-detection model, clinical risk predictor, or diagnostic instrument.
