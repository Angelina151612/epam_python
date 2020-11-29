"""
Написать декоратор instances_counter.

Декоратор применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса.
Имя декоратора и методов не менять.
"""


# flake8: noqa: ANN001
def instances_counter(cls):
    cls.counter = 0

    def __init__(self, *args, **kwargs):
        cls.counter += 1

    def get_created_instances(self=None):
        return cls.counter

    def reset_instances_counter(self=None):
        count_before_reset = cls.counter
        cls.counter = 0
        return count_before_reset

    setattr(cls, "__init__", __init__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls
