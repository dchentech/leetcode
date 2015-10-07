"""
Question:
    Remove Element

    Given an array and a value, remove all instances of that value in place and return the new length.

    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Performance:
    1. Total Accepted: 78411 Total Submissions: 245469 Difficulty: Easy
    2. Your runtime beats 70.75% of python submissions.
"""


class Solution(object):
    def removeElement_bad(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int

        OJ (online judge) really remove `val` from `nums`, not just return the new length.
        """
        return len(filter(lambda num: num != val, nums))

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int

        need to really remove `val` from `nums`, not just return the new length.

        refer to #removeElement_from_jw2013
        """
        last_unvisited_element_position = len(nums) - 1
        curr_idx = 0

        while curr_idx <= last_unvisited_element_position:
            if nums[curr_idx] == val:
                nums[curr_idx], nums[last_unvisited_element_position] = nums[last_unvisited_element_position], nums[curr_idx]
                last_unvisited_element_position -= 1
                # but curr_idx stays as the same value
            else:
                curr_idx += 1  # move forward curr_idx
        # the rest idxes is how many elements we have keep.
        return last_unvisited_element_position + 1

    def removeElement_from_jw2013(self, A, elem):
        last, i = len(A) - 1, 0
        while i <= last:
            if A[i] == elem:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return last + 1


assert Solution().removeElement([4, 5], 4) == 1
