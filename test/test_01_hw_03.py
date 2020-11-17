from unittest import mock

from hw.hw_03_task_01 import cache


def test_cache():
    my_mock = mock.Mock()
    mock_copy = my_mock
    my_mock = cache(times=2)(my_mock)
    my_mock()
    my_mock()
    my_mock()
    assert mock_copy.call_count == 1
    my_mock()
    assert mock_copy.call_count == 2
