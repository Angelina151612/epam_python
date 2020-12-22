from hw.hw_07_task_02 import backspace_compare

import pytest


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("ab#c", "ad#c"),
        ("a##c", "#a#c"),
        ("", ""),
        ("##", "#"),
    ],
)
def test_backspace_compare_true(first: str, second: str):
    assert backspace_compare(first, second) is True


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("a#c", "b"),
        ("a#", "#a"),
    ],
)
def test_backspace_compare_false(first: str, second: str):
    assert backspace_compare(first, second) is False
