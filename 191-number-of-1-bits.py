# -*-coding:utf-8-*-

"""
Question:
    Number of 1 Bits

    Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

    For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

    Credits:
    Special thanks to @ts for adding this problem and creating all test cases.


Performance:
    1. Total Accepted: 53134 Total Submissions: 140123 Difficulty: Easy
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


assert Solution().hammingWeight(0) == 0
assert Solution().hammingWeight(11) == 3
assert Solution().hammingWeight(-11) == 3
