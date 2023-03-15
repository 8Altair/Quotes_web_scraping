import pytest
from main import choice


# Test function to check valid inputs
@pytest.mark.parametrize("test_input, expected_output", [("1", "1"), ("2", "2")])
def test_choice_valid_input(monkeypatch, test_input, expected_output):
    monkeypatch.setattr('builtins.input', lambda _: "1")        # Set the input function to always return "1"
    assert choice() == "1"      # Assert that the function returns "1"

    monkeypatch.setattr('builtins.input', lambda _: "2")        # Set the input function to always return "2"
    assert choice() == "2"      # Assert that the function returns "2"


# Test function to check invalid input
def test_choice_invalid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")        # Set the input function to always return "3"
    # Assert that the function raises a ValueError with the specified message
    with pytest.raises(ValueError, match="Invalid input!"):
        choice()
