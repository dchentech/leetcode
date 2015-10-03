# -*-coding:utf-8-*-

"""
Question:
    Regular Expression Matching

    Implement regular expression matching with support for '.' and '*'.

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).

    The function prototype should be:
    bool isMatch(const char *s, const char *p)

    Some examples:
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "a*") → true
    isMatch("aa", ".*") → true
    isMatch("ab", ".*") → true
    isMatch("aab", "c*a*b") → true

Performance:
    1. Total Accepted: 56922 Total Submissions: 274358 Difficulty: Hard
"""


class CurrentStatus(object):
    def __init__(self, success, next_idx=None, should_next_re_char=False):
        self.success = success  # check this property FIRST!
        self.next_idx = next_idx
        self.should_next_re_char = should_next_re_char

    def __repr__(self):
        return "<CurrentStatus success: {}, :next_idx: {}, :should_next_re_char: {}>".format(
            self.success, self.next_idx, self.should_next_re_char)

class PatternStaticMethods(object):
    @staticmethod
    def fix_regexp(pattern):
        loop = True
        while loop:
            old_len = len(pattern)
            # ... we use native Python regexp engine to solve it quickly.
            pattern = pattern.replace("**", "*")
            if len(pattern) == old_len:
                break
        return pattern

    @staticmethod
    def new(curr_re_char, next_re_char=None):
        assert len(curr_re_char) == 1, curr_re_char
        cls = CharPattern
        if curr_re_char == ".":
            cls = DotPattern
        if curr_re_char == "*":
            cls = StarPattern
        return cls(curr_re_char, next_re_char)

    @staticmethod
    def pattern_generator(input_string):
        for idx, re_char in enumerate(input_string):
            next_char = None if (idx + 1) == len(input_string) else input_string[idx + 1]
            yield Pattern.new(re_char, next_char)


class Pattern(PatternStaticMethods):
    def __init__(self, curr_re_char, next_re_char=None):
        self.curr_re_char = curr_re_char
        self.next_re_char = next_re_char

    def __repr__(self):
        return "<{} curr_re_char: {}, next_re_char: {}>".format(
            self.__class__.__name__, self.curr_re_char, self.next_re_char)

    def process(self, entire_input, start_idx):
        raise NotImplementedError("return True|False")

    def process_single_char_common(self, entire_input, start_idx, yes=lambda: NotImplementedError):
        if not yes():
            return CurrentStatus(False)

        next_idx = start_idx + 1
        should_next_re_char = True
        if next_idx >= len(entire_input):
            should_next_re_char = False
        return CurrentStatus(True, next_idx, should_next_re_char)


class CharPattern(Pattern):
    def process(self, entire_input, start_idx):
        return self.process_single_char_common(
            entire_input,
            start_idx,
            yes=lambda: entire_input[start_idx] == self.curr_re_char)

class DotPattern(Pattern):
    def process(self, entire_input, start_idx):
        return self.process_single_char_common(
            entire_input,
            start_idx,
            yes=lambda: True)

class StarPattern(Pattern):
    def process(self, entire_input, start_idx):
        if self.next_re_char is None:  # match the remain chars directly.
            return CurrentStatus(True, start_idx + 1)

        len_input = len(entire_input)
        end_idx = len_input - 1
        should_next_re_char = False
        while start_idx <= end_idx:
            if start_idx < end_idx:  # still have chars
                if self.next_re_char == entire_input[start_idx + 1]:
                    should_next_re_char = True
                    break  # success & stop
                # going on...
            start_idx += 1

        success = True
        # still have chars, but failed.
        if (start_idx == end_idx) and self.next_re_char and not should_next_re_char:
            success = False

        if should_next_re_char:
            return CurrentStatus(success, start_idx + 1, should_next_re_char)
        else:
            return CurrentStatus(success, start_idx + 1)


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = Pattern.fix_regexp(p)
        start_idx = 0
        is_valid = True

        print "\ninput: s:{}, p:{}".format(s, p)
        for pattern in Pattern.pattern_generator(p):
            print pattern
            status = pattern.process(s, start_idx)
            start_idx = status.next_idx  # update
            print status

            # directly False
            if status.success is False:
                # TODO go to next?
                is_valid = False
                break
            # need another pattern (but maybe there's no remain pattern)
            if status.success is True and status.should_next_re_char:
                continue
            # yes, succesed
            if status.success is True and not status.should_next_re_char:
                break
            raise ValueError("Should not reach here.")

        # yet not finish input:s
        # why: cause pattern only care about itself, but not the total regexp.
        if (start_idx + 1) <= len(s):
            is_valid = False

        return is_valid


"""
assert Solution().isMatch("aa", "a") is False
assert Solution().isMatch("aa", "aa") is True
assert Solution().isMatch("aaa", "aa") is False
assert Solution().isMatch("aa", "a*") is True
assert Solution().isMatch("aa", ".*") is True
assert Solution().isMatch("ab", ".*") is True
"""
assert Solution().isMatch("aab", "c*a*b") is True
assert Solution().isMatch("aab", "c**b") is True
assert Solution().isMatch("aab", "*c") is False
