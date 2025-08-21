#!/bin/bash

(sudo apt update && sudo apt install keychain shellcheck -y)

(gh auth status || gh auth login) && gh extension install https://github.com/nektos/gh-act

(python -m pip install poetry && \
    poetry install --all-groups --no-root && \
    poetry self add poetry-plugin-export && \
    poetry self add 'poethepoet[poetry_plugin]' && \
    poetry self add poetry_git_version_plugin )

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
