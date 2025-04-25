import pytest
from github_action.main import PipReqsAction


@pytest.fixture
def temp_dir(tmp_path):
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

    # Debug: Print file contents
    print(f"\nMain file contents:\n{main_file.read_text()}")
    print(f"\nHelper file contents:\n{sub_file.read_text()}")

    return tmp_path


def test_get_python_files_non_recursive(temp_dir):
    """Test getting Python files without recursive search."""
    files = PipReqsAction.get_python_files(str(temp_dir), recursive=False)
    assert len(files) == 1
    assert files[0] == str(temp_dir)


def test_get_python_files_recursive(temp_dir):
    """Test getting Python files with recursive search."""
    files = PipReqsAction.get_python_files(str(temp_dir), recursive=True)
    assert len(files) == 2
    assert any(f.endswith("main.py") for f in files)
    assert any(f.endswith("helper.py") for f in files)


def test_save_requirements(tmp_path):
    """Test saving requirements to a file."""
    req_file = tmp_path / "requirements.txt"
    requirements = ["requests==2.28.1\n",
                    "json==1.0.0\n", "requests==2.28.1\n"]

    PipReqsAction.save_requirements(str(req_file), requirements)

    assert req_file.exists()
    with open(req_file) as f:
        saved_reqs = f.readlines()

    # Check that duplicates are removed
    assert len(saved_reqs) == 2
    assert "requests==2.28.1\n" in saved_reqs
    assert "json==1.0.0\n" in saved_reqs


def test_generate_requirements(temp_dir, tmp_path):
    """Test generating requirements for a Python file."""
    req_file = tmp_path / "requirements.txt"
    requirements = PipReqsAction.generate_requirements(
        str(req_file), str(temp_dir / "main.py"))

    # Debug: Print generated requirements
    print(f"\nGenerated requirements:\n{requirements}")

    # Check that external package requirements are found
    assert any("requests" in req.lower() for req in requirements)
    # Note: json is part of the standard library, so it won't be in requirements


def test_main_function(temp_dir, tmp_path):
    """Test the main function with a complete workflow."""
    req_file = tmp_path / "requirements.txt"
    pipReqsAction = PipReqsAction(str(req_file), str(temp_dir), recursive=True)
    requirements = pipReqsAction.run()

    # Debug: Print generated requirements
    print(f"\nGenerated requirements (main):\n{requirements}")

    assert req_file.exists()
    assert len(requirements) > 0
    # Check that requirements from both files are included
    assert any("requests" in req.lower() for req in requirements)
    assert any("pandas" in req.lower() for req in requirements)
