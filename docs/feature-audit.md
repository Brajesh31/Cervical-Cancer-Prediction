# Feature availability and leakage audit

## Why this audit is mandatory
The notebook predicts `Dx:Cancer` using a feature subset that includes screening and diagnosis variables. If a predictor is only known after a diagnostic procedure, it cannot support a claim that the model predicts risk before that procedure. Strong association can reflect target leakage rather than useful prospective signal.

## Current notebook feature set
The notebook's selected inputs have been documented as `Dx:HPV`, `Biopsy`, `Citology`, `Schiller`, `Hinselmann`, `Age`, and `Dx:CIN`, with `Dx:Cancer` as the target. Verify this list against the current notebook cell before treating it as a permanent contract.

## Audit table
| Feature | Field family | Timing question | Initial concern |
|---|---|---|---|
| Age | Demographic | Available at intended decision time? | Verify units and missingness |
| Dx:HPV | Diagnosis | When was this diagnosis recorded? | Potential downstream diagnostic information |
| Biopsy | Procedure / diagnostic | Was a biopsy performed before the intended prediction? | High leakage concern |
| Citology | Screening result | What date and stage does it represent? | Potential result leakage |
| Schiller | Screening / diagnostic procedure | Was the result available before the prediction moment? | Potential result leakage |
| Hinselmann | Screening / diagnostic procedure | Was the result available before the prediction moment? | Potential result leakage |
| Dx:CIN | Diagnosis | Is this known only after investigation? | High leakage concern |

This table is a prompt for review, not a definitive clinical interpretation of each variable.

## Required audit record
For every candidate feature, document its definition, coding, source, collection time, availability time, missingness, and relationship to the target. Exclude variables unavailable at the proposed prediction moment. Have a qualified domain expert review uncertain timing.

## Leakage controls
- Split observations before fitting preprocessing.
- Fit imputers, scalers, selectors, and encoders inside training folds.
- Avoid target-derived variables and post-outcome measurements.
- Check duplicate or near-duplicate fields.
- Avoid repeated test-set use during model selection.
- Keep a dated feature-list version with each experiment.

## Approval
No feature set in this repository is approved for clinical or individual-level use. A complete audit improves research transparency but is not clinical validation.
