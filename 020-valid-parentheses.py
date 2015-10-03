"""
Question:
    Valid parenthesis

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Performance:
    1. Total Accepted: 71155 Total Submissions: 265078 Difficulty: Easy
    2. Your runtime beats 61.06% of python submissions.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_left_parenthesis_set = set(["(", "[", "{"])
        valid_right_parenthesis_set = set([")", "]", "}"])
        valid_parenthesis_match_dict = {")": "(", "]": "[", "}": "{"}
        parenthesis_stack = list()
        is_valid = True

        for char in s:
            if char in valid_left_parenthesis_set:
                parenthesis_stack.append(char)
            if char in valid_right_parenthesis_set:
                # the only valid case
                if len(parenthesis_stack) > 0:
                    pop_char = parenthesis_stack.pop()
                    if valid_parenthesis_match_dict[char] == pop_char:  # Don't use "is", use "==" to compare str or unicode type.
                        continue
                # othe invalid cases
                is_valid = False
                break

        # Have remain unpoped items.
        if len(parenthesis_stack) > 0:
            is_valid = False

        return is_valid


assert Solution().isValid("()") is True
assert Solution().isValid("()[]{}") is True
assert Solution().isValid("([])") is True
assert Solution().isValid("(]") is False
assert Solution().isValid("([)]") is False
assert Solution().isValid("[") is False
