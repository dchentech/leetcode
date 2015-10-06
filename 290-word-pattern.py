"""
Question:
    Word Pattern

    Given a pattern and a string str, find if str follows the same pattern.

    Examples:
    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

    Notes:
    Both pattern and str contains only lowercase alphabetical letters.
    Both pattern and str do not have leading or trailing spaces.
    Each word in str is separated by a single space.
    Each letter in pattern must map to a word with length that is at least 1.

    Credits:
    Special thanks to @minglotus6 for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 1839 Total Submissions: 6536 Difficulty: Easy
    2. Sorry. We do not have enough accepted submissions.
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        patterns = list(pattern)
        words = str.split(" ")

        if len(patterns) != len(words):
            return False

        short_to_long = dict()
        seen_longs = set([])
        for idx, short in enumerate(patterns):
            long = words[idx]

            if short not in short_to_long:
                if long in seen_longs:
                    return False
                short_to_long[short] = long
                seen_longs.add(long)
            else:
                if short_to_long[short] != long:
                    return False
        return True


assert Solution().wordPattern("abba", "dog cat cat dog") is True
assert Solution().wordPattern("abba", "dog cat cat fish") is False
assert Solution().wordPattern("aaaa", "dog cat cat dog") is False
assert Solution().wordPattern("abba", "dog dog dog dog") is False
