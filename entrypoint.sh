#!/bin/sh -l

pipreqs --force --savepath $INPUT_REQUIREMENT_PATH $INPUT_PROJECT_PATH

set -e
sh -c "ls"

git config --global --add safe.directory /github/workspace
git config --global user.name "$GITHUB_ACTOR"
git config --global user.email "$GITHUB_ACTOR@users.noreply.github.com"

git diff --exit-code --stat $INPUT_REQUIREMENT_PATH && exit 0

git remote remove origin
git remote add origin "https://${INPUT_TOKEN}@github.com/${INPUT_REPOSITORY}.git"

git add $INPUT_REQUIREMENT_PATH
git commit -m "Updated $INPUT_PROJECT_NAME requirements file [skip-ci]"

if [ "${GITHUB_EVENT_NAME}" = "pull_request" ]; then
    push_to="$GITHUB_HEAD_REF"
else
    push_to="$GITHUB_REF_NAME"
fi

git push --verbose origin $push_to
