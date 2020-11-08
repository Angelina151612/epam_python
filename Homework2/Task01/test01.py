from Task01.task01 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
    open_file,
)

import pytest


@pytest.mark.parametrize(
    ("file_path_open", "expected_result"),
    [
        ("text_open.txt", "Wir atgd gdhd"),
    ],
)
def test_open_file(file_path_open: str, expected_result: str):
    actual_result = open_file(file_path_open)

    assert actual_result == expected_result


def test_get_longest_diverse_words():
    actual_result = get_longest_diverse_words("text_1.txt")

    assert actual_result == [
        "abcdefghijkl",
        "abcdefghijk",
        "abcdefghij",
        "abcdefghi",
        "abcdefgh",
        "abcdefg",
        "abcdef",
        "abcde",
        "abcd",
        "abc",
    ]


def test_get_rarest_char():
    actual_result = get_rarest_char("text_2.txt")

    assert actual_result == "I"


def test_count_punctuation_chars():
    actual_result = count_punctuation_chars("text_3.txt")

    assert actual_result == 2


def test_count_non_ascii_chars():
    actual_result = count_non_ascii_chars("text_4.txt")

    assert actual_result == 6


def test_get_most_common_non_ascii_char():
    actual_result = get_most_common_non_ascii_char("text_4.txt")

    assert actual_result == "\\u00fc"
