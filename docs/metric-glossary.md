# Model evaluation metric glossary

Metrics depend on the chosen positive class and evaluation population. State both whenever reporting results.

| Metric | Meaning | Important caution |
|---|---|---|
| Accuracy | Fraction of all predictions that are correct | Can conceal poor detection of a rare positive class |
| Sensitivity / Recall | Fraction of actual positives detected | High sensitivity can come with many false positives |
| Specificity | Fraction of actual negatives correctly identified | Does not describe positive predictive value |
| Precision / Positive Predictive Value | Fraction of positive predictions that are truly positive | Depends strongly on prevalence |
| Negative Predictive Value | Fraction of negative predictions that are truly negative | Also prevalence-dependent |
| F1 score | Harmonic mean of precision and recall | Hides the trade-off and does not include true negatives directly |
| ROC-AUC | Ranking performance across false-positive rates | Can look strong with imbalanced data; does not select an operating threshold |
| PR-AUC | Precision-recall summary | Baseline and interpretation depend on positive prevalence |
| Calibration | Agreement between predicted probabilities and observed frequencies | Requires adequate sample size and suitable evaluation design |
| Confusion matrix | Counts of true/false positives and negatives | Always label positive class and row/column orientation |
| MSE | Mean squared numeric prediction error | Not a primary classification performance metric for thresholded labels |

## Reporting requirements
- Define positive class and prevalence.
- Include the confusion matrix.
- Include sensitivity, specificity, precision, and recall.
- Include uncertainty where possible.
- Explain threshold selection and consequences of errors.
- Avoid comparing values calculated on different test sets.
- Do not infer clinical utility from these metrics alone.

The current notebook does not provide a clinically justified threshold or validated operating point.
