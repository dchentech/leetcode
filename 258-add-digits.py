"""
Question:
    Add Digits

    Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

    For example:

    Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

    Follow up:
    Could you do it without any loop/recursion in O(1) runtime?

    Hint:

    A naive implementation of the above process is trivial. Could you come up with other methods?
    What are all the possible results?
    How do they occur, periodically or randomly?
    You may find this Wikipedia article useful.
    Credits:

    Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 27859 Total Submissions: 60091 Difficulty: Easy
    2. Your runtime beats 83.45% of python submissions.
"""


class SolutionInStupidWay(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 9:
            return num

        result = 0
        while num > 0:
            remainder = num % 10
            result += remainder
            num /= 10
        return self.addDigits(result)


Solution = SolutionInStupidWay

assert Solution().addDigits(0) == 0
assert Solution().addDigits(38) == 2
