from hw.hw_11_task_01 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


def test_enum():
    assert ColorsEnum.RED == "RED"


def test_iterable():
    assert 4 == sum(1 for _ in ColorsEnum)


def test_len():
    assert len(ColorsEnum) == 4
