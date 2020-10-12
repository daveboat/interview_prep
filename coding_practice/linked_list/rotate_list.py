"""
LC61 - Rotate list

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        # so, we need the length of the list first, so let's do one pass (O(N)) to do that
        l = 0

        node = head
        while node:
            l += 1
            node = node.next

        # now l contains the length of the list. the number of steps to the right we need to perform
        # is k mod l
        r = k % l

        # trivial cases
        if r == 0 or l == 0:
            return head

        # so the linked list needs the element at position l - r to be at the head, the old
        # head node to be the child node of the old last element, and the element at position
        # l - r - 1 to
        # or
        # 0 -> 1 -> 2 -> 3 -> 4 ... -> l-r-1 -> l-r -> l-r+1 -> l-r+2 -> ... -> l-1 -> None
        #
        # becomes
        #
        # l-r -> l-r+1 -> l-r+2 -> ... -> l-1 -> 0 -> 1 -> 2 -> 3 -> 4 -> ... -> l-r-1 -> None
        #
        # let's do that surgery. we need pointers to head (old head), l-r (new head), l-r-1
        # (new tail), and the last node (old tail)
        i = 0
        old_head = head
        new_head = None
        new_tail = None
        old_tail = None

        node = head
        if l - r - 1 == 0:
            new_tail = node
        while node:
            i += 1
            node = node.next
            if i == l - r - 1:
                new_tail = node
            if i == l - r:
                new_head = node
            if i == l - 1:
                old_tail = node

        new_tail.next = None
        old_tail.next = old_head

        return new_head