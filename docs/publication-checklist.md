# Publication and public-sharing checklist

Use this checklist before publishing a notebook, rendered HTML, chart, poster, report, dataset derivative, or release note.

## Data and licensing
- [ ] Confirm dataset source and provenance as far as possible.
- [ ] Preserve UCI attribution and applicable CC BY 4.0 terms if derived from that source.
- [ ] Confirm rights to redistribute data and derived materials.
- [ ] Do not assume the MIT code license covers the dataset.

## Privacy review
- [ ] Inspect notebook output cells, figures, and HTML exports.
- [ ] Remove unnecessary row-level values and small-group disclosures.
- [ ] Remove local file paths, tokens, account information, and other private metadata.
- [ ] Do not include raw patient rows or screenshots.

## Scientific reporting
- [ ] Define target, positive class, population, and prediction time.
- [ ] Explain feature timing and leakage review.
- [ ] Describe missing-value handling and exclusions.
- [ ] Record split design, random seed, and environment.
- [ ] Report class-aware metrics and uncertainty.
- [ ] State whether independent validation exists.

## Medical safety
- [ ] State that the project is not a diagnostic or screening tool.
- [ ] Do not claim early detection or individual risk estimation.
- [ ] Do not provide treatment or screening advice.
- [ ] Do not imply regulatory approval or clinical readiness.

## Final review
- [ ] Review the full diff and the rendered output.
- [ ] Check links, image alt text, headings, and readability.
- [ ] Record the commit and actual verification performed.
