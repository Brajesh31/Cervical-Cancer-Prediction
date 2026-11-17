# Runbook: sensitive-data exposure

## Containment
1. Stop sharing affected links and exports.
2. Identify affected paths, commits, notebook outputs, and destinations.
3. Restrict access where possible.
4. Notify the repository maintainer privately.
5. Do not reproduce exposed records in tickets or notes.

## Assessment
Determine data category, exposure window, visibility, known downloads/forks, and whether direct identifiers or sensitive combinations are present. Consult the responsible institution or data steward.

## Remediation
Removing a file from the latest commit may not remove Git history. Assess history rewriting, cache/purge requests, fork impact, and legal or institutional notifications. Rotate exposed credentials separately.

## Closure
Record timeline and remediation without sensitive values. Verify remaining exposure as far as practical and document limitations honestly.
