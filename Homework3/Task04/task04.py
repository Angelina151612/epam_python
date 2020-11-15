def is_armstrong(number: int) -> bool:
    power = len(str(number))
    res = sum(x ** power for x in map(int, str(number)))
    return number == res
