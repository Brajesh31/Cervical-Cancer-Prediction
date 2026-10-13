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
