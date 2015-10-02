class Solution(object):
    """
    Given an array of integers, find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2

    Show Tags
    Show Similar Problems
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Conditions:
        1. Array are not ordered
        2. Distance between two result indexes maybe large than 2.
        """
        nums_len = len(nums)
        assert nums_len >= 2

        # "You may assume that each input would have exactly one solution.", so we can only choose one, even if it's duplicated.
        num_to_idx_dict = {num: idx + 1 for idx, num in enumerate(nums)}
        # nums_sorted = sorted(nums)  # it's needed, or wee need a double for statement.
        nums_sorted = nums
        # print "num_to_idx_dict:", str(num_to_idx_dict)
        # print "nums_sorted:", str(nums_sorted)

        [index1, index2] = [None, None]  # two indexes result, not zero-based.

        for idx1, num1 in enumerate(nums_sorted):
            if (idx1 + 1) == nums_len:  # reach the end
                break

            num2_expected = target - num1

            # Look for the right index ...
            for idx2, num2 in enumerate(nums_sorted[idx1 + 1:]):
                sum2 = num1 + num2
                if sum2 == target:
                    print "matched..."
                    index1 = num_to_idx_dict[num1]
                    index2 = num_to_idx_dict[num2]
                    break
                if num2 > num2_expected:
                    break

        return sorted([index1, index2])


result = Solution().twoSum([3, 2, 4], 6)
assert result == [2, 3], result
