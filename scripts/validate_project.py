#!/usr/bin/env python3
"""Validate repository documentation links and the notebook JSON structure.

This script deliberately does not read the patient-level CSV.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "GOVERNANCE.md",
    "ACKNOWLEDGMENTS.md",
    "cervical-cancer-risk-data.ipynb",
    "docs/architecture.md",
    "docs/installation.md",
    "docs/data-dictionary.md",
    "docs/dataset-card.md",
    "docs/model-card.md",
    "docs/feature-audit.md",
    "docs/methodology.md",
    "docs/evaluation-protocol.md",
    "docs/validation-strategy.md",
    "docs/metric-glossary.md",
    "docs/data-quality.md",
    "docs/data-flow.md",
    "docs/experiment-tracking.md",
    "docs/notebook-walkthrough.md",
    "docs/clinical-use-boundary.md",
    "docs/publication-checklist.md",
    "docs/research-reporting.md",
    "docs/model-governance.md",
    "docs/research-ethics-checklist.md",
    "docs/known-issues.md",
    "docs/technical-debt.md",
    "docs/decision-log.md",
    "docs/release-process.md",
    "docs/support-matrix.md",
    "docs/privacy.md",
    "docs/ethics-and-governance.md",
    "docs/diagrams/research-workflow.mmd",
    "docs/diagrams/feature-leakage.mmd",
    "docs/assets/research-workflow.svg",
    "docs/assets/project-banner.svg",
    "docs/assets/privacy-boundary.svg",
    "docs/assets/evaluation-gates.svg",
    "docs/runbooks/README.md",
    "docs/templates/README.md",
    "scripts/validate_project.py",
    "scripts/audit_dataset_schema.py",
    "tests/test_repository_contract.py",
    "tests/test_dataset_audit.py",
    "requirements-dev.txt",
    "pyproject.toml",
    "Makefile",
    ".github/dependabot.yml",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/ISSUE_TEMPLATE/dataset_change.md",
    ".github/ISSUE_TEMPLATE/model_evaluation.md",
    ".github/DISCUSSION_TEMPLATE/questions.yml",
    ".github/DISCUSSION_TEMPLATE/ideas.yml",
    ".github/pull_request_template.md",
    ".github/workflows/quality-checks.yml",
)


def markdown_files() -> list[Path]:
    """Return Markdown files included in repository navigation checks."""
    return [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]


def find_broken_markdown_links() -> list[str]:
    """Return broken relative Markdown links without opening dataset content."""
    pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)|\[[^\]]+\]\(([^)]+)\)")
    broken: list[str] = []
    for source in markdown_files():
        text = source.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            raw_target = (match.group(1) or match.group(2) or "").strip()
            target = raw_target.split()[0].strip("<>")
            if not target or target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target_path = unquote(target.split("#", 1)[0])
            if not target_path:
                continue
            candidate = (source.parent / target_path).resolve()
            if not candidate.exists():
                broken.append(f"{source.relative_to(ROOT)} -> {target}")
    return broken


def validate_notebook() -> None:
    """Check notebook JSON structure without executing cells or printing outputs."""
    notebook_path = ROOT / "cervical-cancer-risk-data.ipynb"
    with notebook_path.open(encoding="utf-8") as handle:
        notebook = json.load(handle)
    if notebook.get("nbformat") != 4:
        raise ValueError("Expected a nbformat 4 notebook.")
    if not isinstance(notebook.get("cells"), list) or not notebook["cells"]:
        raise ValueError("Notebook is missing its cells list.")


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).is_file()]
    if missing:
        print("Missing required files:")
        print("\n".join(f"  - {path}" for path in missing))
        return 1

    try:
        validate_notebook()
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Notebook validation failed: {error}")
        return 1

    broken = find_broken_markdown_links()
    if broken:
        print("Broken local Markdown links:")
        print("\n".join(f"  - {item}" for item in broken))
        return 1

    print(f"Repository structure passed: {len(REQUIRED_PATHS)} required files.")
    print(f"Notebook JSON passed; checked links in {len(markdown_files())} Markdown files.")
    print("The patient-level CSV was not read by this validator.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
