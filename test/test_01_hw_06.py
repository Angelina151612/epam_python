from hw.hw_06_task_01 import instances_counter


@instances_counter
class User:
    pass


def test_count_before_creation_is_zero():
    count = User.get_created_instances()
    assert count == 0


def test_count_of_created_instances():
    user, _, _ = User(), User(), User()  # noqa
    count = User.get_created_instances()
    assert count == 3


@instances_counter
class FirstClass:
    def __init__(self, number: int):
        self.counter = number


def test_reset_instances_counter():
    first_cls, _ = FirstClass(20), FirstClass(3)  # noqa
    count_before = FirstClass.reset_instances_counter()
    assert count_before == 2
    count_after = FirstClass.get_created_instances()
    assert count_after == 0
    assert first_cls.counter == 20
