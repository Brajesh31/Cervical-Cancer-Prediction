from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from scripts.audit_dataset_schema import REQUIRED_FIELDS, inspect_csv


class DatasetAuditTests(unittest.TestCase):
    def test_inspect_csv_returns_aggregate_counts_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            csv_path = Path(temporary_directory) / "synthetic.csv"
            fields = sorted(REQUIRED_FIELDS)
            with csv_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(fields)
                writer.writerow(["synthetic" for _ in fields])
                writer.writerow(["synthetic" for _ in fields])

            result = inspect_csv(csv_path)

        self.assertEqual(result["rows"], 2)
        self.assertEqual(result["columns"], len(fields))
        self.assertEqual(result["missing_required_fields"], [])
        self.assertNotIn("records", result)

    def test_duplicate_headers_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            csv_path = Path(temporary_directory) / "duplicate.csv"
            csv_path.write_text("Age,Age\n20,21\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                inspect_csv(csv_path)


if __name__ == "__main__":
    unittest.main()
