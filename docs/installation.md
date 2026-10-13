# Installation

## Prerequisites

- Python 3 compatible with the selected Jupyter and scikit-learn releases.
- Git, if cloning the repository.
- A terminal in the repository root.
- Enough local disk space for the CSV, notebook, and Python environment.

The repository does not specify a tested Python version or lock all
dependencies. The steps below describe a general local notebook setup and have
not been validated as a clinical or production environment.

## Get the source

Clone the repository or use an existing checkout. Open a terminal in the
folder containing cervical-cancer-risk-data.ipynb and DATA _SET (1).csv.

## Create a virtual environment

Windows PowerShell:

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1

macOS or Linux:

    python3 -m venv .venv
    source .venv/bin/activate

If shell activation is unavailable, call the interpreter and Jupyter executable
directly from the environment's Scripts directory on Windows or bin directory
on macOS and Linux.

## Install notebook packages

With the virtual environment active:

    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

The manifest lists Jupyter, pandas, NumPy, Matplotlib, Seaborn, and
scikit-learn. Versions are not pinned.

## Resolve the notebook data path

The first notebook data-loading cell requests data.csv. The tracked file is
named DATA _SET (1).csv. Create a local working copy with the expected filename
in the repository root:

    Copy-Item "DATA _SET (1).csv" data.csv

On macOS or Linux:

    cp "DATA _SET (1).csv" data.csv

The generated data.csv is ignored by Git. Do not stage or commit that copy.
A future source change could instead update the notebook to use the tracked
filename directly.

## Open the notebook

From the repository root, run:

    jupyter notebook cervical-cancer-risk-data.ipynb

Select cells and run them in order with the Jupyter interface. The notebook
contains saved outputs that may not match your current environment or source
data. Use the README warnings before interpreting any metric.

## Data handling

The CSV contains patient-level health-related information. Use the data only
under its applicable license and governance requirements. Do not upload it to
an unapproved cloud notebook or include row-level values in issues and
screenshots. The notebook is not a clinical tool.
