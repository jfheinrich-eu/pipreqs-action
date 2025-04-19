# Automatic requirement.txt for Python Projects on Github

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

[pipreqs](https://github.com/bndr/pipreqs) - Generates pip requirements.txt file based on imports of any project.

This action will automatically create the requirements.txt file for a python project using the pipreqs tool.

You can specify the location of your project folder that contains all the python files within your repository.
You can specify the path to which your requirement.txt has to be saved.
You can specify should the requirements collect recursively or not.

This action works good with the action `stefanzweifel/git-auto-commit-action` together, to commit the changes back to th branch

## Usage <a name = "usage"></a>

### Example workflow

```yaml
name: Integration Test
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Automatic requirements.txt for Python Project
        uses: jfheinrich-eu/pipreqs-action@master

        # Put an example of mandatory inputs here
        with:
          PROJECT_PATH: project_folder   #default is the root of the repository
          REQUIREMENT_PATH: project_folder/requirements.txt  #default is requirement.txt in the root of your repository
          RECURSIVE: 'true'
      - name: Commit changes
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          branch: ${{ github.ref_name }}
          commit_message: 'Updated requirements file on ${{ github.ref_name }} [skip-ci]'
          file_pattern: requirements.txt
```

### Inputs

| Input              | Description                                                                                                     |Default          |
|--------------------|-----------------------------------------------------------------------------------------------------------------|-----------------|
| `PROJECT_PATH`     | Gives the path to the project folder that contains the python files                                             |  .              |
| `REQUIREMENT_PATH` | Gives the path to the location where requirements.txt has to be saved, including the requirements.txt file name | requirements.txt|
| `RECURSIVE`        | Collect the requirements recursively                                                                            | true            |


## Authors
- [@ryan-rozario](https://github.com/ryan-rozario) - Idea & Initial work [ryan-rozario/pipreqs-action](https://github.com/ryan-rozario/pipreqs-action)
- [@afonsoVale](https://github.com/afonsoVale) - Contributor [ryan-rozario/pipreqs-action](https://github.com/ryan-rozario/pipreqs-action)
- [@jfheinrich](https://github.com/jfheinrich) - Contributor on this fork
