# Experiment tracking

## Purpose
A run should be traceable to its source data, code revision, environment, preprocessing, feature set, and evaluation design. A notebook output without this context is not a reproducible experiment record.

## Minimum run record
- Unique experiment identifier and date.
- Git commit SHA.
- Dataset source, license, transformation history, and securely stored checksum.
- Python version and package versions.
- Exact target and positive-class encoding.
- Feature list and feature-availability rationale.
- Missing-value strategy and aggregate rows retained/removed.
- Split strategy, seed, and any grouping or stratification.
- Preprocessing and model hyperparameters.
- Metrics, uncertainty, threshold rationale, and limitations.
- Whether the notebook was run from a clean kernel.

## Naming and storage
Use date-prefixed identifiers such as `YYYY-MM-DD-topic-v1`. Store aggregate results and configuration, not raw records. Never commit patient-level exports, fitted artifacts intended for clinical use, or screenshots of records.

## Comparing runs
Compare runs only when their data, target, split, metrics, and evaluation protocol are sufficiently aligned. Do not compare values from different test partitions as if they were directly comparable.

Use [experiment-record.md](templates/experiment-record.md). Tracking does not establish clinical validity.
