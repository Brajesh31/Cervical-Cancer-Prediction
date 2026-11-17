# Runbook: review a research change

## Intake
- Identify research question and affected notebook cells.
- Confirm dataset source, license, and transformations.
- Ensure public examples contain no patient records.
- Identify changes to target, features, preprocessing, split, or metrics.

## Technical review
- Inspect notebook diff and embedded outputs.
- Verify missing-value handling and aggregate counts.
- Verify feature availability at the prediction time.
- Review leakage and duplicate information.
- Confirm preprocessing is fitted inside training folds.
- Review class balance, metrics, and uncertainty.
- Record seeds, versions, and commit SHA.

## Decision
Execution success is not model validation. Request changes if assumptions are undocumented, attribution is absent, sensitive output is exposed, or medical claims exceed evidence.

## Merge notes
Record changes, checks actually performed, unresolved limitations, and whether the notebook was executed. Do not imply clinical approval.
