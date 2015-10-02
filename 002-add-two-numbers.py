"""
Question:
    You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8

Annotation:
    1.  beats 98.19% submissions
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        nums = [self.val]
        curr = self
        while curr.next:
            nums.append(curr.next.val)
            curr = curr.next
        return str(nums)


class SolutionV1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def convert_listnodes_into_number(listnode):
            reversed_digits = [listnode.val]
            while listnode.next is not None:
                reversed_digits.append(listnode.next.val)
                listnode = listnode.next
            return int("".join(reversed(map(str, reversed_digits))))

        plus_result = convert_listnodes_into_number(l1) + convert_listnodes_into_number(l2)

        def convert_number_into_listnodes(number):
            reversed_digits = map(int, reversed(list(str(number))))
            first_digit = ListNode(reversed_digits[0])

            current_listnode = first_digit
            for digit in reversed_digits[1:]:
                next_listnode = ListNode(digit)
                current_listnode.next = next_listnode
                current_listnode = next_listnode

            return first_digit

        return convert_number_into_listnodes(plus_result)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(None)
        current_listnode = result
        l3 = ListNode(0)  # increase by decade

        while True:
            plus_result = l1.val + l2.val + l3.val
            current_listnode.val = plus_result % 10

            # Prepare next round
            l3_val = 1 if plus_result >= 10 else 0
            l3 = ListNode(l3_val)

            if (l1.next or l2.next) or l3.val:  # must exists at least one.
                current_listnode.next = ListNode(0)
                current_listnode = current_listnode.next
                l1 = l1.next or ListNode(0)
                l2 = l2.next or ListNode(0)
            else:
                break

        return result

l1 = ListNode(0)
ll2 = ListNode(3)
l2 = ListNode(7)
l2.next = ll2
print Solution().addTwoNumbers(l1, l2)
