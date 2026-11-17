# Privacy and sensitive data handling

The CSV contains patient-level health-related information, including reproductive, behavioral, sexual-health, screening, and diagnostic fields. The absence of obvious names does not make records anonymous or safe to publish.

## Safe handling
- Use a trusted local environment with access controls.
- Do not upload the CSV or notebook to an unapproved hosted service.
- Do not paste individual rows into issues, pull requests, chats, or docs.
- Do not include raw values in logs, screenshots, charts, or bug reports.
- Keep local copies out of Git unless a data change is explicitly authorized.
- Review saved notebook output cells before committing or exporting.
- Preserve source attribution and applicable data terms.
- Remove temporary copies when no longer needed, consistent with applicable obligations.

## Notebook outputs
Jupyter may embed tables, images, and printed values in notebook JSON. Removing a CSV from a derivative repository does not automatically remove data-derived information from notebook outputs. Inspect output cells explicitly.

## External services
Before using hosted notebooks, cloud storage, AI tools, analytics, or collaboration platforms, assess transfer, retention, access, training use, jurisdiction, and contractual controls.

## Incident response
1. Stop further sharing and identify affected paths and commits.
2. Restrict access where possible and contact the maintainer privately.
3. Do not reproduce exposed content in incident notes.
4. Assess history rewriting, cache removal, forks, and platform support.
5. Follow applicable institutional, contractual, and legal notification obligations.
6. Record remediation without reproducing sensitive values.

Deleting a file from the latest commit does not guarantee removal from history, forks, caches, or prior downloads.
