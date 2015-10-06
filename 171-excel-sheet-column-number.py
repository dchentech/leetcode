"""
Question:
    Excel Sheet Column Number

    Related to question Excel Sheet Column Title

    Given a column title as appear in an Excel sheet, return its corresponding column number.

    For example:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28

    Credits:
    Special thanks to @ts for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 45512 Total Submissions: 122067 Difficulty: Easy
    2. Your runtime beats 46.05% of python submissions.

Annotation:
    1. refer to 168-excel-sheet-column-title.py
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha_to_num = {chr(idx): idx - 64 for idx in range(ord('A'), ord('Z') + 1)}
        alpha_size = len(alpha_to_num)  # 26

        num = 0
        level = 1
        for char in reversed(s):
            num += alpha_to_num[char] * level
            level *= alpha_size

        return num


assert Solution().titleToNumber("A") == 1
assert Solution().titleToNumber("B") == 2
assert Solution().titleToNumber("C") == 3
assert Solution().titleToNumber("Y") == 25
assert Solution().titleToNumber("Z") == 26
assert Solution().titleToNumber("AA") == 27
assert Solution().titleToNumber("AB") == 28
assert Solution().titleToNumber("AZ") == 52
