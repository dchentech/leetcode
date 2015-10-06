"""
Question:
    Symmetric Tree

    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

    For example, this binary tree is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3
    But the following is not:
        1
       / \
      2   2
       \   \
       3    3

    Note:
    Bonus points if you could solve it both recursively and iteratively.

    confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

Performance:
    1. Total Accepted: 74418 Total Submissions: 232487 Difficulty: Easy
    2. SolutionRecursive # => Your runtime beats 81.30% of python submissions.
    3. SolutionIterate   # => Your runtime beats 46.96% of python submissions.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<TreeNode#{}>".format(self.val)

class SolutionRecursive(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # check them are same value, but opposite directions.
        def func(left_node, right_node):
            # 1. check current
            if left_node is None and right_node is None:
                return True
            # based on the first case
            if left_node is None or right_node is None:
                return False

            # 2. starting recursive
            if not func(left_node.left, right_node.right):
                return False
            if not func(left_node.right, right_node.left):
                return False

            return left_node.val == right_node.val

        if root is None:
            return True
        return func(root.left, root.right)


class SolutionIterate(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        same_level_nodes = [root.left, root.right]
        # Make sure None values still work between the left and the right nodes.
        get_value_with_fix_none_node = lambda n: (n or TreeNode(n)).val

        while same_level_nodes:
            # check it's the same at the same level
            if len(same_level_nodes) % 2 != 0:
                return False

            values = map(get_value_with_fix_none_node, same_level_nodes)
            left_values = values[0:len(values) / 2]
            right_sorted_values = list(reversed(values[len(values) / 2:]))
            if left_values != right_sorted_values:
                return False

            # prepare the next level
            tmp = []
            for node in same_level_nodes:
                # yes, center part of current level are None values.
                if node is None:
                    continue
                tmp += [node.left, node.right]
            same_level_nodes = tmp

        return True

Solution = SolutionRecursive
Solution = SolutionIterate

# Good case
l1 = TreeNode(1)
l2l = TreeNode(2)
l2r = TreeNode(2)
l3l = TreeNode(3)
l3r = TreeNode(3)
l4l = TreeNode(4)
l4r = TreeNode(4)
l1.left = l2l
l1.right = l2r
l2l.left = l3l
l2l.right = l4l
l2r.right = l3r
l2r.left = l4r
assert Solution().isSymmetric(l1) is True
# Bad case (just not mirror, both 3 are right.)
n1 = TreeNode(1)
n2l = TreeNode(2)
n2r = TreeNode(2)
n3l = TreeNode(3)
n3r = TreeNode(3)
n1.left = n2l
n1.right = n2r
n2l.left = n3l
n2l.right = n3r
assert Solution().isSymmetric(n1) is False
