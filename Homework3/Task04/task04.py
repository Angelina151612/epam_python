def is_armstrong(number: int) -> bool:
    digits = list(map(int, str(number)))
    power = len(digits)
    res = sum(list(map(lambda x: x ** power, digits)))
    return number == res
