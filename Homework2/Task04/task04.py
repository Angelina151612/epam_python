"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    my_cache = {}

    def wrapper(*args: Any) -> Any:
        if args in my_cache:
            return my_cache[args]
        else:
            my_cache[args] = func(*args)
            return my_cache[args]

    return wrapper
