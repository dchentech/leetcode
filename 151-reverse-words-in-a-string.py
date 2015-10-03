"""
Question:
    Reverse Words in a String

    Given an input string, reverse the string word by word.

    For example,
    Given s = "the sky is blue",
    return "blue is sky the".

    Update (2015-02-12):
    For C programmers: Try to solve it in-place in O(1) space.

    click to show clarification.

    Clarification:
    What constitutes a word?
    A sequence of non-space characters constitutes a word.
    Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or trailing spaces.
    How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.

Performance:
    1. Total Accepted: 77621 Total Submissions: 507097 Difficulty: Medium
    2. Your runtime beats 72.17% of python submissions.

Annotation:
    1. It's quickest question that I have ever done.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(filter(lambda i: len(i) > 0, s.strip().split(" "))))


assert Solution().reverseWords("the sky is blue") == "blue is sky the"
assert Solution().reverseWords("  the   sky is blue") == "blue is sky the"
