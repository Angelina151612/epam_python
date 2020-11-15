"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""
from typing import Any, List, Sequence


def check_side_to_go(ind_start: int, ind_stop: int, step: int) -> bool:
    if step > 0 and ind_start >= ind_stop:
        return False
    elif step < 0 and ind_start <= ind_stop:
        return False
    else:
        return True


def custom_range(
    seq: Sequence, start: Any, stop: Any = None, step: Any = None
) -> List[Any]:
    if stop is None:
        stop = start
        start = seq[0]

    if step is None:
        step = 1

    res = []

    while True:
        ind_start = seq.index(start)
        ind_stop = seq.index(stop)

        if not check_side_to_go(ind_start, ind_stop, step):
            break
        else:
            res.append(seq[ind_start])
            next_ind = ind_start + step
            if next_ind < 0 or next_ind > seq.index(seq[-1]):
                break
            start = seq[next_ind]
    return res
