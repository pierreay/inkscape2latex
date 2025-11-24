# Features

- Add a `--version` option

# Documentation

- Write `INSTALL.md`
- Write `CONTRIBUTING.md`
- Write a user manual in Markdown or reStructuredText (see `doc/user-manual.md`)

# Reliability

- If Inkscape crash (*e.g.*, when exportation occurs massively parallel)
    - Seems to possibly crash with this on `stderr` or `stdout`
        ```log
        terminate called after throwing an instance of 'Gio::DBus::Error'
        ```
    - Implement an "execute and retry" mechanism
        - Random sleep between retries
        - Stop retrying after defined number of fails
    - Implement an Inkscape logging mechanism
        - Log output of Inkscape into a temporary log file 
        - Display its content if `-v` is passed on command line
        - Parse the logging output of Inkscape to detect an error
            - Use following regex `'parse rerror|failed to create document'`
