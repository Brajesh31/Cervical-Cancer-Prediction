# Release and change process

## Current release model
The repository is an educational notebook project and does not currently define a packaged application release, model registry, or clinical deployment process. A GitHub commit is not a model release or validation certificate.

## Documentation or code release
1. Confirm the change is necessary and within the project's educational scope.
2. Inspect notebook source and outputs for sensitive values.
3. Verify data attribution and third-party terms.
4. Review feature timing, leakage, preprocessing, and evaluation implications.
5. Run applicable repository checks and record the exact results.
6. Update README and related documentation.
7. Update CHANGELOG.md only for meaningful changes.
8. Review pull request and obtain appropriate maintainer approval.
9. Confirm the intended commit is on the default branch.
10. Communicate remaining limitations clearly.

## Versioning
Use tags only for meaningful source snapshots. Do not imply clinical validation or production readiness through version labels. If model artifacts are ever introduced, they require separate model provenance, validation, governance, and release controls.

## Rollback
For a defective code or documentation release, revert the relevant commit where safe, document the reason, and re-run quality checks. If sensitive data was exposed, follow [the incident runbook](runbooks/sensitive-data-incident.md); a normal revert does not purge Git history.
