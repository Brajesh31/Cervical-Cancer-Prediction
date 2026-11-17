# Dataset field guide

## Profile
The tracked CSV contains 858 rows and 36 columns. Its structure appears consistent with UCI's Cervical Cancer (Risk Factors) dataset, but this repository does not contain a checksum or transformation history proving byte-for-byte provenance.

## Field families

| Family | Examples | Review |
|---|---|---|
| Demographic | Age | Units, range, missingness |
| Behavioral | Smoking and habit fields | Coding and reference period |
| Reproductive | Pregnancy-related fields | Sensitive health information |
| Sexual health | Partner, contraceptive, STD fields | Sensitive, context-dependent |
| Screening / diagnosis | Hinselmann, Schiller, Citology, Biopsy, Dx:CIN, Dx:HPV | Establish when collected |
| Target | Dx:Cancer | Confirm encoding and positive class |

Inspect schema without printing row values:

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.shape)
print(list(df.columns))
print(df.dtypes)
print(df.isna().sum())
```

The source is known to use question-mark sentinels for some missing values. The notebook's replacement step is commented out. Verify the source copy and parser before using:

```python
df = pd.read_csv("data.csv", na_values=["?"])
```

This is a generic example, not proof that every question mark in every transformed copy has identical semantics.

## Feature timing and leakage
Document what each field measures, how it is coded, when it is collected, and whether it is available at the intended prediction moment. Diagnosis and screening results may be downstream of the target. Do not use post-diagnosis information to claim prospective prediction.

Use aggregate or synthetic examples only. Preserve data attribution and license obligations.
