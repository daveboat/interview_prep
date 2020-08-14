"""
LC237 - Delete node in a linked list

237. Delete Node in a Linked List
Easy

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your
function.

Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your
function.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # so, instead of giving us the head node and a value, they're giving us the actual node to be deleted
        # so we just need to make the current node equal to the next node's value, and set the current node's next
        # to the current node's next's next

        # edge case: if node.next is None, we need to become None
        if node.next is None:
            node = None
        else:
            node.val = node.next.val
            node.next = node.next.next