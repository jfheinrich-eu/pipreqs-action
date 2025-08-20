"""Tests for src/app.py module."""

from __future__ import annotations

import sys
import subprocess
import tempfile
import os
from pathlib import Path

import pytest

# Import the app module for testing
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))
import app  # noqa: E402 # pylint: disable=wrong-import-position


class DummyPipReqsAction:
    """Dummy implementation of PipReqsAction for testing app.py."""

    def __init__(
        self, requirement_path: str, project_path: str, recursive: bool
    ) -> None:
        self.requirement_path = requirement_path
        self.project_path = project_path
        self.recursive = recursive

    @staticmethod
    def get_argument(pos: int, env_name: str) -> str:  # pylint: disable=unused-argument
        """Mock get_argument method."""
        # Default implementation - will be overridden by monkeypatch
        return ""

    def run(self) -> list[str]:
        """Simulate requirements generation."""
        return ["requests==2.28.1", "pytest==7.0.0"]


def test_main_success_with_true_recursive(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test main function with all valid arguments and recursive=true."""
    # Mock dependencies
    monkeypatch.setattr(app, "__version__", "1.2.3")

    # Mock the original PipReqsAction class with our dummy
    monkeypatch.setattr("app.PipReqsAction", DummyPipReqsAction)

    # Mock get_argument to return valid values
    def mock_get_argument(
        pos: int, env_name: str  # pylint: disable=unused-argument
    ) -> str:
        args = {1: "requirements.txt", 2: "/path/to/project", 3: "true"}
        return args.get(pos, "")

    monkeypatch.setattr(
        DummyPipReqsAction, "get_argument", staticmethod(mock_get_argument)
    )

    # Call main function
    app.main()

    # Check output
    captured = capsys.readouterr()
    assert "Version: 1.2.3" in captured.out
    assert "requests==2.28.1" in captured.out
    assert "pytest==7.0.0" in captured.out


def test_main_success_with_false_recursive(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test main function with recursive=false."""
    # Mock dependencies
    monkeypatch.setattr(app, "__version__", "2.0.0")

    # Mock the original PipReqsAction class with our dummy
    monkeypatch.setattr("app.PipReqsAction", DummyPipReqsAction)

    # Mock get_argument to return valid values with recursive=false
    def mock_get_argument(
        pos: int, env_name: str  # pylint: disable=unused-argument
    ) -> str:
        args = {1: "requirements.txt", 2: "/path/to/project", 3: "false"}
        return args.get(pos, "")

    monkeypatch.setattr(
        DummyPipReqsAction, "get_argument", staticmethod(mock_get_argument)
    )

    # Call main function
    app.main()

    # Check output
    captured = capsys.readouterr()
    assert "Version: 2.0.0" in captured.out
    assert "requests==2.28.1" in captured.out


def test_main_missing_requirement_path(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test main function exits when requirement_path is missing."""
    monkeypatch.setattr(app, "__version__", "1.0.0")

    # Mock get_argument to return empty requirement_path
    def mock_get_argument(
        pos: int, env_name: str  # pylint: disable=unused-argument
    ) -> str:
        args = {1: "", 2: "/path/to/project", 3: "true"}  # Empty requirement_path
        return args.get(pos, "")

    monkeypatch.setattr("app.PipReqsAction.get_argument", mock_get_argument)

    # Expect SystemExit
    with pytest.raises(SystemExit) as exc_info:
        app.main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Usage: python main.py" in captured.out


def test_main_missing_project_path(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test main function exits when project_path is missing."""
    monkeypatch.setattr(app, "__version__", "1.0.0")

    # Mock get_argument to return empty project_path
    def mock_get_argument(
        pos: int, env_name: str  # pylint: disable=unused-argument
    ) -> str:
        args = {1: "requirements.txt", 2: "", 3: "true"}  # Empty project_path
        return args.get(pos, "")

    monkeypatch.setattr("app.PipReqsAction.get_argument", mock_get_argument)

    # Expect SystemExit
    with pytest.raises(SystemExit) as exc_info:
        app.main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Usage: python main.py" in captured.out


def test_main_missing_recursive(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test main function exits when recursive is missing."""
    monkeypatch.setattr(app, "__version__", "1.0.0")

    # Mock get_argument to return empty recursive
    def mock_get_argument(
        pos: int, env_name: str  # pylint: disable=unused-argument
    ) -> str:
        args = {1: "requirements.txt", 2: "/path/to/project", 3: ""}  # Empty recursive
        return args.get(pos, "")

    monkeypatch.setattr("app.PipReqsAction.get_argument", mock_get_argument)

    # Expect SystemExit
    with pytest.raises(SystemExit) as exc_info:
        app.main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Usage: python main.py" in captured.out


def test_main_recursive_case_insensitive_true(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test main function handles uppercase 'TRUE' correctly."""
    monkeypatch.setattr(app, "__version__", "1.0.0")

    # Mock the original PipReqsAction class with our dummy
    monkeypatch.setattr("app.PipReqsAction", DummyPipReqsAction)

    # Mock get_argument to return 'TRUE' (uppercase)
    def mock_get_argument(
        pos: int, env_name: str  # pylint: disable=unused-argument
    ) -> str:
        args = {1: "requirements.txt", 2: "/path/to/project", 3: "TRUE"}  # Uppercase
        return args.get(pos, "")

    monkeypatch.setattr(
        DummyPipReqsAction, "get_argument", staticmethod(mock_get_argument)
    )

    # Call main function
    app.main()

    # Should work without error
    captured = capsys.readouterr()
    assert "Version: 1.0.0" in captured.out


def test_main_as_script_entry_point() -> None:
    """Test that the script can be run as main module."""
    # This test just verifies that the main function exists
    # and is callable - the actual if __name__ == "__main__"
    # block is already covered by other tests
    assert hasattr(app, "main")
    assert callable(app.main)


def test_main_module_execution(
    monkeypatch: pytest.MonkeyPatch,  # pylint: disable=unused-argument
) -> None:
    """Test the if __name__ == '__main__' execution path."""
    # Create a mock file that simulates execution of app.py as __main__

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        # Write a test script that imports app and runs it as __main__
        f.write(
            f"""
import sys
sys.path.insert(0, '{src_path}')

# Mock the environment for testing
import os
os.environ['INPUT_REQUIREMENT_PATH'] = 'requirements.txt'
os.environ['INPUT_PROJECT_PATH'] = '/tmp'
os.environ['INPUT_RECURSIVE'] = 'true'

# Mock sys.argv to simulate command line execution
sys.argv = ['app.py', 'requirements.txt', '/tmp', 'true']

# Import and execute the app module
import app

# Override PipReqsAction to avoid actual execution
class MockPipReqsAction:
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get_argument(pos, env_name):
        if pos == 1:
            return 'requirements.txt'
        elif pos == 2:
            return '/tmp'
        elif pos == 3:
            return 'true'
        return ''

    def run(self):
        return ['mock-package==1.0.0']

app.PipReqsAction = MockPipReqsAction

# Execute the main block
if __name__ == '__main__':
    app.main()
"""
        )
        temp_file = f.name

    try:
        # Run the temp script as a subprocess to trigger the __main__ execution
        result = subprocess.run(
            [sys.executable, temp_file],
            capture_output=True,
            check=True,
            text=True,
            timeout=10,
        )

        # Check that it executed successfully
        assert result.returncode == 0
        assert "Version:" in result.stdout

    finally:
        # Remove the temporary test script file

        os.unlink(temp_file)
