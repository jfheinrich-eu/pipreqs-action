# Generate Python Requirements.txt 🐍

[![GitHub release](https://img.shields.io/github/v/release/jfheinrich-eu/pipreqs-action)](https://github.com/jfheinrich-eu/pipreqs-action/releases)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-generate--python--requirements-blue?logo=github)](https://github.com/marketplace/actions/generate-python-requirements-txt)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/jfheinrich-eu/pipreqs-action)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**🚀 Available on [GitHub Actions Marketplace](https://github.com/marketplace/actions/generate-python-requirements-txt)**

> **Note**: This project is a fork and enhancement of [ryan-rozario/pipreqs-action](https://github.com/ryan-rozario/pipreqs-action) with significant improvements and additional features.

Automated Python requirements and dependency management for CI/CD, DevOps, and package-management workflows. Uses pipreqs for fast, reliable automation of requirements.txt generation and continuous integration.

## ✨ Features

- 🔄 **Python Dependency Management Automation**: Uses pipreqs to analyze imports and generate requirements
- ⚡ **CI/CD & DevOps Integration**: Designed for continuous integration and DevOps workflows
- 📦 **Package Management**: Handles requirements and dependencies for Python projects
- 🛠️ **Automation**: Fully automated requirements.txt generation and updates
- 🔍 **Recursive Scanning**: Optional recursive directory scanning
- ⚡ **Duplicate Handling**: Intelligent handling of duplicate packages with different versions
- ⚠️ **GitHub Warnings**: Automatic warnings in GitHub Actions logs for conflicts
- 🧪 **Comprehensive Testing**: 100% test coverage with robust error handling
- 🐳 **Docker Support**: Containerized execution for consistent environments
- 📊 **Detailed Logging**: Enhanced logging for debugging and monitoring

## 🚀 Quick Start

Add this action to your workflow to automatically generate or update your `requirements.txt`:

```yaml
name: Update Requirements
on: [push, pull_request]
jobs:
  requirements:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5

      - name: Generate Requirements
        uses: jfheinrich-eu/pipreqs-action@v4.4.2  # Use latest stable version
        with:
          PROJECT_PATH: "."
          REQUIREMENT_PATH: "requirements.txt"
          RECURSIVE: "true"

      - name: Commit Changes
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: 'chore: update requirements.txt [skip ci]'
          file_pattern: requirements.txt
```

## 📋 Inputs

| Input              | Description                                                                                                     | Required | Default                             |
|--------------------|-----------------------------------------------------------------------------------------------------------------|----------|-------------------------------------|
| `PROJECT_PATH`     | Path to the project folder containing Python files                                                             | ✅       | `/github/workspace`                 |
| `REQUIREMENT_PATH` | Path where `requirements.txt` should be saved (including filename)                                             | ✅       | `/github/workspace/requirements.txt`|
| `RECURSIVE`        | Whether to scan directories recursively (`'true'` or `'false'`)                                                | ✅       | `'true'`                            |

## 🔧 Advanced Usage

### Custom Project Structure

```yaml
- name: Generate Requirements for Specific Directory
  uses: jfheinrich-eu/pipreqs-action@v4.1.0  # Or pin to SHA: @a1b2c3d4...
  with:
    PROJECT_PATH: src/my_package
    REQUIREMENT_PATH: requirements/base.txt
    RECURSIVE: 'false'
```

### Multiple Requirements Files

```yaml
- name: Generate Requirements for API
  uses: jfheinrich-eu/pipreqs-action@v4.1.0  # Or pin to SHA: @a1b2c3d4...
  with:
    PROJECT_PATH: api
    REQUIREMENT_PATH: api/requirements.txt
    RECURSIVE: 'true'

- name: Generate Requirements for Web App
  uses: jfheinrich-eu/pipreqs-action@v4.1.0  # Or pin to SHA: @a1b2c3d4...
  with:
    PROJECT_PATH: webapp
    REQUIREMENT_PATH: webapp/requirements.txt
    RECURSIVE: 'true'
```

### Security Best Practice - SHA Pinning

For maximum security in production environments, pin to specific commit SHA:

```yaml
- name: Generate Requirements (SHA Pinned)
  uses: jfheinrich-eu/pipreqs-action@a1b2c3d4e5f6789012345678901234567890abcd
  with:
    PROJECT_PATH: src
    REQUIREMENT_PATH: requirements.txt
    RECURSIVE: 'true'
```

> **Why SHA pinning?** Commit SHAs are immutable and prevent supply chain attacks via tag manipulation.

## ⚡ Key Improvements Over Original

This fork includes several enhancements over the original [ryan-rozario/pipreqs-action](https://github.com/ryan-rozario/pipreqs-action):

### 🔄 Duplicate Package Handling
- **Smart Version Resolution**: Automatically selects the highest version when duplicate packages are found
- **Conflict Warnings**: Displays GitHub Actions warnings when version conflicts are detected
- **Clean Output**: Eliminates duplicate entries in `requirements.txt`

### 🧪 Enhanced Testing & Quality
- **98% Test Coverage**: Comprehensive unit and integration tests
- **Type Safety**: Full type annotations and mypy compliance
- **Code Quality**: Pylint, Black, and isort integration
- **Pre-commit Hooks**: Automated code quality checks

### 🐳 Modern Development Practices
- **Poetry Support**: Modern Python dependency management
- **Docker Integration**: Containerized execution environment
- **CI/CD Pipeline**: Automated testing and release workflows
- **Documentation**: Comprehensive README and inline documentation

## 🛠️ Development

### Prerequisites

- Python 3.12+
- Poetry
- Docker (optional)

### Setup

```bash
# Clone the repository
git clone https://github.com/jfheinrich-eu/pipreqs-action.git
cd pipreqs-action

# Install dependencies
poetry install --all-groups

# Run tests
poetry poe test

# Run linting
poetry poe lint

# Format code
poetry poe format
```

### Poetry Environment Management

The repository includes a robust script for managing Poetry virtual environments, which helps maintain a consistent development environment.

```bash
# Run with Poetry Exec
poetry poe reset_venv

# Or directly from scripts folder
./scripts/reset-poetry-venv
```

Available options:

```
Options:
  -h, --help                 Show this help message
  -r, --reset                Completely reset the environment (includes cache and config)
  -u, --update               Update the existing environment (default)
  -n, --new                  Create a new environment
  -p, --python VERSION       Specify Python version (e.g., 3.12)
  -d, --delete-venv          Delete the virtual environment only
  -c, --clear-cache          Clear Poetry cache
  -g, --clear-config         Clear Poetry configuration
  -i, --install-poetry       Reinstall Poetry
  -v, --verbose              Enable verbose output

Examples:
  ./scripts/reset-poetry-venv --reset                 # Complete reset
  ./scripts/reset-poetry-venv --update                # Update dependencies
  ./scripts/reset-poetry-venv --new --python 3.12     # Create with Python 3.12
```

When run without parameters, the script enters interactive mode with a menu of options. The script automatically configures VS Code to use the Poetry virtual environment.

### Testing

```bash
# Run all tests with coverage
poetry poe test

# Run specific test file
pytest tests/test_main.py -v

# Generate coverage report
pytest --cov --cov-report=html
```

## 📖 Examples

### Basic Python Project

```
my-project/
├── src/
│   ├── main.py          # imports: requests, pandas
│   └── utils.py         # imports: numpy, matplotlib
├── requirements.txt     # Generated: requests, pandas, numpy, matplotlib
└── .github/
    └── workflows/
        └── requirements.yml
```

### Monorepo Structure

```
monorepo/
├── api/
│   ├── app.py          # imports: fastapi, sqlalchemy
│   └── requirements.txt # Generated: fastapi, sqlalchemy
├── worker/
│   ├── tasks.py        # imports: celery, redis
│   └── requirements.txt # Generated: celery, redis
└── .github/workflows/requirements.yml
```

## 🎯 GitHub Actions Marketplace

This action is available on the [GitHub Actions Marketplace](https://github.com/marketplace/actions/generate-python-requirements-txt). It falls under the following categories:

### 📦 **Dependency Management**
- Automatically analyzes Python projects for dependencies and requirements
- Generates clean, deduplicated requirements.txt files for package-management
- Handles version conflicts intelligently for dependency-management

## 🔧 **Continuous Integration**
- Integrates seamlessly with GitHub Actions workflows for CI/CD
- Provides detailed logging and error reporting for automation and DevOps
- Supports various project structures and layouts for continuous-integration

## 🐍 **Python Development**
- Specialized for Python ecosystem and package-management
- Works with all major Python package managers and dependency-management tools
- Supports both standard library and third-party packages

## 💡 **Usage Tips for Marketplace Users**
1. **Version Pinning**: Always use a specific version tag (e.g., `@v4.4.2`) for production workflows
2. **Security**: Consider pinning to a specific commit SHA for maximum security
3. **Testing**: Test the action in a feature branch before deploying to main workflows
4. **Monitoring**: Enable GitHub Actions notifications to stay informed about workflow runs
5. **SEO Keywords**: This action is ideal for Python developers, DevOps engineers, and CI/CD pipelines needing automated dependency and package management. It streamlines continuous integration and ensures up-to-date requirements for every workflow.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Original Project**: [ryan-rozario/pipreqs-action](https://github.com/ryan-rozario/pipreqs-action) by [@ryan-rozario](https://github.com/ryan-rozario)
- **Contributors**: [@afonsoVale](https://github.com/afonsoVale) for contributions to the original project
- **pipreqs**: [bndr/pipreqs](https://github.com/bndr/pipreqs) for the core functionality

## 📊 Project Stats

- **Test Coverage**: 98%
- **Python Version**: 3.12+
- **Dependencies**: Minimal and well-maintained
- **Docker Image Size**: Optimized for CI/CD environments

---

<p align="center">
  <a href="https://github.com/jfheinrich-eu/pipreqs-action/issues">Report Bug</a> •
  <a href="https://github.com/jfheinrich-eu/pipreqs-action/issues">Request Feature</a> •
  <a href="https://github.com/jfheinrich-eu/pipreqs-action/releases">Releases</a>
</p>

## 📈 Keywords

python, requirements, dependencies, pipreqs, automation, ci-cd, package-management, devops, dependency-management, continuous-integration
