"""
LC513 - Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse_breadth_first(root):
    if root is None:
        return

    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)

        if node.right is not None:
            queue.append(node.right)

        if node.left is not None:
            queue.append(node.left)

    return node.val

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # the idea is to do a right-to-left breadth-first search. Then the last node popped off must be the bottom left
        # node

        return traverse_breadth_first(root)