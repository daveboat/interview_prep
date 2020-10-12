"""
Facebook interview question: average value of each level of a tree

Strategy is to use depth first search. We start with a node count of 1, since that's the number of nodes in the first
level. Whenever we add a node's children, we keep track of how many nodes the nodes in the current level adds. In this
way, we keep track of how many nodes are on each level.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def level_average(head):
    ret = []

    queue = [head]

    level_counter = 0  # counter for how many nodes we've popped on the current level
    last_level_counter = 1
    next_level_counter = 0  # counter for how many nodes are in the next level
    sum_counter = 0

    while queue:
        cur_node = queue.pop(0)

        for child in cur_node.children:
            queue.append(child)
            next_level_counter += 1

        level_counter += 1

        sum_counter += cur_node.val

        if level_counter == last_level_counter:
            ret.append(sum_counter/level_counter)

            # reset counters
            level_counter = 0
            last_level_counter = next_level_counter
            next_level_counter = 0
            sum_counter = 0

    return ret


if __name__ == '__main__':
    head = Node(1)

    head.children = [Node(2), Node(3), Node(4)]

    head.children[0].children = [Node(5), Node(6), Node(7), Node(8)]
    head.children[1].children = [Node(9), Node(10)]
    head.children[2].children = [Node(11), Node(12), Node(13)]

    print(level_average(head))