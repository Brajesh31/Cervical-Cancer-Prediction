# Deployment and sharing

## Current status

This repository has no web application, API, container, deployment manifest,
or saved model artifact. The notebook is intended for interactive local
analysis. There is no supported clinical or production deployment path.

## Local reproducibility

Follow docs/installation.md to create an isolated environment, install the
notebook dependencies, create the expected local data.csv filename, and open
the notebook from the repository root. Record the commit and package versions
when sharing a non-clinical research result.

## Sharing notebook material

Before sharing the repository, an exported notebook, or rendered output:

- Verify UCI dataset attribution and applicable CC BY 4.0 terms.
- Review saved notebook outputs for patient-level rows.
- Remove unnecessary records and local paths from outputs.
- Include the medical-safety disclaimer and analysis limitations.
- Do not include private or newly collected patient data.

A public dataset can still contain sensitive health information. Public
availability is not a substitute for privacy review or a license check.

## Hosted notebook environments

A managed Jupyter service changes where data and outputs are stored. Review
the provider's access controls, network access, logs, backups, retention,
sharing defaults, and data-use terms before uploading the CSV. Use only an
environment approved for the dataset and its intended use.

## Model deployment

The notebook does not save an estimator, define a prediction request schema,
or validate a model for individual use. Do not turn its current scores into a
patient-facing prediction service. Data leakage, missing-value handling,
reproducibility, class imbalance, and clinical validity remain unresolved.

## Future release requirements

A future service would require a defined and justified task, authorized data,
leakage-resistant validation, independent evaluation, clinical and privacy
review, access controls, secure operations, monitoring, incident response,
and documented regulatory assessment. This repository has not completed those
steps.
