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
            is_end = (idx + 1) == len(input_string)
            yield Pattern.new(re_char, next_char), is_end


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
            return CurrentStatus(False, start_idx)  # still the same start_idx

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
        if self.next_re_char is None:  # * match the remain chars directly.
            return CurrentStatus(True, start_idx)

        len_input = len(entire_input)
        end_idx = len_input - 1
        should_next_re_char = False
        while start_idx <= end_idx:  # still have chars
            # If match next char, and no need to increase below start_idx.
            if (start_idx != end_idx) and (self.next_re_char == entire_input[start_idx + 1]):
                should_next_re_char = True
                break  # success & stop
            # going on...
            start_idx += 1

        success = True
        # still have chars, but failed.
        if (start_idx == end_idx) and self.next_re_char and not should_next_re_char:
            success = False

        if should_next_re_char:
            return CurrentStatus(success, start_idx, should_next_re_char)
        else:
            return CurrentStatus(success, start_idx + 1)


class SolutionWrong1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = Pattern.fix_regexp(p)
        start_idx = 0
        # is_success_in_the_end = True
        current_status = None
        is_reach_pattterns_end = False

        if len(s) == 0 and len(set(p) - set(["*", "."])) > 0:
            return False
        if len(p) == 0 and len(s) > 0:
            return False
        if len(p) == 0 and len(s) == 0:
            return False

        print "\n=====>>>>>>input: s:{}, p:{}".format(s, p)
        for pattern, is_end in Pattern.pattern_generator(p):
            print pattern, "|"*10
            is_reach_pattterns_end = is_end
            status = pattern.process(s, start_idx)
            current_status = status
            start_idx = status.next_idx  # update
            print status
            print "  =>", " " * start_idx, s[start_idx:]

            # directly False
            if status.success is False:
                continue  # go to next regexp pattern
            # need another pattern (but maybe there's no remain pattern)
            if status.success is True and status.should_next_re_char:
                continue
            # yes, succesed
            if status.success is True and not status.should_next_re_char:
                break  # even still has remain pattern
            raise ValueError("Should not reach here.")

        print
        if not is_reach_pattterns_end:
            return False

        # . full success
        return current_status.success and \
            (start_idx >= len(s))  # quick hack, but TODO == is greater

        """
        # 2. yet not finish input:s
        # why: cause pattern only care about itself, but not the total regexp.
        if (start_idx + 1) <= len(s):
            is_success_in_the_end = False
        """

        # return is_success_in_the_end


class Solution2(object):
    def isMatch(self, string, pattern):
        """
        :type string: str
        :type pattern: str
        :rtype: bool
        """
        pattern_curr_idx = 0
        pattern_end_idx = len(pattern) - 1

        for char_idx, char in enumerate(string):
            while pattern_curr_idx <= pattern_end_idx:
                # match directly or any
                if char == pattern[pattern_curr_idx] or pattern[pattern_curr_idx] == ".":
                    pattern_curr_idx += 1
                    break  # continue to next for loop
                if pattern[pattern_curr_idx] == "*":
                    # * matching pattern. Ready for the next round.
                    if char == pattern[pattern_curr_idx + 1]:
                        pattern_curr_idx += 1
                        continue
                    else:
                        break  # continue to next char
                if char != pattern[pattern_curr_idx]:
                    # NOTE but maybe rest pattern matches
                    pattern_curr_idx += 1  # continue to next pattern
                    break

            if pattern_curr_idx == pattern_end_idx and char_idx == len(string) - 1:
                return True
        return False

class Solution(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


assert Solution().isMatch("aa", "a") is False
assert Solution().isMatch("aa", "aa") is True
assert Solution().isMatch("aaa", "aa") is False
assert Solution().isMatch("aa", "a*") is True
assert Solution().isMatch("aa", ".*") is True
assert Solution().isMatch("ab", ".*") is True
assert Solution().isMatch("ab", ".*c") is False
assert Solution().isMatch("aab", "c*a*b") is True
# assert Solution().isMatch("aab", "c**b") is True
assert Solution().isMatch("", "c*") is True
assert Solution().isMatch("a", "") is False
assert Solution().isMatch("", "") is True
# assert Solution().isMatch("aab", "*c") is False
