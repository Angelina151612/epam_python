import string
from typing import Any, List

from Task05.task05 import custom_range

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
    ],
)
def test_custom_range(value: List[Any], expected_result: List[str]):
    actual_result = custom_range(*value)

    assert actual_result == expected_result
