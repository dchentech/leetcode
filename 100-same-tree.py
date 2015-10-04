"""
Question:
    Same Tree

    Given two binary trees, write a function to check if they are equal or not.

    Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Performance:
    1. Total Accepted: 83658 Total Submissions: 200527 Difficulty: Easy
    2. Your runtime beats 86.00% of python submissions.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 1. zero case (important, or will recursive in step.2
        if p is None and q is None:
            return True

        # 2. fix value
        p = p or TreeNode(None)
        q = q or TreeNode(None)

        # 3. check if is the same node
        if p.val != q.val:
            return False

        # 4. recursively check
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False

        # 5. success finally
        return True


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n7 = TreeNode(7)
n4.left = n2
n4.right = n7
n2.left = n1
n2.right = n3

m1 = TreeNode(1)
m2 = TreeNode(2)
m3 = TreeNode(3)
m4 = TreeNode(4)
m7 = TreeNode(7)
m4.left = m2
m4.right = m7
m2.left = m1
m2.right = m3

l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l7 = TreeNode(7)
l4.left = l2
l4.right = l7
l2.right = l3

assert Solution().isSameTree(n4, m4) is True, Solution().isSameTree(n4, m4)
assert Solution().isSameTree(n4, l4) is False, Solution().isSameTree(n4, l4)
assert Solution().isSameTree(None, None) is True
assert Solution().isSameTree(n1, None) is False
