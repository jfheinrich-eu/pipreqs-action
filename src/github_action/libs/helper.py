"""Helper module for pipreqs-action.
This module provides utility classes and functions, such as version retrieval.
Contains:
    - Class Helper
        - Helper::get_version() -> str
"""

import importlib.metadata


class Helper:  # pragma no cover  # pylint: disable=too-few-public-methods
    """Class for helper methods such as version retrieval."""

    @staticmethod
    def get_version() -> str:
        """Returns the package version as set by setuptools_scm"""
        try:
            return importlib.metadata.version("pipreqs-action")
        except importlib.metadata.PackageNotFoundError:
            return "unknown"
