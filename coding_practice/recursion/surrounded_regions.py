"""
LC130 - Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to
'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells
are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution(object):
    def recursive_flip(self, board, row, col, M, N):
        """
        Changes an O here to a P and recurse to all four adjacent tiles. Otherwise stop.
        M and N are board rows and cols, respectively
        """

        if 0 <= row < M and 0 <= col < N and board[row][col] == 'O':
            board[row][col] = 'P'
            self.recursive_flip(board, row + 1, col, M, N)
            self.recursive_flip(board, row - 1, col, M, N)
            self.recursive_flip(board, row, col + 1, M, N)
            self.recursive_flip(board, row, col - 1, M, N)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # initial attempt: seek O's along the four border regions, not counting corners (since corner O's don't matter)
        # for each O along the border region, write a recursive function to go through and change all connected O's to
        # some placeholder, like P. Afterwards, go through the board and flip P's to O's and O's to X's

        if not board or not board[0]:
            return

        M = len(board)
        N = len(board[0])

        # go through all four boundaries for O's, and run our recursive flip on them
        # top and bottom:
        for i in range(N):
            if board[0][i] == 'O':
                self.recursive_flip(board, 0, i, M, N)
            if board[M - 1][i] == 'O':
                self.recursive_flip(board, M - 1, i, M, N)
        # left and right:
        for i in range(M):
            if board[i][0] == 'O':
                self.recursive_flip(board, i, 0, M, N)
            if board[i][N - 1] == 'O':
                self.recursive_flip(board, i, N - 1, M, N)

        # Now, go through and flip P's to O's and O's to X's
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'P':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'