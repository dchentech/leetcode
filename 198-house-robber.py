# -*-coding:utf-8-*-

"""
Question:
    House Robber

    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

    Credits:
    Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.

Performance:
    1. Total Accepted: 35321 Total Submissions: 115955 Difficulty: Easy
    2. Your runtime beats 80.18% of python submissions.
"""


class SolutionWrong1(object):
    def rob(self, moneys):
        """
        :type moneys: List[int]
        :rtype: int
        """
        class MoneyIdx(object):
            def __init__(self, money, idx):
                self.money = money
                self.idx = idx

            def __repr__(self):
                return "<MoneyIdx money:{}, idx:{}>".format(self.money, self.idx)

            def is_adjacent(self, another):
                assert isinstance(another, MoneyIdx)
                return abs(self.idx - another.idx) == 1

        moneyidxes = [MoneyIdx(money, idx) for idx, money in enumerate(moneys)]
        sorted_moneyidxes = sorted(moneyidxes, key=lambda ni: (- ni.money, ni.idx))

        result = []
        last_moneyidx = None
        for curr_idx, curr_moneyidx in enumerate(sorted_moneyidxes):
            if last_moneyidx is None:
                last_moneyidx = curr_moneyidx  # set default value
                result.append(curr_moneyidx)
                continue

            # skip if adjacent houses.
            if curr_moneyidx.is_adjacent(last_moneyidx):
                continue  # skip current
            result.append(curr_moneyidx)

        return sum(map(lambda mi: mi.money, result))


class SolutionWrong2(object):
    """
    Split moneys ino chunks. After a chunk is processed, and next chunk should not adjacent to the last element of previous chunk.
    """
    def rob(self, moneys):
        """
        :type moneys: List[int]
        :rtype: int
        """
        if len(moneys) <= 2:
            return max(moneys + [0])  # Fix zero items

        def compute_max_in_a_chunk(chunk):
            """
            # case 1 -------------
            [2, 3, 2, 0]
             √     √

            # case 2 -------------
            [2, 3, 2, 1]
             √     √

            # case 3 -------------
            [2, 3, 2, 1, 5]
             √     √     √

            # case 4 -------------
            [2, 3, 2, 2, 5]
             √     √     √
            """
            # make sure chunk always has four elements
            chunk += [0, 0, 0]
            chunk = chunk[0:4]
            # result
            left = chunk[0] + chunk[2]
            right = chunk[1] + chunk[3]
            if left >= right:
                return {"value": left, "keep_last": True}
            else:
                return {"value": right, "keep_last": False}

        total = 0
        while moneys:
            result = compute_max_in_a_chunk(moneys[0:4])
            total += result["value"]

            remain_start = 4 if result["keep_last"] else 5
            moneys = moneys[remain_start:]

        return total


class SolutionWrong3(object):
    def rob(self, nums):
        leng = len(nums)
        if leng == 0:
            return 0
        elif leng == 1:
            return nums[0]
        elif leng == 2:
            return max(nums[0], nums[1])

        money = [0] * leng
        # set initial state
        money[0] = nums[0]
        money[1] = nums[1]
        money[2] = nums[0] + nums[2]

        # set the bigger one
        for i in range(3, leng):
            money[i] = max(money[i-2] + nums[i], money[i-3] + nums[i])

        return max(money[leng-1], money[leng-2])


class Solution(object):
    def rob(self, moneys):
        """
        :type moneys: List[int]
        :rtype: int

        Original code is https://leetcode.com/discuss/55538/java-dp-solution-in-simple-terms-and-comments.

        DP solution.
        preRob - max value if rob previous house.
        preNotRob - max value if not rob previous house.
        rob - max value if rob current house.
        notRob - max value if not rob current house.
        """
        preRob = 0
        preNotRob = 0
        rob = 0
        notRob = 0

        for money in moneys:
            """
             dp(i-1) -> dp(i) key bridging:

             dp[i][1] = dp[i-1][0] + nums[i-1]
             dp[i][0] = Max(dp[i-1][0], dp[i-1][1])
             whereas dp[i][1] means rob current house and dp[i][0] not rob,
             nums[i-1] is the cash from the current house (0 based index).
            """
            rob = preNotRob + money
            notRob = max(preRob, preNotRob)

            preNotRob = notRob
            preRob = rob

        return max(rob, notRob)


# assert Solution().rob([]) == 0
assert Solution().rob([3]) == 3
assert Solution().rob([3, 2]) == 3
assert Solution().rob([3, 2, 1]) == 4
assert Solution().rob([3, 1, 2]) == 5
assert Solution().rob([3, 3, 1]) == 4

# bad cases from LeetCode
assert Solution().rob([2, 3, 2]) == 4

# more test cases
assert Solution().rob([2, 3, 2, 2, 5]) == 9, Solution().rob([2, 3, 2, 2, 5])
#                     [2, 3, 4, 2, 5]
#                     [2, 3, 4, 5, 5]
#                     [2, 3, 4, 5, 9]
