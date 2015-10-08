"""
Question:
    Pascal's Triangle

    Given numRows, generate the first numRows of Pascal's triangle.

    For example, given numRows = 5,
    Return

    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]

Performance:
    1. Total Accepted: 59781 Total Submissions: 195093 Difficulty: Easy
    2. Your runtime beats 34.55% of python submissions.
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        def generate_next_nums(prev_nums):
            first_num = 0  # set a dummy first
            num_idx = 0
            result = []
            while num_idx <= len(prev_nums):
                second_num = prev_nums[num_idx] if num_idx < len(prev_nums) else 0
                result.append(first_num + second_num)

                # prepare next round
                first_num = second_num
                num_idx += 1
            return result

        curr_num_row = 2
        result = [[1]]
        while curr_num_row <= numRows:  # from low to high
            curr_level_nums = generate_next_nums(result[-1])
            result.append(curr_level_nums)
            curr_num_row += 1

        return result


assert Solution().generate(0) == []
assert Solution().generate(1) == [[1]]
assert Solution().generate(2) == [[1], [1, 1]]
assert Solution().generate(3) == [[1], [1, 1], [1, 2, 1]]
assert Solution().generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
