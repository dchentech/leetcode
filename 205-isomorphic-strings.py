"""
Question:
    Isomorphic Strings

    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

    For example,
    Given "egg", "add", return true.

    Given "foo", "bar", return false.

    Given "paper", "title", return true.

    Note:
    You may assume both s and t have the same length.

Performance:
    1. Total Accepted: 30395 Total Submissions: 119565 Difficulty: Easy
    2. Your runtime beats 29.67% of python submissions.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def generate_idxes(string):
            char_to_idx = dict()
            curr_idx = 0
            idx_sequence = list()

            for char in string:
                if char not in char_to_idx:
                    char_to_idx[char] = curr_idx
                    curr_idx += 1
                idx_sequence.append(char_to_idx[char])
            return idx_sequence

        return generate_idxes(s) == generate_idxes(t)


assert Solution().isIsomorphic("egg", "add") is True
assert Solution().isIsomorphic("foo", "bar") is False
assert Solution().isIsomorphic("paper", "title") is True
