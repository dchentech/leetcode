"""
Question:
    Longest Substring Without Repeating Characters My Submissions Question Solution

    Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.


Annotation:
    1. In a O(1) algorithm, just start from the duplicated found element, and don't start with the window begin next element, cause it's already the longest substring without repeating characters until now.
    2. performance, "Your runtime beats 37.55% of python submissions."
"""


class Solution_slow(object):
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


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print "\ninput:", s
        if len(s) == 0:
            return 0

        not_exists_idx = -1  # the index that we can't found an element in a Python array.
        last_appeared_char_idxes = dict()
        longest_length = 0
        window_begin = 0
        window_end = None

        for idx, char in enumerate(s):
            window_end = idx + 1
            idx_pre = last_appeared_char_idxes.get(char, not_exists_idx)
            if idx_pre != not_exists_idx:
                window_begin = max(window_begin, idx_pre + 1)  # don't look back, cause there're more than two duplicated chars.
            longest_length = max(longest_length, window_end - window_begin)
            last_appeared_char_idxes[char] = idx
            # print "idx:", idx, "longest_length:", longest_length, "window_begin:", window_begin, "window_end:", window_end

        return longest_length


result = Solution().lengthOfLongestSubstring("")
assert result == len(""), result

result = Solution().lengthOfLongestSubstring("c")
assert result == len("c"), result

result = Solution().lengthOfLongestSubstring("abcabcbb")
assert result == len("abc"), result

result = Solution().lengthOfLongestSubstring("bbbbb")
assert result == len("b"), result

result = Solution().lengthOfLongestSubstring("abbaaaaaaaa")  # double duplicated chars testcase.
assert result == len("ab"), result

result = Solution().lengthOfLongestSubstring("wobgrovw")
assert result == len("bgrovw"), result
