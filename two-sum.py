"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Show Tags
Show Similar Problems
"""


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Conditions:
        1. Array are not ordered
        2. Distance between two result indexes maybe large than 2.
        """
        num_exists_dict = dict()
        [index1, index2] = [None, None]

        for idx1, num1 in enumerate(nums):
            index1 = idx1 + 1
            num2_expected = target - num1

            index2_expect = num_exists_dict.get(num2_expected, None)
            if index2_expect is None:  # not in the dict
                num_exists_dict[num1] = index1
            else:
                # Find it!
                index2 = index2_expect
                break

        return sorted([index1, index2])


result = Solution().twoSum([3, 2, 4], 6)
assert result == [2, 3], result

result = Solution().twoSum([-3, 4, 3, 90], 0)
assert result == [1, 3], result
