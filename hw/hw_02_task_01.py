"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import List


def open_file(file_path: str) -> str:
    with open(file_path) as f:
        return bytes(f.read(), "ascii").decode("unicode-escape")


def get_longest_diverse_words(file_path: str) -> List[str]:
    text = open_file(file_path)
    exclude = set(string.punctuation)
    text = "".join(ch for ch in text if ch not in exclude)
    word_list = text.split()
    word_list = sorted(word_list, key=lambda x: (-len(set(x)), -len(x)))
    return word_list[:10]


# flake8: noqa: R503
def get_rarest_char(file_path: str) -> str:
    text = open_file(file_path)
    counter = {}
    for elem in text:
        if elem not in counter:
            counter[elem] = 1
        else:
            counter[elem] += 1
    minimum = min(counter.values())
    for num, count in counter.items():
        if count == minimum:
            return num


def count_punctuation_chars(file_path: str) -> int:
    text = open_file(file_path)
    count = sum(1 for elem in text if elem in string.punctuation)
    return count


def count_non_ascii_chars(file_path: str) -> int:
    text = open_file(file_path)
    count = 0
    for elem in text:
        if ord(elem) > 128:
            count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    text = open_file(file_path)
    chars = [char for char in text if ord(char) > 128]
    chars_counter = {chars.count(val): val for val in set(chars)}
    return chars_counter[max(chars_counter.keys())]
