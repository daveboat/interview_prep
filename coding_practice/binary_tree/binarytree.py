def get_level_helper(node, data, level):
    if node is None:  # this must mean we reached the end of a tree, so we return -1
        return -1

    if node.data == data:  # if we found what we were looking for, return the level, which propagates all the way up
        return level

    downlevel = get_level_helper(node.left, data, level + 1)  # look to the left
    if downlevel != -1:  # this is so that, if we didn't find it in the left subtree, we move onto the right subtree
        return downlevel

    downlevel = get_level_helper(node.right, data, level + 1)  # look to the right
    return downlevel  # this allows returning of -1


def get_level(node, data):
    # get level for an element == data for an unstructured binary tree (i.e. not a binary search tree)
    return get_level_helper(node, data, 0)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def traverse_inorder(self):
        if self.left is not None:
            self.left.traverse_inorder()
        print(self.data)
        if self.right is not None:
            self.right.traverse_inorder()

    def traverse_preorder(self):
        print(self.data)
        if self.left is not None:
            self.left.traverse_preorder()
        if self.right is not None:
            self.right.traverse_preorder()

    def traverse_postorder(self):
        if self.left is not None:
            self.left.traverse_postorder()
        if self.right is not None:
            self.right.traverse_postorder()
        print(self.data)


def traverse_breadth_first(root):
    # traverse a binary tree breadth-first with the help of a queue. This is a left-to-right traversal in each level of
    # the tree. To do a right-to-left traversal, simply reverse the left and right queue appends

    if root is None:
        return

    queue = [root]

    while len(queue) > 0:
        print(queue[0].data)

        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


def reverse(t):
    if t is not None:
        tmp = t.left
        t.left = reverse(t.right)
        t.right = reverse(tmp)

    return t


def isequal(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif (t1 is None and t2 is not None) or (t1 is not None and t2 is None):
        return False
    elif t1.data == t2.data:
        return isequal(t1.left, t2.left) and isequal(t1.right, t2.right)
    else:
        return False


def isCousins(root, x, y):
    """
    Solution for computing if node with value x and node with value y are on the same level of the tree, but with
    different parents
    """
    # do a traversal through the tree, keeping track of level of x and y (global_levels)
    # and parent data of x and y
    global_levels = [-1, -1]
    parents = [-1, -1]

    def get_level_global_helper(node, data, level, parent_data):
        if node is None:
            return

        if node.data == data[0]:  # we've found x, so update its information (level and parent data)
            global_levels[0] = level
            parents[0] = parent_data
        elif node.data == data[1]:  # we've found y, so update its information (level and parent data
            global_levels[1] = level
            parents[1] = parent_data

        if -1 not in global_levels:  # if we've already found both x and y, no need to continue
            return
        else:  # otherwise continue
            get_level_global_helper(node.left, data, level + 1, node.data)
            get_level_global_helper(node.right, data, level + 1, node.data)

    get_level_global_helper(root, [x, y], 0, -1)

    if global_levels[0] == global_levels[1] and parents[0] != parents[1]:
        return True
    else:
        return False


class Solution:
    """
    Solution for kth smallest value in a binary search tree
    """
    def kthSmallest(self, root, k):
        self.k = k
        self.ret = None
        self.in_order(root)
        return self.ret

    def in_order(self, root):
        if not root:
            return

        if root.left:
            self.in_order(root.left)

        self.k -= 1
        if self.k == 0:
            self.ret = root.data

        if root.right:
            self.in_order(root.right)


class Solution2(object):
    """
    Solution for finding the longest chain of nodes in a binary tree

    Idea is to recursively find the max length in the left side of the tree, and the right side of the tree. Each time we
    compute both left and right side lengths, update the max length if the total length, including the root node, is
    arger than the stored max length
    """
    def __init__(self):
        self.max_len = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        current_len = self.bt_length(root.left) + self.bt_length(root.right)
        if current_len > self.max_len:
            self.max_len = current_len

        return self.max_len

    def bt_length(self, node):
        # termination condition
        if node == None:
            return 0

        left_len = self.bt_length(node.left)
        right_len = self.bt_length(node.right)

        current_len = left_len + right_len
        if current_len > self.max_len:
            self.max_len = current_len

        # return the greater of the left and right lengths, plus 1
        return max(left_len, right_len) + 1


if __name__ == '__main__':
    # bt = Node(1)
    # bt.left = Node(2)
    # bt.right = Node(3)
    # bt.left.right = Node(4)
    # bt.right.right = Node(5)


    # bt.traverse_inorder()
    # # print('')
    # # bt.traverse_preorder()
    # # print('')
    # # bt.traverse_postorder()
    # rt = reverse(copy.copy(bt))
    # print(isequal(bt, rt))
    # rt.traverse_inorder()


    st = Node(5)
    st.insert(2)
    st.insert(8)
    st.insert(4)
    st.insert(6)
    st.insert(3)
    st.insert(9)
    traverse_breadth_first(st)

    # s = Solution()
    # s.kthSmallest(st, 3)

    # st.traverse_inorder()

    #

    # print(isequal(bt, st))
