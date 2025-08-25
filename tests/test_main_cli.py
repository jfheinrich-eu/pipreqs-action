"""Tests for the __main__ module.

This module contains tests for the main CLI entry point.
"""

from unittest.mock import patch

from github_action.__main__ import main


def test_main_successful_execution() -> None:
    """Test main function with successful execution."""
    with patch("github_action.__main__.cli") as mock_cli:
        main()
        mock_cli.assert_called_once()


def test_main_handles_import_error() -> None:
    """Test main function handles ImportError correctly."""
    with patch("github_action.__main__.cli", side_effect=ImportError("Test error")):
        with patch("sys.exit") as mock_exit:
            main()
            mock_exit.assert_called_once_with(1)


def test_main_handles_runtime_error() -> None:
    """Test main function handles RuntimeError correctly."""
    with patch("github_action.__main__.cli", side_effect=RuntimeError("Test error")):
        with patch("sys.exit") as mock_exit:
            main()
            mock_exit.assert_called_once_with(1)


def test_main_handles_value_error() -> None:
    """Test main function handles ValueError correctly."""
    with patch("github_action.__main__.cli", side_effect=ValueError("Test error")):
        with patch("sys.exit") as mock_exit:
            main()
            mock_exit.assert_called_once_with(1)
