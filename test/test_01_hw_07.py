from typing import Any

from hw.hw_07_task_01 import find_occurrences

import pytest


example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": 15,
        "jhl": "RED",
        "complex_key": {
            "RED": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"RED": "RED"}],
        },
    },
    "fourth": "RED",
}


@pytest.mark.parametrize(
    ("element", "expected_result"),
    [
        ("RED", 8),
        (15, 1),
        ("A", 0),
    ],
)
def test_find_occurrences(element: Any, expected_result: int):
    actual_result = find_occurrences(example_tree, element)

    assert actual_result == expected_result
