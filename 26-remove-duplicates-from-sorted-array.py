"""
Question:
    Remove Duplicates from Sorted Array

    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this in place with constant memory.

    For example,
    Given input array nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Performance:
    1. Total Accepted: 85387 Total Submissions: 273423 Difficulty: Easy
    2. Your runtime beats 56.02% of python submissions.
"""


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0

        uniq_idx = 0

        # put duplicates at the end of this array, so the left of array are all unique.
        for idx in xrange(1, len(A)):
            if A[idx] != A[uniq_idx]:
                # if it's different, put it at the right side of current unique char.
                A[uniq_idx + 1], A[idx] = A[idx], A[uniq_idx + 1]
                uniq_idx += 1
        return uniq_idx + 1  # zero-based


assert Solution().removeDuplicates([]) == 0
assert Solution().removeDuplicates([1]) == 1
assert Solution().removeDuplicates([1, 1, 2]) == 2
