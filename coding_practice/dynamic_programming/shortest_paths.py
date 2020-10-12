"""
LC62 - Shortest Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

Constraints:

    1 <= m, n <= 100
    It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

------------------------------------------------------------------------------------------------------------------------

It turns out the math solution is m+n-2 choose n-1
"""
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # I don't know if there's an elegant math solution (for example, for a square grid where you're not allowed
        # to cross the diagonal, the answer is the catalan sequence)
        #
        # But I know you can do this with dynamic programming in O(m*n) time. What's not clear is if there's an O(1)
        # math formula that you can derive

        #         dp = [[0 for _ in range(m)] for _ in range(n)]

        #         # we start from 1 at the top left instead of going backwards from the bottom right for simplicity
        #         for i in range(n):
        #             for j in range(m):
        #                 if i == 0 or j == 0:
        #                     dp[i][j] = 1
        #                 else:
        #                     dp[i][j] = dp[i-1][j] + dp[i][j-1]

        #         return dp[-1][-1]

        return ncr(m + n - 2, n - 1)