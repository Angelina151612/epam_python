import sys


# flake8: noqa: T001
def my_precious_logger(text: str) -> None:
    if text.startswith("error"):
        print(text, file=sys.stderr, end="")
    else:
        print(text, file=sys.stdout, end="")
