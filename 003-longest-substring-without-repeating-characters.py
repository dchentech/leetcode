"""
Question:
    Longest Substring Without Repeating Characters My Submissions Question Solution

    Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        class MaxWindow(object):
            def __init__(self, string, start_idx, max_idx):
                self.string = string
                self.start_idx = start_idx
                self.max_idx = max_idx
                self.substring = set([])

            def run(self):
                assert self.start_idx <= self.max_idx, [self.start_idx, self.max_idx]
                end_idx = self.start_idx

                while end_idx <= self.max_idx:
                    curr_char = self.string[end_idx]
                    if curr_char in self.substring:
                        break
                    else:
                        self.substring.add(curr_char)
                        end_idx += 1

                return self

            def __repr__(self):
                return "<MaxWindow %s {start_idx: %s, substring: %s}" % (hash(self), self.start_idx, str(self.substring))

        if len(s) == 0:
            return 0
        s_max_idx = len(s) - 1

        result = [MaxWindow(s, char_idx, s_max_idx).run() for char_idx in xrange(len(s))]

        max_window = max(result, key=lambda item: len(item.substring))
        print max_window
        return len(max_window.substring)

result = Solution().lengthOfLongestSubstring("")
assert result == len(""), result

result = Solution().lengthOfLongestSubstring("c")
assert result == len("c"), result

result = Solution().lengthOfLongestSubstring("abcabcbb")
assert result == len("abc"), result

result = Solution().lengthOfLongestSubstring("bbbbb")
assert result == len("b"), result
