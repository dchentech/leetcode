"""
Question:
    Balanced Binary Tree

    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Performance:
    1. Total Accepted: 75753 Total Submissions: 235055 Difficulty: Easy
    2. Your runtime beats 77.45% of python submissions.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<Node#{}>".format(self.val)

class SolutionWrong(object):
    """
    This solution can't handle comparing the height of both left and right.
    """
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def func(node, parent):
            if node is None:
                return True

            if not func(node.left, node):
                print "node.left:", node.left
                return False

            if not func(node.right, node):
                print "node.right:", node.right
                return False

            if parent is None:
                print "no parent:", node, parent
                return True
            else:
                # as a leaf
                if node.left is None and node.right is None:
                    print "both left and right:", node
                    return True
                # when parent is present, left and right must exists.
                if bool(node.left or node.right) and bool(parent.left and parent.right):
                    print "no left and right and parent:", node
                    return True
                # the bad case, only one exists, and has a parent.
                print "node:", node
                return False
        return func(root, None)


import math

class SolutionFromJw2013:
    def isBalanced(self, root):
        return self.getHeight(root) != -1

    def getHeight(self, root):
        if root is None:
            return 0
        left_height, right_height = self.getHeight(root.left), self.getHeight(root.right)
        if left_height < 0 or right_height < 0 or math.fabs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1


class SolutionImproved(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # so we can know two subtree differ by more than 1,
        # when we do abs(left - right) > 1
        invalid_sign = -1

        def get_height_of_a_tree(node):
            # it means we reach at the end of current tree
            if node is None:
                return 0
            # recursively get the height, as the balanced tree is defined recursively
            left_height, right_height = get_height_of_a_tree(node.left), get_height_of_a_tree(node.right)

            # it's also because another return of -1
            is_invalid = left_height == invalid_sign or right_height == invalid_sign
            # the definition of un-balanced-binary-tree
            is_over_height = abs(left_height - right_height) > 1
            if is_invalid or is_over_height:
                return invalid_sign  # here is the recursive starting point
            return max(left_height, right_height) + 1

        return get_height_of_a_tree(root) != invalid_sign


Solution = SolutionImproved

"""
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
 """

print "n:", "#"*30
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

assert Solution().isBalanced(n4) is True
assert Solution().isBalanced(n2) is True
assert Solution().isBalanced(n1) is True


"""
         4
       /   \
      2     7
     / \   /
    1   3 6
 """

print "m:", "#"*30
m1 = TreeNode(1)
m2 = TreeNode(2)
m3 = TreeNode(3)
m4 = TreeNode(4)
m6 = TreeNode(6)
m7 = TreeNode(7)
# m9 = TreeNode(9)  # remove this one
m4.left = m2
m4.right = m7
m2.left = m1
m2.right = m3
m7.left = m6
# n7.right = n9  # and the link

assert Solution().isBalanced(m4) is True


"""
         4
       /
      2
     /
    1
 """

print "l:", "#"*30
l4 = TreeNode(4)
l2 = TreeNode(2)
l1 = TreeNode(1)
l4.left = l2
l2.left = l1
assert Solution().isBalanced(l4) is False


"""
         4
       /   \
      2     7
     / \
    1   3
   /
  0
 """

print "s:", "#"*30
s0 = TreeNode(0)
s1 = TreeNode(1)
s2 = TreeNode(2)
s3 = TreeNode(3)
s4 = TreeNode(4)
s6 = TreeNode(6)
s7 = TreeNode(7)
# s9 = TreeNode(9)  # remove this one
s4.left = s2
s4.right = s7
s2.left = s1
s1.left = s0
s2.right = s3
# s7.left = s6
# s7.right = s9  # and the link

assert Solution().isBalanced(s4) is False


"""
Bad case.

Runtime Error Message:
Line 17: TypeError: unsupported operand type(s) for -: 'str' and 'str'
Last executed input:
[1,2,2,3,null,null,3,4,null,null,4]

         1
       /   \
      2     2
     /       \
    3         3
   /           \
  4             4
 """

print "t:", "#"*30
t1 = TreeNode(1)
t2l = TreeNode(2)
t2r = TreeNode(2)
t3l = TreeNode(3)
t3r = TreeNode(3)
t4l = TreeNode(4)
t4r = TreeNode(4)
t1.left = t2l
t1.right = t2r
t2l.left = t3l
t3l.left = t4l
t2r.left = t3r
t3r.left = t4r
assert Solution().isBalanced(t1) is False
