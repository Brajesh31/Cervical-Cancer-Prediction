# Research result reporting guide

## Minimum context
A result is meaningful only when readers know the dataset, target, positive class, population, feature set, prediction time, cleaning process, split strategy, and evaluation metrics.

## Report structure
1. Research question and educational purpose.
2. Dataset source, provenance confidence, license, and cohort limitations.
3. Target definition and positive-class encoding.
4. Feature list and availability-time audit.
5. Missingness, exclusions, and preprocessing.
6. Split or validation design and randomness.
7. Model specifications and tuning procedure.
8. Confusion matrix and class-aware metrics.
9. Uncertainty, calibration, and validation limitations.
10. Bias, privacy, and ethical considerations.
11. Limitations and non-clinical-use statement.

## Language
Use phrases such as “exploratory classification result on this dataset” and “requires further validation.” Avoid “detects cancer,” “predicts patient risk,” “early diagnosis,” “clinically accurate,” or “ready for doctors.”

## Reproducibility
Link to the source revision and record environment versions. Do not share private row data or dataset exports. Use [experiment tracking](experiment-tracking.md) and the [experiment record template](templates/experiment-record.md).

## Interpretation
Do not infer causality from predictive associations. Do not interpret a high score as evidence that the data represents a current population or that the model would improve health outcomes.
