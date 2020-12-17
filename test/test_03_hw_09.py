import os
from pathlib import Path

from hw.hw_09_task_03 import universal_file_counter

import pytest


@pytest.fixture()
def start_dir():
    for i in range(1, 4):
        filename = "./hw/file_" + str(i) + ".txt"
        with open(filename, "w") as f:
            f.write((((str(i) + " ") * i) + "\n") * i)
    yield Path("./hw")
    for i in range(1, 4):
        os.remove("./hw/file_" + str(i) + ".txt")


def test_universal_file_counter(start_dir):
    assert universal_file_counter(start_dir, "txt") == 6
    assert universal_file_counter(start_dir, "txt", str.split) == 14
