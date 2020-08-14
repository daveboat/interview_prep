"""
LC200 - Number of islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

------------------------------------------------------------------------------------------------------------------------

Recursive solution for finding the number of contiguous islands in a list of lists of ones and zeroes.

First solution I tried, which was to increment the number of islands by 1 whenever the elements at i,j is 1 and the
elements at i-1,j and i,j-1 are both 0 didn't work because of situations where islands wrap around, like

000010000
000010000
000010000
011111100
000000000
"""


def kill(grid, i, j, rows, cols):
    if grid[i][j] == '1':
        grid[i][j] = '0'
        if i > 0:
            kill(grid, i - 1, j, rows, cols)
        if i < rows - 1:
            kill(grid, i + 1, j, rows, cols)
        if j > 0:
            kill(grid, i, j - 1, rows, cols)
        if j < cols - 1:
            kill(grid, i, j + 1, rows, cols)


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    kill(grid, i, j, rows, cols)

        return islands

s = [["1","1","1"],
     ["0","1","0"],
     ["1","1","1"]]

S = Solution()

print(S.numIslands(s))