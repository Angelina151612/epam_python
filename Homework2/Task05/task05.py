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
from typing import List, Sequence


def custom_range(
    seq: Sequence, start: str, stop: str = None, step: str = None
) -> List[str]:
    if stop is None:
        stop = start
        start = seq[0]

    if step is None:
        step = 1

    res = []
    while True:
        if step > 0 and seq.index(start) >= seq.index(stop):
            break
        elif step < 0 and seq.index(start) <= seq.index(stop):
            break
        else:
            ind = seq.index(start)
            res.append(seq[ind])
            start = seq[ind + step]
    return res
