"""
LC211 - Add and search word - data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
"""


import string


class Node:
    def __init__(self, char='*', complete=False):
        self.char = char
        self.d = {letter: None for letter in string.ascii_lowercase}
        self.complete = complete


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.add_helper(word, self.root)

    def add_helper(self, word, node):
        # if our word is empty
        if len(word) == 0:
            if node is not None:
                node.complete = True
            return

        if not node.d[word[0]]:  # if the appropriate node doesn't exist, make it
            node.d[word[0]] = Node(char=word[0])
        self.add_helper(word[1:], node.d[word[0]])  # continue with inserting down the line

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        if word[0] == '.':  # wildcard case, search all child nodes, return False if none of them are acceptable
            for child_node in self.root.d.values():
                if self.search_helper(word, child_node):
                    return True
            return False
        else:  # regular case, recurse into appropriate child node
            return self.search_helper(word, self.root.d[word[0]])

    def search_helper(self, word, node):
        """
        Search for words in the trie that we've constructed. If we see a wildcard, we need to search all possible next
        nodes
        """
        # return false if we entered this node but it doesn't exist
        if not node:
            return False

        # termination case, return node.complete
        if len(word) == 1:
            return node.complete
        else:
            # general case, recurse into all child nodes for a wildcard, otherwise recurse into the appropriate child node
            if word[1] == '.':  # wildcard case - recurse into all children, return False if we leave the loop
                for child_node in node.d.values():
                    if self.search_helper(word[1:], child_node):
                        return True
                return False
            else:  # otherwise - word[1] is not a wildcard
                return self.search_helper(word[1:], node.d[word[1]])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)