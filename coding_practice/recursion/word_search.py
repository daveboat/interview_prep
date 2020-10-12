"""
LC73 - Word search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3
"""


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
    def word_search(self, i, j, word, board, visited, rows, cols):
        # if the word is complete, return True regardless of visited state or board character
        if len(word) == 0:
            return True

        # if this cell has been visited, or it hasn't been visited but the letter doesn't match, return False
        if visited[i][j] or board[i][j] != word[0]:
            return False

        # if we get here, we must not be visited here and the board letter must match the first letter of the word
        visited[i][j] = True

        # send recursive searches off in the valid directions
        for k, l in neighbours(i, j, rows, cols):
            if self.word_search(k, l, word[1:], board, visited, rows, cols):
                return True

        # set visited flag for this cell to false after we recurse out of it, so future recursions
        # can visit it
        visited[i][j] = False

        # if we leave the recursion without returning True, return False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # our strategy here is to go through the board, shooting off recursive functions which look through all possible
        # directions, returning False if there's nowhere left to go or if the letter we run into is not the next letter
        # in the word, and returning true if we get to the end of our word. We keep an array of bools to keep track of
        # our visited state. We flip visited to true when we recurse into a cell, and flip ot to false when we recurse
        # out of the cell, so that future recursions are allowed to visit it

        rows = len(board)
        cols = len(board[0])

        # trivial case, but the way we wrote our recursive function, it can't handle this, so we handle it here
        if rows == cols == 1 and len(word) == 1:
            return board[0][0] == word[0]

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if self.word_search(i, j, word, board, visited, rows, cols):
                    return True

        return False
