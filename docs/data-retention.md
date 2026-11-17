# Data retention and deletion guidance

## Current data footprint
The repository tracks a CSV dataset and a notebook with saved outputs. Local users may also create an ignored `data.csv` copy, virtual environments, notebook checkpoints, exported figures, or temporary files.

## Repository retention
A file removed from the latest commit may still exist in Git history, forks, caches, releases, or previously downloaded copies. Do not treat an ordinary file deletion as proof of secure erasure.

## Local working copies
- Keep access limited to people authorized to handle the dataset.
- Avoid creating unnecessary duplicate copies.
- Store temporary files in approved protected locations.
- Clear unneeded notebook output and checkpoint files.
- Remove local working copies when no longer needed, subject to applicable research and institutional retention requirements.
- Review backups and synchronized folders separately.

## Hosted services
Before moving data to cloud storage, hosted notebooks, AI tools, or collaboration systems, review location, access, retention, backup, deletion, subprocessors, and contractual obligations. Do not assume that a public dataset can be uploaded to any service.

## Future collection or storage
The current repository does not implement user data collection or an application database. Any future feature that accepts or retains additional health information requires a documented purpose, lawful basis, minimum field set, retention schedule, deletion workflow, access controls, audit trail, incident plan, and accountable data steward.

## Incident handling
For accidental exposure, follow [the sensitive-data incident runbook](runbooks/sensitive-data-incident.md). Document remediation without reproducing the exposed values.
