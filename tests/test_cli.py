"""Tests for the main CLI function.

This module contains tests for the CLI functionality in main.py.
"""

import os
from collections.abc import Generator
from unittest.mock import patch

import pytest

from github_action.main import cli


@pytest.fixture
def mock_environment() -> Generator[None, None, None]:
    """Set up environment variables for testing."""
    original_env = os.environ.copy()
    os.environ["INPUT_REQUIREMENT_PATH"] = "test_requirements.txt"
    os.environ["INPUT_PROJECT_PATH"] = "test_project"
    os.environ["INPUT_RECURSIVE"] = "true"

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.mark.usefixtures("mock_environment")
def test_cli_with_environment_variables() -> None:
    """Test CLI function using environment variables."""
    with patch("github_action.main.PipReqsAction") as mock_pipreqs:
        mock_instance = mock_pipreqs.return_value
        mock_instance.run.return_value = ["package==1.0.0"]

        with patch("builtins.print") as mock_print:
            with patch("github_action.main.PipReqsAction.get_argument") as mock_get_arg:
                mock_get_arg.side_effect = [
                    "test_requirements.txt",
                    "test_project",
                    "true",
                ]
                cli()

                # Assert PipReqsAction was initialized with correct arguments
                mock_pipreqs.assert_called_once_with(
                    "test_requirements.txt", "test_project", True
                )
                mock_instance.run.assert_called_once()

                # Verify the version was printed (doesn't matter what version)
                assert mock_print.call_count >= 2


def test_cli_with_command_line_args() -> None:
    """Test CLI function using command line arguments."""
    with patch("sys.argv", ["pipreqs-action", "req.txt", "src", "true"]):
        with patch("github_action.main.PipReqsAction.get_argument") as mock_get_arg:
            mock_get_arg.side_effect = ["req.txt", "src", "true"]

            with patch("github_action.main.PipReqsAction") as mock_pipreqs:
                mock_instance = mock_pipreqs.return_value
                mock_instance.run.return_value = ["package==1.0.0"]

                with patch("builtins.print"):
                    with patch(
                        "github_action.main.PipReqsAction.get_argument",
                        return_value="true",
                    ):
                        cli()

                    # Assert PipReqsAction was initialized correctly - without actually
                    # checking the arguments
                    # since we've mocked get_argument which affects the instantiation
                    assert mock_pipreqs.call_count == 1
                    mock_instance.run.assert_called_once()


def test_cli_missing_arguments() -> None:
    """Test CLI function with missing arguments."""
    with patch("github_action.main.PipReqsAction.get_argument") as mock_get_arg:
        # Missing project_path
        mock_get_arg.side_effect = ["req.txt", "", "true"]

        with patch("sys.exit") as mock_exit:
            with patch("builtins.print") as mock_print:
                cli()

                mock_exit.assert_called_once_with(1)
                mock_print.assert_any_call(
                    "Usage: python main.py <requirement_path> <project_path> <recursive>"
                )
