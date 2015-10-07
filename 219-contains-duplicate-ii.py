"""
Question:
    Contains Duplicate II

    Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

Performance:
    1. Total Accepted: 28832 Total Submissions: 107900 Difficulty: Easy
    2. Your runtime beats 25.98% of python submissions.
"""

from collections import defaultdict

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 1. build indexes
        num_to_idxes = defaultdict(list)
        for idx, num in enumerate(nums):
            num_to_idxes[num].append(idx)  # sorted number list

        # 2. remove wrong k-v.
        num_to_idxes = {k: v for k, v in num_to_idxes.iteritems() if len(v) >= 2}
        if len(num_to_idxes) == 0:
            return False

        for num, idxes in num_to_idxes.iteritems():
            # select first one, and keep moving a window to loop.
            # one is original num's idxes, another is the index of num's idexes.
            curr_idxidx = 0
            while curr_idxidx < len(idxes) - 1:
                for idx in idxes[curr_idxidx + 1:]:
                    if idx - idxes[curr_idxidx] <= k:
                        return True
                curr_idxidx += 1

        return False


assert Solution().containsNearbyDuplicate([], 0) is False
assert Solution().containsNearbyDuplicate([], 1) is False
assert Solution().containsNearbyDuplicate([1], 1) is False
assert Solution().containsNearbyDuplicate([1, 1], 1) is True
assert Solution().containsNearbyDuplicate([1, 0, 1], 3) is True
assert Solution().containsNearbyDuplicate([1, 2, 3, 4, 1], 2) is False

assert Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) is True
