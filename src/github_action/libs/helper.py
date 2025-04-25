"""
Helper classes

Contains:
    - Helper
        - Helper::get_version() -> str
"""

import os
from git import Repo


class Helper:
    """Class for helper method"""

    @staticmethod
    def get_version() -> str:
        """Returns the package version"""

        gitbase = os.path.realpath(__file__)
        while (gitbase != '/' and not os.path.exists(os.path.join(gitbase, '.git'))):
            gitbase = os.path.realpath(os.path.join(gitbase, '..'))

        repo = Repo(gitbase)
        tags = repo.tags
        tagref = tags[-1]
        return tagref
