"""
LC382 - Linked List Random Node

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability
of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without
using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
"""

import random


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # we use a strategy called Reservoir sampling, which is a family of algorithms for randomly sampling
    # with size of the pool unknown. For a single random sample, we iterate through the linked list,
    # and each time we go to a new node, we decide whether to replace the current return value with the
    # node's value. Our choice has decreasing probability as we go through the list, specifically we
    # choose with a probability 1/k, where k is the number of nodes we have visited. This way, the first
    # node's value is assigned with 100% probability, the second node's value with 50% probability, then
    # 33% probability, and so forth. This guarantees each node's value has equal probability of being
    # the final chosen value.
    #
    # this is O(1) space, since we don't need to store the contents of the linked list anywhere.
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1.0 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()