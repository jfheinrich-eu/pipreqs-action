#!/bin/bash

(sudo apt update && sudo apt install keychain shellcheck -y)

(gh auth status || gh auth login) && gh extension install https://github.com/nektos/gh-act

(python -m pip install -user pip)
(cd src && pip3 install --user pipreqs pytest pytest-cov flake8 auto8 )
(python3 -m pip install --user pre-commit && pre-commit --version)
# missing dependencis for pre-commit configuration black, isort, pyupgrade
(python3 -m pip install --user black isort pyupgrade)
(python3 -m pip install --user setuptools-scm)
(python3 -m pip install --user .[dev])
#(python -m pip install poetry)
#(poetry install --with dev)


npm ci

/usr/bin/keychain \
--dir "$HOME"/.ssh/.keychain \
--gpg2 --agents gpg,ssh \
"$(find "$HOME"/.ssh -name '*ed25519*' ! -iname '*.pub')"

# shellcheck source=/home/vscode/.ssh/.keychain/$HOSTNAME-sh
# shellcheck disable=SC1091
source "$HOME"/.ssh/.keychain/"$HOSTNAME"-sh
# shellcheck source=/home/vscode/.ssh/.keychain/$HOSTNAME-sh-gpg
# shellcheck disable=SC1091
source "$HOME"/.ssh/.keychain/"$HOSTNAME"-sh-gpg

# Set GPG environment.
GPG_TTY=$(tty)
export GPG_TTY
