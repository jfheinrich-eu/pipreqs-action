"""Tests for the pipreqs-action main module.

Includes tests for PipReqsAction and related functionality.
"""

import os
from pathlib import Path

import pytest

from github_action.main import PipReqsAction


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Create a temporary directory with some Python files for testing."""
    # Create a main Python file
    main_file = tmp_path / "main.py"
    main_content = """
import os
import sys
import requests
import json

def test_function():
    response = requests.get('https://api.example.com')
    return response.json()
"""
    main_file.write_text(main_content)

    # Create a subdirectory with another Python file
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    sub_file = subdir / "helper.py"
    sub_content = """
import json
import requests
import pandas as pd

def process_data():
    df = pd.DataFrame({'a': [1, 2, 3]})
    return df.to_json()
"""
    sub_file.write_text(sub_content)

    sub_file2 = subdir / "helper.txt"
    sub2_content = """
This file shoud ignored bei PipReqsActon
"""
    sub_file2.write_text(sub2_content)

    # Debug: Print file contents
    print(f"\nMain file contents:\n{main_file.read_text()}")
    print(f"\nHelper file contents:\n{sub_file.read_text()}")

    return tmp_path


def test_get_python_files_non_recursive(
    temp_dir: Path,  # pylint: disable=redefined-outer-name
) -> None:
    """Test getting Python files without recursive search."""
    action = PipReqsAction("dummy.txt", str(temp_dir), recursive=False)
    files = action.get_python_files()
    assert len(files) == 1
    assert files[0] == str(temp_dir)


def test_get_python_files_recursive(
    temp_dir: Path,  # pylint: disable=redefined-outer-name
) -> None:
    """Test getting Python files with recursive search."""
    action = PipReqsAction("dummy.txt", str(temp_dir), recursive=True)
    files = action.get_python_files()
    assert len(files) == 2
    assert any(f.endswith("main.py") for f in files)
    assert any(f.endswith("helper.py") for f in files)


def test_save_requirements(tmp_path: Path) -> None:
    """Test saving requirements to a file."""
    req_file = tmp_path / "requirements.txt"
    requirements = [
        "requests==2.28.1\n",
        "json==1.0.0\n",
        "requests==2.28.1\n",
        "pytest>=7.0.0\n",
    ]

    action = PipReqsAction(str(req_file), "dummy", False)
    warning = action.save_requirements(str(req_file), requirements)

    assert req_file.exists()
    with open(req_file, encoding="utf-8") as f:
        saved_reqs = f.readlines()

    # Check that duplicates are removed
    assert len(saved_reqs) == 3
    assert "requests==2.28.1\n" in saved_reqs
    assert "json==1.0.0\n" in saved_reqs
    assert warning == ""


def test_save_requirements_duplicate_versions(tmp_path: Path) -> None:
    """Test saving requirements with duplicate modules and different versions."""
    req_file: Path = tmp_path / "requirements.txt"
    requirements: list[str] = [
        "Github==3.4.4\n",
        "Github==3.4.5\n",
        "json==1.0.1\n",
        "json==1.0.0\n",
        "requests==2.28.1\n",
        "requests==2.28.1\n",
    ]
    action: PipReqsAction = PipReqsAction(str(req_file), "dummy", False)
    warning: str = action.save_requirements(str(req_file), requirements)

    assert req_file.exists()

    saved_reqs: list[str] = []
    with open(req_file, encoding="utf-8") as f:
        saved_reqs = f.readlines()

    # Only the highest version should be kept for Github
    assert "Github==3.4.5\n" in saved_reqs
    assert "Github==3.4.4\n" not in saved_reqs
    assert (
        "Module 'Github' found with versions 3.4.4 and 3.4.5. Using highest version."
        in warning.splitlines()
    )
    assert (
        "Module 'json' found with versions 1.0.1 and 1.0.0. Using highest version."
        in warning.splitlines()
    )
    assert "requests==2.28.1\n" in saved_reqs
    assert len(saved_reqs) == 3  # Only unique modules should be saved


def test_save_requirements_duplicate_modules(tmp_path: Path) -> None:
    """Test saving requirements with duplicate modules and not == as match operator."""
    req_file = tmp_path / "requirements.txt"
    requirements = [
        "Github==3.4.5\n",
        "requests==2.28.1\n",
        "requests>=2.28.1\n",
    ]
    action = PipReqsAction(str(req_file), "dummy", False)
    warning = action.save_requirements(str(req_file), requirements)

    assert req_file.exists()
    assert warning.startswith(
        "Warning: Duplicate modules still found after filtering: requests"
    )


def test_generate_requirements(
    temp_dir: Path, tmp_path: Path  # pylint: disable=redefined-outer-name
) -> None:
    """Test generating requirements for a Python file."""
    req_file = tmp_path / "requirements.txt"
    action = PipReqsAction(str(req_file), str(temp_dir / "main.py"), False)
    requirements = action.generate_requirements(
        str(req_file), str(temp_dir / "main.py")
    )

    # Debug: Print generated requirements
    print(f"\nGenerated requirements:\n{requirements}")

    # Check that external package requirements are found
    assert any("requests" in req.lower() for req in requirements)
    # Note: json is part of the standard library, so it won't be in requirements


def test_get_argument() -> None:
    """Test get a commandline argument"""
    argv: list[str] = ["program name", "./src/requirements.txt"]
    value = PipReqsAction.get_argument(1, None, argv)
    assert value is not None
    assert value == "./src/requirements.txt"


def test_get_argument_environment() -> None:
    """Test get a commandline argument from environment variable."""
    argv: list[str] = ["program name", "./src/requirements.txt"]
    os.environ["INPUT_PYTEST_DATE"] = "2025-04-26"

    value = PipReqsAction.get_argument(2, "INPUT_PYTEST_DATE", argv)
    assert value is not None
    assert value == "2025-04-26"

    # Clean up environment variable
    del os.environ["INPUT_PYTEST_DATE"]


def test_get_argument_env_fallback() -> None:
    """Test get_argument fallback to empty string if env is not set and arg missing."""
    argv: list[str] = ["program name"]
    value = PipReqsAction.get_argument(1, "NOT_SET_ENV", argv)
    assert value == ""


def test_get_argument_none_env() -> None:
    """Test get_argument fallback to empty string if env_name is None and arg missing."""
    argv: list[str] = ["program name"]
    value = PipReqsAction.get_argument(1, None, argv)
    assert value == ""


def test_run_prints_warning(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Test that run prints warnings if save_requirements returns a warning."""
    called = {}

    def fake_save_requirements(
        _self: object, _file_path: str, _requirements: list[str]
    ) -> str:
        called["printed"] = False
        print("::warning::Test warning")
        called["printed"] = True
        return "Test warning"

    monkeypatch.setattr(PipReqsAction, "save_requirements", fake_save_requirements)
    action = PipReqsAction(str(tmp_path / "requirements.txt"), str(tmp_path), False)
    result = action.run()
    assert called["printed"]
    assert isinstance(result, list)


def test_get_python_files_empty_dir(tmp_path: Path) -> None:
    """Test get_python_files with empty directory and recursive=True."""
    action = PipReqsAction("dummy.txt", str(tmp_path), recursive=True)
    files = action.get_python_files()
    assert not files


def test_get_python_files_single_file(tmp_path: Path) -> None:
    """Test get_python_files with single file and recursive=False."""
    file_path = tmp_path / "single.py"
    file_path.write_text("import sys\n")
    action = PipReqsAction("dummy.txt", str(file_path), recursive=False)
    files = action.get_python_files()
    assert files == [str(file_path)]
