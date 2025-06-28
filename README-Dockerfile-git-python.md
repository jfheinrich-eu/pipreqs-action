# jfheinrich/pipreqs-action Image

## Overview

This image provides a minimal Python 3.12 environment based on Alpine Linux, bundled with a custom-built version of Git (v2.50.0). It is designed for CI/CD pipelines, automation tasks, and development environments that require both Python and an up-to-date Git installation.

---

## Features

- **Python 3.12** based on Alpine Linux for a small footprint
- **Git 2.50.0** built from source and installed to `/opt/git`
- Multi-stage build for a clean and minimal final image
- Environment variables set for Git binaries and libraries

---

## Usage

```sh
docker pull jfheinrich/pipreqs-action:latest
```

Run a Python script inside the container:

```sh
docker run --rm -it jfheinrich/pipreqs-action python3 your_script.py
```

Git is available on the `PATH`:

```sh
docker run --rm -it jfheinrich/pipreqs-action git --version
```

---

## Environment Variables

- `PATH` includes `/opt/git/bin` so the custom Git is used by default.
- `LD_LIBRARY_PATH` includes `/opt/git/lib` for Git dependencies.

---

## Example Dockerfile (for your own builds)

```dockerfile
FROM jfheinrich/pipreqs-action:latest
COPY . /app
WORKDIR /app
CMD ["python3", "your_script.py"]
```

---

## License

This image is provided as-is under the MIT License.
Git is licensed under the GNU General Public License v2.0.
Python is licensed under the Python Software Foundation License.

---

## Maintainer

Joerg Heinrich
[joerg@jfheinrich.eu](mailto:joerg@jfheinrich.eu)

---

## Notes

- The image is intended for use in CI/CD and automation scenarios.
- For production workloads, review and adjust the image to your security and compliance
