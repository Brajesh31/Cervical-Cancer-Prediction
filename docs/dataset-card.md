# Dataset Card: Cervical Cancer (Risk Factors) copy

## Summary
The repository tracks a CSV named `DATA _SET (1).csv` with **858 rows and 36 columns**. Its column names and dimensions appear consistent with the UCI Machine Learning Repository's Cervical Cancer (Risk Factors) dataset. The repository does not contain a checksum or transformation history proving that this exact file is byte-identical to the UCI download.

## Source and attribution
UCI record: [Cervical Cancer (Risk Factors)](https://doi.org/10.24432/C5Z310), credited to Kelwin Fernandes, Jaime Cardoso, and Jessica Fernandes (2017). UCI lists the dataset under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Verify provenance and retain the required attribution before redistribution.

## Content profile
The columns include demographic, behavioral, reproductive-history, sexual-health, diagnosis, and screening information. Values are patient-level and health-related. A schema grouping is maintained in [data-dictionary.md](data-dictionary.md).

## Intended context
This copy is used in an educational notebook exercise. The repository does not document patient recruitment, data collection, consent, study protocol, representativeness, or local transformation lineage. Consult the original dataset record and associated publication for source context.

## Known limitations
- Local file provenance and transformation history are not verified by a stored hash.
- Missing values appear as question-mark sentinels in the source copy.
- No row-level values should be copied into public project discussions.
- A historical dataset is not a substitute for contemporary clinical evidence.
- The dataset cannot by itself establish an appropriate prospective screening population or prediction time.

## Sensitive data handling
Even if names are not present, records can remain sensitive through combinations of demographic and health attributes. Restrict access to approved environments. Inspect notebook outputs, exported figures, logs, and copies. Do not upload the data to unapproved services.

## Licensing
The repository's MIT license applies only to original project code and documentation. The dataset and derivative dataset materials remain subject to their separate terms. See [LICENSE](../LICENSE).

## Update procedure
When the dataset is replaced or transformed, document the canonical source, license, checksum, transformation script, aggregate record counts, schema changes, missing-value semantics, and review/approval. Never include patient-level rows in the change record.
