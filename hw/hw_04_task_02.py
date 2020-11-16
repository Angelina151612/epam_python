import urllib.request


def count_dots_on_i(url: str) -> int:
    try:
        page = urllib.request.urlopen(url)
        data = page.read().decode()
        return sum(1 for symb in data if symb == "i")
    except ValueError:
        raise ValueError("Unreachable {url}")
