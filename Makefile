install:
		pipx install .

uninstall:
		pipx uninstall py-prs

test:
		python -m pytest

lint:
		pylint --rcfile=.pylintrc ./**/*.py

format:
		yapf -r -i .

.venv: 
		python3 -m venv .venv

dev: .venv 
		sh ./install_deps.sh
    