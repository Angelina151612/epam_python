from hw.hw_09_task_02 import SuppressorCls, suppressor_gen

import pytest


def test_class_suppressed_passed_exception():
    with SuppressorCls(IndexError):
        [][2]


def test_generator_suppressed_passed_exception():
    with suppressor_gen(IndexError):
        [][2]


def test_class_not_suppressed_exception():
    with pytest.raises(ZeroDivisionError):  # noqa:
        with suppressor_gen(IndexError):
            1 / 0


def test_generator_not_suppressed_exception():
    with pytest.raises(ZeroDivisionError):  # noqa:
        with SuppressorCls(IndexError):
            1 / 0


def test_generator_and_class_supressed_subclass_exceptions():
    with SuppressorCls(Exception):
        raise IndexError()
    with suppressor_gen(Exception):
        raise IndexError()
