"""
LC279 - Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to
n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

------------------------------------------------------------------------------------------------------------------------

In my first try, I used a dynamic programming approach.

Apparently there's a basically O(N) math solution using Lagrange's four square theorem, which says that any positive
integer can be written as the sum of four squares (including zero), so the answer to this question can only be
1, 2, 3, or 4. The algorithm goes like this:

If it's a perfect square itself, then the answer is 1
Next, if it can be written in the form 4^k*(8*m + 7), the answer is 4. Can check this by dividing by 4 until the number
is no longer divisible by 4, then checking if the number, divided by 8, has a remainder of 7
Next, we can check if 2 is the result by checking every square up to sqrt(n) to see if n minus that square is also a
perfect square.
If none of the above was true, the answer must be 3.
"""


import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # so, the greedy algorithm (always using the next smallest perfect square) doesn't work... a counterexample
        # is 12, for which the greedy algorith would use 9, 1, 1, 1 instead of 4, 4, 4
        #
        # so we treat this like the coin change problem except we use perfect squares. We iterate from 1 to n, checking
        # perfect squares from 1 to sqrt(n) (really we should check to sqrt(i) but taking a sqrt every iteration might be
        # slower than just checking to sqrt(n) and only square rooting once)
        #
        # For n=12, for example, our array should look like
        #
        # 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3 <-- final 3 comes from checking 12-4, which has a minimum of 2 perfect squares
        #                                        and adding one more perfect square (4)
        #
        # this solution is O(n*sqrt(n)) in time and O(n) in space

        dp = [0]
        m = int(math.floor(math.sqrt(n)))

        for i in range(1, n + 1):
            min_list = []
            for j in range(1, m + 1):
                sq = j * j
                if i - sq >= 0:
                    min_list.append(dp[i - sq] + 1)

            dp.append(min(min_list))

        return dp[-1]


if __name__ == '__main__':
    S = Solution()

    S.numSquares(12)
