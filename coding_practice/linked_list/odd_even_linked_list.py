"""
LC328 - Odd even linked list

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #         # attempt 1: slow fast pointers -- doesn't work because even index nodes don't end up in the correct order
        #         slow = head
        #         fast = head

        #         # swap odd and even elements into place
        #         while fast.next and fast.next.next:
        #             slow = slow.next
        #             fast = fast.next.next

        #             slow.val, fast.val = fast.val, slow.val

        #         slow = slow.next

        # attempt 2: odd/even linked list approach. split the linked list into two linked lists, join tail of one to head
        # of the other

        # trivial cases (ll only has one or two nodes)
        if not head or not head.next or not head.next.next:
            return head

        # odd-even linked list approach
        head_odd = head
        head_even = head.next

        odd = head_odd
        even = head_even

        while odd and even and odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = head_even
        return head_odd