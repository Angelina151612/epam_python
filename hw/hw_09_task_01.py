from typing import Generator, Iterator, List, Optional


def get_value_from_file(path: str) -> int:
    with open(path) as f:
        for line in f:
            yield int(line)


def get_next_from_iterator(iterator: Generator) -> Optional[int]:
    try:
        value = next(iterator)
    except StopIteration:
        value = None
    return value  # noqa


def merge_sorted_files(file_list: List[str]) -> Iterator:

    first_arr = get_value_from_file(file_list[0])
    second_arr = get_value_from_file(file_list[1])
    first = next(first_arr)
    second = next(second_arr)

    while True:
        if first is None and second is None:
            break

        elif second is None:
            yield first
            first = get_next_from_iterator(first_arr)

        elif first is None:
            yield second
            second = get_next_from_iterator(second_arr)

        elif first < second:
            yield first
            first = get_next_from_iterator(first_arr)
        else:
            yield second
            second = get_next_from_iterator(second_arr)
