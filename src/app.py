#!/usr/bin/env python
"""Entry point for pipreqs-action.

Handles argument parsing and runs the main logic.
"""

import sys

from github_action import __version__
from github_action.main import PipReqsAction

# from typing import List


def main() -> None:
    """Main function to execute the pipreqs action."""
    print(f"Version: {__version__}")

    requirement_path: str = PipReqsAction.get_argument(1, "INPUT_REQUIREMENT_PATH")
    project_path: str = PipReqsAction.get_argument(2, "INPUT_PROJECT_PATH")
    recursive: str = PipReqsAction.get_argument(3, "INPUT_RECURSIVE")

    if not requirement_path or not project_path or not recursive:
        print("Usage: python main.py <requirement_path> <project_path> <recursive>")
        sys.exit(1)

    pip_reqs_action = PipReqsAction(
        requirement_path, project_path, recursive.lower() == "true"
    )

    requirements: list[str] = pip_reqs_action.run()
    print(requirements)


if __name__ == "__main__":  # pragma: no cover
    main()
