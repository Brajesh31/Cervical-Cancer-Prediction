# Known issues and current technical debt

This list describes issues observed in the checked-in notebook and repository. It is not an exhaustive code audit.

| ID | Issue | Impact | Suggested next action | Status |
|---|---|---|---|---|
| K-01 | Notebook reads `data.csv`; tracked file has another name | Fresh checkout needs a manual copy | Use a repository-relative data path | Open |
| K-02 | Question-mark sentinel replacement is commented out | Missing values may remain as strings | Audit and parse missing markers explicitly | Open |
| K-03 | Diagnosis/screening predictors may leak `Dx:Cancer` | Invalidates prospective interpretation | Define prediction time and audit every feature | Open |
| K-04 | Split is unseeded and not stratified | Results vary and class proportions may shift | Define a reproducible split protocol | Open |
| K-05 | Evaluation emphasizes accuracy and MSE | May obscure minority-class performance | Report class-aware metrics and uncertainty | Open |
| K-06 | No external validation or calibration | No evidence of generalization or clinical utility | Design independent validation only after research review | Open |
| K-07 | Notebook stores outputs | May expose data-derived row values | Review and clear unnecessary outputs | Open |
| K-08 | Requirements are unpinned | Environment can drift | Validate and lock a supported environment | Open |
| K-09 | No reusable inference interface or saved model | Cannot serve predictions as a supported product | Keep notebook-only scope unless separately reviewed | By design |

Fix priority should consider data privacy and validity before presentation or convenience. Update this table when a verified change resolves an item.
