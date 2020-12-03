"""
Given a dictionary (tree), that can contains multiple nested structures.

Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Iterable


def find_occurrences(tree: Iterable, element: Any) -> int:
    counter = 0
    if isinstance(tree, (set, tuple, list)):
        for elem in tree:
            counter += find_occurrences(elem, element)
    if isinstance(tree, dict):
        for k in tree:
            if k == element:
                counter += 1
            counter += find_occurrences(tree[k], element)
    elif tree == element:
        counter += 1
    return counter
