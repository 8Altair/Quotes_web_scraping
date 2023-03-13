import pytest
from main import choice


@pytest.mark.parametrize("test_input, expected_output", [("1", "1"), ("2", "2"), ("3\n1", "1")])
def test_choice(monkeypatch, test_input, expected_output):
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    assert choice() == expected_output


def test_choice_invalid_input(monkeypatch):
    test_input = "invalid\n" * 5
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    with pytest.raises(Exception):
        choice()
