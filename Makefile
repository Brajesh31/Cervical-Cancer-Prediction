PYTHON ?= python

.PHONY: install install-dev notebook validate test audit-data

install:
	$(PYTHON) -m pip install -r requirements.txt

install-dev:
	$(PYTHON) -m pip install -r requirements.txt -r requirements-dev.txt

notebook:
	jupyter notebook cervical-cancer-risk-data.ipynb

validate:
	$(PYTHON) scripts/validate_project.py

test:
	$(PYTHON) -m pytest -q

audit-data:
	$(PYTHON) scripts/audit_dataset_schema.py "DATA _SET (1).csv"

