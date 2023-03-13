import pytest
from main import choice


@pytest.mark.parametrize("test_input, expected_output", [("1", "1"), ("2", "2")])
def test_choice(monkeypatch, test_input, expected_output):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert choice() == "1"

    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert choice() == "2"


def test_choice_invalid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")
    with pytest.raises(ValueError, match="Invalid input!"):
        choice()
