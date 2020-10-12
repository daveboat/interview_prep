"""
LC1290 - Convert binary number in a linked list to integer
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """

        # math solution: if we were in base 10, and we were getting numbers one at a time from the most significant
        # digit to the least, then for each new number we get, we multiply the existing number by 10 and add the new
        # number, and keep doing this as long as there are numbers still coming in. This is no different in base 2, we
        # just multiply by 2

        counter = 0

        while head:
            counter = 2 * counter + head.val
            head = head.next

        return counter