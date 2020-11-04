import pytest
from typing import Tuple

from task03 import find_maximum_and_minimum


def create_file(file_name: str, nums: list) -> str:
    f = open(file_name, "w+")
    with open(file_name, "w+") as f:
        for i in range(len(nums)):
            f.write(str(nums[i]) + "\n")
    return file_name


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (create_file("t1.txt", [1, 3, 2, 7, 5]), (1, 7)),
        (create_file("t2.txt", [1]), (1, 1)),
    ],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)
    assert actual_result == expected_result
