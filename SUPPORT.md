# Support

This is a small educational notebook repository maintained on a best-effort
basis. It is not a medical product and does not provide clinical advice,
diagnosis, or guaranteed support response times.

## Before asking for help

1. Read README.md and the relevant guide in docs/.
2. Identify the notebook cell and action that failed.
3. Record your operating system, Python version, package versions, and how the
   notebook was launched.
4. Reproduce the issue with synthetic or otherwise non-sensitive input.
5. Search existing repository issues for a related report.

## Technical questions and bugs

Open a GitHub issue with a clear title, the expected and observed behavior,
the relevant cell, and sanitized error output. Include the dependency versions
when the problem may depend on the environment. Do not attach the CSV, copied
patient rows, saved notebook output, or private health information.

## Where to report

- Use an issue for a documentation question or reproducible technical problem.
- Read CONTRIBUTING.md before submitting a change.
- Follow SECURITY.md for a suspected vulnerability; do not publish exploit
  details or patient information.
- Follow CODE_OF_CONDUCT.md for a private conduct concern.

## Support boundaries

There is no clinical support, model interpretation service, data-subject
contact process, or commercial service-level commitment. Questions asking for
individual medical advice cannot be answered from this notebook. Contact a
qualified health professional for medical decisions.
## Dataset questions

The local file appears structurally consistent with UCI's Cervical Cancer
(Risk Factors) dataset, but its precise provenance and transformation history
are not recorded. Consult the UCI source and retain attribution if reusing it.
## Missing data questions

The dataset includes question-mark sentinels. The notebook's intended
replacement statement is commented out, and dropna does not necessarily
remove literal question marks. Check parsing and missingness before
interpreting any result.
## Model metric questions

Reported metrics come from one unseeded, non-stratified split and features
include diagnosis or screening fields. They are exploratory and are not
clinical performance evidence. Do not request interpretation for a specific
person.
