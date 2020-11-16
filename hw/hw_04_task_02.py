import urllib.request


# flake8: noqa: S310
def count_dots_on_i(url: str) -> int:
    try:
        page = urllib.request.urlopen(url)
        data = page.read().decode()
        return sum(1 for symb in data if symb == "i")
    except ValueError:
        raise ValueError("Unreachable {url}")
