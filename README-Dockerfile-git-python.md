# jfheinrich/pipreqs-action Docker Image

## Overview

This image provides a minimal Python 3.12 environment based on Alpine Linux, bundled with a custom-built version of Git (v2.50.0) and the pipreqs-action. It is designed for use with the GitHub Action [jfheinrich-eu/pipreqs-action](https://github.com/jfheinrich-eu/pipreqs-action).

---

## Features

- **Python 3.12** based on Alpine Linux for minimal footprint
- **Git 2.50.0** built from source and installed to `/opt/git`
- **pipreqs** library for automatic requirements.txt generation
- **Multi-stage build** for clean and minimal final image
- **Optimized environment** variables for Git binaries and libraries
- **Security-focused** with non-root user execution

---

## Usage

### Pull the Image

```sh
docker pull jfheinrich/pipreqs-action:latest
```

### Run with Docker

```sh
docker run --rm -v $(pwd):/workspace jfheinrich/pipreqs-action:latest
```

---

## Environment Variables

- `PATH` includes `/opt/git/bin` so the custom Git is used by default
- `LD_LIBRARY_PATH` includes `/opt/git/lib` for Git dependencies
- `PYTHONPATH` configured for optimal Python execution

---

## Available Tags

- `latest` - Latest stable version with Python 3.12 and Git 2.50.0
- `v4` - Specific version tag for reproducible builds

---

## Example Usage in GitHub Actions

```yaml
name: Generate Requirements
on: [push]

jobs:
  pipreqs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: jfheinrich-eu/pipreqs-action@v4
        with:
          REQUIREMENTS_PATH: requirements.txt
          PROJECT_PATH: .
          RECURSIVE: true
```

---

## Building from Source

```dockerfile
FROM jfheinrich/pipreqs-action:latest

# Add your custom Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add your application
COPY . /app
WORKDIR /app

CMD ["python3", "your_script.py"]
```

---

## Security Features

- **Non-root execution** - Runs with dedicated user for enhanced security
- **Minimal attack surface** - Alpine Linux base with only essential packages
- **Regular updates** - Built with latest security patches
- **Reproducible builds** - Pinned versions for consistency

---

## Performance Characteristics

- **Image Size**: ~150MB (optimized multi-stage build)
- **Cold Start**: <2 seconds for typical pipreqs operations
- **Memory Usage**: <50MB for standard Python projects
- **Git Performance**: Custom-built Git 2.50.0 for optimal speed

---

## License

This image is provided under the MIT License.

**Included Software Licenses:**
- Git: GNU General Public License v2.0
- Python: Python Software Foundation License
- Alpine Linux: Various open source licenses

---

## Support & Maintenance

**Maintainer:** Jörg Heinrich
**Email:** [joerg@jfheinrich.eu](mailto:joerg@jfheinrich.eu)
**GitHub:** [jfheinrich-eu/pipreqs-action](https://github.com/jfheinrich-eu/pipreqs-action)

### Issues & Feature Requests

Please report issues and feature requests via [GitHub Issues](https://github.com/jfheinrich-eu/pipreqs-action/issues).

---

## Notes

- This image is designed for CI/CD and automation scenarios
- For production workloads, review and adjust security settings as needed
- Regular updates ensure compatibility with latest Python ecosystem changes
- Compatible with all major CI/CD platforms (GitHub Actions, GitLab CI, Jenkins, etc.)

---

## Changelog

### v4 (Latest)
- Updated to Python 3.12
- Custom Git 2.50.0 build
- Enhanced security with non-root execution
- Optimized image size and performance
- Added comprehensive test coverage
