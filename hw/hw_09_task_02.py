"""
Write a context manager, that suppresses passed exception.

Do it both ways: as a class and as a generator.
"""

from contextlib import contextmanager


# flake8: noqa: R503
class SuppressorCls:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type == self.exception


@contextmanager
def suppressor_gen(exception):
    try:
        yield
    except exception:
        pass
