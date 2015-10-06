"""
Question:
    Ugly Number

    Write a program to check whether a given number is an ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

    Note that 1 is typically treated as an ugly number.

    Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 19816 Total Submissions: 60714 Difficulty: Easy
    2. Your runtime beats 60.64% of python submissions.
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        for ugly_divisor in [2, 3, 5]:
            while (num % ugly_divisor) == 0:
                num /= ugly_divisor
        return num == 1

assert Solution().isUgly(0) is False
assert Solution().isUgly(1) is True
assert Solution().isUgly(2) is True
assert Solution().isUgly(3) is True
assert Solution().isUgly(4) is True
assert Solution().isUgly(5) is True
assert Solution().isUgly(6) is True
assert Solution().isUgly(7) is False
assert Solution().isUgly(8) is True
assert Solution().isUgly(9) is True
assert Solution().isUgly(10) is True
assert Solution().isUgly(11) is False
assert Solution().isUgly(12) is True
assert Solution().isUgly(14) is False
assert Solution().isUgly(-2147483648) is False
