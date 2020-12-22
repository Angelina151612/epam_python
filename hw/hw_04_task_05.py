from itertools import cycle
from typing import Generator


def fizzbuzz(n: int) -> Generator:
    fizz = cycle(["", "", "Fizz"])
    buzz = cycle(["", "", "", "", "Buzz"])
    for i in range(1, n + 1):
        yield (next(fizz) + next(buzz)) or str(i)
