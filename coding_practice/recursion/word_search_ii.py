"""
LC212 - Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:

    All inputs are consist of lowercase letters a-z.
    The values of words are distinct.
"""


class TrieNode:
    def __init__(self, char='*', complete=False):
        self.char = char
        self.children = dict()
        self.complete = complete
        self.already_added = False


def insert_helper(node, word):
    # if our word is empty and we're not at the root node
    if len(word) == 0:
        if node is not None and node.char != '*':
            node.complete = True
        return

    if word[0] not in node.children:  # if the appropriate node doesn't exist, make it
        node.children[word[0]] = TrieNode(char=word[0])
    insert_helper(node.children[word[0]], word[1:])  # continue with inserting down the line


def build_trie(root, words):
    for word in words:
        insert_helper(root, word)


def neighbours(i, j, rows, cols):
    return_lst = []
    if i != 0:
        return_lst.append((i - 1, j))
    if j != 0:
        return_lst.append((i, j - 1))
    if i != rows - 1:
        return_lst.append((i + 1, j))
    if j != cols - 1:
        return_lst.append((i, j + 1))

    return return_lst


class Solution(object):
    def word_search(self, board, rows, cols, visited, i, j, node, current_word, found_words):
        # this is the meat of the algorithm. At each board position i,j and trie node, recurse to all board neighbours
        # which are in the children of the current trie node, and add that letter to current_word
        # if we find a node that is complete, add the current word to found_words

        # visit this node
        current_word += node.char
        if node.complete and not node.already_added:
            found_words.append(current_word)
            node.already_added = True
        visited[i][j] = True

        # recurse to surrounding nodes which are in this node's children and aren't visited
        for next_i, next_j in neighbours(i, j, rows, cols):
            if board[next_i][next_j] in node.children and not visited[next_i][next_j]:
                self.word_search(board, rows, cols, visited, next_i, next_j, node.children[board[next_i][next_j]],
                                 current_word, found_words)

        # when i recurse out of a node, I need to set visited to False so that the next recursion is allowed to visit
        visited[i][j] = False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # so we build a trie out of the words
        root = TrieNode()
        build_trie(root, words)

        found_words = []

        rows = len(board)
        cols = len(board[0])

        # make a visited array
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # then, we loop through each i,j in board
        for i in range(rows):
            for j in range(cols):
                # do the recursive search at this i,j if the character at this location is in the first level
                # of the tree
                if board[i][j] in root.children:
                    self.word_search(board, rows, cols, visited, i, j, root.children[board[i][j]], "", found_words)

        return list(set(found_words))  # make sure we have no duplicates


if __name__ == '__main__':
    S = Solution()
    board = [["a","a","a","a"],
             ["a","a","a","a"],
             ["a","a","a","a"],
             ["a","a","a","a"],
             ["b","c","d","e"],
             ["f","g","h","i"],
             ["j","k","l","m"],
             ["n","o","p","q"],
             ["r","s","t","u"],
             ["v","w","x","y"],
             ["z","z","z","z"]]
    words = ["aaaaaaaaaaaaaabc"]
    print(S.findWords(board, words))

    # [["a","a","a","a"],
    # ["a","a","a","a"],
    # ["a","a","a","a"],
    # ["a","a","a","a"],
    # ["b","c","d","e"],
    # ["f","g","h","i"],
    # ["j","k","l","m"],
    # ["n","o","p","q"],
    # ["r","s","t","u"],
    # ["v","w","x","y"],
    # ["z","z","z","z"]]
    #["aaaaaaaaaaaaaaaa",
    # "aaaaaaaaaaaaaaab",
    # "aaaaaaaaaaaaaaac",
    # "aaaaaaaaaaaaaaad",
    # "aaaaaaaaaaaaaaae",
    # "aaaaaaaaaaaaaabc",
    # "aaaaaaaaaaaaaabf",
    # "aaaaaaaaaaaaaacb",
    # "aaaaaaaaaaaaaacd",
    # "aaaaaaaaaaaaaacg",
    # "aaaaaaaaaaaaaadc",
    # "aaaaaaaaaaaaaade",
    # "aaaaaaaaaaaaaadh",
    # "aaaaaaaaaaaaaaed",
    # "aaaaaaaaaaaaaaei"]