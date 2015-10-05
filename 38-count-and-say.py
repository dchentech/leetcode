"""
    Count and Say

    The count-and-say sequence is the sequence of integers beginning as follows:
    1, 11, 21, 1211, 111221, ...

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth sequence.

    Note: The sequence of integers will be represented as a string.

    ----------------- A better description from careercup.com ---------------
    "Count and Say problem" Write a code to do following:
    n String to print
    0 1
    1 1 1
    2 2 1
    3 1 2 1 1
    ...
    Base case: n = 0 print "1"
    for n = 1, look at previous string and write number of times a digit is seen and the digit itself. In this case, digit 1 is seen 1 time in a row... so print "1 1"
    for n = 2, digit 1 is seen two times in a row, so print "2 1"
    for n = 3, digit 2 is seen 1 time and then digit 1 is seen 1 so print "1 2 1 1"
    for n = 4 you will print "1 1 1 2 2 1"

    Consider the numbers as integers for simplicity. e.g. if previous string is "10 1" then the next will be "1 10 1 1" and the next one will be "1 1 1 10 2 1"


Performance:
    1. Total Accepted: 56840 Total Submissions: 219756 Difficulty: Easy
"""

class Solution(object):
    # Thanks https://github.com/jw2013/Leetcode-Py/blob/master/Count%20and%20Say.py
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = "1"

        for time in xrange(n - 1):
            idx, next_sequence = 0, ""
            end_idx = len(sequence) - 1
            while idx < len(sequence):
                count = 1
                while idx < end_idx and sequence[idx] == sequence[idx + 1]:
                    idx += 1
                    count += 1
                next_sequence += "{}{}".format(count, sequence[idx])
                idx += 1
            sequence = next_sequence

        return sequence


def test_func(result, expect):
    assert result == expect, [result, expect]

test_func(Solution().countAndSay(1), "1")
test_func(Solution().countAndSay(2), "11")
test_func(Solution().countAndSay(3), "21")
test_func(Solution().countAndSay(4), "1211")
test_func(Solution().countAndSay(5), "111221")
test_func(Solution().countAndSay(6), "312211")


"""
        if n == 0:
            return sequence

        while n > 0:
            next_sequence = ""
            curr_char = sequence[0]
            curr_char_matching_count = 1
            dummy_end = len(sequence)  # to finish the last count+num
            is_same = False
            for idx in xrange(1, dummy_end + 1):
                if idx < dummy_end:
                    is_same = sequence[idx] == curr_char
                    if is_same:
                        curr_char_matching_count += 1

                if (idx == dummy_end) or not is_same:
                    next_sequence += curr_char + str(curr_char_matching_count)

                # prepare next round
                if (idx < dummy_end) and (not is_same):
                    curr_char = sequence[idx]

            sequence = next_sequence
            n -= 1"""

"""
NOTE: If dont use a cursor, but use some variables to hold position informations, it's hard to debug!!! And it costs me several hours...

class Solution(object):
    def countAndSay(self, num):
        sequence = "1"  # the default start

        for time in range(num):
            next_sequence = ""
            curr_char_matching_count = 1

            for idx, curr_char in enumerate(sequence):
                if idx < len(curr_char) - 1:
                    if curr_char == sequence[idx + 1]:
                        curr_char_matching_count += 1
                    else:
                        next_sequence += (str(curr_char_matching_count) + curr_char)
                        curr_char_matching_count = 0
                if idx == len(curr_char) - 1:
                    next_sequence += (str(curr_char_matching_count) + curr_char)
            sequence = next_sequence

        print "sequence:", sequence
        print "-"*100
        print
        return sequence

"""
