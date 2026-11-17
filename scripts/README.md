# 🛠️ Local maintenance scripts

These scripts are optional utilities for maintainers. They are not part of the model or an inference interface.

| Script | Purpose | Reads patient-level CSV? |
|---|---|---|
| [validate_project.py](validate_project.py) | Checks required project files, notebook JSON, and relative Markdown links | No |
| [audit_dataset_schema.py](audit_dataset_schema.py) | Reports aggregate CSV dimensions and required-field presence | Yes, locally only |

## Run repository validation

```bash
python scripts/validate_project.py
```

This validator checks the notebook JSON structure and documentation links. It does not execute notebook cells and does not open the CSV.

## Run the optional local dataset schema audit

```bash
python scripts/audit_dataset_schema.py "DATA _SET (1).csv"
```

The audit reads the local CSV but prints only aggregate row/column counts and whether required header names are present. It does not print or upload record values. Run it only in an environment approved to handle the dataset.

## Exit codes
- `0`: checks completed successfully.
- `1`: validation or schema check failed.
- `2`: requested dataset file was not found.

These checks do not establish data representativeness, model validity, or clinical utility.
