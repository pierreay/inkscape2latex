# Variables
# ==============================================================================

# Main package name (also used as command-line script name in `pyproject.toml`)
PKG_NAME=scapex

# Targets
# ==============================================================================

# Create the virtual environnement
.venv-$(PKG_NAME):
	python -m venv $@

# Install the Python package inside the virtual environnement
.venv-$(PKG_NAME)/bin/$(PKG_NAME): .venv-$(PKG_NAME)
	sh -c "source .venv-$(PKG_NAME)/bin/activate && pip install --editable ."

# Goals
# ==============================================================================

# Test logging module
test/log:
	PYTHONPATH=src src/$(PKG_NAME)/log.py

# Install the Python package inside a local virtual environnement in editable mode
install: .venv-$(PKG_NAME)/bin/$(PKG_NAME)

# TODO: Build the Python distribution of our project.
build:
	python -m build

# Clean all generated files during building and installing
# NOTE: Sync with `.gitignore`
clean:
	rm -rf build
	rm -rf dist
	rm -rf src/$(PKG_NAME).egg-info
	rm -rf src/$(PKG_NAME)/__pycache__
	rm -rf .venv-scapex
	cd examples && make clean
