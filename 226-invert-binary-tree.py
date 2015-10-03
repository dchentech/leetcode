# -*-coding:utf-8-*-

"""
Question:
    Invert Binary Tree

    Invert a binary tree.

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    to
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

    Trivia:
    This problem was inspired by this original tweet by Max Howell:
    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

Performance:
    1. Total Accepted: 40077 Total Submissions: 101621 Difficulty: Easy
    2. Your runtime beats 48.69% of python submissions.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n6 = TreeNode(6)
n7 = TreeNode(7)
n9 = TreeNode(9)
n4.left = n2
n4.right = n7
n2.left = n1
n2.right = n3
n7.left = n6
n7.right = n9

Solution().invertTree(n4)
assert n4.left == n7
assert n4.right == n2
assert n7.left == n9
assert n7.right == n6
assert n2.left == n3
assert n2.right == n1
