# Testing and verification

## Test layers currently available

| Layer | How to run | What it checks | What it does not prove |
|---|---|---|---|
| Repository contract tests | `python -m pytest -q` | Required files, README safety wording, documented path mismatch | Scientific or clinical validity |
| Synthetic dataset audit tests | Included in pytest suite | Header uniqueness and aggregate CSV parser behavior with synthetic fixtures | Quality of every real-world health record |
| Repository validator | `python scripts/validate_project.py` | Required paths, notebook JSON, relative Markdown links | Notebook cell execution |
| Ruff | `ruff check scripts tests` | Style and common Python errors in maintenance code | Model correctness |
| Notebook JSON | `python -m json.tool cervical-cancer-risk-data.ipynb` | JSON syntax | Whether notebook cells run or results are valid |
| Optional local CSV schema audit | `python scripts/audit_dataset_schema.py` | Aggregate dimensions and required header presence | Clinical dataset suitability |

## Install developer tools

```bash
python -m pip install -r requirements-dev.txt
```

## Run checks locally

```bash
ruff check scripts tests
python -m pytest -q
python scripts/validate_project.py
python -m json.tool cervical-cancer-risk-data.ipynb > /dev/null
```

## Continuous integration boundary
GitHub Actions runs the repository and synthetic-data checks. It deliberately does not load or print the patient-level CSV. This reduces unnecessary processing of sensitive data in a hosted CI environment.

## Notebook execution
The notebook can be run manually in an approved local environment. A successful run only shows that a particular code and data combination executed. It does not establish that the feature set is leakage-free, that results generalize, or that the model has medical utility.

## Future tests
Before changing model logic, add synthetic unit tests for missing-marker parsing, data transformations, split behavior, leakage safeguards, evaluation metrics, and reproducibility. Keep fixtures synthetic and do not copy patient records into tests.
