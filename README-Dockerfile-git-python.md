# jfheinrich/pipreqs-action Image

## Overview

This image provides a minimal Python 3.12 environment based on Alpine Linux, bundled with a custom-built version of Git (v2.50.0) and the Github Action jfheinrich-eu/pipreqs-action. It is designed for use from the Gthub action.

---

## Features

- **Python 3.12** based on Alpine Linux for a small footprint
- **Git 2.50.0** built from source and installed to `/opt/git`
- **jfheinrich-eu/pipreqs-action v4**
- Multi-stage build for a clean and minimal final image
- Environment variables set for Git binaries and libraries

---

## Usage

```sh
docker pull jfheinrich/pipreqs-action:latest requirements.txt . "true"
```

---

## Environment Variables

- `PATH` includes `/opt/git/bin` so the custom Git is used by default.
- `LD_LIBRARY_PATH` includes `/opt/git/lib` for Git dependencies.

---

## Example Dockerfile (for your own builds)

```dockerfile
FROM jfheinrich/pipreqs-action:latest AS builder

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
