# Validation strategy

## Current validation status
The repository contains a single exploratory notebook and no established validation pipeline. It does not provide independent external validation, temporal validation, calibration, prospective evaluation, or clinical utility analysis.

## Research-grade validation plan
1. Define population, target, intended timepoint, and use case.
2. Confirm dataset provenance, permission, and cohort construction.
3. Audit data quality, missingness, duplicates, and label coding.
4. Audit all features for availability and target leakage.
5. Separate development, tuning, and final evaluation data.
6. Use stratified splits or grouped/temporal splits where the study design requires them.
7. Keep preprocessing and feature selection inside training folds.
8. Compare with simple, transparent baselines.
9. Report class-aware metrics, uncertainty, and calibration.
10. Perform external or temporal validation on an appropriate independent cohort.
11. Assess subgroup performance and uncertainty.
12. Obtain expert and ethics review before making any clinical claim.

## Data leakage checks
Check for target aliases, diagnosis codes, post-outcome procedures, repeated people across partitions, duplicate rows, and transformations performed before the split.

## Validation is not deployment approval
Even a robust retrospective validation does not establish clinical safety, regulatory status, or fitness for patient care. This repository does not support clinical use.
