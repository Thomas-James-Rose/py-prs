# PyPrs

To install this as a CLI tool you will need [`pipx`](https://github.com/pypa/pipx). Once setup simply run the following in the root directory of this project:

```sh
pipx install .
```

You can uninstall it using:

```sh
pipx uninstall py-prs
```

## Development

To setup the virtual environment and install dependencies in it run:

```sh
make dev
```

Don't forget to activate the virtual environment:

```sh
# bash or zsh
source .venv/bin/activate.fish

# fish
source .venv/bin/activate.fish

# csh
source .venv/bin/activate.csh
```

To run the tests:

```sh
make test
```
