"""
Question:
    String to Integer (atoi)

    Implement atoi to convert a string to an integer.

    Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

    Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

    Update (2015-02-10):
    The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

    spoilers alert... click to show requirements for atoi.

    Requirements for atoi:
    The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Performance:
    1. Total Accepted: 68934 Total Submissions: 535085 Difficulty: Easy
    2. Your runtime beats 94.41% of python submissions.
"""

INT_MAX = 2147483647
INT_MIN = -2147483648
valid_nums = set(map(str, range(0, 10)))


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # str = str.replace(" ", "")  # don't remove internal zero
        str = str.strip()
        if not str:  # length equals to zero.
            return 0

        # 1. get sign
        sign, first_char = 1, str[0]
        if first_char in ["-", "+"]:
            sign = {"+": 1, "-": -1}[first_char]
            str = str[1:]

        # 2. get result
        curr_idx = 0
        tmp_nums = []
        while curr_idx < len(str):
            if str[curr_idx] in valid_nums:
                tmp_nums.append(str[curr_idx])
                curr_idx += 1
            else:
                break
        num_str = "".join(tmp_nums) or "0"
        result = sign * int(num_str)

        # 3. fix result
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result


# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
assert Solution().myAtoi("8") == 8
assert Solution().myAtoi(" 88") == 88

# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
assert Solution().myAtoi(" +88") == 88
assert Solution().myAtoi(" -88") == -88

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
assert Solution().myAtoi(" +88s") == 88
assert Solution().myAtoi(" 8is") == 8

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
assert Solution().myAtoi("") == 0
assert Solution().myAtoi("  ") == 0
assert Solution().myAtoi(" ss") == 0

#  If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
assert Solution().myAtoi("2147483647") == 2147483647
assert Solution().myAtoi("2147483648") == 2147483647
assert Solution().myAtoi("-2147483648") == -2147483648
assert Solution().myAtoi("-2147483649") == -2147483648

# bad cases from leetcode test cases.
assert Solution().myAtoi("+-2") == 0
assert Solution().myAtoi("   +0 123") == 0
