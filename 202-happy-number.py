"""
Question:
    Happy Number

    Write an algorithm to determine if a number is "happy".

    A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

    Example: 19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

    Credits:
    Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 34378 Total Submissions: 104779 Difficulty: Easy
    2. Your runtime beats 55.38% of python submissions.
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = self.compute(n)
        if result["is_endless"]:
            return False
        return True

    def compute(self, n):
        num = n  # n is already a positive integer

        is_endless = False
        same_nums = set([])  # check if it's already in a endless loop

        while num != 1 and not is_endless:
            num = sum(map(lambda i: i * i, map(int, list(str(num)))))
            if num in same_nums:
                is_endless = True
                break
            same_nums.add(num)
        return {"num": num, "is_endless": is_endless}


assert Solution().compute(19)["num"] == 1
assert Solution().compute(0)["num"] == 0
assert Solution().compute(1)["num"] == 1


assert Solution().isHappy(19) is True
assert Solution().isHappy(0) is False
assert Solution().isHappy(1) is True
