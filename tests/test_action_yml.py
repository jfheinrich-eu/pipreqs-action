"""Tests for action.yml configuration."""

import yaml
import os


def test_action_yml_description_length():
    """Test that action.yml description meets GitHub Marketplace requirements."""
    action_yml_path = os.path.join(os.path.dirname(__file__), '..', 'action.yml')
    MAX_DESCRIPTION_LENGTH = int(os.getenv('MAX_DESCRIPTION_LENGTH', '125'))

    with open(action_yml_path, 'r', encoding='utf-8') as f:
        action_config = yaml.safe_load(f)

    description = action_config.get('description', '')

    # GitHub Marketplace typically recommends descriptions under 125 characters
    # for better display and SEO
    assert len(description) <= MAX_DESCRIPTION_LENGTH, f"Description is {len(description)} characters, should be <= {MAX_DESCRIPTION_LENGTH}"

    # Ensure description is not empty
    assert len(description) > 0, "Description should not be empty"

    # Ensure description contains key terms
    assert 'requirements.txt' in description.lower(), "Description should mention requirements.txt"
    assert 'python' in description.lower(), "Description should mention Python"


def test_action_yml_structure():
    """Test that action.yml has required fields."""
    action_yml_path = os.path.join(os.path.dirname(__file__), '..', 'action.yml')

    with open(action_yml_path, 'r', encoding='utf-8') as f:
        action_config = yaml.safe_load(f)

    # Required fields for GitHub Actions
    required_fields = ['name', 'description', 'runs']
    for field in required_fields:
        assert field in action_config, f"action.yml must contain '{field}' field"

    # Ensure name and description are strings
    assert isinstance(action_config['name'], str), "name must be a string"
    assert isinstance(action_config['description'], str), "description must be a string"
