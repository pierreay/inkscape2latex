# How to run

Follow one of the following method to run `scapex` directly from the repository --- including changes from the working directory.

In both case, ensure that the following binaries are available in your `PATH`:
- `inkscape`

## Method 1 -- Without virtual environment

This method use a Bash script located in `bin`, allowing to execute `scapex` directly without involving Python virtual environment.

<!-- Ensure that the following Python packages are available in your `PYTHONPATH`: -->
<!-- - `colorlog` -->

You can test the script using:

```bash
./bin/scapex -h
```

Update your `PATH` to include it:

```bash
export PATH="$(realpath bin):${PATH}"
```

You are now able to run `scapex`:

```bash
scapex -h
```

## Method 2 -- With a virtual environment

This method use the Makefile to create a local virtual environment using `venv` under the repository root.
This will automatically install necessary Python packages inside the `venv`.

First, create the virtual environment:

```bash
make venv
```

Activate it to update the `PATH` and `PYTHONPATH` variables:

```bash
source .venv-scapex/bin/activate
```

You are now able to run `scapex`:

```bash
scapex -h
```

<!-- TODO: To write -->
<!-- # How to code -->

<!-- TODO: To write -->
<!-- # How to push upstream -->
