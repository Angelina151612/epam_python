"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
import string
from typing import List


def open_file(file_path: str) -> str:
    f = open(file_path)
    return f.read()


def get_longest_diverse_words(file_path: str) -> List[str]:
    text = open_file(file_path)
    word_list = re.sub(r"[^\w\s]", "", text).split()
    all_words = [(elem, len(elem), len(set(elem))) for elem in set(word_list)]
    sorted_words = sorted(all_words, key=lambda point: (-point[2], -point[1]))
    return [a[0] for a in sorted_words[:10]]


def get_rarest_char(file_path: str) -> str:
    text = open_file((file_path))
    counter = {}
    for elem in text:
        if elem not in counter:
            counter[elem] = 1
        else:
            counter[elem] += 1
    minimum = min(counter.values())
    for num, count in counter.items():
        if count == minimum:
            minimum = num
    return minimum


def count_punctuation_chars(file_path: str) -> int:
    text = open_file(file_path)
    count = 0
    for i, elem in enumerate(text):
        if not (elem == "\\" and text[i + 1] == "u"):
            if elem in string.punctuation:
                count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    text = open_file(file_path)
    count = 0
    for i, elem in enumerate(text):
        if elem == "\\" and text[i + 1] == "u":
            count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    text = open_file(file_path)
    words = re.findall(r"\\u\w\w\w\w", text)
    words_counter = {words.count(val): val for val in set(words)}
    return words_counter[max(words_counter.keys())]
