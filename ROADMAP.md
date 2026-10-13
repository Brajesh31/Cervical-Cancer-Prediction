# Roadmap

This roadmap describes possible improvements for the exploratory notebook. It
is not a release schedule or promise. Priorities may change after review of
data provenance, privacy, and project scope.

## Project direction

Keep the repository educational and reproducible. Correct data handling and
honest evaluation should come before adding models or presenting results as
clinical prediction.

## Near-term priorities

1. Fix the notebook's data path or document a reliable local-copy workflow.
2. Record the dataset source, transformation history, attribution, and
   applicable license.
3. Replace question-mark sentinels explicitly before missing-value analysis.
4. Define a prediction question and feature availability time; review possible
   target leakage from diagnosis and screening fields.
5. Make the split reproducible and use stratification where justified.
6. Report class counts and metrics beyond accuracy.

## Medium-term priorities

- Add a documented environment lock or dependency constraints.
- Separate preprocessing from estimation in a reproducible pipeline.
- Add tests for data parsing, missing-value handling, and evaluation logic.
- Clear unnecessary row-level notebook outputs and review generated figures.
- Document model-selection choices and uncertainty.

## Longer-term considerations

- Evaluate whether a prospective clinical prediction task is scientifically
  justified before changing the target or feature set.
- Seek independent, appropriately governed data for external validation only
  with the required authorization and privacy review.
- Consider fairness, calibration, subgroup performance, and clinical utility
  only within a qualified research and governance process.
- Keep deployment out of scope unless the project purpose and safety controls
  are formally changed.

## Out of scope

This repository is not intended to diagnose, screen, treat, triage, or make
individual care decisions. A future notebook improvement would not by itself
make the model clinically suitable.
## Data path completion criteria

The notebook should load the tracked dataset path reliably, without creating
an untracked duplicate as a hidden prerequisite. The expected filename and
repository-relative location should be exercised in a clean environment.
## Missingness completion criteria

Convert documented sentinel values to missing values before counting or
dropping them. Record row counts after each cleaning step and explain whether
missingness may bias the retained sample.
## Prediction-time criteria

For each predictor, identify when it would be known relative to the target.
Remove post-diagnosis or confirmatory test variables if the stated task is
early risk prediction, and justify any remaining feature.
## Evaluation completion criteria

Use a fixed and documented split, preserve class proportions where
appropriate, and report uncertainty. Compare with a transparent baseline and
avoid selecting and evaluating a model on the same holdout.
