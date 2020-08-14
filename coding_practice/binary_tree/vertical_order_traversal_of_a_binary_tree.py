"""
LC987 - Vertical Order Traversal of a Binary Tree

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and
(X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report
the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Example 1:

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:

Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.

Note:

    The tree will have between 1 and 1000 nodes.
    Each node's value will be between 0 and 1000.
"""


import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # The solution to this problem is pretty straightforward. We assign each node a coordinate value. The root
        # is (0, 0), the left child of the root is (-1, 1), the right child of the root is (1, 1), etc. In other words,
        # each level increases y by 1, and x spans out from 0 in both directions.
        #
        # We make a custom depth-first search function which tracks the coordinate of each node, adding them to
        # a dictionary keyed by x, value with y and the value of the node. This dictionary has the form
        # {x: [[y, node.val], [y, node.val], ...], ...}. When outputting, we simply have to make sure the output list
        # is formatted so that the inner lists are in order by y, and the outer lists are in order by x

        # output list
        ret = []

        xs = collections.defaultdict(list)

        def dfs(node, x=0, y=0):
            if not node:
                return None
            xs[x].append([y, node.val])
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)

        dfs(root)

        items = list(xs.items())
        items.sort()  # first, we sort by x so that the output list is in the correct order
        for k, v in items:  # then, for each list
            v.sort()
            item = [x[1] for x in v]
            ret.append(item)
        return ret