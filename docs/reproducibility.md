# Reproducibility guide

## Current state
Dependencies are listed but unpinned. A tested Python version and lockfile are not recorded. The notebook uses a train/test split without a fixed seed and does not define a complete experiment protocol.

## Record each run
- Python version and operating system.
- Exact package versions.
- Git commit SHA.
- Dataset provenance and securely stored checksum.
- Notebook execution date and method.
- Cleaning steps and aggregate retained/removed counts.
- Feature list and availability-time rationale.
- Split strategy and random seed.
- Model configuration and metrics.

Example environment capture:

```bash
python --version
python -m pip freeze > environment-freeze.txt
git rev-parse HEAD
```

Review generated environment files for local paths or secrets before publishing.

## Randomness
Set and record seeds for splitting and estimators where supported. A fixed seed helps repeatability but does not remove sampling uncertainty or establish external validity.

## Data path
The notebook expects `data.csv`, but the committed file uses another name. Follow the README workaround or make a reviewed path correction. Do not commit a duplicate CSV.

## Output hygiene
Restart the kernel and run cells in order for a fresh analysis. Check for stale output and sensitive information before sharing.

Reproducibility is necessary for careful research, but it is not proof of validity or medical utility.
