# Architecture

## System overview

This repository is a notebook-based exploratory analysis, not an application
service. Its core files are a Jupyter notebook and a patient-level CSV. The
notebook imports the CSV into pandas, selects columns, trains several
scikit-learn estimators, prints metrics, and plots a small comparison.

    CSV file -> pandas DataFrame -> row filtering and column selection
       -> one train/test split -> model fitting -> predictions and metrics

There is no backend API, web UI, database, authentication, scheduled job, or
saved model-serving process.

## Repository components

- cervical-cancer-risk-data.ipynb: 66 cells of analysis and saved outputs.
- DATA _SET (1).csv: 858 rows and 36 fields of health-related data.
- README.md: setup, attribution, intended use, and limitations.
- requirements.txt: notebook dependencies.
- docs/: project policies and technical guidance.
- .idea/: IDE metadata, not required to execute the notebook.

## Notebook pipeline

The notebook imports pandas, NumPy, Matplotlib, Seaborn, and scikit-learn.
It reads a file named data.csv, inspects rows, dimensions, nulls and
duplicates, and creates a subset with selected diagnosis, screening, and age
features. Dx:Cancer is used as the target.

It splits the rows with test_size set to 0.20, without a fixed random_state or
stratification. It fits a default RandomForestClassifier, SVC, and
LogisticRegression. It calculates accuracy, mean squared error for some
predictions, classification reports for some estimators, and a bar chart of
accuracy values.

No trained estimator is serialized. There is no reusable preprocessing
pipeline, inference function, prediction endpoint, or model-loading code.

## Data path and provenance

The notebook expects data.csv in its current working directory. The tracked
file is named DATA _SET (1).csv, so the notebook does not run with the checked
in filename unless the path is changed or a local copy is created.

The CSV's 858-by-36 structure matches the UCI Cervical Cancer (Risk Factors)
dataset profile. The repository does not document the exact file checksum or
transformation history. See README.md and LICENSE for attribution and
third-party license notes.

## Important modeling boundaries

The notebook's "early prediction" description is not supported by the
implemented feature set. Predictors include diagnosis and screening indicators
such as Biopsy, Dx:CIN, and other diagnostic variables along with Dx:Cancer.
The feature availability time is not defined, so target leakage and circular
evaluation are possible.

Missing-value processing is also uncertain: a question-mark replacement line
is commented out before dropna is used. Literal question marks may not be
treated as missing values by pandas. The split is unseeded and not
stratified, and the code does not assess calibration, external validity,
fairness, or clinical utility.

## Data handling and outputs

The analysis runs locally in notebook memory and uses a committed CSV. The
notebook also stores output cells, including previews and row-level values
derived from the data. No application database is defined, but this does not
make the patient-level records non-sensitive. Review outputs before sharing
a derivative notebook and preserve dataset attribution.
## File resolution

Jupyter generally runs a notebook relative to its working directory, but the
source explicitly names data.csv. A local copy under that name is ignored by
Git for convenience. Prefer correcting the source path to a deliberate
repository-relative path in a reviewed code change.
## Missing-value flow

The intended replacement of question-mark values with NaN is commented out.
The later dropna calls remove recognized missing values, but literal string
sentinels can remain. Cleaning behavior should be made explicit before model
fitting.
## Split properties

The 20 percent holdout uses the library defaults for shuffling and has no
fixed seed or stratification. This makes results variable and can produce an
unrepresentative split for an imbalanced target.
