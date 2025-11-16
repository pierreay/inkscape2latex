# Dependencies

- Python
- Inkscape

<!-- TODO: Write the different methods from the old documentation: -->
<!---->
<!-- ## Project-wide -->
<!---->
<!-- ScapeX can be installed as a `git` submodule for a self-contained project. -->
<!-- Here is an example installing it into `TOPLEVEL_PROJECT/modules/scapex`: -->
<!---->
<!-- ```bash -->
<!-- cd TOPLEVEL_PROJECT && mkdir modules -->
<!-- git submodule add https://github.com/pierreay/scapex modules/scapex -->
<!-- ```  -->
<!---->
<!-- You have then to add `scapex/bin` into your `$PATH` using your preferred method. -->
<!-- Here is an exemple: -->
<!---->
<!-- ```bash -->
<!-- cat << EOF > .env -->
<!-- export PATH="${PATH}${PATH+:}$(realpath modules/scapex/bin)" -->
<!-- EOF -->
<!-- ``` -->
<!---->
<!-- The `.env` file should be sourced in the current shell, using a plugin (*e.g*, using [`dotenv`](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/dotenv) or `direnv`) or either manually: -->
<!---->
<!-- ```bash -->
<!-- source .env -->
<!-- ``` -->
<!---->
<!-- ## System-wide -->
<!---->
<!-- ScapeX can be installed system-wide for a single user. -->
<!-- Here is an example installing it into `~/.local/src/scapex`: -->
<!---->
<!-- ```bash -->
<!-- mkdir ~/.local/src && cd ~/.local/src -->
<!-- git clone https://github.com/pierreay/scapex -->
<!-- ``` -->
<!---->
<!-- You have then to add `scapex/bin` into your `$PATH` using your preferred method. -->
<!-- Here is an exemple for Bash: -->
<!---->
<!-- ```bash -->
<!-- cat << EOF >> ~/.bashrc -->
<!-- export PATH="${PATH}${PATH+:}${HOME}/.local/src/scapex/bin" -->
<!-- EOF -->
<!-- ``` -->
