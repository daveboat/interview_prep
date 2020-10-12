"""
LC100 - Same tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # check for equality for the root
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False

        # let's do a dfs, with a stack! Maybe though this problem is easier with recursion instead of a stack...

        p_stack = [p]
        q_stack = [q]

        while p_stack and q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()

            # check for equality to the left and right of this node before adding them to the stack
            if p_node.right and q_node.right and p_node.right.val == q_node.right.val:  # equality, and add nodes
                p_stack.append(p_node.right)
                q_stack.append(q_node.right)
            elif not p_node.right and not q_node.right:  # equality, but don't add nodes
                pass
            else:  # inequality, return false
                return False
            if p_node.left and q_node.left and p_node.left.val == q_node.left.val:  # equality, and add nodes
                p_stack.append(p_node.left)
                q_stack.append(q_node.left)
            elif not p_node.left and not q_node.left:  # equality, but don't add nodes
                pass
            else:  # inequality, return false
                return False

        # if we've left the loop, then our guys are equal
        return True


# or we could do it recursively, which is probably easier
def same(t1, t2):
    if not t1 and not t2:
        return True
    elif (not t1 and t2) or (t1 and not t2):
        return False
    elif t1.val == t2.val:
        return same(t1.left, t2.left) and same(t1.right, t2.right)
    else:  # e.g. if t1 and t2 and t1.val != t2.val
        return False