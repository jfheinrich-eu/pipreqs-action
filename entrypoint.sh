#!/bin/sh -l

pipreqs --force --savepath $INPUT_REQUIREMENT_PATH $INPUT_PROJECT_PATH

set -e
sh -c "ls"

git config --global --add safe.directory /github/workspace
git config --global user.name "$GITHUB_ACTOR"
git config --global user.email "$GITHUB_ACTOR@users.noreply.github.com"

git diff --exit-code --stat $INPUT_REQUIREMENT_PATH && exit 0

git add $INPUT_REQUIREMENT_PATH
git commit -m "Updated $INPUT_PROJECT_NAME requirements file [skip-ci]"

if [ "${GITHUB_EVENT_NAME}" = "pull_request" ]; then
    git push origin $GITHUB_HEAD_REF
else
    git push origin $GITHUB_REF_NAME
fi
