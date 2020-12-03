"""
Given two strings.

Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from itertools import zip_longest
from typing import List


def return_final_str(text: str) -> List[str]:
    return [
        cur for cur, next_ in zip_longest(text, text[1:]) if cur != "#" and next_ != "#"
    ]


def backspace_compare(first: str, second: str) -> bool:
    first = return_final_str(first)
    second = return_final_str(second)
    return first == second
