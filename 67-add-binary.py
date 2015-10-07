"""
Question:
    Add Binary

    Given two binary strings, return their sum (also a binary string).

    For example,
    a = "11"
    b = "1"
    Return "100".

Performance:
    1. Total Accepted: 58639 Total Submissions: 234979 Difficulty: Easy
    2. Your runtime beats 81.60% of python submissions.
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = int(a, 2)
        int_b = int(b, 2)
        int_result = int_a + int_b
        bin_result = bin(int_result)  # '0b11'
        return bin_result[2:]  # fix it

assert Solution().addBinary("11", "1") == "100", Solution().addBinary("11", "1")
