"""
LC463 - Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there
is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square
with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

------------------------------------------------------------------------------------------------------------------------

An alternative way to do this is to check for all horizontal and vertical transitions (0 to 1 or 1 to 0), but there
would be special cases needed for the edges
"""


class Solution(object):
    def __init__(self):
        self.perimeter = 0

    def visit(self, i, j, rows, cols, grid):
        # if we're out of bounds or if we're in a 0, increase perimeter by 1 and then stop
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
            self.perimeter += 1
            return

        # if we're at a previously visited island location, just stop
        if grid[i][j] == -1:
            return

        # we must be at a 1, so set this grid location to visited
        grid[i][j] = -1

        # now, recurse to left, down, up, right
        self.visit(i - 1, j, rows, cols, grid)
        self.visit(i, j - 1, rows, cols, grid)
        self.visit(i + 1, j, rows, cols, grid)
        self.visit(i, j + 1, rows, cols, grid)

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # so, I don't think we can do better than O(N^2) in general, but we can speed things up by not visiting
        # unnecessary tiles via recursively only visiting tiles with ones. We can keep track of where we've visited
        # by altering the grid to a number like -1

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.visit(i, j, rows, cols, grid)
                    break  # we can break after calling visit, because there's guaranteed to be only one island

        return self.perimeter


if __name__ == '__main__':
    S = Solution()

    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

    print(S.islandPerimeter(grid))