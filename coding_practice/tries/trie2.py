# a better, less naive implementation of a trie

class Node:
    def __init__(self, complete=False):
        self.d = dict()
        self.complete = complete


def insert(node, word):
    # if our word is empty
    if len(word) == 0:
        node.complete = True
        return

    if word[0] not in node.d:  # if the appropriate node doesn't exist, make it
        node.d[word[0]] = Node()
    insert(node.d[word[0]], word[1:])  # continue with inserting down the line


if __name__ == '__main__':
    t = Node()
    insert('apple')
