# 🧪 Automated checks

The test suite checks repository contracts and the dataset audit helper with synthetic test data. It does not execute the analysis notebook or assess clinical performance.

## Install developer dependencies

```bash
python -m pip install -r requirements-dev.txt
```

## Run tests

```bash
python -m pytest -q
```

## Test boundaries
- Notebook JSON structure is checked without executing cells.
- Required files and Markdown relative links are checked.
- Medical safety and the known CSV path mismatch are checked as documentation contracts.
- CSV audit behavior is tested using temporary synthetic files.
- The actual health-related CSV is not loaded by CI tests.

A passing test suite means these software/documentation checks passed. It does not mean the model is clinically validated.
