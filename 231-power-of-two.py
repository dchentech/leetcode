"""
Question:
    Power of Two

    Given an integer, write a function to determine if it is a power of two.

    Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 31274 Total Submissions: 99121 Difficulty: Easy
    2. Your runtime beats 82.84% of python submissions.
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        """
        Example output
        >>> bin(2)
        '0b10'
        >>> bin(4)
        '0b100'
        >>> bin(8)
        '0b1000'
        >>> bin(64)
        '0b1000000'
        >>> bin(512)
        '0b1000000000'
        """
        bin_str = bin(n)
        bin_str_left = bin_str[0:3]
        bin_str_right = bin_str[3:]
        result_left = bin_str_left == "0b1"
        result_right = bin_str_right.count("0") == len(bin_str_right)
        return result_left and result_right

    def isPowerOfTwo_from_other(self, n):
        """
        >>> 4&3
        0
        >>> bin(4)
        '0b100'
        >>> bin(3)
        '0b11'
        """
        return n > 0 and (n & (n - 1)) == 0


assert Solution().isPowerOfTwo(0) is False
assert Solution().isPowerOfTwo(-1) is False
assert Solution().isPowerOfTwo(1) is True
assert Solution().isPowerOfTwo(2) is True
assert Solution().isPowerOfTwo(3) is False
assert Solution().isPowerOfTwo(4) is True
assert Solution().isPowerOfTwo(15) is False
assert Solution().isPowerOfTwo(16) is True
