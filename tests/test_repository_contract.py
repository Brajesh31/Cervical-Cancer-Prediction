from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.validate_project import (
    REQUIRED_PATHS,
    ROOT,
    find_broken_markdown_links,
    validate_notebook,
)


class RepositoryContractTests(unittest.TestCase):
    def test_required_project_files_exist(self) -> None:
        missing = [path for path in REQUIRED_PATHS if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_notebook_is_valid_nbformat_four_json(self) -> None:
        validate_notebook()
        with (ROOT / "cervical-cancer-risk-data.ipynb").open(encoding="utf-8") as handle:
            notebook = json.load(handle)
        self.assertGreater(len(notebook["cells"]), 0)

    def test_markdown_relative_links_resolve(self) -> None:
        self.assertEqual(find_broken_markdown_links(), [])

    def test_readme_contains_medical_safety_boundary(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("not a diagnostic system", readme)
        self.assertIn("not clinically validated", readme)
        self.assertIn("patient-level", readme)

    def test_data_path_mismatch_is_documented(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("data.csv", readme)
        self.assertIn("DATA _SET (1).csv", readme)


if __name__ == "__main__":
    unittest.main()
