"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


# flake8: noqa: CCR001
def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    for j in range(1, k + 1):
        i = 0
        while i + j <= len(nums):
            comb = nums[i : i + j]
            curr_sum = sum(comb)
            if curr_sum > max_sum:
                max_sum = curr_sum
            i += 1
    return max_sum
