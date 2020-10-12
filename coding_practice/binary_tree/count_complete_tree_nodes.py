"""
LC222 - Count complete tree nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # first attempt: bfs (O(N))
        #         if not root:
        #             return 0

        #         # just bfs for the solution?

        #         queue = [root]

        #         count = 0

        #         while queue:
        #             node = queue.pop(0)

        #             count += 1

        #             if node.left:
        #                 queue.append(node.left)
        #             if node.right:
        #                 queue.append(node.right)

        #         return count

        # second attempt: DFS, taking advantage of completeness of tree. Since we know that the tree must be filled such
        # that all levels are full except for the last level, we check the tree for completeness, and if it's complete,
        # just return 2^levels - 1. If it's incomplete, then recurse to its left and right subtrees. In this way,
        # we save a lot of work, since at least one of the left and right trees in the beginning will be complete, and then
        # other subtrees might also be complete.
        #
        # The strategy is thus:
        # 1. for each node, check "left depth" and "right depth" by going down the left subtree until reaching the end
        # and going down the right subtree until reaching the end.
        # 2a. If the left depth and the right depth are equal, the tree is perfect (fully complete), and we can just return
        # 2 ^ (left or right depth) - 1
        # 2b. If the left depth is greater than the right depth, that means the tree at the node is not complete, and so we
        # recurse by returning to 1. for both the left and right subtrees
        #
        # The time complexity of this is O(logN * logN) since at each node we need to do O(logN) operations to compute
        # the depths, and we need to go through O(logN) total nodes

        left_depth = 0
        right_depth = 0

        # compute left and right depths
        left = root
        right = root
        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1

        # if the left and right depths are equal, return the number of nodes via math
        if left_depth == right_depth:
            return 2 ** left_depth - 1
        else:  # the only other possibility is left_depth > right_depth, so we recurse
            return self.countNodes(root.left) + self.countNodes(root.right) + 1