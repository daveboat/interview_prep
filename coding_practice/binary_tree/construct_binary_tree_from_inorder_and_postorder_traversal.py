"""
LC106 - Construct binary tree from inorder and postorder traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # For this problem, we note that in the in-order traversal, the root node of a tree divides the array
        # into left subtree elements and right subtree elements. We also note that the post-order traversal
        # has the root node of a tree at the rightmost position; going from right to left, the very next element
        # is the root of the right subtree, if it exists, and after all elements in the right subtree are counted,
        # the root of the left subtree appears.
        #
        # So, we keep track of a few indices. We keep a left and right index in our inorder array, which keeps
        # track of where we are in the tree. We also keep an index in the postorder array which tells us which
        # root node we are on. We need to use list.index() to find the corresponding location of the root node
        # from the postorder array in the inorder array, at which point we can shift our left and right inorder
        # indices accordingly for the left and right subtrees

        return self.build_tree_helper(inorder, postorder, 0, len(inorder) - 1, len(postorder) - 1)

    def build_tree_helper(self, inorder, postorder, left, right, index):
        # left and right are indices in the inorder array
        # index is the root index in the postorder array

        # termination condition, when we have no subtree at all. This also prevents indexing errors
        if right < left: return None

        root = TreeNode(val=postorder[index])  # create the subtree root node

        inorder_root_index = inorder.index(postorder[index])  # find the index of the current root in the inorder array

        # construct right subtree. index decreases by 1 in the postorder array, left goes to inorder_root_index +1
        root.right = self.build_tree_helper(inorder, postorder, inorder_root_index + 1, right, index - 1)
        # construct left subtree. index decreases by number of node in right subtree + 1, which is
        # (right - inorder_root_index) + 1, right goes to inorder_root_index - 1
        root.left = self.build_tree_helper(inorder, postorder, left, inorder_root_index - 1,
                                           index - (right - inorder_root_index) - 1)

        return root
