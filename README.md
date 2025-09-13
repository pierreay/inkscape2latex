# Inkscape2LaTeX

The Inkscape exporter designed for LaTeX projects.

This is a small Bash utility that take an SVG draw to export it in PDF or EPS.
The export can be configured such as:
- The fonts can be rendered by Inkscape during the export of by LaTeX during the compilation of the document,
- The figure can be exported in multiple fragments depending on objects identifiers.

The fragment export feature allows to create animated slides using Beamer.

# Installation

> [!NOTE]
> In the following code snippets, remplace the installation directory by the one of your choice.

## Project-wide

Inkscape2LaTeX can be installed as a `git` submodule for a self-contained project.
Here is an example installing it into `TOPLEVEL_PROJECT/modules/inkscape2latex`:

```bash
cd TOPLEVEL_PROJECT && mkdir modules
git submodule add https://github.com/pierreay/inkscape2latex modules/inkscape2latex
``` 

You have then to add `inkscape2latex/bin` into your `$PATH` using your preferred method.
Here is an exemple:

```bash
cat << EOF > .env
export PATH="${PATH}${PATH+:}$(realpath modules/inkscape2latex/bin)"
EOF
```

The `.env` file should be sourced in the current shell, using a plugin (*e.g*, using [`dotenv`](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/dotenv) or `direnv`) or either manually:

```bash
source .env
```

## System-wide

Inkscape2LaTeX can be installed system-wide for a single user.
Here is an example installing it into `~/.local/src/inkscape2latex`:

```bash
mkdir ~/.local/src && cd ~/.local/src
git clone https://github.com/pierreay/inkscape2latex
```

You have then to add `inkscape2latex/bin` into your `$PATH` using your preferred method.
Here is an exemple for Bash:

```bash
cat << EOF >> ~/.bashrc
export PATH="${PATH}${PATH+:}${HOME}/.local/src/inkscape2latex/bin"
EOF
```

# Usage

## Command-line interface

Inkscape2LaTeX can be used as the following:

```bash
$ inkscape2latex --help
Usage: inkscape2latex [-l LAYERFILE.json] [--inkscape-fonts] INFILE.svg OUTFILE.(pdf | eps)

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
$ inkscape2latex -l utils/layers.json gfx/inkscape/drawing.svg build/gfx/inkscape/drawing.pdf
```

## Makefile

Inkscape2LaTeX is also suitable to be used inside a Makefile for automatic dependency handling.
See the example under [examples/Makefile](./examples/Makefile).
