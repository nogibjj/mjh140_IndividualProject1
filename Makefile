#Variables:
VENV := venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip
BLACK := $(VENV)/bin/black
RUFF := $(VENV)/bin/ruff
PYTEST := $(VENV)/bin/pytest

.PHONY: all venv install format test clean

all: venv install test format lint

#Activate VENV
venv:
	python3 -m venv $(VENV)
	python3 -m pip install --upgrade pip

#Install requirements using VENV
install:
	$(PIP) install -r requirements.txt

#Format using black
format: install
	$(BLACK) src/
	$(BLACK) tests/

#Lint using ruff
lint: format
	$(RUFF) src/

#Perform unit tests under tests/ directory
test: lint
	$(PYTEST) --nbval-lax src/*.ipynb
	$(PYTEST) tests/

#Clean __pycache__ and remove venv
clean: test
	rm -rf __pycache__
	rm -rf $(VENV)