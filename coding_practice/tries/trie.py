"""
LC208 - Implement Trie

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
"""


import string


class Node:
    def __init__(self, char='*', complete=False):
        self.char = char
        self.d = {letter: None for letter in string.ascii_lowercase}
        self.complete = complete


def insert_helper(node: Node, word: str):
    # if our word is empty
    if len(word) == 0:
        if node is not None:
            node.complete = True
        return

    if node.d[word[0]] is None:  # if the appropriate node doesn't exist, make it
        node.d[word[0]] = Node(char=word[0])
    insert_helper(node.d[word[0]], word[1:])  # continue with inserting down the line


def search_helper(node: Node, word: str, starts_only: bool = False):
    if node is not None and node.char == '*':  # if we're at the head
        return search_helper(node.d[word[0]], word, starts_only)

    if len(word) == 1:  # termination case
        if node is None:
            return False
        if node.char == word:
            if starts_only:
                return True
            else:
                return node.complete
    else:
        if node is None:
            return False
        if node.char == word[0]:
            return search_helper(node.d[word[1]], word[1:], starts_only)
        else:
            return False


class Trie(object):
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        insert_helper(self.head, word)

    def search(self, word):
        return search_helper(self.head, word)

    def startsWith(self, word):
        return search_helper(self.head, word, starts_only=True)


if __name__ == '__main__':
    t = Trie()
    t.insert('apple')
    print(t.search('apple'))
    print(t.search('app'))
    print(t.startsWith('app'))
