"""
Helper classes

Contains:
    - Helper
        - Helper::get_version() -> str
"""

import os
from git import Repo


class Helper:  # pragma no cover
    """Class for helper method"""

    @staticmethod
    def get_version() -> str:
        """Returns the package version"""

        gitbase = os.path.realpath(__file__)
        while (gitbase != '/' and not os.path.exists(os.path.join(gitbase, '.git'))):
            gitbase = os.path.realpath(os.path.join(gitbase, '..'))

        repo = Repo(gitbase)
        tags = repo.tags
        if len(tags) > 0:
            tags.reverse()
            tagref = tags[0]
            return tagref
        else:
            return repo.active_branch
