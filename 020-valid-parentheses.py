"""
Question:
    Valid Parentheses My Submissions Question Solution

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Performance:
    1. Total Accepted: 71155 Total Submissions: 265078 Difficulty: Easy
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_set = set(["()", "[]", "{}"])
        max_group = (len(s) + 1) / 2
        is_valid = True

        for idx in xrange(max_group):
            curr_group = s[idx*2:idx*2+2]
            if curr_group not in valid_set:
                is_valid = False
                break

        return is_valid


assert Solution().isValid("()") is True
assert Solution().isValid("()[]{}") is True
assert Solution().isValid("([])") is True
assert Solution().isValid("(]") is False
assert Solution().isValid("([)]") is False
assert Solution().isValid("[") is False
