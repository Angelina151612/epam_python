from typing import List


# flake8: noqa: CCR001
def fizzbuzz(n: int) -> List[str]:
    """
       Function takes a number N as an input and returns N FizzBuzz numbers.

    Instruction:
        - Install Python 3.8 (https://www.python.org/downloads/)
        - Clone the repository https://github.com/Angelina151612/epam_python
        - Checkout branch HW4T04
        - Open terminal
        - Run python hw/hw_04_task_04.py -v

       >>> fizzbuzz(5)
       ['1', '2', 'Fizz', '4', 'Buzz']
       >>> fizzbuzz(1.5)
       Traceback (most recent call last):
           ...
       TypeError: Wrong number!
    """
    try:
        res = []
        for i in range(1, n + 1):
            div_3 = i % 3
            div_5 = i % 5
            if div_3 == 0 and div_5 == 0:
                res.append("Fizz Buzz")
            elif div_3 == 0:
                res.append("Fizz")
            elif div_5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
    except TypeError:
        raise TypeError("Wrong number!")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
