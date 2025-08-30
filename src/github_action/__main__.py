#!/usr/bin/env python3

"""Entry point for the pipreqs-action command line interface.

This module provides the entry point for the pipreqs-action CLI tool,
handling exceptions and proper exit codes.
"""

import sys

from .main import cli


def main() -> None:
    """Execute the main CLI function with error handling.

    This function serves as the entry point for the pipreqs-action CLI tool.
    It calls the main CLI function and handles any exceptions that might occur,
    printing the error message and exiting with a non-zero status code.

    Returns:
        None

    Raises:
        SystemExit: If an exception occurs, exits with code 1
    """
    try:
        cli()
    except (ImportError, RuntimeError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
