"""
Question:
    Remove Nth Node From End of List My Submissions Question Solution

    Given a linked list, remove the nth node from the end of list and return its head.

    For example,

       Given linked list: 1->2->3->4->5, and n = 2.

       After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:
    Given n will always be valid.
    Try to do this in one pass.

Performance:
    1. Total Accepted: 74515 Total Submissions: 274695 Difficulty: Easy
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        idx_to_node = dict()
        curr_node = head
        curr_idx = 0

        # 1. Build reversed indexes of nodes
        while curr_node:
            idx_to_node[curr_idx] = curr_node
            curr_node = curr_node.next
            curr_idx += 1

        # 2. Remote the nth node
        total_len = len(idx_to_node)
        positive_idx_should_removed = total_len - n  # 5 - 2 = 3
        positive_idx_after_should_removed = positive_idx_should_removed + 1

        if positive_idx_should_removed == 0:
            head = head.next
        elif positive_idx_after_should_removed == total_len:
            idx_to_node[positive_idx_should_removed - 1].next = None
        elif 0 < positive_idx_should_removed < total_len:
            idx_to_node[positive_idx_should_removed - 1].next = idx_to_node[positive_idx_should_removed + 1]

        return head

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

result = Solution().removeNthFromEnd(n1, 2)
assert result == n1, result
assert n3.next == n5

m1 = ListNode(1)
result = Solution().removeNthFromEnd(m1, 1)
assert result is None, result

l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
result = Solution().removeNthFromEnd(l1, 1)
assert result is l1, result
