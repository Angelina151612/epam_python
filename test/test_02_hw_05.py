import functools

from hw.hw_05_task_02 import print_result


@print_result
def custom_sum(*args):
    """Description of the function."""
    return functools.reduce(lambda x, y: x + y, args)


def test__doc__():
    assert custom_sum.__doc__ == "Description of the function."


def test__name__():
    assert custom_sum.__name__ == "custom_sum"


def test_has_atr__oiginal_func():
    assert hasattr(custom_sum, "__original_func") is True


def test__original_func():
    without_print = custom_sum.__original_func
    assert str(without_print).startswith("<function custom_sum at")


def test_results():
    without_print = custom_sum.__original_func
    assert custom_sum(1, 2, 3, 4) == without_print(1, 2, 3, 4)
