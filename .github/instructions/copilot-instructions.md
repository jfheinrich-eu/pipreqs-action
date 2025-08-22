# Copilot Instructions for pipreqs-action

## Project Overview

- **Purpose:** Automates generation of `requirements.txt` for Python projects using [pipreqs](https://github.com/bndr/pipreqs), with enhanced duplicate handling and GitHub Actions integration.
- **Main Components:**
  - `src/github_action/main.py`: Core logic in `PipReqsAction` class. Handles file discovery, requirements generation, duplicate resolution, and warning reporting.
  - `src/github_action/libs/`: Helper modules, including `save_requirements_result.py` for result typing.
  - `tests/`: Comprehensive pytest suite, 98% coverage, covering all edge cases and error handling.

---

## Architecture & Data Flow

- **Entry Point:** Workflows call the action via `action.yml`, which invokes the Python entry point.
- **Requirements Generation:**
  - Scans project files (recursive or non-recursive).
  - Uses pipreqs to infer dependencies.
  - Deduplicates modules, selects highest version, and emits GitHub warnings for conflicts.
  - Writes results to the specified requirements file.

---

## Project-Specific Patterns

- **Duplicate Handling:** When multiple versions of a package are found, the highest version is selected and a warning is logged.
- **SHA Pinning:** All workflow examples recommend pinning the action to a commit SHA for security.
- **Type Safety:** All core modules use type hints and are mypy-compliant.
- **Pre-commit Hooks:** Configured for code quality enforcement.

---

## Developer Workflows

- **Dependency Management:** Uses Poetry (`pyproject.toml`). Dev dependencies (flake8, black, isort, pytest, etc.) are in `[tool.poetry.group.dev.dependencies]`.
- **Linting:** Run with `poetry run flake8 src` or via GitHub Actions (`python -m flake8 src`).
- **Testing:** Use `poetry poe test` or `pytest tests/ --cov`.
- **Formatting:** Use `poetry poe format` (Black, isort).
- **CI/CD:** GitHub Actions workflows in `.github/workflows/` automate linting, testing, coverage, and release.

---

## Release & Docker Workflow

- **Version Synchronization:**
  - On every GitHub release, the Docker image is pushed to DockerHub with the same version tag.
  - The Docker image description is synchronized with the current `README-Dockerfile-git-python.md`.
  - Versioning is consistent between GitHub Releases and DockerHub tags (e.g., `v4.1.0`).

- **Automation:**
  - The release workflow (`.github/workflows/release.yml`) automatically builds and pushes the image.
  - The description can be updated via API or manually—see DockerHub documentation.

- **Best Practice:**
  - Before each release, ensure the DockerHub README is up to date.
  - Use the same tag structure for GitHub and DockerHub to avoid confusion.
  - Example tagging:
    ```bash
    docker build -t jfheinrich/pipreqs-action:v4.1.0 .
    docker push jfheinrich/pipreqs-action:v4.1.0
    ```

- **Note:**
  - The DockerHub description should reflect features, version, and security practices.
  - Changes to the Docker README should always be synchronized with the release.

---

## Integration Points

- **pipreqs:** Used for requirements inference; invoked via internal API, not CLI.
- **GitHub Actions:** Action is designed for CI/CD pipelines; outputs warnings using `::warning::` for visibility in logs.
- **Docker:** Optional containerized execution for reproducibility.

---

## Conventions

- **Commit Messages:** Conventional Commits format (`feat:`, `fix:`, etc.).
- **Tests:** AAA pattern (Arrange, Act, Assert), high coverage required.
- **Inputs:** All workflow inputs are string-typed and documented in README.

---

## Key Files

- `src/github_action/main.py`: Main logic and patterns.
- `pyproject.toml`: Dependency and tool configuration.
- `tests/test_main.py`: Shows edge case handling and test conventions.
- `.github/workflows/lint_tests.yml`: CI pipeline structure.

---

## Example: Adding a New Linter

- Add to `[tool.poetry.group.dev.dependencies]` in `pyproject.toml`.
- Update `lint_tests.yml` to install and run the new linter.
- Add a test for linter integration in `tests/`.

---

## Language Policy

- **All responses from AI coding agents must be in English.**
