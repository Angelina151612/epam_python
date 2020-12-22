from typing import List

from hw.hw_07_task_03 import tic_tac_toe_checker

import pytest


@pytest.mark.parametrize(
    ("board", "expected_result"),
    [
        ([["x", "o", "o"], ["o", "x", "x"], ["x", "x", "o"]], "draw!"),
        ([["o", "o", "o"], ["o", "-", "-"], ["x", "-", "o"]], "o wins!"),
        ([["x", "o", "-"], ["o", "x", "-"], ["-", "x", "x"]], "x wins!"),
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished"),
    ],
)
def test_tic_tac_toe_checker(board: List[List], expected_result: str):
    actual_result = tic_tac_toe_checker(board)

    assert actual_result == expected_result
