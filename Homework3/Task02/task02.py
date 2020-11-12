import hashlib
import random
import struct
import time
from collections.abc import Callable
from multiprocessing import Pool


# flake8: noqa: S311,S303
def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_calculate(func: Callable = slow_calculate) -> int:
    po = Pool(processes=40)
    res = po.map_async(func, list(range(501)))
    return sum(res.get())
