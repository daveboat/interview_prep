"""
LC64 - Minimum path sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum
of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

------------------------------------------------------------------------------------------------------------------------

For this problem, we use a DP table. Since we're only allowed to move left and down, the first row and first colums are
just cumulative sums across and down, respectively. The other cells are the minimum of the cell above and left of it in
the dp table, plus itself.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # get grid shape, M = rows, N = cols
        M = len(grid)
        N = len(grid[0])

        # solve with a DP table
        dp = [[0] * N for _ in range(M)]

        # do the first row first
        dp[0][0] = grid[0][0]
        for j in range(1, N):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # do the rest of the grid
        for i in range(1, M):
            for j in range(0, N):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[M - 1][N - 1]