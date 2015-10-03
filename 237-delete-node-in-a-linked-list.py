"""
Question:
    Delete Node in a Linked List

    Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

    Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

Performance:
    1. Total Accepted: 32965 Total Submissions: 73695 Difficulty: Easy
    2. Your runtime beats 45.99% of python submissions.

Annotation:
    1. So stupid, I had submitted it for 4 times!!!, and after looked @haoel 's C++ code.
    2. I was confused, what is exactly delete a node, just changed the value.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
Solution().deleteNode(n3)
assert n2.next.val == 4, n2.next.val

m0 = ListNode(0)
m1 = ListNode(1)
m0.next = m1
Solution().deleteNode(m0)
assert m0.val == 1
