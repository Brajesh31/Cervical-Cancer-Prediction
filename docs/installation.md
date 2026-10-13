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
## Verify the interpreter

Use python --version and python -m pip --version to confirm that Python and
pip refer to the active virtual environment. Report package versions when
troubleshooting dependency or notebook behavior.
## PowerShell activation fallback

If local policy prevents running Activate.ps1, use
.venv\Scripts\python.exe -m pip install -r requirements.txt and launch
.venv\Scripts\jupyter.exe notebook cervical-cancer-risk-data.ipynb. Do not
change machine-wide execution policy just to start the notebook.
## Notebook working directory

The notebook reads a relative filename. Start Jupyter from the repository
root so data.csv resolves there. If the kernel starts elsewhere, inspect its
current working directory without printing patient rows.
## Dependency reproducibility

The manifest does not pin transitive versions or a Python runtime. Separate
installations may differ. Record versions used for a result and use a reviewed
lock strategy if repeatability is required.
## Dataset provenance

The local CSV matches the UCI dataset's reported dimensions, but its
transformation history is not documented. Keep UCI attribution and CC BY 4.0
information with any permitted reuse, and review README.md and LICENSE.
## No environment secrets

The notebook currently reads no API keys or application secrets. Do not add
credentials to .env.example. If a future workflow requires them, keep real
values outside the repository and document the integration.
