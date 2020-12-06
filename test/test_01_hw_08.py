import os

from hw.hw_08_task_01 import KeyValueStorage

import pytest


@pytest.fixture()
def file_name(data: str):
    filename = "task1.txt"
    with open(filename, "w") as f:
        f.write(data)
    yield filename
    os.remove(filename)


@pytest.mark.parametrize(
    ("data"),
    [
        ("name=kek 1=run"),
    ],
)
def test_value_error(file_name):
    with pytest.raises(ValueError, match="Key should be a string!"):
        KeyValueStorage(file_name)


@pytest.mark.parametrize(
    ("data", "dictionary"),
    [
        (
            "name=kek last_name=top power=9001 song=shadilay",
            {"name": "kek", "last_name": "top", "power": 9001, "song": "shadilay"},
        ),
        ("name=kek name=run", {"name": "kek"}),
    ],
)
def test_key_value_storage(file_name, dictionary):
    storage = KeyValueStorage(file_name)
    assert storage == dictionary
    assert storage["name"] == storage.name == dictionary["name"]
