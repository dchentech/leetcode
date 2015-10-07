"""
Question:
    Rectangle Area

    Find the total area covered by two rectilinear rectangles in a 2D plane.

    Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

    Rectangle Area
    Assume that the total area is never beyond the maximum possible value of int.

    Credits:
    Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.

Performance:
    1. Total Accepted: 19441 Total Submissions: 73008 Difficulty: Easy
    2. Your runtime beats 20.57% of python submissions.
"""

class Solution(object):
    """
    result = Rectangle 1 + Rectangle 2 - common Rectangle

    My spatial ability is too poor..., and I refer to other one's solution finally.


    """

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def compute(a, b, c, d):
            return abs((c - a) * (d - b))
        first_area = compute(A, B, C, D)
        second_area = compute(E, F, G, H)

        # common area.
        common_a = max(A, E)
        common_b = max(B, F)
        common_c = min(C, G)
        common_d = min(D, H)
        # if it's separated to the opposite direction, then modify to zero.
        overlap = max(common_c - common_a, 0) * max(common_d - common_b, 0)

        return first_area + second_area - overlap

    def computeArea_from_jw2013(self, A, B, C, D, E, F, G, H):
        overlap = max(min(C, G)-max(A, E), 0) * max(min(D, H)-max(B, F), 0)
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap


# 1. has common
# 45 = 24 + 27 - 6
assert Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 45, Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2)

# 16 = 16 + 16 - 16
assert Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2) == 16

# 2. has no common
assert Solution().computeArea(-2, -2, 2, 2, 3, 3, 4, 4) == 17

# 3. one inside another
assert Solution().computeArea(-2, -2, 2, 2, -1, -1, 1, 1) == 16

assert Solution().computeArea(-2, -2, 2, 2, -3, -3, -2, -2) == 17  # 13


"""
Bad code ...

        first_area = compute(A, B, C, D)
        second_area = compute(E, F, G, H)

        has_common = False
        if A <= E <= C or A <= G <= C:
            has_common = True

        # 1. no common
        # (B >= H) or (C <= E)

        bigger_area = None
        result = set([A <= E, B <= F, C >= G, D >= H])
        if result == set([True]):
            bigger_area = first_area
        if result == set([False]):
            bigger_area = second_area
        is_inside = bool(bigger_area)

        import pdb
        pdb.set_trace()

        # let `is_inside` go ahead of `has_common`, cause `is_inside` is specific case of `has_common`
        if is_inside:
            return bigger_area

        if has_common:
            # Maybe it's not ordered well
            common_rectangle_1 = B
            common_rectangle_2 = E
            common_rectangle_3 = C
            common_rectangle_4 = H

            common_area = compute(common_rectangle_1, common_rectangle_2, common_rectangle_3, common_rectangle_4)

            return first_area + second_area - common_area

        return first_area + second_area
"""
