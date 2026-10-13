# Frequently asked questions

## What is this repository?

It is a small exploratory machine-learning project for a cervical-cancer risk-factor dataset. The repository contains a Jupyter notebook and a CSV file. The notebook compares Random Forest, support vector machine, and logistic regression classifiers and prints several evaluation summaries. It is an educational experiment, not a maintained application.

## Does it diagnose cervical cancer or recommend care?

No. It is not a medical device, screening tool, diagnostic system, or source of treatment advice. Its results have not been clinically validated and must not be used for decisions about a person's health. Consult a qualified healthcare professional for medical questions.

## How do I open the project?

Install Python and the packages in `requirements.txt`, then launch Jupyter from the repository root with `jupyter notebook`. Follow [installation](installation.md) and use the notebook kernel that belongs to the environment where the packages were installed.

## Why does the notebook fail to read the CSV?

The notebook expects `data.csv`, but the tracked CSV has a different name. Adjust the path in a local working copy or make a private local copy named `data.csv`. The repository ignores `/data.csv`; do not commit a private or patient-level data file.

## Is the included CSV definitely the original UCI dataset?

The schema and row/column count appear consistent with the UCI Cervical Cancer (Risk Factors) dataset, but this repository does not document a verified acquisition or transformation history. The [UCI record](https://archive.ics.uci.edu/dataset/383/cervical%2Bcancer) identifies the dataset as 858 instances and 36 features and lists CC BY 4.0 terms. Verify the provenance of this exact local copy before redistribution; see the third-party data notice in [LICENSE](../LICENSE) and attribution in [README.md](../README.md).

## Why are there question marks or missing values?

The CSV uses `?` as a missing-value marker. The notebook's replacement step is commented out, and `dropna()` does not necessarily interpret a literal question mark as missing. Review [troubleshooting](troubleshooting.md) before drawing conclusions from any revised analysis.

## Can I rely on the reported accuracy?

No. The notebook does not establish a reproducible or clinically valid estimate. The split is not stratified or seeded, preprocessing is incomplete, and diagnosis-related fields among the predictors may leak information about the target. Class imbalance, missing-value handling, and test-set reuse also affect interpretation. Read [architecture](architecture.md) and [development](development.md) for the current limitations.

## Does it predict cancer before diagnosis?

That is not established. The target is `Dx:Cancer`, while candidate inputs include other diagnosis-related fields. The timing and availability of those fields are undocumented, so the notebook cannot support a claim about early prediction or screening.

## Is there an API, web app, database, or deployment?

No. The repository has no API, user interface, persistence layer, trained-model service, or deployment configuration. The respective guides document these boundaries: [API](api.md), [database](database.md), and [deployment](deployment.md).

## How can I contribute or report a problem?

Read [CONTRIBUTING.md](../CONTRIBUTING.md) for proposed changes and [SUPPORT.md](../SUPPORT.md) for help channels. Do not attach sensitive health records. Report suspected vulnerabilities privately according to [SECURITY.md](../SECURITY.md).

## How is the software licensed?

The original project code and documentation are offered under the MIT License, with attribution to Brajesh Kumar. The dataset has separate third-party terms and attribution requirements; the MIT license does not replace them. See [LICENSE](../LICENSE).

## Can I use another CSV file?

You can adapt the notebook for a different dataset only after checking its license, provenance, schema, target definition, and permitted use. Update the documentation and evaluation plan, and do not assume that matching column names make two datasets interchangeable.

## Why does the notebook have saved output cells?

Notebook outputs may be retained from a previous run. They are not a guarantee that the current source and data reproduce those values. Restart the kernel, run the notebook in order, and review outputs for sensitive information before sharing a notebook copy.

## Does the repository include a trained model?

No trained model artifact or supported model-loading interface is provided. The notebook fits estimators during its exploratory workflow; it does not define a production model lifecycle or guarantee reproducibility.

## Can I publish the dataset in a fork?

Check the dataset's source and applicable terms first, provide the required attribution, and verify the provenance of this exact copy. Health-related data deserves careful handling even when a dataset is publicly available. Do not add identifiable or confidential records.
