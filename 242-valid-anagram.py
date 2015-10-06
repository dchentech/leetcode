"""
Question:
    Valid Anagram

    Given two strings s and t, write a function to determine if t is an anagram of s.

    For example,
    s = "anagram", t = "nagaram", return true.
    s = "rat", t = "car", return false.

    Note:
    You may assume the string contains only lowercase alphabets.

Performance:
    1. Total Accepted: 27749 Total Submissions: 76856 Difficulty: Easy
    2. Your runtime beats 67.92% of python submissions.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            return sorted(s) == sorted(t)


assert Solution().isAnagram("anagram", "nagaram") is True
assert Solution().isAnagram("rat", "cat") is False
assert Solution().isAnagram("", "") is True
