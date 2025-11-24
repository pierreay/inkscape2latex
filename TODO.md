# ONGOING

- Continue writing `CONTRIBUTING.md`

# FUTURE

## Features

- Add a `--version` option

## Documentation

- Write a user manual in Markdown or reStructuredText (see `doc/user-manual.md`)

## Reliability

- Implement an Inkscape logging mechanism
    - Log output of Inkscape into a temporary log files
    - Display its content if `-v / --verbose` is passed on command line
    - Parse the logging output of Inkscape to display important messages, *e.g.*,
        - `'parse rerror|failed to create document'`
