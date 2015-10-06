# -*-coding:utf-8-*-


"""
Question:
    Lowest Common Ancestor of a Binary Search Tree

    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

            _______6______
           /              \
        ___2__          ___8__
       /      \        /      \
       0      _4       7       9
             /  \
             3   5
    For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Performance:
    1. Total Accepted: 28843 Total Submissions: 75868 Difficulty: Easy
    2. Your runtime beats 7.19% of python submissions.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    The main idea is figure out to using the order of nodes values.

    Getting ideas from http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
    1. Get the finding a node idea first. Wrong, cause there still no back way to find the sequence.
    2. It's a binary search tree, left is smaller than right. It's the key.
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # cause root is already the highest.
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

n0 = TreeNode(0)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n6.left = n2
n6.right = n8
n2.left = n0
n2.right = n4
n8.left = n7
n8.right = n9
n4.left = n3
n4.right = n5
n2.left = n0

assert Solution().lowestCommonAncestor(n6, n2, n8) is n6
assert Solution().lowestCommonAncestor(n6, n2, n4) is n2
