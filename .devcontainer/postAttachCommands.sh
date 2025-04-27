#!/bin/bash

(gh auth status || gh auth login) && gh extension install https://github.com/nektos/gh-act

(cd src && pip3 install --user pipreqs pytest pytest-cov flake8 auto8)
(cd src && pip3 install --user -r requirements.txt)

npm ci
