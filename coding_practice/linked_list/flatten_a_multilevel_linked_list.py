"""
LC430 - Flatten a multilevel doubly linked list

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
which may or may not point to a separate doubly linked list. These child lists may have one or more children of their
own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first
level of the list.

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL

Example 3:

Input: head = []
Output: []
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        child_head, child_tail = self.flatten_helper(head)

        return child_head

    def flatten_helper(self, head):
        # should return the head and tail of a flattened linked list, so that we can connect it to our existing list
        # do this recursively with children

        node = head
        tail = head

        while node:
            if node.child:
                nextnode = node.next
                child_head, child_tail = self.flatten_helper(node.child)

                #################
                # perform surgery: attach the child head to the current node, attack the child tail to the next node,
                # and set the child of the current node to None
                child_tail.next = nextnode
                node.next = child_head
                child_head.prev = node
                node.child = None
                if nextnode:
                    nextnode.prev = child_tail
                #################

                node = nextnode  # jump past the re-attached child linked list
                if nextnode:  # if the original next node exists, set the tail to it
                    tail = nextnode
                else:  # otherwise, set the tail to the tail of the child linked list
                    tail = child_tail
            else:
                if node.next:
                    tail = node.next
                node = node.next

        return head, tail


if __name__ == '__main__':
    S = Solution()

    ll = Node(1, None, None, None)
    ll.child = Node(2, None, None, None)
    ll.child.child = Node(3, None, None, None)

    S.flatten(ll)
