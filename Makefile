# Variables
# ==============================================================================

# Main package name (also used as command-line script name in `pyproject.toml`)
PKG_NAME=scapex

# Whether to download/upload from/on official or testing PyPi [testpypi | pypi]
UPLOAD_REPO=testpypi

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
venv: .venv-$(PKG_NAME)/bin/$(PKG_NAME)

# Build the Python distribution for uploading
build: clean
	python -m build

# Upload the Python distribution on PyPi
upload: build
ifeq ($(UPLOAD_REPO),testpypi)
	twine upload --verbose --repository testpypi dist/*
else
	twine upload --verbose dist/*
endif

# Install using PipX
install:
ifeq ($(UPLOAD_REPO),testpypi)
	pipx install --index-url https://test.pypi.org/simple/ $(PKG_NAME)
else
	pipx install $(PKG_NAME)
endif

# Uninstall using PipX
uninstall:
	pipx uninstall $(PKG_NAME)

# Clean all generated files during building and installing
# NOTE: Sync with `.gitignore`
clean:
	rm -rf build
	rm -rf dist
	rm -rf src/$(PKG_NAME).egg-info
	rm -rf src/$(PKG_NAME)/__pycache__
	rm -rf .venv-scapex
	cd examples && make clean
