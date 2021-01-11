from hw.hw_11_task_01 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


def test_enum():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLUE == "BLUE"
    assert ColorsEnum.ORANGE == "ORANGE"
    assert ColorsEnum.BLACK == "BLACK"
