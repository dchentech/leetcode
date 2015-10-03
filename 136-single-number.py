"""
Question:
    Single Number

    Given an array of integers, every element appears twice except for one. Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Performance:
    1. Total Accepted: 92009 Total Submissions: 199999 Difficulty: Medium
    2.  Your runtime beats 55.22% of python submissions.
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Google it, and suddenly understand that `xor` let two same number convert all bits to zero, so the single one lefted.
        """
        result = 0

        for num in nums:
            result ^= num

        return result


assert Solution().singleNumber([1, 0, 1]) == 0
assert Solution().singleNumber([1, 3, 1]) == 3
