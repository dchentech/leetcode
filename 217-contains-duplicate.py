"""
Question:
    Contains Duplicate

    Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Performance:
    1. Total Accepted: 39720 Total Submissions: 105895 Difficulty: Easy
    2. Your runtime beats 68.81% of python submissions.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


assert Solution().containsDuplicate([]) is False
assert Solution().containsDuplicate([1]) is False
assert Solution().containsDuplicate([1, 1]) is True
assert Solution().containsDuplicate([1, 1, 2]) is True
