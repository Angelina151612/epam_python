from typing import List

import pytest

from task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("value1", "value2", "expected_result"),
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, -1, 1, -1, 1, -1], 5, 1),
        ([0, -3, 2, 6, 1, 2], 1, 6),
    ],
)
def test_find_maximal_subarray_sum(
    value1: List[int], value2: int, expected_result: int
):
    actual_result = find_maximal_subarray_sum(value1, value2)

    assert actual_result == expected_result
