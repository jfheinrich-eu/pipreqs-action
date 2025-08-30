#!/bin/bash

(sudo apt update && sudo apt install keychain shellcheck -y)

(gh auth status || gh auth login)

GH_INSTALLED_VERSION=$(gh --version)
GH_LATEST_RELEASE=$(gh release view --json tagName -q .tagName --repo cli/cli)

if [ "$GH_INSTALLED_VERSION" != "$GH_LATEST_RELEASE" ]; then
    echo "Updating GitHub CLI from $GH_INSTALLED_VERSION to $GH_LATEST_RELEASE"

    (type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O"$out" https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& sudo cat "$out" | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y
fi
    gh extension upgrade nektos/gh-act || gh extension install nektos/gh-act

python -m pip install poetry && \
    poetry install --all-groups --no-root && \
	poetry self add poetry-plugin-export && \
	poetry self add 'poethepoet' && \
	poetry self add poetry-git-version-plugin

npm ci

/usr/bin/keychain \
--dir "$HOME"/.ssh/.keychain \
--gpg2 --agents gpg,ssh \
"$(find "$HOME"/.ssh -name '*github*ed25519*' ! -iname '*.pub')"

# shellcheck source=/home/vscode/.ssh/.keychain/$HOSTNAME-sh
# shellcheck disable=SC1091
source "$HOME"/.ssh/.keychain/"$HOSTNAME"-sh
# shellcheck source=/home/vscode/.ssh/.keychain/$HOSTNAME-sh-gpg
# shellcheck disable=SC1091
source "$HOME"/.ssh/.keychain/"$HOSTNAME"-sh-gpg

# Set GPG environment.
GPG_TTY=$(tty)
export GPG_TTY
