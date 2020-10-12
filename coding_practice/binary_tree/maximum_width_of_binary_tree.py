"""
LC662 - Maximum width of binary tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum
width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the
level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

Note: Answer will in the range of 32-bit signed integer.

------------------------------------------------------------------------------------------------------------------------

The code I used was a level-aware breadth-first search, noting that if the root has width index 1, then all child
width indices are 2k - 1 and 2k for a parent width index of k. At each level, we compute the width by keeping track of
the first and last nodes we see.

A depth-first approach is also possible, which keeps track of the level and width-index of the nodes being recursed
into, and keeps a running list of widths for each level, computing the max width after the DFS finishes

I think the BFS solution makes more sense to me, though you need slightly more space: a list of O(N) instead of
O(logN), since with BFS you need a queue of nodes, and with DFS you need a list of widths per level.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # our old friend, breadth-first search.
        # we can do our level-aware breadth-first search, but with additional bookkeeping for lvel width.
        # the level width can be calculated by keeping track of the first and last node added at the next level.
        # we keep track of the width value of the parent node, k - the left and right child nodes have width
        # values 2k -1 and 2k respectively. when we encounter a node, the left index gets set to that width
        # value and so does the right index. When we encounter another node, the right index gets set to the
        # new width value, and so on. That way, we end up keeping track of the width of each level. We simply
        # return the maximum width so far.

        # this is O(N) in time, since we visit each node, and O(N) in space, since we visit each node

        # trivial case
        if not root: return 0

        max_width = 1  # smallest max width is 1 if we have a root node
        left_index = -1
        right_index = -1

        # level-aware BFS machinery
        queue = [[root, 1]]  # queue contains node, and node width index
        current_level_counter = 0
        current_level_nodes = 1
        next_level_nodes = 0

        while queue:
            node, width_index = queue.pop(0)

            current_level_counter += 1

            # do width index bookkeeping stuff
            if left_index < 0:
                left_index = width_index
            right_index = width_index

            if node.left:
                queue.append([node.left, 2 * width_index - 1])  # left child node has width index 2k-1
                next_level_nodes += 1
            if node.right:
                queue.append([node.right, 2 * width_index])  # right child node has width index 2k
                next_level_nodes += 1

            if current_level_counter >= current_level_nodes:
                current_level_nodes = next_level_nodes
                next_level_nodes = 0
                current_level_counter = 0

                # do width index bookkeeping stuff
                current_level_width = right_index - left_index + 1
                if current_level_width > max_width:
                    max_width = current_level_width
                right_index = -1
                left_index = -1

        return max_width
