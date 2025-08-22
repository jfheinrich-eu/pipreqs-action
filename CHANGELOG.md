# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v4.4.3] - 2025-08-22
### :sparkles: New Features
- **marketplace**: optimize action.yml for GitHub Marketplace publishing
- **branding**: update icon to "package" and color to "blue" for better marketplace visibility
- **docs**: improve input descriptions for better developer experience

### :wrench: Chores
- **marketplace**: prepare action for GitHub Actions Marketplace publication

## [v4.4.0] - 2025-07-27
### :sparkles: New Features
- [`997f84d`](https://github.com/jfheinrich-eu/pipreqs-action/commit/997f84d2bfb0fa6b8a3e6b719651502c4ad1566f) - enhance save_requirements to handle duplicate modules and keep highest version *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`bc826df`](https://github.com/jfheinrich-eu/pipreqs-action/commit/bc826df8b0565cb5aa2c5d2875c661f916f337da) - update Dockerfile to use specific Python version and enhance build process with additional dependencies *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`dd16b9f`](https://github.com/jfheinrich-eu/pipreqs-action/commit/dd16b9fd388f40d59f2080ebca9870409ee2ad95) - update devcontainer configuration to include shellcheck and improve path handling *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`91e859f`](https://github.com/jfheinrich-eu/pipreqs-action/commit/91e859f90d0fb7c9cd7b83130d7a88773c5bf978) - update pre-commit configuration to include gitleaks and shellcheck, and upgrade flake8 version *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`3e52a3e`](https://github.com/jfheinrich-eu/pipreqs-action/commit/3e52a3eee1ffa9628e48327fb4d1fb17d7752b18) - update VSCode settings for improved Python development and formatting *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`571c76e`](https://github.com/jfheinrich-eu/pipreqs-action/commit/571c76ed86c82578bda653f3c8fac6652167a53c) - add pylint configuration to disable assignment-from-no-return warning *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`0755c73`](https://github.com/jfheinrich-eu/pipreqs-action/commit/0755c736aea8e937686f7dd5b6201530b12901c2) - enhance requirements handling by filtering duplicates and adding warnings *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`9790732`](https://github.com/jfheinrich-eu/pipreqs-action/commit/97907323e26822796e9d6348724866d336d64d29) - **requirements**: improve duplicate module handling, add type safety and tests *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :bug: Bug Fixes
- [`0f15f0c`](https://github.com/jfheinrich-eu/pipreqs-action/commit/0f15f0c75d35a94f981b4e32764ebdf68933b44c) - correct YAML syntax and update platforms for Docker build *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`056737b`](https://github.com/jfheinrich-eu/pipreqs-action/commit/056737bfd49e9b466c546cf18f2f6f8af62bca86) - **docs**: update Docker image documentation link in release workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`f6ae604`](https://github.com/jfheinrich-eu/pipreqs-action/commit/f6ae6042420dbd27d30e1384ddc2abdd243b236a) - sort and clean pyproject.toml sections for clarity and best practices *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`ed33985`](https://github.com/jfheinrich-eu/pipreqs-action/commit/ed33985efbd3fd448a408cc3d3fca8f56e8ca4a6) - **lint**: update pylint configuration for project conventions *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`2d9637e`](https://github.com/jfheinrich-eu/pipreqs-action/commit/2d9637ed1adc1ea717f4aa9685951cb354c0ce78) - remove redundant docstring from main entry point and update helper class comment *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`9e2ee75`](https://github.com/jfheinrich-eu/pipreqs-action/commit/9e2ee75de6cae7b780aee952ebdb0e9fb3ee5bd0) - **project**: update pyproject.toml for improved structure and *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`ac68143`](https://github.com/jfheinrich-eu/pipreqs-action/commit/ac681435cf62c96745b878d5615fabff659559c9) - **vscode**: update VSCode settings for enhanced Python formatting and analysis *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`2e1a787`](https://github.com/jfheinrich-eu/pipreqs-action/commit/2e1a7875cddfab97f18051879d168f96b614e314) - **requirements**: remove GitPython dependency from requirements *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.3.2] - 2025-07-13
### :bug: Bug Fixes
- [`c70b01d`](https://github.com/jfheinrich-eu/pipreqs-action/commit/c70b01d9bc8db4a6b66f3303fd10a5615e1bafa0) - sanitize docker image tag names *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :recycle: Refactors
- [`2b39f0a`](https://github.com/jfheinrich-eu/pipreqs-action/commit/2b39f0a3a4f132be42d8fdec6f4895ec2a292192) - refactor manifest creation *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`2f77592`](https://github.com/jfheinrich-eu/pipreqs-action/commit/2f775921bfe1e480e0a4603365fa1d4e3a8705fa) - build multiarch image in one step *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`7138722`](https://github.com/jfheinrich-eu/pipreqs-action/commit/71387223d51fef73983ab0c0154aeb34fa8d3308) - **vscode**: configure translator *(commit by [@jfheinrich](https://github.com/jfheinrich))*


## [v4.3.1] - 2025-07-12
### :sparkles: New Features
- [`4d5b233`](https://github.com/jfheinrich-eu/pipreqs-action/commit/4d5b23387ce17b25ca205a559e4722e9d70ccb4f) - add Dockerfile change verification and update related actions in release workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :bug: Bug Fixes
- [`f366a96`](https://github.com/jfheinrich-eu/pipreqs-action/commit/f366a96e4644fcbf1519fa39c33af6f692e3f5c9) - resolve secret issues *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`1fa9ecc`](https://github.com/jfheinrich-eu/pipreqs-action/commit/1fa9ecc632217b288fa18c29fb651738ba096f0d) - insert forgotten checkout *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`5cbdbca`](https://github.com/jfheinrich-eu/pipreqs-action/commit/5cbdbca874ce2b477e292c27a9327634fce777da) - rename directory with local action *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`bd170be`](https://github.com/jfheinrich-eu/pipreqs-action/commit/bd170bed31d0957e688f1d40e7fa21493d065a72) - Add inputs to local action *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :recycle: Refactors
- [`ae8e3ca`](https://github.com/jfheinrich-eu/pipreqs-action/commit/ae8e3caeaea0749612db9e8f6a4e6d9f8b79d7b3) - use a complete base image *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`a3cb4b7`](https://github.com/jfheinrich-eu/pipreqs-action/commit/a3cb4b7cc5ca187f3a4c0a888b88eb9be42399a7) - robust and clearer structure *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`6a95086`](https://github.com/jfheinrich-eu/pipreqs-action/commit/6a95086f0dc9a22c5c2eb59159a10b2c6556b01c) - image build and push *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`4cb197c`](https://github.com/jfheinrich-eu/pipreqs-action/commit/4cb197c0837dbcef8be0347ff4c57d362efe35fb) - **deps**: bump jefflinse/pr-semver-bump from 1.7.2 to 1.7.3 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`2232f76`](https://github.com/jfheinrich-eu/pipreqs-action/commit/2232f764fb9e1ea576010ec4457f1b5da99c584f) - **deps**: bump brace-expansion in the npm_and_yarn group *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`d197c25`](https://github.com/jfheinrich-eu/pipreqs-action/commit/d197c2501a1738cd1e9211267dcfa40f9fba70c0) - **deps**: bump @template-tools/sync-cli from 3.5.40 to 3.5.74 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`c6c46a9`](https://github.com/jfheinrich-eu/pipreqs-action/commit/c6c46a931bb5218f92f91211636ec237499905da) - add daily report *(commit by [@jfheinrich](https://github.com/jfheinrich))*


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
[v4.3.1]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.3.0...v4.3.1
[v4.3.2]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.3.1...v4.3.2
[v4.4.0]: https://github.com/jfheinrich-eu/pipreqs-action/compare/v4.3.2...v4.4.0
