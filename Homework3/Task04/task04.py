def is_armstrong(number: int) -> bool:
    digits = list(map(int, str(number)))
    power = len(digits)
    res = sum(elem ** power for elem in digits)
    return number == res
