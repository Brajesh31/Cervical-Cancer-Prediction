# Model governance and change control

## Current status
The notebook fits estimators locally but does not version fitted models, define a model registry, provide inference, monitor a service, or establish clinical governance.

## Any future change to model behavior must record
- Research question and intended prediction time.
- Dataset source, rights, and provenance.
- Target and positive class.
- Feature list and feature-availability audit.
- Preprocessing and split strategy.
- Model algorithm, hyperparameters, and random seeds.
- Evaluation metrics, uncertainty, and independent validation.
- Known limitations, subgroup evidence, and potential harms.
- Reviewer and approval record.

## Change categories
- Documentation-only change: verify statements and links.
- Preprocessing change: require synthetic tests and data-quality evidence.
- Feature or target change: require a new leakage and research-question review.
- Model or metric change: require a documented evaluation plan.
- Data-source change: require provenance, rights, privacy, and transformation review.
- Any patient-facing proposal: outside current project scope and requires independent expert and regulatory assessment.

## Rollback and audit trail
Keep changes traceable to commits and experiment records. Do not overwrite historical result descriptions without recording the reason. If sensitive data is exposed, follow the dedicated incident process.

## Approval boundary
Maintainer approval to merge code is not clinical approval, scientific endorsement, or regulatory clearance.
