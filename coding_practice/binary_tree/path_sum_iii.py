"""
LC437 - Path sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0

    def custom_dfs(self, node, sum, prev_sum):
        # termination condition
        if not node:
            return

        # check prev sum for sum - node.val, add to count
        self.count += prev_sum.count(sum - node.val)

        # account for the case where the node itself is equal to sum
        if node.val == sum:
            self.count += 1

        # add current value to prev sum
        curr_sum = [p + node.val for p in prev_sum]
        curr_sum.append(node.val)

        # recurse left and right
        self.custom_dfs(node.left, sum, curr_sum)
        self.custom_dfs(node.right, sum, curr_sum)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # so, let's try a DFS where we keep track of the previous path sums

        self.custom_dfs(root, sum, [])

        return self.count
