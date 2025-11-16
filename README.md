<p align="center">
    <a href="https://github.com/pierreay/scapex">
        <img align="center" src="https://github.com/pierreay/scapex/raw/master/doc/logo.svg" width="300"/>
    </a>
</p>

# ScapeX — The command-line Inkscape eXporter, Makefile and LaTeX friendly

<!-- TODO: When the screencast will be done... -->
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

**ScapeX** is a **Python** utility that will invoke **Inkscape** to export an **SVG** drawing into a single or a set of **PDF** file(s).

It is meant to export **high quality drawings**, graphics and diagrams, therefore the choice for the PDF format containing vector graphics.
The design of the command-line interface makes it suitable to be used as a tool on the fly, or to be included inside a **Makefile**-based build system (*e.g.*, for **LaTeX**).
In addition, this tool with its `fragments` export feature can be used to **create animated slides** (*e.g.*, using **Beamer**).

# Features

- Command-line interface with **autocompletion**
- Each **figure exportation** can be **configured by a sidecar TOML** file
- The `fragments` export mode will **create multiple PDFs** based on **arbitrary layers combinations**
- The **fonts rendering** can be done by **Inkscape** during the **exportation** or by **LaTeX** during the **compilation**
- **Out-of-tree** exportation

# Installation

The easiest way of installing ScapeX is to use [PipX](https://pipx.pypa.io/stable/), a [Pip](https://pip.pypa.io/en/stable/) wrapper creating automatically a [virtual environment](https://docs.python.org/3/library/venv.html).

```bash
pipx install scapex
```

In order to setup the Zsh autocompletion, add the following in your `~/.zshrc`:

> [!WARNING]
> This should be added before the very first call to `compinit` (which initialize the autocompletion system)

```zshrc
which scapex >/dev/null && fpath+=($(scapex --completions-zsh))
```

You are ready to go!

# Usage

The simplest usage is to export a single PDF file, optionally into another build directory:

```bash
scapex -o BUILD_DIRECTORY INPUT.svg
```

The fonts rendering can be let to be controlled by LaTeX using the `--fonts-engine=latex` option.
This will create a `.pdf_tex` sidecar file to the `.pdf` file, containing the text that will be processed by LaTeX when including the exported PDF using the `\input{FILE.pdf_tex}` command:

```bash
scapex --fonts-engine=latex INPUT.svg
```

To create animated export, you can first generate a TOML configuration file for your diagram using:

```bash
scapex --generate INPUT.svg
```

Open the file and modify its configuration according to layer identifier defined in Inkscape:

```bash
vim INPUT.toml
```

Once done, you can perform the `fragments` exportation:

```bash
scapex --fragments INPUT.svg
```

For additional usage, see:

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

ScapeX can also be used inside a Makefile, allowing automatic exportation when a drawing is modified and dependency handling.
See the self-documented example under [examples/Makefile](./examples/Makefile).
