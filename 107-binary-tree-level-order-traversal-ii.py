"""
Question:
    Binary Tree Level Order Traversal II

    Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

    For example:

    Given binary tree {3,9,20,#,#,15,7},
        3
       / \
      9  20
        /  \
       15   7

    return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]

    confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

Performance:
    1. Total Accepted: 54938 Total Submissions: 174631 Difficulty: Easy
    2. Your runtime beats 91.80% of python submissions.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<TreeNode#{}>".format(self.val)
        # return "<TreeNode#{} left:{}, right:{}>".format(self.val, self.left, self.right)


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        curr_level_nodes = [root]
        result = []

        while curr_level_nodes:
            result.insert(0, map(lambda n: n.val, curr_level_nodes))

            tmp = []
            for node in curr_level_nodes:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            curr_level_nodes = tmp

        return result


l3 = TreeNode(3)
l9 = TreeNode(9)
l20 = TreeNode(20)
l15 = TreeNode(15)
l7 = TreeNode(7)
l3.left = l9
l3.right = l20
l20.left = l15
l20.right = l7

l_expect = [
    [15, 7],
    [9, 20],
    [3],
]

assert Solution().levelOrderBottom(l3) == l_expect
