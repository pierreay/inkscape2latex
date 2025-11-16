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
    <a href="https://badge.fury.io/py/scapex"><img src="https://badge.fury.io/py/scapex.svg"></a>
    <a href="https://badge.fury.io/py/scapex"><img src="https://static.pepy.tech/badge/scapex"></a>
</p>

This is a Python utility that take an SVG draw to export it in PDF.
The export can be configured such as:
- The fonts can be rendered by Inkscape during the export of by LaTeX during the compilation of the document,
- The figure can be exported entirely (full mode) or in multiple fragments depending on layers identifiers.

The fragment export feature allows to create animated slides, *e.g.*, using Beamer.

# Features

- Command-line interface
- Optional per-figure TOML configuration file
- Two different exportation mode, full or fragments
- Project-wide or system-wide installation
- Out-of-tree exportation

# Usage

## Command-line

<!-- TODO: Dump of old Bash help. Write a step by step guide (with one summary screenshot ?) -->

The source file (INFILE) should be an SVG.

If --inkscape-fonts is not passed, the SVG which will be exported in two files:
- An output file excluding text (OUTFILE).
- An sidecar TeX file including text (OUTFILE_tex).
The figure can be included into LaTex using the '\input{OUTFILE.pdf_tex}' command.

If --inkscape-fonts is passed, the SVG which will be exported in one file:
- An output file including text (OUTFILE).
The figure can be included into LaTex using the '\includegraphics{OUTFILE.(pdf}' command.

Optionnaly:
- The script can export multiple layer combinations of the input.
- The supported filetypes for the output is PDF.
    pdf: Portable Document Format (PDF) 
        Support transparancy and page area export.

## Makefile

ScapeX is also suitable to be used inside a Makefile.
It allows automatic exportation and dependency handling, and to be included inside any LaTeX build system.
See the self-documented example under [examples/Makefile](./examples/Makefile).

# Installation

## PipX

```bash
pipx install scapex
```

In order to setup the Zsh autocompletion, add the following in your `~/.zshrc`:

> [!WARNING]
> This should be added before the very first call to `compinit` (which initialize the autocompletion system)

```zshrc
which scapex >/dev/null && fpath+=($(scapex --completions-zsh unexisting.svg))
```

## DEPRECATED

> [!NOTE]
> In the following code snippets, remplace the installation directory by the one of your choice.

## Project-wide

ScapeX can be installed as a `git` submodule for a self-contained project.
Here is an example installing it into `TOPLEVEL_PROJECT/modules/scapex`:

```bash
cd TOPLEVEL_PROJECT && mkdir modules
git submodule add https://github.com/pierreay/scapex modules/scapex
``` 

You have then to add `scapex/bin` into your `$PATH` using your preferred method.
Here is an exemple:

```bash
cat << EOF > .env
export PATH="${PATH}${PATH+:}$(realpath modules/scapex/bin)"
EOF
```

The `.env` file should be sourced in the current shell, using a plugin (*e.g*, using [`dotenv`](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/dotenv) or `direnv`) or either manually:

```bash
source .env
```

## System-wide

ScapeX can be installed system-wide for a single user.
Here is an example installing it into `~/.local/src/scapex`:

```bash
mkdir ~/.local/src && cd ~/.local/src
git clone https://github.com/pierreay/scapex
```

You have then to add `scapex/bin` into your `$PATH` using your preferred method.
Here is an exemple for Bash:

```bash
cat << EOF >> ~/.bashrc
export PATH="${PATH}${PATH+:}${HOME}/.local/src/scapex/bin"
EOF
```

# Usage

## Command-line interface

ScapeX can be used as the following:

```bash
$ scapex --help
Usage: scapex [-l LAYERFILE.json] [--inkscape-fonts] INFILE.svg OUTFILE.(pdf | eps)

Export an Inkscape source file for LaTeX.

The source file (INFILE) should be an SVG.

If --inkscape-fonts is not passed, the SVG which will be exported in two files:
- An output file excluding text (OUTFILE).
- An sidecar TeX file including text (OUTFILE_tex).
The figure can be included into LaTex using the '\input{OUTFILE.(pdf | eps)_tex}' command.

If --inkscape-fonts is passed, the SVG which will be exported in one file:
- An output file including text (OUTFILE).
The figure can be included into LaTex using the '\includegraphics{OUTFILE.(pdf | eps)}' command.

Optionnaly:
- The script can export multiple layer combinations of the input.
- The supported filetypes for the output are PDF and EPS.
    eps: Encapsulated PostScript (EPS)
        Do not support transparancy or page aera export.
    pdf: Portable Document Format (PDF) 
        Support transparancy and page aera export.

Dependencies:
- inkscape
- jq
- bc

Options:
    -l LAYERFILE:       Path to a JSON layer file.
    --inkscape-fonts:   Font rendered by Inkscape intead of LaTeX.

Examples:
$ scapex -l utils/layers.json gfx/inkscape/drawing.svg build/gfx/inkscape/drawing.pdf
```
