import pytest
from typing import Sequence

from task02 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2], True),
        ([], False),
        ([0], False),
        ([0, 1, 1, 3], False),
        ([1, 1, 2], False),
    ],
)
def test_check_fibonacci(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
