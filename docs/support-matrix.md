# Support and compatibility matrix

## Current support statement
This is an exploratory notebook repository. No supported production deployment or patient-facing application is provided.

| Component | Repository evidence | Support status |
|---|---|---|
| Python | Python 3 environment expected | Exact supported version not pinned |
| Jupyter | Notebook is the main entry point | Interactive local use, best effort |
| pandas / NumPy | Imported by notebook | Version ranges not pinned |
| Matplotlib / Seaborn | Used for plots | Version ranges not pinned |
| scikit-learn | Random Forest, SVC, Logistic Regression | Version not pinned |
| Operating system | Setup examples for Windows, macOS, Linux | Not exhaustively tested |
| Database | None | Not applicable |
| API / serving | None | Not available |
| Clinical workflow | None | Explicitly unsupported |

## Reporting compatibility issues
Include OS, Python version, package versions, commit SHA, and sanitized error messages. Do not attach data rows, screenshots, environment tokens, or private paths.

## Updating this matrix
Update only after a platform or package combination has actually been tested. Do not infer support from a successful installation on one machine.
