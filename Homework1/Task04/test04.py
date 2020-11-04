import pytest
from typing import List


from task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["value1", "value2", "value3", "value4", "expected_result"],
    [
        ([0, 0, 2, 3], [0, 0, 7, 7], [0, 5, 7, 7], [0, 6, 7, 7], 4),
        ([1, 0, 2, 3], [1, 0, 7, 7], [8, 5, 7, 7], [2, 6, 7, 7], 0),
        ([0], [0], [0], [0], 1),
        ([0], [-5], [0], [5], 1),
        ([], [], [], [], 0),
    ],
)
def test_check_sum_of_four(
    value1: List[int],
    value2: List[int],
    value3: List[int],
    value4: List[int],
    expected_result: int,
):
    actual_result = check_sum_of_four(value1, value2, value3, value4)
    assert actual_result == expected_result
