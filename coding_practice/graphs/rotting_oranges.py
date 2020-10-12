"""
LC994 - Rotting oranges

In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.
"""


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # so, when we're given a problem with "time steps" and updates that happen per time step, we usually
        # want to frame the solution as a graph breadth-first search, which processes everything at one level
        # before moving onto the next level.
        #
        # In this case, we need to do an O(row * col) operation to add all rotten oranges cells to the queue,
        # and count all fresh oranges. We then BFS, processing all rotten oranges at each time step before
        # moving onto the next time step, and count the number of time steps we take

        # get rows and cols
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])

        # our queue, and tracking counters for the number of fresh oranges, and number of time steps
        queue = []
        t = 0
        fresh = 0

        # go through the grid, adding the (row, col) of rotten oranges to the queue, and counting the number
        # of fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # now, begin BFS'ing
        while queue and fresh > 0:
            t += 1
            # we want to do process things in a way where we do all rotten oranges at a time step
            for _ in range(len(queue)):
                i, j = queue.pop(0)  # get the next rotten orange at this time step
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # try to visit all four neighbouring cells
                    # continue if out of bounds
                    if i + di >= rows or j + dj >= cols or i + di < 0 or j + dj < 0:
                        continue
                    # continue if grid[i+di][j+dj] is a 0 or 2
                    if grid[i + di][j + dj] == 0 or grid[i + di][j + dj] == 2:
                        continue
                    # else, add to our queue, decrement the fresh counter, and change the cell to a 2,
                    # since we must have hit a 1
                    queue.append((i + di, j + dj))
                    fresh -= 1
                    grid[i + di][j + dj] = 2

        # return t, or -1 if fresh is > 0 after all this
        return t if fresh == 0 else -1
