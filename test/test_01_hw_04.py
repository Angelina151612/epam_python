import os

from hw.hw_04_task_01 import read_magic_number

import pytest


@pytest.fixture()
def file_name(text: str):
    filename = "file_with_number"
    with open(filename, "w") as f:
        f.write(text)
    yield filename
    os.remove(filename)


@pytest.mark.parametrize(
    ("text"),
    [
        ("1"),
        ("2"),
        ("1.2\n other line"),
    ],
)
def test_num_from_interval(file_name):
    actual_result = read_magic_number(file_name)

    assert actual_result is True


@pytest.mark.parametrize(
    ("text"),
    [
        ("3"),
        ("0"),
    ],
)
def test_num_not_from_interval(file_name):
    actual_result = read_magic_number(file_name)

    assert actual_result is False


@pytest.mark.parametrize(
    ("text"),
    [
        ("Hello"),
        ("It's me"),
    ],
)
def test_value_error(file_name):
    with pytest.raises(ValueError, match="it's not a number!"):
        read_magic_number(file_name)


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError, match="No file here!"):
        read_magic_number("non_existent_file.txt")
