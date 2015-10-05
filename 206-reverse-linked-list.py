"""
Question:
    Reverse Linked List

    Reverse a singly linked list.

    click to show more hints.

    Hint:
    A linked list can be reversed either iteratively or recursively. Could you implement both?

Performance:
    1. Total Accepted: 48424 Total Submissions: 141893 Difficulty: Easy
    2. Your runtime beats 98.99% of python submissions.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        the most important thing is to figure out holding two vairable, and the reverse steps.
        """
        if head is None:
            return None

        orig_next_node = head.next
        last_reverseing_node = head
        last_reverseing_node.next = None

        while orig_next_node:
            # hold the next point
            _orig_next_node = orig_next_node.next

            # switch
            orig_next_node.next = last_reverseing_node

            # next round
            last_reverseing_node = orig_next_node
            orig_next_node = _orig_next_node

        return last_reverseing_node


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

assert Solution().reverseList(n1) == n5
assert n1.next is None
assert n2.next is n1
assert n3.next is n2
assert n4.next is n3
assert n5.next is n4

m1 = ListNode(1)
assert Solution().reverseList(m1) == m1

assert Solution().reverseList(None) is None
