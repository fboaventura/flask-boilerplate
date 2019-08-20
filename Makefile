.PHONY: help prepare-dev test lint run doc

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PIP=$(VENV_NAME)/bin/pip
PYTHON=$(VENV_NAME)/bin/python

.DEFAULT: help
help:
		@echo "make venv"
		@echo "       prepare the venv environment"
		@echo "make test"
		@echo "       run tests"
		@echo "make lint"
		@echo "       run pylint and mypy"
		@echo "make run"
		@echo "       run project"
		@echo "make clean_cache"
		@echo "       clean up pyc and __pycache__ files and folders"
		@echo "make doc"
		@echo "       build sphinx documentation"

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
		test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
		$(PYTHON) -m pip install -U pip
		$(PYTHON) -m pip install -r requirements.txt
		touch $(VENV_NAME)/bin/activate

#test: venv
#		$(PYTHON) -m pytest

#lint: venv
#		$(PYTHON) -m pylint
#		$(PYTHON) -m mypy

run: venv
		$(PYTHON) run.py

clean_cache:
		find . -type f -iname '*.pyc' -delete
		find . -type d -iname __pycache__ -delete

#doc: venv
#		$(VENV_ACTIVATE) && cd docs; make html
