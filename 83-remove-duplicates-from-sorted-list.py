"""
Question:
    Remove Duplicates from Sorted List

    Given a sorted linked list, delete all duplicates such that each element appear only once.

    For example,
    Given 1->1->2, return 1->2.
    Given 1->1->2->3->3, return 1->2->3.


Performance:
    1. Total Accepted: 79069 Total Submissions: 227384 Difficulty: Easy
    2. Your runtime beats 58.09% of python submissions.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        curr_node = head

        while curr_node.next:
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        return head


l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l1.next = l2
l2.next = l3

Solution().deleteDuplicates(l1)
assert l1.next is l3


m1 = ListNode(1)
m2 = ListNode(1)
m3 = ListNode(2)
m4 = ListNode(3)
m5 = ListNode(3)
m1.next = m2
m2.next = m3
m3.next = m4
m4.next = m5

Solution().deleteDuplicates(m1)
assert m1.next is m3
assert m3.next is m4

n1 = ListNode(1)
n2 = ListNode(1)
n1.next = n2
Solution().deleteDuplicates(n1)
assert n1.next is None
