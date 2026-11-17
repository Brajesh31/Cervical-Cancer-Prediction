# Clinical-use boundary and medical safety

## Explicit project boundary
This repository is not a medical device, diagnostic product, cervical-cancer screening system, clinical decision-support tool, or substitute for a qualified health professional.

Do not use the notebook or its outputs to:
- Diagnose or rule out cervical cancer.
- Estimate or communicate an individual's cancer risk.
- Recommend screening, treatment, follow-up, or clinical triage.
- Reassure a person that they do not need medical evaluation.
- Prioritize access to care.

## Why this boundary matters
The implementation is exploratory and has not been clinically validated. The current predictor set includes diagnosis and screening-related fields alongside `Dx:Cancer`. Feature availability timing is not defined, so leakage is possible. The split and evaluation process are limited and there is no external validation, calibration, or clinical utility study.

## Do not confuse metrics with evidence
An accuracy score or classification report from one data split does not demonstrate diagnostic accuracy, sensitivity in a real screening population, clinical benefit, safety, or generalization.

## If the project scope is ever proposed to change
The proposal must be independently assessed by qualified clinical, statistical, ethics, privacy, security, and regulatory experts. A prospective research design, authorized data governance, leakage-resistant features, external validation, calibration, subgroup review, and assessment of harms are among the required considerations. This repository currently has none of the approvals necessary for individual-facing use.

## How to communicate results
Call them exploratory results on a historical dataset. State uncertainty, dataset limitations, and the absence of clinical validation prominently. Never turn model output into advice for a person.
