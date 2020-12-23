"""
LC445 - Add two numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def get_number(self, node):
        ret = 0

        while node:
            ret = 10 * ret + node.val
            node = node.next

        return ret

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # can we just get the first number, get the second number, add them, then make a new ll
        n1 = self.get_number(l1)
        n2 = self.get_number(l2)

        s = n1 + n2
        if s == 0:
            return ListNode(0)

        nn = None
        while s:
            n = ListNode(s % 10, nn)
            s //= 10
            nn = n

        return nn
