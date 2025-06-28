#!/usr/bin/env python3

import os
import sys
import typing
from pipreqs import pipreqs  # type: ignore
if typing.TYPE_CHECKING:
    pass
# from typing import List


class PipReqsAction:
    """Generate requirements.txt, optional recursive"""

    requirement_path: str
    project_path: str
    recursive: bool

    def __init__(self, requirement_path: str, project_path: str, recursive: bool):
        self.requirement_path = requirement_path
        self.project_path = project_path
        self.recursive = recursive

    def get_python_files(self) -> list[str]:
        """
        Get all Python files in the project directory.

        Returns:
            List of paths to Python files
        """
        if not self.recursive:
            return [self.project_path]

        python_files: list[str] = []
        for root, _, files in os.walk(self.project_path):
            for file in files:
                if file.endswith(".py") and not file.startswith("."):
                    python_files.append(os.path.join(root, file))
        return python_files

    def generate_requirements(self, file_path: str, project_path: str) -> list[str]:
        """
        Generate requirements for a single Python file using pipreqs.

        Args:
            file_path: Path to save requirements
            project_path: Path to the Python file or directory

        Returns:
            List of requirements
        """
        project_dir = (
            os.path.dirname(project_path)
            if os.path.isfile(project_path)
            else project_path
        )
        args: dict[str, typing.Any] = {
            "<path>": project_dir,
            "--savepath": file_path,
            "--force": True,
            "--print": False,
            "--encoding": None,
            "--ignore": None,
            "--no-follow-links": False,
            "--debug": False,
            "--mode": None,
            "--pypi-server": None,
            "--proxy": None,
            "--use-local": None,
            "--diff": None,
            "--clean": None,
        }
        pipreqs.init(args)  # type: ignore

        try:
            with open(file_path) as f:
                return f.readlines()
        except FileNotFoundError as e:  # pragma: no cover
            raise FileNotFoundError(f"pipreqs throws exception: {e}")

    def save_requirements(self, file_path: str, requirements: list[str]) -> None:
        """
        Save unique requirements to a file.

        Args:
            file_path: Path to save requirements
            requirements: List of requirements to save
        """
        unique_requirements = list(
            {req for req in requirements if req.strip()})
        with open(file_path, "w") as f:
            f.writelines(unique_requirements)

    def run(self) -> list[str]:
        """
        Main function to generate and save project requirements.

        Returns:
            List of generated requirements
        """
        python_files = self.get_python_files()
        all_requirements: list[str] = []

        for file_path in python_files:
            requirements = self.generate_requirements(
                self.requirement_path, file_path)
            all_requirements.extend(requirements)

        self.save_requirements(self.requirement_path, all_requirements)
        return all_requirements

    @staticmethod
    def get_argument(
        arg_position: int, env_name: typing.Optional[str] = None, args: typing.Optional[list[str]] = None
    ) -> str:
        """
        Helper function to get the program arguments from the commandline or the environment

        Args:
            arg_position: Index in sys.argv
            env_name: Name of the environment variable, optional
            args: List of arguments, if None then use sys.argv
        """
        ArgumentList = sys.argv if args is None else args

        if len(ArgumentList) > arg_position:
            return ArgumentList[arg_position]

        value = os.getenv(env_name) if env_name is not None else ""
        return value if value is not None else ""
