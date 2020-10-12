"""
LC518 - Coin change 2

You are given coins of different denominations and a total amount of money. Write a function to compute the number of
combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1

"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # use DP.
        # the columns are the amounts in increasing order, from 0 to amount
        # the rows are the coins, from index 0 representing using no coins, index 1 representing forming amounts with
        # just the first coin, index 2 representing using just the first two coins, etc
        # the trick is to notice that, for each (i,j) in the dp table, we can form the amount by either including the ith
        # coin or not including the ith coin. Inclusion means looking at element (i, j - value of ith coin) since
        # that element of the table is how many ways of making the correct amount are possible if we include
        # the ith coin. Exclusion means looking at element (i-1, j), since that is how many ways of making the correct
        # amount are possible if we don't use the ith coin.

        #         dp = [[1] + [0] * amount for _ in range(len(coins) + 1)]

        #         for i in range(1, len(coins) + 1):
        #             for j in range(1, amount + 1):
        #                 dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i - 1]] if j >= coins[i - 1] else 0)

        #         return dp[-1][-1]

        # there is also a way to do this with less space by only using one row of the DP table and overwriting it
        # each iteration, since the current value only depends on its value on the previous row and values earlier
        # in the same row

        # another possibility, have a single row DP table, iterate over the coins. For each DP cell, each coin adds a number equal
        # to the dp table at the current index - the value of the coin.
        # effectively, this means, when the dp table doesn't yet include a coin, the coin adds to the existing number of combinations (which
        # don't include it) plus the number of combinations that could be made if the coin were added.

        dp = [1] + [0] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]