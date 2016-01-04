# -*-coding:utf-8-*-


"""
Question:
    Range Sum Query - Immutable My Submissions Question

    Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
    Given nums = [-2, 0, 3, -5, 2, -1]

    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.

Performance:
    1. Total Accepted: 12780 Total Submissions: 53592 Difficulty: Easy
    2. Your runtime beats 34.71% of python submissions.
"""


class NumArray_TimeLimitExceeded(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.result_cache = {}

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        begin_idx = max(0, i)
        end_idx = min(len(self.nums) - 1, j)
        cache_key = (begin_idx, end_idx)

        if cache_key not in self.result_cache:
            self.result_cache[cache_key] = self.calculate(begin_idx, end_idx)
        return self.result_cache[cache_key]

    def calculate(self, begin_idx, end_idx):
        curr_sum = 0
        curr_idx = begin_idx

        while curr_idx <= end_idx:
            curr_sum += self.nums[curr_idx]
            curr_idx += 1

        return curr_sum


class NumArray(object):
    """
    Thanks Python version in https://leetcode.com/discuss/68725/5-lines-c-4-lines-python
    """
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accumulate = [0]
        for n in nums:
            self.accumulate += [self.accumulate[-1] + n]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accumulate[j+1] - self.accumulate[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)


numArray = NumArray([-2, 0, 3, -5, 2, -1])
assert numArray.sumRange(0, 2) == 1
assert numArray.sumRange(2, 5) == -1
assert numArray.sumRange(0, 5) == -3
