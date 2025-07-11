#!/bin/bash

(sudo apt update && sudo apt install keychain -y)

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
--dir ~/.ssh/.keychain \
--gpg2 --agents gpg,ssh \
$(find ~/.ssh -name '*ed25519*' ! -iname '*.pub')

source ~/.ssh/.keychain/$HOSTNAME-sh
source ~/.ssh/.keychain/$HOSTNAME-sh-gpg

# Set GPG environment.
export GPG_TTY=$(tty)
