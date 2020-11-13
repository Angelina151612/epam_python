from Task04.task04 import is_armstrong

import pytest


@pytest.mark.parametrize(
    ("value"),
    [
        (153),
        (371),
        (3),
    ],
)
def test_value_is_armstrong(value: int):
    assert is_armstrong(value) is True


@pytest.mark.parametrize(
    ("value"),
    [
        (10),
        (379),
        (8206),
    ],
)
def test_value_is_not_armstrong(value: int):
    assert is_armstrong(value) is False
