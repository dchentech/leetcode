# -*-coding:utf-8-*-

"""
Question:
    Majority Element

    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always exist in the array.

    Credits:
    Special thanks to @ts for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 66274 Total Submissions: 180546 Difficulty: Easy
    2. Your runtime beats 99.28% of python submissions.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # when the array is sorted, the majority element must exists in the middle.
        return sorted(nums)[int(len(nums) / 2)]


assert Solution().majorityElement([1]) == 1
assert Solution().majorityElement([1, 1]) == 1
assert Solution().majorityElement([1, 1, 0]) == 1
