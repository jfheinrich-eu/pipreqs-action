#!/usr/bin/env python3

"""Main module for pipreqs-action.

Contains the PipReqsAction class for generating requirements.txt files.
"""


import contextlib
import io
import os
import re
import sys
import typing

from pipreqs import pipreqs  # type: ignore

from github_action import __version__
from github_action.libs.save_requirements_result import SaveRequirementsResult

if typing.TYPE_CHECKING:  # pragma: no cover
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
        output_buffer = io.StringIO()
        with (
            contextlib.redirect_stdout(output_buffer),
            contextlib.redirect_stderr(output_buffer),
        ):
            pipreqs.init(args)  # type: ignore
        pipreqs_output = output_buffer.getvalue()
        if pipreqs_output:  # pragma: no cover
            # Only print debug output if pipreqs produced any output
            # This avoids cluttering the logs with empty output
            print(f"::debug::pipreqs output: {pipreqs_output}")

        try:
            with open(file_path, encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError as e:  # pragma: no cover
            raise FileNotFoundError(f"pipreqs throws exception: {e}") from e

    def save_requirements(
        self, file_path: str, requirements: list[str]
    ) -> SaveRequirementsResult:
        """
        Save requirements to a file, keeping only the highest version for each module.
        If duplicate modules with different versions are found, a warning is returned.

        Args:
            file_path: Path to save requirements
            requirements: List of requirements to save

        Returns:
            Warning message if duplicates with different versions were found, else empty string.
        """
        module_versions, warnings = self.__filter_requirements(requirements)
        requirements = []
        with open(file_path, "w", encoding="utf-8") as f:
            for module, version in module_versions.items():
                line = f"{module}=={version}" if version else module
                requirements.append(line)
                f.write(line + "\n")

        self.__report_duplicate_modules(requirements, warnings)

        result: SaveRequirementsResult = {
            "requirements": requirements,
            "warnings": "\n".join(warnings) if warnings else "",
        }
        return result

    def __report_duplicate_modules(
        self, requirements: list[str], warnings: list[str]
    ) -> None:
        module_names = [
            m.group(1)
            for req in requirements
            if req.strip() and (m := re.match(r"^([a-zA-Z0-9_\-]+)", req.strip()))
        ]
        duplicates = {name for name in module_names if module_names.count(name) > 1}
        if duplicates:
            warnings.append(
                "Warning: Duplicate modules still found after filtering:"
                f" {', '.join(sorted(duplicates))}"
            )

    def __filter_requirements(
        self, requirements: list[str]
    ) -> tuple[dict[str, str], list[str]]:
        version_pattern = re.compile(r"^([a-zA-Z0-9_\-]+)==([\d\.]+)")
        module_versions: dict[str, str] = {}
        warnings: list[str] = []

        for req in (r.strip() for r in requirements if r.strip()):
            match = version_pattern.match(req)
            if match:
                module, version = match.groups()
                prev_version = module_versions.get(module)
                if prev_version is not None and prev_version != version:
                    warnings.append(
                        f"Module '{module}' found with versions {prev_version} and {version}. "
                        "Using highest version."
                    )
                    # Compare versions as tuples of ints
                    prev_tuple = tuple(map(int, prev_version.split(".")))
                    new_tuple = tuple(map(int, version.split(".")))
                    if new_tuple > prev_tuple:
                        module_versions[module] = version
                elif prev_version is not None and prev_version == version:
                    continue
                else:
                    module_versions.setdefault(module, version)
            else:
                module_versions.setdefault(req, "")
        return module_versions, warnings

    def run(self) -> list[str]:
        """
        Main function to generate and save project requirements.

        Returns:
            List of generated requirements
        """
        python_files = self.get_python_files()
        all_requirements: list[str] = []

        for file_path in python_files:
            requirements = self.generate_requirements(self.requirement_path, file_path)
            all_requirements.extend(requirements)

        final_requirements: SaveRequirementsResult = self.save_requirements(
            self.requirement_path, all_requirements
        )
        for warning in final_requirements["warnings"].split("\n"):
            if warning != "":  # pragma: no cover
                print(f"::warning::{warning}")
        return final_requirements["requirements"]

    @staticmethod
    def get_argument(
        arg_position: int,
        env_name: str | None = None,
        args: list[str] | None = None,
    ) -> str:
        """
        Helper function to get the program arguments from the commandline or the environment

        Args:
            arg_position: Index in sys.argv
            env_name: Name of the environment variable, optional
            args: List of arguments, if None then use sys.argv
        """
        argument_list = sys.argv if args is None else args

        if len(argument_list) > arg_position:
            return argument_list[arg_position]

        value = os.getenv(env_name) if env_name is not None else ""
        return value if value is not None else ""


def cli() -> None:
    """
    Command-line interface for the application.
    """
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
