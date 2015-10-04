"""
Question:
    Implement strStr().

    Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Update (2014-11-02):
    The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button  to reset your code definition.

Performance:
    1. Total Accepted: 71923 Total Submissions: 315607 Difficulty: Easy
"""


class SolutionBruteMatch(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack_idx = -1

        if len(needle) > len(haystack):
            return haystack_idx
        if len(needle) == 0:
            return 0

        for idx, char in enumerate(haystack):
            if char == needle[0]:
                if haystack[idx:idx+len(needle)] == needle:
                    haystack_idx = idx
                    break
        return haystack_idx


class SolutionKMP(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """


Solution = SolutionKMP


assert Solution().strStr("", "") == 0
assert Solution().strStr("", "Bar") == -1
assert Solution().strStr("Foo Bar Baz", "Bar") == 4  # testcase from strStr man page.
assert Solution().strStr("Foo Bar Baz", " ") == 3
assert Solution().strStr("a", "") == 0

"""
1
2
3
char:  | a | b | a | b | a | b | c | a |
index: | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
value: | 0 | 0 | 1 | 2 | 3 | 4 | 0 | 1 |
I know KMP partial table is about count common prefix or suffix string.
But this example are confused, it's also can be explained as with start, 1-6 abab is part of 1-6 ababab, c is not matching, and a is still starting at 1.
"""
