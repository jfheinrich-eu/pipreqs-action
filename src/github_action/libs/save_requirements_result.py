"""TypedDict for save_requirements return type."""

import typing


class SaveRequirementsResult(typing.TypedDict):
    """TypedDict for save_requirements return type."""

    requirements: list[str]
    warnings: str
