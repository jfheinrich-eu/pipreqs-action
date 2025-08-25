"""This script updates the `readme_file.md` file to reference the latest tag of the GitHub Action.
It finds the line that uses the action and replaces it with the latest tag and SHA.
It assumes the action is referenced in the format `uses: jfheinrich-eu/github-daily-report@<tag>`.
The script is intended to be run in a GitHub Actions workflow or locally in a repository where the action is defined.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

readme_file: Path
ACTION: str = "jfheinrich-eu/github-daily-report"


def get_and_check_readme() -> Path:
    """Get the README file path from the environment variable or default to 'README.md'."""
    readme_path_str: str = os.environ.get("README_FILE", "").strip()
    readme_path: Path = Path(readme_path_str) if readme_path_str else Path("README.md")

    if not readme_path.exists():
        raise RuntimeError(f"File does not exist: {readme_path}")
    if not readme_path.is_file():
        raise RuntimeError(f"Path is not a file: {readme_path}")
    if not os.access(readme_path, os.R_OK):
        raise RuntimeError(f"File is not readable: {readme_path}")
    if not os.access(readme_path, os.W_OK):
        raise RuntimeError(f"File is not writable: {readme_path}")

    return readme_path


def get_latest_tag() -> str:
    """Get the latest tag from the git repository."""
    # Use git describe to get the latest tag, which is the most recent annotated tag
    # The --abbrev=0 option gives the tag name without the commit hash
    # If there are no tags, this will raise an error, which we can handle if needed
    try:
        tag = (
            subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
            .decode()
            .strip()
        )
    except subprocess.CalledProcessError:
        raise RuntimeError(
            "Cannot determine the latest tag. Please create a tag first."
        )
    return tag


def get_tag_sha(tag: str) -> str:
    """Get the SHA of the given tag."""
    # Use git rev-list to get the commit SHA for the given tag
    # This will return the SHA of the commit that the tag points to
    try:
        # Decode the output and strip any extra whitespace
        sha = (
            subprocess.check_output(["git", "rev-list", "-n", "1", tag])
            .decode()
            .strip()
        )
    except subprocess.CalledProcessError:
        raise RuntimeError(
            f"Cannot find SHA for tag '{tag}'. Please check the tag name."
        )
    return sha


def main(readme_file: Path):
    """Main function to update the readme_file.md with the latest action tag."""
    # Get the latest tag and its SHA
    tag = get_latest_tag()
    sha = get_tag_sha(tag)
    new_line = f"  uses: {ACTION}@{sha}  # {tag}\n"

    content = readme_file.read_text().splitlines(keepends=True)
    pattern = re.compile(rf"\s*uses:\s*{re.escape(ACTION)}@.*")
    changed = False
    for i, line in enumerate(content):
        if pattern.match(line):
            content[i] = new_line
            changed = True
            break
    if changed:
        readme_file.write_text("".join(content))
    else:
        raise RuntimeError("No matching line found in readme_file.md.")


if __name__ == "__main__":
    # Ensure the script is run in a git repository
    if not Path(".git").exists():
        raise RuntimeError("This script must be run in a git repository.")
    try:
        readme_file: Path = get_and_check_readme()
        main(readme_file)
        print(
            f"Updated {readme_file} to use the latest tag '{get_latest_tag()}' with SHA '{get_tag_sha(get_latest_tag())}'."
        )
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
