# API

## API status

This repository exposes no application-owned REST, GraphQL, command-line
prediction service, or stable programmatic interface. Its main workflow is a
Jupyter notebook that reads a local CSV and produces exploratory analysis
outputs inside a notebook kernel.

Notebook cell order, variable names, and saved outputs are implementation
details, not a supported API contract.

## Inputs to the current workflow

The first data-loading cell calls pandas read_csv with the relative filename
data.csv. It expects a tabular file with 36 fields matching the notebook's
column references. The committed file is named DATA _SET (1).csv, so a local
copy or source-path update is needed before execution.

The analysis selects Dx:HPV, Biopsy, Citology, Schiller, Hinselmann, Age, and
Dx:CIN as features and uses Dx:Cancer as the target. These variables describe
diagnosis and screening as well as risk factors; the timing and suitability of
this feature set are unresolved.

## Models and outputs

The notebook fits RandomForestClassifier, SVC, and LogisticRegression using a
single train/test split. It prints or plots selected metrics. It does not
accept a per-person prediction request, define a response schema, save model
objects, or return predictions through a service.

## Errors and reproducibility

There are no stable error codes, input-size rules, authentication controls,
rate limits, versioned schemas, or service logs. Execution depends on local
file paths, notebook cell order, dependency versions, and an unseeded split.
Do not build an external integration against the current notebook variables.

## Future API proposals

A future programmatic interface would need a clearly justified use case,
authorized input data, a validated model, versioned input and output schemas,
error behavior, access controls, audit and retention rules, and clinical and
privacy review. This repository is not ready to provide individual medical
predictions.
## Relative path contract

The data-loading cell expects data.csv relative to the active kernel directory.
That filename is not present in a clean checkout. Treat this as a reproducibility
defect, not an undocumented public API parameter.
## Feature schema concerns

The selected predictors contain diagnosis or screening indicators. A future
contract must define prediction timing and exclude features unavailable at the
intended decision point; otherwise the result may be target-leaked.
## No authentication

No user identity or role is implemented. A hosted notebook's login page or
repository access setting would be an external platform control, not
application-level authorization.
## No request persistence

The notebook does not store prediction requests or expose a per-person
inference route. Kernel variables exist only during the notebook execution
session unless the operator separately saves them.
