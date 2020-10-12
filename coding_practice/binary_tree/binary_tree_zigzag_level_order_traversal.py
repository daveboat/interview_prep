"""
LC103 - Binary tree zigzag level order traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # okay, level-aware breadth-first search, again!
        # only difference here is that we append a list of nodes to a master list, and reverse the order of the nodes
        # every other level

        ret = []
        current_level_nodes = []

        if not root:
            return ret

        queue = [root]
        level = 1
        current_level_counter = 0
        next_level_counter = 0
        number_of_nodes_in_current_level = 1

        while queue:
            node = queue.pop(0)
            current_level_nodes.append(node.val)

            current_level_counter += 1

            if node.left:
                queue.append(node.left)
                next_level_counter += 1
            if node.right:
                queue.append(node.right)
                next_level_counter += 1

            if current_level_counter >= number_of_nodes_in_current_level:
                current_level_counter = 0
                number_of_nodes_in_current_level = next_level_counter
                next_level_counter = 0
                ret.append(current_level_nodes[::-1] if level % 2 == 0 else current_level_nodes)
                current_level_nodes = []
                level += 1

        return ret
