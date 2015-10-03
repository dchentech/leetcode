"""
Question:
    Longest Common Prefix My Submissions Question Solution

    Write a function to find the longest common prefix string amongst an array of strings.

Performance:
    1. Total Accepted: 67458 Total Submissions: 261684 Difficulty: Easy
    2. Your runtime beats 77.68% of python submissions.

Annotation:
    1.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        min_length = min(map(len, strs))
        result = []

        for idx in xrange(min_length):
            same_idx_chars = map(lambda s: s[idx], strs)
            if len(set(same_idx_chars)) == 1:
                result.append(same_idx_chars[0])
            else:
                break

        return "".join(result)


result = Solution().longestCommonPrefix([])
assert result == "", result

result = Solution().longestCommonPrefix(["hello", ""])
assert result == "", result

result = Solution().longestCommonPrefix(["hello", "world"])
assert result == "", result

result = Solution().longestCommonPrefix(["hello", "hallo"])
assert result == "h", result

result = Solution().longestCommonPrefix(["abc", "abcd", "abcdefgh"])
assert result == "abc", result
