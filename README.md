# Generate Python Requirements.txt 🐍

[![GitHub release](https://img.shields.io/github/v/release/jfheinrich-eu/pipreqs-action)](https://github.com/jfheinrich-eu/pipreqs-action/releases)
[![GitHub marketplace](https://img.shields.io/badge/marketplace-generate--python--requirements-blue?logo=github)](https://github.com/marketplace/actions/generate-python-requirements-txt)
[![Test Coverage](https://img.shields.io/badge/coverage-98%25-brightgreen)](https://github.com/jfheinrich-eu/pipreqs-action)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Note**: This project is a fork and enhancement of [ryan-rozario/pipreqs-action](https://github.com/ryan-rozario/pipreqs-action) with significant improvements and additional features.

Automatically generates `requirements.txt` files for Python projects using [pipreqs](https://github.com/bndr/pipreqs) with enhanced duplicate handling, GitHub Actions integration, and comprehensive testing.

## ✨ Features

- 🔄 **Automatic Requirements Generation**: Uses pipreqs to analyze Python imports
- 🔍 **Recursive Scanning**: Optional recursive directory scanning
- ⚡ **Duplicate Handling**: Intelligent handling of duplicate packages with different versions
- ⚠️ **GitHub Warnings**: Automatic warnings in GitHub Actions logs for conflicts
- 🧪 **Comprehensive Testing**: 98% test coverage with robust error handling
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
      - uses: actions/checkout@v4
      
      - name: Generate Requirements
        uses: jfheinrich-eu/pipreqs-action@a1b2c3d4e5f6789012345678901234567890abcd  # Pin to SHA for security
        with:
          PROJECT_PATH: src
          REQUIREMENT_PATH: requirements.txt
          RECURSIVE: 'true'
          
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
