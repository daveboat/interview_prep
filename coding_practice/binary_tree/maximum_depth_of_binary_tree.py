"""
LC104 - Maximum depth of binary tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf
node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # must have an O(N) solution because we need to visit every node. Can BFS or DFS. DFS is easier to
        # code.

        def dfs(node, depth):
            if not node:
                return

            if depth > self.max_depth:
                self.max_depth = depth

            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 1)

        return self.max_depth