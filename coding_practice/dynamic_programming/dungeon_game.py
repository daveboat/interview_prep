"""
LC174 - Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and
must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or
below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other
rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each
step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path
RIGHT-> RIGHT -> DOWN -> DOWN.
-2 (K) 	-3 	3
-5 	-10 	1
10 	30 	-5 (P)

Note:
    The knight's health has no upper bound.
    Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the
    princess is imprisoned.

------------------------------------------------------------------------------------------------------------------------

The key insight of this problem is realizing that the state of the DP table at a cell only depends on what's ahead of
it, not what's behind it.
"""


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # use a DP approach. In each DP cell, we keep the mimimum health needed to reach the end from that cell
        #
        # Our DP table is filled backwards, because we note that the minimum health needed to reach the end from a cell
        # depends only on future values, not past values
        #
        # When in the very last cell (rows, cols), we take the minimum health we need to end up with, 1, and subtract
        # the dungeon value. We take the higher of 1 and that value -- if the final dungeon value is positive, we just
        # need 1 initial health to reach it from itself, since we have to start with at least 1 health
        #
        # for all other cells, take the minimum of dp[i+1][j] and dp[i][j+1], which is the minimum health needed to
        # reach the end from that cell, and subtract the value of the dungeon at [i][j]. If the resulting value is
        # positive, that is the minimum value needed to reach the end from [i][j]. If the value is negative, then we
        # could have started from [i][j] with a negative health value and still reached the end, but since we must
        # maintain at least one health at all times, we give dp[i][j] a value of 1

        rows = len(dungeon)
        cols = len(dungeon[0])

        dp = [[None for _ in range(cols)] for _ in range(rows)]

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                print(i, j)
                if i == rows - 1 and j == cols - 1:  # we're in the bottom right cell
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                elif i == rows - 1:  # we're on the bottom row
                    dp[i][j] = max(1, dp[i][j+1] - dungeon[i][j])
                elif j == cols - 1:  # we're on the rightmost column
                    dp[i][j] = max(1, dp[i+1][j] - dungeon[i][j])
                else:  # every other cell
                    # we take the minimum of dp[i+1][j] and dp[i][j+1], subtract dungeon[i][j] from it, then take the
                    # maximum of that value with 1
                    dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

        return dp[0][0]


if __name__ == '__main__':
    S = Solution()

    d = [[1,-3,3],[0,-2,0],[-3,-3,-3]]

    print(S.calculateMinimumHP(d))