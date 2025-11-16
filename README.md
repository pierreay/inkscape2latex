<p align="center">
    <a href="https://github.com/pierreay/scapex">
        <img align="center" src="https://github.com/pierreay/scapex/raw/master/doc/logo.svg" width="300"/>
    </a>
</p>

# ScapeX — The command-line Inkscape eXporter, Makefile and LaTeX friendly

<!-- TODO: When the screencast is done... -->
<!-- <p align="center"> -->
<!--     <a href="https://github.com/pierreay/scapex/raw/master/doc/demo.gif"> -->
<!--         <img src="https://github.com/pierreay/scapex/raw/master/doc/demo.gif"/> -->
<!--     </a> -->
<!-- </p> -->

<p align="center">
    <a href="https://inkscape.org/"><img src="https://img.shields.io/badge/Inkscape-e0e0e0?style=for-the-badge&logo=inkscape&logoColor=080A13"></a>
    <a href="https://www.latex-project.org/"><img src="https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a>
    <br>
    <a href="https://pypi.org/project/scapex/"><img src="https://badge.fury.io/py/scapex.svg"></a>
</p>

**ScapeX** is a **Python** utility that invokes **Inkscape** to export an **SVG** drawing into a single **PDF** file or a set of **PDFs**.

It is designed to export **high-quality drawings**, graphics, and diagrams, hence the choice of the PDF format for vector graphics.
The design of the command-line interface makes it suitable for on-the-fly usage or integration in a **Makefile**-based build system (*e.g.*, for **LaTeX**).
In addition, thanks to its `fragments` export feature, this tool can be used to **create animated slides** (*e.g.*, using **Beamer**).

# Features

- Command-line interface with **autocompletion**
- Each **figure export** can be **configured via a sidecar TOML** file
- The `fragments` export mode **creates multiple PDFs** based on **arbitrary layer combinations**
- **Fonts rendering** can be performed either by **Inkscape** during *export* or by **LaTeX** during *compilation*
- **Out-of-tree** export capability

# Installation

The easiest way to install ScapeX is to use [PipX](https://pipx.pypa.io/stable/), a [Pip](https://pip.pypa.io/en/stable/) wrapper that automatically creates a [virtual environment](https://docs.python.org/3/library/venv.html).

```bash
pipx install scapex
````

To enable Zsh autocompletion, add the following to your `~/.zshrc`:

> [!WARNING]
> This must be added **before** the very first call to `compinit` (which initializes the autocompletion system).

```zshrc
which scapex >/dev/null && fpath+=($(scapex --completions-zsh))
```

Restart your shell and you are ready to go!

# Usage

The simplest usage is to export a single PDF file, optionally into another build directory:

```bash
scapex -o BUILD_DIRECTORY INPUT.svg
```

## Fragments (animations)

To create animated exports, first generate a TOML configuration file for your diagram:

```bash
scapex --generate INPUT.svg
```

Open the file and adjust its configuration according to the layer identifiers defined in Inkscape:

```bash
vim INPUT.toml
```

Once ready, perform the `fragments` export:

```bash
scapex --fragments INPUT.svg
```

## Interfacing with LaTeX (fonts rendering)

Fonts rendering can be delegated to LaTeX using the `--fonts-engine=latex` option.
This will create a `.pdf_tex` sidecar file to the `.pdf`, containing the text that will be processed by LaTeX when including the exported PDF with `\input{FILE.pdf_tex}`:

```bash
scapex --fonts-engine=latex INPUT.svg
```

## Interfacing with Makefile

ScapeX can also be used inside a Makefile, enabling automatic export when a drawing is modified and proper dependency handling.
See the self-documented example under [examples/Makefile](./examples/Makefile).

## Getting help

For additional usage, see `scapex -h`:

```bash
usage: scapex [-h] [-v] [-o OUTPUT_DIR] [--generate]
              [--fonts-engine {latex,inkscape}] [--fragments | --no-fragments]
              [--completions-zsh]
              [SVG_FILE]

The command-line Inkscape eXporter, Makefile and LaTeX friendly

positional arguments:
  SVG_FILE              Inkscape drawing in SVG format to export

options:
  -h, --help            show this help message and exit
  -v, --verbose         Increase verbosity if set
  -o, --output-dir OUTPUT_DIR
                        Set the output directory [default = .]
  --generate            Generate a TOML template configuration file for input
                        SVG file (instead of exporting)
  --fonts-engine {latex,inkscape}
                        Set the font rendering engine [default = inkscape]
  --fragments, --no-fragments
                        Enable (or disable) fragments exportation (instead of
                        full exportation) [default = False]
  --completions-zsh     Print the path of the directory containing the Zsh
                        autocompletion script (instead of exporting)
```
