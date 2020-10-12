"""
LC1022 - Sum of root to leaf binary numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the
most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary,
which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

Example 1:

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:

    The number of nodes in the tree is between 1 and 1000.
    node.val is 0 or 1.
    The answer will not exceed 2^31 - 1.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node):
        # return this node's value appended in MSB position to the lists returned from all child nodes

        # if we get to a None, return [], so that we can naively recurse into all nodes
        if not node:
            return []
        # leaf nodes are the special case where we need to return the raw value
        elif not node.left and not node.right:
            return [str(node.val)]

        # otherwise, recurse into left and right
        left_list = self.dfs(node.left)
        right_list = self.dfs(node.right)

        # return our value place in front of all child values
        return [str(node.val) + val for val in left_list] + [str(node.val) + val for val in right_list]

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # let's DFS recursively, each call returns a list of bits as strings.
        #
        # Edit: accepted with 99.6%

        return sum([int(val, 2) for val in self.dfs(root)])
