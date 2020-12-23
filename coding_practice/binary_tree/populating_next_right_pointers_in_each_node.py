"""
LC116 - Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The
binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to
its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # trivial case
        if not root:
            return None

        # since the binary tree is perfect, we can do a breadth-first search with a known number of
        # nodes at each level (i.e. 2^i where i is the level, starting from 0). This necessarily
        # O(N) time (need to visit every node) and O(N) space (need to store on average N/2 nodes in
        # the queue)

        curr_level = 0
        queue = [root]
        level_node_counter = 0

        while queue:
            # pop node and add children
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            # increment counter and do assignment of node.next
            level_node_counter += 1
            if level_node_counter == 2 ** curr_level:  # end of level
                node.next = None
                curr_level += 1
                level_node_counter = 0
            else:  # otherwise
                node.next = queue[0]

        return root