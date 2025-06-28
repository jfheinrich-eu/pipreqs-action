# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v4.3.0] - 2025-06-28
### :sparkles: New Features
- [`0df55bd`](https://github.com/jfheinrich-eu/pipreqs-action/commit/0df55bdbfd1dddd9fa2e4aa9b2085ad8c88a103f) - add Dockerfile for building custom Python image with Git *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`d8d5020`](https://github.com/jfheinrich-eu/pipreqs-action/commit/d8d5020e73d763040173871263989ed8f8f2c126) - add GitHub workflows for labeler and CI configuration *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`e92a644`](https://github.com/jfheinrich-eu/pipreqs-action/commit/e92a644eb58f33726a0060a0cd1c3eed98a10704) - update Python version to 3.12 in lint_tests workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :bug: Bug Fixes
- [`9f411cb`](https://github.com/jfheinrich-eu/pipreqs-action/commit/9f411cb727e508f23c9efdf4eff7a179868c3b86) - update Dockerfile to use pipreqs-action base image and streamline build process *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :recycle: Refactors
- [`59dd441`](https://github.com/jfheinrich-eu/pipreqs-action/commit/59dd441a12692431cee3f8a481354c61b9abc6c3) - improve code structure and readability in app.py, helper.py, main.py, and test_main.py *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`0c510ce`](https://github.com/jfheinrich-eu/pipreqs-action/commit/0c510ce944a84c84b2fd926ba02da48bc12ac384) - reorganize pytest configuration in pyproject.toml for improved clarity *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`4698d52`](https://github.com/jfheinrich-eu/pipreqs-action/commit/4698d529e1d562956994cf5bb9ca1588d5659ee6) - enhance module docstrings for clarity in app.py, helper.py, and main.py *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`6b1ffe2`](https://github.com/jfheinrich-eu/pipreqs-action/commit/6b1ffe2632ea5c9f29c9fdea8e3603a6418c73ed) - update module docstring in test_main.py for improved clarity *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`60c5acb`](https://github.com/jfheinrich-eu/pipreqs-action/commit/60c5acb002dc8b2988f68a816c063154c6ae5ac2) - clean up code formatting and improve readability in workflow and Python files *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`1580074`](https://github.com/jfheinrich-eu/pipreqs-action/commit/1580074f4e5d3b81f062e69f9c53d47f021d894f) - comment out poetry installation in postAttachCommands.sh *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.2.7] - 2025-06-21
### :recycle: Refactors
- [`9fa66e2`](https://github.com/jfheinrich-eu/pipreqs-action/commit/9fa66e2ec383308c72abe040c34ffa2ef7ca6838) - consolidate release creation and asset upload steps in workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.2.5] - 2025-06-21
### :bug: Bug Fixes
- [`a97372b`](https://github.com/jfheinrich-eu/pipreqs-action/commit/a97372b819682eae6068b903ff51ed5f6819c846) - update Python version in Dockerfile and correct pip install command in postAttachCommands.sh *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.2.4] - 2025-06-21
### :bug: Bug Fixes
- [`c8b292e`](https://github.com/jfheinrich-eu/pipreqs-action/commit/c8b292e0ff1bfbb57be5adaa9bab33545bf96306) - update .gitignore to include coverage directory *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`d44e651`](https://github.com/jfheinrich-eu/pipreqs-action/commit/d44e651b078ce6e5a34f487f37f1b27b4495e631) - correct file permission command and improve argument validation *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.2.3] - 2025-06-14
### :bug: Bug Fixes
- [`338b803`](https://github.com/jfheinrich-eu/pipreqs-action/commit/338b8034fd83a7083893f09a389c69644b158f7c) - specify exact versions for pipreqs and GitPython in dependencies *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.2.1] - 2025-04-27
### :bug: Bug Fixes
- [`d48f035`](https://github.com/jfheinrich-eu/pipreqs-action/commit/d48f03507491ff96555256c4dd33195a7f807762) - resolve workflow permission issues *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.1.1] - 2025-04-25
### :sparkles: New Features
- [`1a71c3e`](https://github.com/jfheinrich-eu/pipreqs-action/commit/1a71c3e0d896c4c058ab4bcc2e514707d5448f8d) - add template sync *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :bug: Bug Fixes
- [`ecc80f0`](https://github.com/jfheinrich-eu/pipreqs-action/commit/ecc80f063744508c6c91c03be1b519d0d3c1a673) - resolve image name issues *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`c45d500`](https://github.com/jfheinrich-eu/pipreqs-action/commit/c45d50046a9229094f5ded0c54cd31384994deaa) - **deps**: bump pytest from 7.4.3 to 8.3.5 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`c0124a8`](https://github.com/jfheinrich-eu/pipreqs-action/commit/c0124a8b7996b5d123258c885196fb7c0a3a9a75) - **deps**: bump pipreqs from 0.4.13 to 0.5.0 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*


## [v4.1.0] - 2025-04-20
### :sparkles: New Features
- [`b3ed5d6`](https://github.com/jfheinrich-eu/pipreqs-action/commit/b3ed5d68a20956258dadc8bd3f5264f06ec91e4d) - add python script to collect the reqs recursively *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :bug: Bug Fixes
- [`e80f5c4`](https://github.com/jfheinrich-eu/pipreqs-action/commit/e80f5c4e477de05c6ab30c40893f8a3739427ccf) - resolve flake8 issues *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`c2a57a3`](https://github.com/jfheinrich-eu/pipreqs-action/commit/c2a57a3be76b7c95814a0ac3d46df52e992e7365) - add missing pytest *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`8a97fc0`](https://github.com/jfheinrich-eu/pipreqs-action/commit/8a97fc0b4b1b53a736437d888639e4c0f350494c) - add missing pipreqs *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :recycle: Refactors
- [`79956d5`](https://github.com/jfheinrich-eu/pipreqs-action/commit/79956d55a52b8ebe7608bf857e2a69347a846578) - full refactor of requirements.txt creation *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`395c5eb`](https://github.com/jfheinrich-eu/pipreqs-action/commit/395c5ebfde58d064140487de16d4c6a5d0633ee0) - remove backup copies *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`6686017`](https://github.com/jfheinrich-eu/pipreqs-action/commit/66860179dba8bd81e1ccee15e855053daa690035) - remove misplaced requirements.txt *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.0.3] - 2025-04-18
### :bug: Bug Fixes
- [`e5ab1c4`](https://github.com/jfheinrich-eu/pipreqs-action/commit/e5ab1c48cc499e64b2144280afa027b6dd020b27) - exclude dependabot pull requests *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`0f44021`](https://github.com/jfheinrich-eu/pipreqs-action/commit/0f44021afbfe701d233b79b3e8f669db6060fb6c) - refactor git push origin workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`192af1c`](https://github.com/jfheinrich-eu/pipreqs-action/commit/192af1cf9cdd3007fe248fb01931ec1d345b179c) - fix git push back workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`1073801`](https://github.com/jfheinrich-eu/pipreqs-action/commit/1073801b820bf1fe0ad8684245fe425c2169a91f) - **deps**: bump jefflinse/pr-semver-bump from 1.7.1 to 1.7.2 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*


## [v4.0.2] - 2025-04-18
### :bug: Bug Fixes
- [`256cd19`](https://github.com/jfheinrich-eu/pipreqs-action/commit/256cd19187ebf354b3cd194fe86443d034b075bf) - add noop labels *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`19b8f41`](https://github.com/jfheinrich-eu/pipreqs-action/commit/19b8f414e1c9406fe7a29cf1594f3e2202a8e029) - resolve git authentication issue *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.0.1] - 2025-04-13
### :bug: Bug Fixes
- [`ad8acb8`](https://github.com/jfheinrich-eu/pipreqs-action/commit/ad8acb87e2fbf43a13d72d3b8e7eb9c5600bb5c6) - resolve git commit issues *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.0.0] - 2025-04-13
### :sparkles: New Features
- [`0aeb154`](https://github.com/jfheinrich-eu/pipreqs-action/commit/0aeb154551d7aaa630443a5eb509a7c2e51efeb5) - update Dockerfile and entrypoint.sh *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`8ba5bf9`](https://github.com/jfheinrich-eu/pipreqs-action/commit/8ba5bf9f5e1f99c4ba23246ff0f30ba65ecde4d4) - add CODEOWNERS file *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`87e4d43`](https://github.com/jfheinrich-eu/pipreqs-action/commit/87e4d431d7ead3ba3410003736b678a26873dbcd) - add vscode setting *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`1970619`](https://github.com/jfheinrich-eu/pipreqs-action/commit/19706191d51cdd86b443e8f85558e8c4bb91affb) - add pull-request template *(commit by [@jfheinrich](https://github.com/jfheinrich))*

[v4.0.0]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v3.0.0...v4.0.0
[v4.0.1]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.0.0...v4.0.1
[v4.0.2]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.0.1...v4.0.2
[v4.0.3]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.0.2...v4.0.3
[v4.1.0]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.0.3...v4.1.0
[v4.1.1]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.1.0...v4.1.1
[v4.2.1]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.2.0...v4.2.1
[v4.2.3]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.2.2...v4.2.3
[v4.2.4]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.2.3...v4.2.4
[v4.2.5]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.2.4...v4.2.5
[v4.2.7]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.2.6...v4.2.7
[v4.3.0]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.2.7...v4.3.0
