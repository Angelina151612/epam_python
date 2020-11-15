from unittest import mock

from hw.hw_03_task_01 import cache


def test_cache():
    m = mock.Mock()
    n = m
    m = cache(times=2)(m)
    for _ in range(4):
        m()

    assert n.call_count == 2
