# Changelog

There are no tagged releases yet. Record changes under Unreleased until a
release is actually published; do not invent release dates or versions.

## Unreleased

### Added

- Added project and maintainer documentation for setup, contribution,
  security, support, roadmap, deployment, data handling, and troubleshooting.
- Added an MIT license scoped to original project code and documentation.
- Documented the separate attribution and CC BY 4.0 terms associated with the
  likely UCI-derived dataset.
- Added a dependency manifest for the packages imported by the notebook.

### Clarified

- The notebook compares Random Forest, SVC, and Logistic Regression on one
  train/test split; it is not a clinical prediction service.
- The notebook expects data.csv, but the tracked CSV uses another filename.
- The data file appears structurally consistent with the UCI Cervical Cancer
  (Risk Factors) dataset; exact local provenance is not documented.
- Missing-marker handling, split reproducibility, feature timing, and possible
  target leakage need review before interpreting the metrics.

### Safety

- Added explicit warnings against using notebook outputs for diagnosis,
  screening, treatment, or individual clinical decisions.
### Data provenance record

The UCI dataset record identifies 858 instances and 36 features and lists
CC BY 4.0. The local CSV has the same dimensions, but its exact transformation
history is not recorded. The documentation preserves this distinction.
### Notebook output warning

The notebook contains saved table previews and row-level values. The
documentation asks maintainers to inspect or clear unnecessary outputs before
sharing a derivative copy.
### Evaluation caveats

The split has no random seed or stratification. The notebook does not provide
external validation, calibration, fairness assessment, or a clinical
operating threshold. Metric displays are exploratory only.
