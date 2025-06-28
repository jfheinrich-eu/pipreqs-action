"""
Helper classes

Contains:
    - Helper
        - Helper::get_version() -> str
"""

import importlib.metadata


class Helper:  # pragma no cover
    """Class for helper method"""

    @staticmethod
    def get_version() -> str:
        """Returns the package version as set by setuptools_scm"""
        try:
            return importlib.metadata.version("pipreqs-action")
        except importlib.metadata.PackageNotFoundError:
            return "unknown"
