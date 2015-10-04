"""
Question:
    Move Zeroes

    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

    Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

    Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 15730 Total Submissions: 38045 Difficulty: Easy
    2. Sorry. We do not have enough accepted submissions.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        reached_zero_count = 0

        for idx, num in enumerate(nums):
            if num == 0:
                reached_zero_count += 1
            if num != 0:
                if reached_zero_count > 0:  # make sure has reached at least a zero.
                    nums[idx - reached_zero_count] = num
                    nums[idx] = 0


def test_func(nums, result):
    Solution().moveZeroes(nums)
    assert nums == result, [nums, result]

test_func([], [])
test_func([0], [0])
test_func([1], [1])
test_func([0, 0], [0, 0])
test_func([0, 1], [1, 0])
test_func([1, 1], [1, 1])
test_func([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
test_func([0, 1, 0, 3, 12, 0], [1, 3, 12, 0, 0, 0])
test_func([0, 1, 0, 0, 0, 3, 12, 0], [1, 3, 12, 0, 0, 0, 0, 0])
