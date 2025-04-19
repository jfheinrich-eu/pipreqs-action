#!/bin/sh -l

pipreqs --force --savepath $INPUT_REQUIREMENT_PATH $INPUT_PROJECT_PATH

set -e
sh -c "ls"
