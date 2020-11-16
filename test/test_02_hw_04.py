from unittest.mock import MagicMock, patch

from hw.hw_04_task_02 import count_dots_on_i

import pytest


@patch("urllib.request.urlopen")
def test_count_dots_on_i(mock_urlopen):
    my_mock = MagicMock()
    my_mock.read.return_value = b"iii"
    mock_urlopen.return_value = my_mock
    res = count_dots_on_i(my_mock)
    assert res == 3


@patch("urllib.request.urlopen")
def test_unreachable_url(mock_urlopen):
    my_mock = MagicMock()
    mock_urlopen.side_effect = ValueError
    with pytest.raises(ValueError, match="Unreachable {url}"):
        count_dots_on_i(my_mock)
