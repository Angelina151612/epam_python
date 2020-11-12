import string
from typing import Any, List

from task05 import check_side_to_go, custom_range

import pytest


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([string.ascii_lowercase, "g"], ["a", "b", "c", "d", "e", "f"]),
        (
            [string.ascii_lowercase, "g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ([string.ascii_lowercase, "p", "g", -2], ["p", "n", "l", "j", "h"]),
        ([string.ascii_lowercase, "p", "g", -20], ["p"]),
        ([string.ascii_lowercase, "a", "c", 15], ["a"]),
    ],
)
def test_custom_range(value: List[Any], expected_result: List[Any]):
    actual_result = custom_range(*value)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([1, 15, -10], False),
        ([1, 15, 10], True),
    ],
)
def test_check_side_to_go(value: List[int], expected_result: bool):
    actual_result = check_side_to_go(*value)

    assert actual_result == expected_result
