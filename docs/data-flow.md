# Data flow and trust boundaries

## Current local workflow
The repository's primary data path is a local CSV loaded by a Jupyter notebook. Data is processed inside the notebook kernel. Display calls can embed tables and values into saved notebook outputs.

```text
Tracked CSV
   |
   v
Local approved environment
   |
   v
Jupyter kernel and pandas DataFrame
   |
   +--> preprocessing and feature selection
   |
   +--> estimator fitting and predictions
   |
   +--> displayed metrics, tables and plots
             |
             v
        notebook output JSON
```

## Trust boundaries
- Git repository: source code, notebook, and tracked dataset are accessible according to repository visibility.
- Local environment: copies, kernels, caches, and exports are controlled by the operator.
- Hosted notebook or third-party service: a separate data-transfer and retention boundary requiring prior review.
- Public issues and pull requests: must contain only synthetic or aggregate information, never patient records.

## Current absence
There is no application API, account system, database, hosted inference endpoint, model registry, or production data pipeline.

## Output risk
A notebook can retain data-derived values after the source CSV is removed. Review outputs before commits and exports. Do not assume that clearing one visible cell removes all artifacts from the repository history.

## Future change gate
Any upload, API, database, or automated processing feature changes the trust model. Before implementation, define purpose, lawful authority, minimum data, access control, encryption, retention, deletion, audit logging, incident response, and responsible ownership.
