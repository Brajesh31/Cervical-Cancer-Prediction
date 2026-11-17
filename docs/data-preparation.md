# Data preparation guidance

## Current state
The notebook's missing-value replacement for question-mark sentinels is commented out. It then calls missing-value removal, which may not recognize literal question marks. The notebook also reads a filename that differs from the tracked CSV.

## Recommended preparation sequence
1. Resolve the source file path explicitly.
2. Verify schema, provenance, licensing, and aggregate dimensions.
3. Inspect missing markers and data types.
4. Convert documented sentinel values deliberately.
5. Report aggregate counts before and after each filtering step.
6. Check duplicates and possible repeated observations.
7. Review plausible ranges and categorical encodings.
8. Define target semantics and positive class.
9. Audit features for availability and leakage.
10. Split before fitting learned preprocessing.

## Illustrative missing-marker parsing
A generic pandas example is:

```python
import pandas as pd

frame = pd.read_csv("DATA _SET (1).csv", na_values=["?"])
```

Verify this is appropriate for the exact data copy and field semantics before using it. Avoid silently changing categorical values or discarding rows.

## Pipeline discipline
Imputation, scaling, feature selection, and other learned transformations should be fitted on training data only, preferably within cross-validation pipelines.

## Output and privacy
Do not print full patient tables into saved notebook outputs. Prefer aggregate summaries and synthetic examples. The local schema audit script prints only aggregate shape and required-header status.
