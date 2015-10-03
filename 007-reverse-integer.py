"""
Question:
    Reverse digits of an integer.

    Example1: x = 123, return 321
    Example2: x = -123, return -321

    click to show spoilers.

    Have you thought about this?
    Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

    If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

    Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

    Update (2014-11-10):
    Test cases had been added to test the overflow behavior.

Annotation:
    1. Your runtime beats 51.75% of python submissions.
    2. Optimize: Or use Math operation on the original x.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        max_int = 2147483647

        reversed_x = int("".join(reversed(list(str(abs(x))))))
        if reversed_x >= max_int:
            return 0

        if is_negative:
            reversed_x = -1 * reversed_x
        return reversed_x


assert Solution().reverse(123) == 321
assert Solution().reverse(-123) == -321
assert Solution().reverse(1000000003) == 0  # overflow
assert Solution().reverse(0) == 0
assert Solution().reverse(10) == 1
assert Solution().reverse(1000000) == 1
assert Solution().reverse(1534236469) == 0
