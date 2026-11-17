# Runbook: local notebook session

## Before starting
1. Confirm the environment is approved for this health-related dataset.
2. Check out the intended Git revision.
3. Create and activate a virtual environment.
4. Install packages from requirements.txt.
5. Create the ignored local data.csv copy if the notebook path is unchanged.
6. Confirm no dataset copy will be uploaded or committed.

## Execute
1. Launch Jupyter from the repository root.
2. Open cervical-cancer-risk-data.ipynb.
3. Restart the kernel and run cells in order.
4. Stop if schema or missing-value assumptions do not match.
5. Record environment and aggregate run details only.

## After execution
- Review warnings and errors.
- Inspect output cells for record-level information.
- Do not describe results as clinical performance.
- Do not commit duplicate data or sensitive outputs.
- Close the kernel and clean up temporary files under applicable rules.

## Recovery
If data.csv is missing, confirm the working directory and use the README workaround. Do not rename or overwrite source files blindly.
