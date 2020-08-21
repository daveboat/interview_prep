"""
LC143 - Reorder list

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # trivial cases
        if not head or not head.next or not head.next.next:
            return head

        # put nodes in a list, then perform reconnections?
        # go through list, put nodes in a list (O(N) time, O(N) space)
        node = head
        node_list = []
        while node:
            node_list.append(node)
            node = node.next

        # now traverse in the zigzag order we need, and attach the last visited node to None (O(N) time)
        N = len(node_list)
        even = N % 2 == 0
        for i in range(N // 2 if even else N // 2 + 1):
            node_list[i].next = node_list[N - 1 - i]
            node_list[N - 1 - i].next = node_list[i + 1]
        node_list[N - 1 - i].next = None
