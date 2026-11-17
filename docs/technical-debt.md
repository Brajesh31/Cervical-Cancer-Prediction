# Technical debt register

| ID | Debt | Reason / evidence | Risk | Proposed resolution |
|---|---|---|---|---|
| TD-01 | Dataset filename and notebook path differ | Notebook expects `data.csv` | Fresh checkout fails without workaround | Use a configured repository-relative path |
| TD-02 | Unpinned dependencies | requirements.txt has package names only | Environment drift | Validate and lock supported versions |
| TD-03 | Notebook logic is not modular | Analysis is contained in notebook cells | Difficult to test and reuse | Extract pure preprocessing and evaluation helpers after research review |
| TD-04 | Missing-value handling incomplete | '?' replacement is commented out | Invalid cleaning | Explicit missing-marker parsing and audit |
| TD-05 | Feature timing undocumented | Diagnosis and screening predictors selected | Potential leakage | Feature-level availability audit |
| TD-06 | Evaluation is a single split | No seed or stratification | Unstable estimate | Define reproducible validation plan |
| TD-07 | No automated test suite existed in baseline | Analysis is notebook-only | Regression risk | Add safe structural and synthetic-data tests |
| TD-08 | Saved outputs retained | Notebook contains output cells | Sensitive-data exposure | Clear unnecessary output and review diffs |

Prioritize data safety and research validity over cosmetic refactoring. Update this register when an item is fixed and verified.
