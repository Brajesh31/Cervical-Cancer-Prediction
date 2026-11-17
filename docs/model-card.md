# Model Card: current notebook estimators

## Status
This is a description of estimators used in an educational notebook, not a model release, validated model card, or approval for deployment. No trained model artifact or supported inference interface is committed.

## Models present in the notebook
- Random Forest classifier.
- Support Vector Classifier (SVC).
- Logistic Regression.

The notebook trains these estimators during an exploratory run and compares selected metrics. This repository does not version their fitted parameters, training environment, or a stable preprocessing pipeline.

## Intended use
Educational demonstration of a basic tabular classification workflow. Do not use for individual diagnosis, screening, triage, treatment, reassurance, or clinical decision-making.

## Data and target
The notebook uses `Dx:Cancer` as the target. Candidate predictors include screening and diagnosis fields. Prediction timing is not defined, and some predictors may be unavailable until diagnosis or a clinical procedure has occurred.

## Evaluation limitations
- One unseeded, non-stratified train/test split.
- Incomplete missing-value sentinel handling.
- Potential target leakage.
- No nested or repeated cross-validation.
- No external validation.
- No calibration or clinically justified threshold.
- No confidence intervals or clinical utility assessment.
- Accuracy is emphasized despite the need for class-aware metrics.

## Performance
No performance number in a saved notebook output should be treated as a stable or clinically validated estimate. Reruns can differ. Review the [evaluation protocol](evaluation-protocol.md) before interpreting any result.

## Fairness and representativeness
The repository does not provide an adequate subgroup fairness assessment, dataset representativeness analysis, or evidence that the cohort reflects a current target population.

## Deployment
There is no supported serving code, API, monitoring, model registry, or clinical workflow. The model must not be deployed for patient-facing decisions.

## Required evidence before any expanded claim
Define a prospective research question, audit feature timing and leakage, establish data provenance and governance, use a reproducible validation design, report class-aware metrics with uncertainty, validate independently, and obtain relevant clinical, ethics, privacy, and regulatory review.

A technically correct training run does not satisfy these requirements.
