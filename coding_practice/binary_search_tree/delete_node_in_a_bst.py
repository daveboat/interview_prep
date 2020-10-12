"""
LC450 - Delete node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def min_node(self, node):
        # returns the minimum descendent for a node in a BST
        while node.left:
            node = node.left

        return node

    def max_node(self, node):
        # returns the maximum descendent for a node in a BST
        while node.right:
            node = node.right

        return node

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # This is a little more complicated than I initially thought. Since this is a binary search tree instead of
        # a binary tree, there's more to it than just finding the node and performing surgery. The general procedure
        # is to find the successor of the node to be deleted, which is the minimum value in the right subtree of the
        # node (this could be none or just the very next right node), or the predecessor node, which is the maximum
        # value in the left subtree, copy the value of the successor/predecessor into the node to be deleted, delete
        # the successor/predecessor (we can do this by calling deleteNode again). This results in a valid BST with
        # the node deleted.
        #
        # There are also easier cases if the node to be deleted has one child or no children
        #
        # also, searching for the node doesn't need a full O(N) search, since we know the tree is a binary search tree

        # key not in tree
        if root is None:
            return root

        # if the key is less than us, recurse left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # if the key is greater than us, recurse right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # key found
        else:
            print(root.val)
            # case 1: node to be deleted has no children
            if not root.left and not root.right:
                root = None

            # case 2: node to be deleted has two children
            elif root.left and root.right:
                # find its predecessor node (could also use the successor node here)
                predecessor = self.max_node(root.left)

                # copy the value of predecessor to current node
                root.val = predecessor.val

                # recursively delete the predecessor. By definition, the predecessor will have at most one child,
                # since it must be the maximum node in the left subtree
                root.left = self.deleteNode(root.left, predecessor.val)

            # case 3: node to be deleted has only one child
            else:
                child = root.left if root.left else root.right
                root = child

        return root