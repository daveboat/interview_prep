"""
LC1305 - All elements in two binary search trees

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:

    Each tree has at most 5000 nodes.
    Each node's value is between [-10^5, 10^5].
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self, root):
        # getting values is easier with a stack instead of recursion
        node = root
        stack = []
        ret = []

        while True:
            if node:
                stack.append(node)
                node = node.left  # go left
            elif (stack):
                node = stack.pop()
                ret.append(node.val)  # visit
                node = node.right  # go right
            else:
                break

        return ret

    def merge(self, list1, list2):
        # merge two lists which are already sorted in ascending order

        ret = []
        idx1 = 0
        idx2 = 0

        while idx1 < len(list1) or idx2 < len(list2):
            if idx1 >= len(list1):
                ret.append(list2[idx2])
                idx2 += 1
            elif idx2 >= len(list2):
                ret.append(list1[idx1])
                idx1 += 1
            else:
                if list1[idx1] <= list2[idx2]:
                    ret.append(list1[idx1])
                    idx1 += 1
                else:
                    ret.append(list2[idx2])
                    idx2 += 1

        return ret

    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        # let's do an in-order traversal of both trees to get the elements in ascending order, then merge the arrays

        return self.merge(self.inOrder(root1), self.inOrder(root2))
