from time import perf_counter

from Task02.task02 import fast_calculate


def test_fast_calculate():
    t_start = perf_counter()
    fast_calculate()
    t_stop = perf_counter()
    assert t_stop - t_start < 60
