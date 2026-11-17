# Data quality review

## Current evidence
The checked-in CSV is described as 858 rows by 36 columns. Its header includes age, sexual and reproductive history, STD-related fields, diagnosis fields, and screening/procedure indicators. The dataset uses question-mark sentinels in fields with unavailable values.

## Review dimensions
- Schema completeness and duplicate column names.
- Data types and categorical encodings.
- Missing-value markers, including literal question marks.
- Plausible numeric ranges and outliers.
- Duplicate records and repeated-subject concerns.
- Target prevalence and label semantics.
- Date/time provenance, where available.
- Consistency across diagnosis and screening indicators.
- Source provenance and transformation history.

## Safe reporting
Publish aggregate counts and schema findings only. Suppress small groups if they could expose an individual's record. Never paste a raw row, full table, or screenshot of the dataset into public discussion.

## Missing-value caution
Pandas `dropna()` does not necessarily treat a literal `?` as missing. The notebook's replacement line is commented out. Confirm the raw encoding and handle it explicitly before reporting cleaned row counts.

## Record changes
Use [dataset change record](templates/dataset-change-record.md) and preserve source attribution. No quality audit alone proves representativeness or clinical validity.
