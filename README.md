# Cervical Cancer Risk Factors: Exploratory Notebook

This repository contains one Jupyter notebook and a tabular dataset for an
exploratory machine-learning exercise involving cervical-cancer risk factors.
The notebook compares a Random Forest classifier, an SVM classifier, and
Logistic Regression using scikit-learn.

## Medical safety statement

This repository is for education and reproducible code review only. It is not
a medical device, screening service, clinical decision-support tool, or
diagnostic system. Its code and reported metrics have not been clinically
validated. Do not use its outputs to diagnose, screen, triage, treat, reassure,
or make decisions about an individual. Consult qualified health professionals
for medical questions.

## Repository contents

- cervical-cancer-risk-data.ipynb: the exploratory notebook, including saved
  cell outputs.
- DATA _SET (1).csv: a patient-level tabular file with 858 records and 36
  fields, including demographic, behavioral, reproductive-health, STD, and
  diagnosis information.
- README.md: project overview and responsible-use guidance.
- docs/: project, data, development, deployment, and troubleshooting guides.

The notebook attempts to read a file named data.csv, but the tracked CSV has a
different filename. Create a local copy named data.csv next to the notebook
before running it, or update the notebook path as a reviewed code change. The
local copy is ignored by Git.

## Dataset attribution and license

The column names and 858-by-36 structure appear to match the UCI Machine
Learning Repository's Cervical Cancer (Risk Factors) dataset. The exact
provenance and transformations of the file in this repository are not
recorded, so verify them before redistribution.

UCI credits Kelwin Fernandes, Jaime Cardoso, and Jessica Fernandes (2017),
Cervical Cancer (Risk Factors), UCI Machine Learning Repository,
https://doi.org/10.24432/C5Z310. UCI lists the dataset under the Creative
Commons Attribution 4.0 International license (CC BY 4.0):
https://creativecommons.org/licenses/by/4.0/

The MIT license in this repository applies to original project code and
documentation. It does not replace the separate license and attribution
requirements for the dataset or dataset-derived notebook outputs. See LICENSE
and docs/database.md.

## Environment and installation

Use a supported Python 3 environment. The repository does not record a tested
Python version or pinned package environment. The notebook imports pandas,
NumPy, Matplotlib, Seaborn, and scikit-learn; Jupyter is needed to run the
notebook interactively.

Create a virtual environment and install the listed dependencies:

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    Copy-Item "DATA _SET (1).csv" data.csv
    jupyter notebook cervical-cancer-risk-data.ipynb

On macOS or Linux, use python3 -m venv .venv, activate it with
source .venv/bin/activate, and copy the dataset with
cp "DATA _SET (1).csv" data.csv before starting Jupyter.

See docs/installation.md for more detail. Never commit private data or secrets.

## Notebook workflow

The notebook loads the CSV, inspects missing values and duplicates, filters a
subset of columns, and uses Dx:Cancer as its target. It trains Random Forest,
SVC, and Logistic Regression classifiers on one random train/test split. It
prints accuracy, mean squared error, and classification reports for some
models, then plots a comparison of accuracy.

This is an exploratory analysis, not a reproducible model pipeline. The split
has no fixed random seed or stratification. The notebook's attempted
replacement of question-mark missing-value markers is commented out before
dropna is called. Predictors include diagnosis and screening fields such as
Biopsy and Dx:CIN; these may overlap with the cancer target and create target
leakage. The feature timing and prediction question are not defined as a
prospective clinical task.

## Privacy and responsible handling

The dataset contains patient-level health-related records. Even without direct
names in the visible column list, row-level medical and sexual-health values
are sensitive. Do not upload the CSV or notebook to an unapproved service, and
do not share screenshots or logs that reveal individual rows. Follow the
dataset license and institutional or organizational data-handling rules that
apply to your use.

## Limitations

- The notebook reads data.csv while the committed dataset uses another name.
- Missing-value handling is incomplete; literal question marks may not be
  treated as missing values by the notebook.
- The prediction target and the included diagnosis/screening predictors may
  cause leakage and do not define early prediction.
- The class distribution and threshold behavior are not analyzed as a
  clinical screening problem.
- The train/test split is unseeded and not stratified; there is no repeated
  evaluation, calibration, external validation, or fairness assessment.
- The notebook does not save a trained model or provide an inference app,
  database, or public API.
- Saved notebook outputs include table previews and row-level values. Review
  or clear them before creating a derivative copy for sharing.

## Contributing and support

Read CONTRIBUTING.md before proposing changes. Use synthetic examples in
issues and pull requests. For technical questions, follow SUPPORT.md; report a
suspected vulnerability privately as described in SECURITY.md.

## Documentation

- System structure: docs/architecture.md
- Setup: docs/installation.md
- Notebook development: docs/development.md
- Deployment considerations: docs/deployment.md
- API status: docs/api.md
- Data and persistence: docs/database.md
- Troubleshooting: docs/troubleshooting.md
- Frequently asked questions: docs/faq.md
- Planned improvements: ROADMAP.md
## Intended research question

The existing notebook predicts the Dx:Cancer column from a selected subset
that includes other diagnosis and screening indicators. It does not establish
that those predictors were available before diagnosis, so its result must not
be described as early detection or prospective risk prediction.
## Dataset dimensions

The tracked CSV contains 858 rows and 36 columns. The UCI record reports the
same number of instances and features and describes demographic, habit, and
medical-history fields. This structural match supports the likely source but
does not prove that the local file is byte-identical to the UCI download.
## Saved notebook output

The committed notebook has saved outputs, including previews of data tables
and selected feature values. Those are dataset-derived patient-level values.
Clear outputs before publishing transformed notebooks where row-level
information is not needed, while retaining proper dataset attribution.
## Class imbalance and metrics

Accuracy alone can conceal behavior on an uncommon positive class. Review
class counts, sensitivity, specificity, precision, recall, and uncertainty
before drawing any research conclusion. The notebook does not provide a
clinical operating threshold or validation study.
## Reproducibility

The notebook does not set random_state on train_test_split or the random
forest. Reruns can produce different partitions and results. Record software
versions and split details if continuing the analysis, and do not treat a
single displayed result as stable evidence.
## Dataset license boundary

Keep the UCI dataset attribution and CC BY 4.0 terms with the dataset and
derivative outputs when applicable. The repository's MIT notice is scoped to
project-authored code and documentation and cannot relicense third-party
records.
## Reporting limitations

For a documentation or code issue, include the notebook cell, sanitized
error, and software versions. Do not attach patient-level rows, private
health information, or screenshots of saved dataset outputs.

Last updated: 2026-10-30 01:42 UTC
