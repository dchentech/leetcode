"""
Question:
    Excel Sheet Column Title

    Given a positive integer, return its corresponding column title as appear in an Excel sheet.

    For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

    Credits:
    Special thanks to @ifanchu for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 38719 Total Submissions: 205685 Difficulty: Easy
    2. Your runtime beats 88.29% of python submissions.  # weird, same code but different result.

Annotation:
    1. Thanks https://github.com/haoel/leetcode/blob/master/algorithms/excelSheetColumnTitle/excelSheetColumnTitle.cpp for the idea.
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        num_to_alpha = {idx - 64: chr(idx) for idx in range(ord('A'), ord('Z') + 1)}
        alpha_size = len(num_to_alpha)

        digits = []
        while n > 0:
            m = n % alpha_size  # like the decimal system, 12 % 10 == 1
            if m == 0:  # Fix display Z
                m = alpha_size
            digits.insert(0, m)  # put m in the end
            n -= m  # remove stored result, and calculate next level.
            n /= alpha_size

        alphas = map(lambda d: num_to_alpha[d], digits)
        result = "".join(alphas)
        # print "result:", result
        return result


assert Solution().convertToTitle(1) == "A"
assert Solution().convertToTitle(2) == "B"
assert Solution().convertToTitle(3) == "C"
assert Solution().convertToTitle(25) == "Y"
assert Solution().convertToTitle(26) == "Z"
assert Solution().convertToTitle(27) == "AA"
assert Solution().convertToTitle(28) == "AB"
assert Solution().convertToTitle(52) == "AZ"
