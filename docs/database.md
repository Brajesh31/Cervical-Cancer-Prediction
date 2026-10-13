# Data and database

## Database status

The repository does not define a database, ORM, schema migration, account
store, or persistence layer. The analysis is performed in a Jupyter kernel
against a committed CSV file. The CSV is data storage in Git, not an
application database.

## Dataset profile and source

The tracked CSV contains 858 rows and 36 columns covering age, behavior,
reproductive-health information, STDs, diagnoses, and screening results. Its
structure matches the UCI Cervical Cancer (Risk Factors) dataset profile, but
the exact transformation history of this local copy is not recorded.

UCI attributes the source dataset to Kelwin Fernandes, Jaime Cardoso, and
Jessica Fernandes (2017), DOI 10.24432/C5Z310, and lists it under CC BY 4.0.
See the UCI record and attribution details in README.md and LICENSE.

## Sensitive data

These are patient-level health-related records. The absence of a visible name
column does not make the records non-sensitive. Some fields concern sexual
health and reproductive history. Handle the CSV and saved notebook outputs
under the license, privacy, and governance requirements applicable to your
use.

Do not add new patient records or share row-level values in public issues,
screenshots, rendered notebooks, or unapproved hosted environments.

## Missing values and cleaning

The source uses question-mark sentinels for unanswered values. The notebook
contains a commented-out replacement line and later calls dropna. If literal
question marks are not converted to recognized missing values, dropna will
not remove them. Verify the parser and document row counts for each cleaning
step before interpreting results.

## Persistence and retention

The notebook does not write predictions to a database or save a trained
estimator. Jupyter may save cell outputs into the notebook file, and users may
save derived files manually. Hosted notebook services may retain kernels,
files, logs, or backups according to their own controls.

## Governance before future storage

Before adding a database, cache, upload, or hosted inference service, define
the purpose, minimum fields, lawful authority, access control, encryption,
retention, deletion, backup lifecycle, incident process, and accountable
operator. Update the data-flow documentation and privacy notice before
collecting additional information.
## Provenance limitation

The repository does not include a checksum or documented transformation
history for the CSV. Treat its UCI attribution as the likely source based on
its schema and dimensions, and confirm the exact provenance before
redistributing transformed data.
## Notebook outputs

Executed table displays and feature previews are saved in the notebook. They
can preserve record-level information even if the CSV is later removed from
a derivative package. Review outputs before sharing.
## Data license versus code license

Original project code is under MIT. The likely source dataset is listed by UCI
under CC BY 4.0. Preserve the correct attribution and license for each
component; one notice does not replace the other.
