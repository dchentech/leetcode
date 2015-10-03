"""
Question:
    Maximum Depth of Binary Tree

    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Performance:
    1. Total Accepted: 90742 Total Submissions: 198956 Difficulty: Easy
    2. Your runtime beats 93.77% of python submissions.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        max_depth = 0
        current_level_nodes = [root]

        while len(current_level_nodes) > 0:
            tmp_level_nodes = []
            for node in current_level_nodes:
                if node.left:
                    tmp_level_nodes.append(node.left)
                if node.right:
                    tmp_level_nodes.append(node.right)
            max_depth += 1
            current_level_nodes = tmp_level_nodes

        return max_depth


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n7 = TreeNode(7)
n4.left = n2
n4.right = n7
n2.left = n1
n2.right = n3
assert Solution().maxDepth(n4) == 3, Solution().maxDepth(n4)
assert Solution().maxDepth(n1) == 1
assert Solution().maxDepth(None) == 0
