from typing import Iterator, List


def merge_sorted_files(file_list: List[str]) -> Iterator:
    with open(file_list[0]) as f1:
        first_arr = list(f1.read().split())
    with open(file_list[1]) as f2:
        second_arr = list(f2.read().split())
    i = j = 0
    n1 = len(first_arr)
    n2 = len(second_arr)
    while i < n1 and j < n2:
        if first_arr[i] < second_arr[j]:
            yield int(first_arr[i])
            i += 1
        else:
            yield int(second_arr[j])
            j += 1
    while i < n1:
        yield int(first_arr[i])
        i += 1

    while j < n2:
        yield int(second_arr[j])
        j += 1
