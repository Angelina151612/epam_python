"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List
import itertools


def contains_sublist(my_list, sublist):
    n = len(sublist)
    return any((sublist == my_list[i : i + n]) for i in range(len(my_list) - n + 1))


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    for j in range(1, k + 1):
        comb = [
            i
            for i in itertools.combinations(nums, j)
            if contains_sublist(nums, list(i))
        ]
        for l in range(len(comb)):
            if sum(comb[l]) > max_sum:
                max_sum = sum(comb[l])
    return max_sum
