"""
Question:
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

Performance:
    1. Total Accepted: 59004 Total Submissions: 272050 Difficulty: Easy
    2.

"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        mid_row = numRows / 2 + 1
        group_chars_size = numbers + 1
        result = []

        for each_row in numRows:
            pass
        """


result = Solution().convert("PAYPALISHIRING", 3)
assert result == "PAHNAPLSIIGYIR", result
