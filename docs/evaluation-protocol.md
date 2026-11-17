# Model evaluation protocol

This is a proposed protocol, not a claim that the current notebook meets it or that a clinically validated model exists.

## 1. Define the question
Specify the population, intended research use, outcome, prediction horizon, and moment at which a prediction would be made. Retrospective classification is not automatically prospective risk prediction.

## 2. Audit leakage
Create a feature-availability table. Exclude diagnosis, procedure, and post-outcome information unavailable at the proposed decision point. Review proxy features and target-derived fields.

## 3. Inspect data
Report aggregate class counts, encoding, missingness, and duplicates. Do not publish row-level values.

## 4. Split before preprocessing
Use a defensible holdout or cross-validation plan, stratified where appropriate. Record seeds. Fit imputation, scaling, selection, and other preprocessing inside training folds only. Avoid repeated tuning against the final test set.

## 5. Use pipelines
For scale-sensitive models, use scikit-learn Pipeline and fit scaling only on training data. Document each transformation and its rationale.

## 6. Report appropriate metrics
Consider confusion matrix, sensitivity, specificity, precision, recall, ROC-AUC, precision-recall analysis, calibration, confidence intervals, and threshold rationale. Explain the positive class and prevalence context. Accuracy and mean squared error alone are not enough for a screening-related research question.

## 7. Validate independently
A single holdout from one dataset is limited evidence. External validation, subgroup review, and data-quality assessment may be necessary. Do not imply clinical utility without appropriately designed studies and expert review.

## 8. Document fairness and uncertainty
Describe dataset representation, measurement limitations, missingness, and subgroup uncertainty. Do not draw causal conclusions from predictive associations.

## 9. Record reproducibility
Record source provenance, environment versions, commit SHA, preprocessing, features, split, model configuration, and aggregate results. Do not include patient records.

## 10. Release boundary
This repository does not support individual-facing or clinical use. Any such proposal requires independent clinical, ethical, privacy, governance, and regulatory review. Passing software tests or obtaining a high metric does not satisfy that requirement.
