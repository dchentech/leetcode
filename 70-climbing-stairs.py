"""
Question:
    Climbing Stairs

    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Performance:
    1. Total Accepted: 72958 Total Submissions: 209852 Difficulty: Easy
    2. Your runtime beats 90.55% of python submissions.
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        prev1 = 0
        prev2 = 1
        result = None

        while n >= 1:
            # at first time, + prev1==0, prev1 and prev2 became the same number, 1.
            # and then, going on..., prev2 is bigger than prev1 for ever now.
            result = prev1 + prev2
            prev1, prev2 = prev2, result
            n -= 1
        return result


assert Solution().climbStairs(0) == 0
assert Solution().climbStairs(1) == 1  # [[1], ]
assert Solution().climbStairs(2) == 2  # [[1,1], [2], ]
assert Solution().climbStairs(3) == 3  # [[1,1,1], [1,2], [2,1], ]
assert Solution().climbStairs(4) == 5  # [[1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2], ]
assert Solution().climbStairs(5) == 8  # [[1,1,1,1,1], [2,1,1,1], [1,2,1,1], [1,1,2,1], [1,1,1,2], [2,2,1], [2,1,2], [1,2,2], ]
assert Solution().climbStairs(6) == 13  # [[1,1,1,1,1,1], [2,1,1,1,1], [1,2,1,1,1], [1,1,2,1,1], [1,1,1,2,1], [1,1,1,1,2], [2,2,1,1], [2,1,2,1], [2,1,1,2], [1,2,2,1], [1,2,1,2], [1,1,2,2], [2,2,2], ]


# This version is a little diffcult to understand totally.
class SolutionFromJw2013:
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, current + prev
        return current


"""
        remain_size = n - 0
        already_steps = 0

        def rest_steps(remain_size, already_steps):
            if remain_size > 0:
                if remain_size == 1:
                    already_steps += 1
                    return rest_steps(remain_size - 1, already_steps)
                else:  # >= 2
                    already_steps *= 2
                    rest_steps(remain_size - 1, already_steps)
            return already_steps

        return rest_steps(remain_size, already_steps)
"""
