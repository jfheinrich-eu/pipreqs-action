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
          REPOSITORY: jfheinrich-eu/pipreq-action
```

### Inputs

| Input              | Description                                                                                                     |Default          |
|--------------------|-----------------------------------------------------------------------------------------------------------------|-----------------|
| `PROJECT_PATH`     | Gives the path to the project folder that contains the python files                                             |  .              |
| `REPOSITORY`       | Repository in which is to be written back.Example: Jfheinrich-EU/Pipreqs action                                 |                 |
| `TOKEN`            | Token to write in the repository                                                                                | $GITHUB_TOKEN   |
| `REQUIREMENT_PATH` | Gives the path to the location where requirements.txt has to be saved, including the requirements.txt file name | requirements.txt|
| `PROJECT_NAME`     | Includes the project name in the commit                                                                         |                 |


## Authors
- [@ryan-rozario](https://github.com/ryan-rozario) - Idea & Initial work [ryan-rozario/pipreqs-action](https://github.com/ryan-rozario/pipreqs-action)
- [@afonsoVale](https://github.com/afonsoVale) - Contributor [ryan-rozario/pipreqs-action](https://github.com/ryan-rozario/pipreqs-action)
- [@jfheinrich](https://github.com/jfheinrich) - Contributor on this fork
