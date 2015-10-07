"""
Question:
    Length of Last Word

    Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a character sequence consists of non-space characters only.

    For example,
    Given s = "Hello World",
    return 5.

Performance:
    1. Total Accepted: 67210 Total Submissions: 244191 Difficulty: Easy
    2. Your runtime beats 81.96% of python submissions.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = filter(lambda w: w, s.split(" "))
        if words:
            return len(words[-1])
        else:
            return 0

assert Solution().lengthOfLastWord("Hello World") == 5
assert Solution().lengthOfLastWord("Hello World  ") == 5
assert Solution().lengthOfLastWord("Hello   World") == 5
assert Solution().lengthOfLastWord("World") == 5
assert Solution().lengthOfLastWord("World  ") == 5
assert Solution().lengthOfLastWord("   World") == 5
assert Solution().lengthOfLastWord("   ") == 0
