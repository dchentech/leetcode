"""
Question:
    Merge Two Sorted Lists

    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Performance:
    1. Total Accepted: 82513 Total Submissions: 250918 Difficulty: Easy
    2. Your runtime beats 93.72% of python submissions.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Make everything easy, just take the next at the end.
        dummy_head = ListNode(0)
        curr_node = dummy_head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr_node.next = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                l2 = l2.next
            curr_node = curr_node.next
        curr_node.next = l1 or l2  # append the rest.

        return dummy_head.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n1.next = n3
n3.next = n5
n5.next = n7
n2.next = n4
n4.next = n6
n6.next = n8

result = Solution().mergeTwoLists(n1, n2)
assert result is n1
assert n1.next is n2
assert n2.next is n3
assert n3.next is n4
assert n4.next is n5
assert n5.next is n6
assert n6.next is n7
assert n7.next is n8
