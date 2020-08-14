"""
LC203 - Removed linked list elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # trivial case
        if not head:
            return head

        # we have to deal with a chain of vals at the start of the linked list
        while head and head.val == val:
            head = head.next

        # now we deal with nodes in the middle or at the end of the list. We might have several in a row, so we
        # need two while loops: an inner loop to go through chunks of values to be removed, and an outer loop to
        # keep track of which node preceeded the chunk of removed values
        node = head

        while node:
            next_node = node.next
            while next_node and next_node.val == val:
                next_node = next_node.next

            node.next = next_node
            node = node.next

        return head