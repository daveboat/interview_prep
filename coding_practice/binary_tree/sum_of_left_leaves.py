"""
LC404 - Sum of left leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def left_sum_dfs(self, node, left=False):
        if not node.left and not node.right:  # if we're at a leaf node
            return node.val if left else 0

        # if we're not at a leaf node
        s_left = self.left_sum_dfs(node.left, True) if node.left else 0
        s_right = self.left_sum_dfs(node.right, False) if node.right else 0

        return s_left + s_right

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # question is ambiguous as stated. want all left LEAF nodes, not all left nodes period. We just do a simple
        # dfs, which passes whether we're at a left child or right child node. At each node we check if we're
        # at a leaf node, and act accordingly.

        # trivial case
        if not root:
            return 0

        return self.left_sum_dfs(root)
