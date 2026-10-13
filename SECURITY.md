# Security Policy

## Scope and limitations

This repository contains a Jupyter notebook and a patient-level health
dataset. It does not implement a web service, authentication, database, or
application security boundary. It is an educational analysis, not a medical
product. The absence of a hosted app does not make the committed dataset or
saved notebook outputs non-sensitive.

## Supported versions

There are no tagged releases or maintained release branches. Reports should
identify the affected commit and file. The maintainer will assess a fix for
the current default branch on a best-effort basis.

## Report a vulnerability privately

Do not publish unpatched vulnerability details, patient-level records,
credentials, or private data in a public issue. Use GitHub's private
vulnerability reporting feature for this repository if enabled. If it is not
available, contact Brajesh31 privately through the GitHub profile and request
a secure reporting route before sending technical details.

Include, when safe:

- The affected commit and file.
- A concise description of impact and prerequisites.
- Minimal reproduction steps that use synthetic data.
- A suggested mitigation, if known.
- A safe way to request follow-up information.

Do not test systems you do not own or have permission to assess.

## Response process

The maintainer will acknowledge and investigate reports as practical, then
coordinate a fix and disclosure timeline with the reporter. Timing depends on
severity and maintainer availability. Allow time for review before public
disclosure.

## Safe handling

- Treat the CSV and notebook outputs as sensitive health-related material.
- Do not upload patient-level rows to public notebook services or analytics.
- Do not commit credentials, private health information, or unapproved data.
- Review notebook output cells before publishing a derivative notebook.
- Keep Python and dependencies updated in the environment you operate.
- Do not treat the model output as an individual diagnosis or clinical action.
