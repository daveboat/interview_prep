"""
LC107 - Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by
level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        # strategy is to use a breadth-first search, counting elements added in the next level

        return_list = []

        queue = [root]

        previous_level_count = 1
        current_level_counter = 0
        next_level_counter = 0

        current_level = 0

        while queue:
            node = queue.pop(0)

            if current_level_counter == 0:
                return_list.append([])

            current_level_counter += 1

            return_list[current_level].append(node.val)

            if node.left:
                queue.append(node.left)
                next_level_counter += 1
            if node.right:
                queue.append(node.right)
                next_level_counter += 1

            if current_level_counter >= previous_level_count:
                previous_level_count = next_level_counter
                next_level_counter = 0
                current_level_counter = 0

                current_level += 1

        return return_list[::-1]