#!/bin/sh -l

pipreqs --force --savepath $INPUT_REQUIREMENT_PATH $INPUT_PROJECT_PATH

set -e
sh -c "ls"

git config --global --add safe.directory /github/workspace
git config --global user.name "$GITHUB_ACTOR"
git config --global user.email "$GITHUB_ACTOR@users.noreply.github.com"

git diff --exit-code --stat && exit 0

git add $INPUT_REQUIREMENT_PATH
git commit -m "Updated $INPUT_PROJECT_NAME requirements file [skip-ci]"
git push -u origin HEAD
