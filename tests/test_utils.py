import pytest
from runbooks.utils import validate_input


def test_validate_input_valid():
    """Tests valid numeric inputs."""
    assert validate_input("10") == 10.0
    assert validate_input("5.5") == 5.5


def test_validate_empty_input():
    """Tests empty input handling."""
    with pytest.raises(ValueError, match="Input cannot be empty."):
        validate_input("")  # Empty string input


def test_validate_invalid_input():
    """Tests invalid numeric input handling."""
    with pytest.raises(ValueError, match="Invalid input 'abc'. Must be a number."):
        validate_input("abc")  # Non-numeric string
