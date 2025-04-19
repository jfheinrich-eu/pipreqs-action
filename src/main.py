import os
import sys
from typing import List
from pipreqs import pipreqs


def get_python_files(project_path: str, recursive: bool) -> List[str]:
    """
    Get all Python files in the project directory.

    Args:
        project_path: Path to the project directory
        recursive: Whether to search recursively in subdirectories

    Returns:
        List of paths to Python files
    """
    if not recursive:
        return [project_path]

    python_files = []
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.py') and not file.startswith('.'):
                python_files.append(os.path.join(root, file))
    return python_files


def generate_requirements(file_path: str, project_path: str) -> List[str]:
    """
    Generate requirements for a single Python file using pipreqs.

    Args:
        file_path: Path to save requirements
        project_path: Path to the Python file or directory

    Returns:
        List of requirements
    """
    # Use pipreqs programmatically with all required parameters
    project_dir = (
        os.path.dirname(project_path) if os.path.isfile(project_path) else
        project_path
    )
    args = {
        '<path>': project_dir,
        '--savepath': file_path,
        '--force': True,
        '--print': False,
        '--encoding': None,
        '--ignore': None,
        '--no-follow-links': False,
        '--debug': False,
        '--mode': None,
        '--pypi-server': None,
        '--proxy': None,
        '--use-local': None,
        '--diff': None,
        '--clean': None
    }
    pipreqs.init(args)

    try:
        with open(file_path, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def save_requirements(file_path: str, requirements: List[str]) -> None:
    """
    Save unique requirements to a file.

    Args:
        file_path: Path to save requirements
        requirements: List of requirements to save
    """
    unique_requirements = list(set(req for req in requirements if req.strip()))
    with open(file_path, 'w') as f:
        f.writelines(unique_requirements)


def main(requirement_path: str, project_path: str, recursive: bool) -> List[str]:
    """
    Main function to generate and save project requirements.

    Args:
        requirement_path: Path to save requirements.txt
        project_path: Path to the project directory
        recursive: Whether to search recursively in subdirectories

    Returns:
        List of generated requirements
    """
    python_files = get_python_files(project_path, recursive)
    all_requirements = []

    for file_path in python_files:
        requirements = generate_requirements(requirement_path, file_path)
        all_requirements.extend(requirements)

    save_requirements(requirement_path, all_requirements)
    return all_requirements


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python main.py <requirement_path> <project_path> <recursive>")
        sys.exit(1)

    requirement_path = sys.argv[1]
    project_path = sys.argv[2]
    recursive = sys.argv[3].lower() == 'true'

    requirements = main(requirement_path, project_path, recursive)
    print(requirements)
