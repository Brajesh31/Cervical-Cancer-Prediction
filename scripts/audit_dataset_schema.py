#!/usr/bin/env python3
"""Print aggregate CSV shape/schema checks without printing patient-level rows.

Run locally in an environment approved for the dataset. This tool reads the
CSV but does not display cell values or upload data.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REQUIRED_FIELDS = {
    "Age",
    "Dx:Cancer",
    "Dx:CIN",
    "Dx:HPV",
    "Hinselmann",
    "Schiller",
    "Citology",
    "Biopsy",
}


def inspect_csv(path: Path) -> dict[str, object]:
    """Return aggregate schema facts; never return or print record values."""
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration as error:
            raise ValueError("CSV is empty.") from error
        row_count = sum(1 for _ in reader)

    if len(header) != len(set(header)):
        raise ValueError("CSV contains duplicate column names.")
    missing_fields = sorted(REQUIRED_FIELDS.difference(header))
    return {
        "rows": row_count,
        "columns": len(header),
        "missing_required_fields": missing_fields,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inspect aggregate CSV shape without printing record values."
    )
    parser.add_argument(
        "csv_path",
        nargs="?",
        default="DATA _SET (1).csv",
        help="Path to the local dataset CSV.",
    )
    parser.add_argument("--expected-rows", type=int, default=858)
    parser.add_argument("--expected-columns", type=int, default=36)
    args = parser.parse_args()

    path = Path(args.csv_path)
    if not path.is_file():
        print(f"Dataset file not found: {path}")
        return 2

    try:
        result = inspect_csv(path)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"Dataset audit failed: {error}")
        return 1

    print(f"Rows: {result['rows']}")
    print(f"Columns: {result['columns']}")
    print(
        "Required schema fields: "
        + ("present" if not result["missing_required_fields"] else "missing")
    )
    if result["missing_required_fields"]:
        print("Missing required field count: " + str(len(result["missing_required_fields"])))
    if result["rows"] != args.expected_rows or result["columns"] != args.expected_columns:
        print(
            "Shape differs from the documented reference "
            f"({args.expected_rows} rows, {args.expected_columns} columns)."
        )
        return 1
    if result["missing_required_fields"]:
        return 1
    print("Aggregate schema check passed. No record values were printed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
