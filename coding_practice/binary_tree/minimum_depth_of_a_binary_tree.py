"""
LC111 - Minimum depth of binary tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # trivial case
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1

        # probably a level-aware breadth first search makes sense for this. Go through in a bfs, keeping
        # track of the level. The first node we find that has no children, we return. O(N) worst case

        queue = [root]
        level = 1
        nodes_in_current_level = 1
        nodes_in_next_level = 0
        current_level_node_counter = 0

        while queue:
            node = queue.pop(0)

            # check for leaf, return immediately if we are at a leaf
            if not node.left and not node.right:
                return level

            if node.left:
                queue.append(node.left)
                nodes_in_next_level += 1
            if node.right:
                queue.append(node.right)
                nodes_in_next_level += 1

            current_level_node_counter += 1
            if current_level_node_counter == nodes_in_current_level:
                nodes_in_current_level = nodes_in_next_level
                level += 1
                current_level_node_counter = 0
                nodes_in_next_level = 0
