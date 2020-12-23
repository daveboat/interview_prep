"""
LC1290 - Convert binary number in a linked list to integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or
1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:

Input: head = [0]
Output: 0

Example 3:

Input: head = [1]
Output: 1

Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:

Input: head = [0,0]
Output: 0

Constraints:

    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.
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