from collections.abc import Callable
from typing import Any, List


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions: List[Callable]):
        self.functions = functions

    def apply(self, data: List[Any]) -> List[Any]:
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords: Any) -> Filter:
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(data: dict, k: Any = key, val: Any = value) -> bool:
            return data.get(k) == val

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)
