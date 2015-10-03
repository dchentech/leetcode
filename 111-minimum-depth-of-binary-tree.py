"""
Question:
    Minimum Depth of Binary Tree

    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Performance:
    1. Total Accepted: 73485 Total Submissions: 251971 Difficulty: Easy
    2. Your runtime beats 95.77% of python submissions.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        based on the work of 104-maximum-depth-of-binary-tree.py
        """
        if root is None:
            return 0

        min_depth = 0
        is_find_min = False
        current_level_nodes = [root]

        while len(current_level_nodes) > 0:
            tmp_level_nodes = []
            for node in current_level_nodes:
                if node.left is None and node.right is None:
                    is_find_min = True
                    break  # the min depth, the first leaf with no children.
                if node.left:
                    tmp_level_nodes.append(node.left)
                if node.right:
                    tmp_level_nodes.append(node.right)
            min_depth += 1
            current_level_nodes = tmp_level_nodes

            if is_find_min:
                break

        return min_depth


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n7 = TreeNode(7)
n4.left = n2
n4.right = n7
n2.left = n1
n2.right = n3
assert Solution().minDepth(n4) == 2, Solution().minDepth(n4)
assert Solution().minDepth(n1) == 1
assert Solution().minDepth(None) == 0
