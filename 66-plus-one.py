"""
Question:
    Plus One

    Given a non-negative number represented as an array of digits, plus one to the number.

    The digits are stored such that the most significant digit is at the head of the list.

Performance:
    1. Total Accepted: 66486 Total Submissions: 216562 Difficulty: Easy
    2. Your runtime beats 66.37% of python submissions.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        to_number = int("".join(map(str, digits)))
        result_number = to_number + 1
        return map(int, list(str(result_number)))

assert Solution().plusOne([0]) == [1]
assert Solution().plusOne([3]) == [4]
assert Solution().plusOne([9]) == [1, 0]
assert Solution().plusOne([9, 9]) == [1, 0, 0]
assert Solution().plusOne([1, 9, 9]) == [2, 0, 0]
