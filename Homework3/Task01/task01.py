from collections.abc import Callable
from typing import Any


def cache(times: int) -> Callable:
    def func_cache(func: Callable) -> Callable:
        my_cache = []

        def wrapper(*args: Any) -> Any:
            for idx, [arg, res, t] in enumerate(my_cache):
                if arg == args and t > 0:
                    my_cache[idx][2] = t - 1
                    return res
            my_cache.append([args, func(*args), times])
            return func(*args)

        return wrapper

    return func_cache
