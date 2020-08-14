"""
LC2 - Add two numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        remainder = 0
        out_ll = ListNode(val=0)
        node = out_ll
        while l1 is not None or l2 is not None or remainder > 0:

            if l1 is not None:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0
            if l2 is not None:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0

            s = (n1 + n2 + remainder) % 10
            remainder = (n1 + n2 + remainder) // 10

            node.val = s
            if l1 is not None or l2 is not None or remainder > 0:
                node.next = ListNode()
                node = node.next

        return out_ll