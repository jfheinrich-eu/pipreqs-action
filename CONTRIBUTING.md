# Contributing to pipreqs-action

Thank you for your interest in contributing to pipreqs-action! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues
- Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) for bugs
- Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md) for new features
- Search existing issues before creating new ones
- Provide detailed information and reproduction steps

### Submitting Changes

1. **Fork the repository**
2. **Create a feature branch** from `master`
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following our coding standards
4. **Test your changes** thoroughly
5. **Commit with conventional commits**
6. **Submit a pull request**

## 🏗️ Development Setup

### Prerequisites
- Python 3.12+
- Poetry for dependency management
- Docker for containerization
- Git 2.30+

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/jfheinrich-eu/pipreqs-action.git
   cd pipreqs-action
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Activate virtual environment**
   ```bash
   poetry shell
   ```

4. **Install pre-commit hooks**
   ```bash
   poetry run pre-commit install
   ```

### Development Commands

```bash
# Run tests
poetry run pytest

# Run tests with coverage
poetry poe test

# Format code
poetry run black src/ tests/

# Lint code
poetry run flake8 src/ tests/
poetry run pylint src/

# Type checking
poetry run mypy src/

# Run pre-commit on all files
poetry run pre-commit run --all-files
```

## 📋 Coding Standards

### Python Code Style
- Follow **PEP 8** guidelines
- Use **Black** for formatting (line length: 88)
- Use **isort** for import sorting
- Use **type hints** for all functions
- Write **docstrings** for public functions

### Testing
- Write tests for all new functionality
- Maintain **98%+ test coverage**
- Use **pytest** for testing
- Follow **AAA pattern** (Arrange, Act, Assert)

### Example Test Structure
```python
def test_save_requirements_with_duplicates(tmp_path):
    """Test that duplicate modules are handled correctly."""
    # Arrange
    project_path = tmp_path / "test_project"
    project_path.mkdir()

    # Act
    result = main.save_requirements(str(project_path))

    # Assert
    assert result.success is True
    assert len(result.warnings) > 0
```

### Commit Messages
Use [Conventional Commits](https://www.conventionalcommits.org/) format:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `style`: Code formatting changes
- `refactor`: Code refactoring
- `test`: Test additions/modifications
- `chore`: Maintenance tasks

**Examples:**
```
feat(core): add support for custom requirements file names
fix(parser): handle edge case with empty import statements
docs(readme): update usage examples
test(main): add tests for duplicate module handling
```

### Documentation
- Update README.md for user-facing changes
- Update CHANGELOG.md following [Keep a Changelog](https://keepachangelog.com/)
- Include docstrings for all public APIs
- Add inline comments for complex logic

## 🧪 Testing Guidelines

### Test Categories
1. **Unit Tests**: Test individual functions/methods
2. **Integration Tests**: Test component interactions
3. **End-to-End Tests**: Test complete workflows

### Coverage Requirements
- **Minimum**: 95% overall coverage
- **Target**: 98%+ coverage
- Use `# pragma: no cover` sparingly and with justification

### Running Tests

```bash
# All tests
poetry run pytest

# Specific test file
poetry run pytest tests/test_main.py

# With coverage report
poetry run pytest --cov=src --cov-report=html

# Verbose output
poetry run pytest -v

# Fast fail
poetry run pytest -x
```

## 🚀 Release Process

### Version Management
- Uses **semantic versioning** (SemVer)
- Versions are managed by **setuptools-scm** from Git tags
- Create releases through GitHub UI

### Release Checklist
1. Update CHANGELOG.md
2. Ensure all tests pass
3. Update documentation if needed
4. Create GitHub release with tag
5. Automated workflows handle the rest

## 🐳 Docker Development

### Building Images
```bash
# Build main action image
docker build -t pipreqs-action .

# Build base image with Git
docker build -f Dockerfile-git-python -t pipreqs-base .
```

### Testing Docker Images
```bash
# Test action locally
docker run --rm -v $(pwd):/workspace pipreqs-action

# Interactive testing
docker run --rm -it -v $(pwd):/workspace pipreqs-action sh
```

## 📝 Documentation

### README Updates
- Keep examples current and tested
- Update badges and links
- Include all new features
- Maintain clear usage instructions

### API Documentation
- Use Google-style docstrings
- Include parameter types and descriptions
- Provide usage examples
- Document exceptions and return values

## 🎯 Pull Request Guidelines

### Before Submitting
- [ ] All tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated
- [ ] Pre-commit hooks pass

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

### Review Process
1. **Automated checks** must pass
2. **Code review** by maintainer
3. **Testing** verification
4. **Documentation** review
5. **Merge** after approval

## 🏆 Recognition

Contributors will be:
- **Listed** in CHANGELOG.md
- **Mentioned** in release notes
- **Added** to contributors list
- **Credited** in documentation

## 📞 Getting Help

### Questions?
- **GitHub Discussions**: For general questions
- **Issues**: For bug reports and feature requests
- **Email**: [joerg@jfheinrich.eu](mailto:joerg@jfheinrich.eu) for private matters

### Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Poetry Documentation](https://python-poetry.org/docs/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

Thank you for contributing to make pipreqs-action better for everyone! 🎉
