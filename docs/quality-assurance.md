# Quality assurance and CI boundaries

## Automated checks
The `.github/workflows/quality-checks.yml` workflow runs on pushes and pull requests targeting `main`. It installs developer tools, runs Ruff, executes tests, validates project files and Markdown links, parses notebook JSON, and parses GitHub YAML configuration.

## What the workflow intentionally does not do
- It does not execute the notebook.
- It does not load the patient-level CSV.
- It does not train estimators.
- It does not compute or publish health-related model metrics.
- It does not assess fairness, calibration, external validity, or clinical utility.

## Local validation
The repository validator and synthetic test suite are safe to run without the actual dataset. The separate dataset schema-audit utility reads the CSV locally and reports only aggregate counts and required-header status. Only run it in an environment approved for the data.

## Interpreting status
A green workflow indicates that the configured software and documentation checks passed for that commit. It is not a scientific review, clinical validation, regulatory approval, or permission to use the model with people.

## Failure handling
Read the failing job step, reproduce with synthetic data where possible, fix the root cause, and update tests or docs. Never attach patient-level rows, private identifiers, secrets, or notebook output to a public issue.
