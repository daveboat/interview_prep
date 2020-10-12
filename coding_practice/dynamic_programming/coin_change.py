"""
LC322 - Coin change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # i think a greedy algorithm works here, use largest coin until amount < largest coin, then use second largest coin, etc.
        # if amount reaches 0, we're good. if amount can't reach 0 with the last coin,
        #         coins = sorted(coins)
        #         c = len(coins) - 1  # coin index
        #         counter = 0  # number of coins used counter

        #         while amount > 0: # keep iterating while amount is greater than zero

        #             if coins[c] > amount:
        #                 # if we can no longer use the largest coin, use the next largest. if there is no next largest, return -1
        #                 if c == 0:
        #                     return -1
        #                 else:
        #                     c -= 1
        #             else:
        #                 # use a coin
        #                 amount -= coins[c]
        #                 counter += 1

        #         return counter

        # no, actually the greedy algorithm doesn't work for general coins. Look at the case coins=[17, 20], amount=3*17=51
        # the greedy algorithm would return -1 since it would try to use 20 twice

        # we have to do an O(coins * amount) algorithm. This works by iterating from 0 to amount. At each index, iterate
        # through each coin. Finds the minimum of all the dp[i-coin] that exist (not -1), and finds the minimum of them
        # and adds 1 for the current coin. dp[0] is 0, since it takes 0 coins to get to 0. By the time we get to
        # dp[amount], we will have tabulated, for each dp[amount - coin], the smallest number of coins that could have
        # gotten there, so we just want the minimum of all the dp[amount - coin]'s, and add 1
        dp = [0]

        for i in range(1, amount + 1):
            # add values based on coins
            mincheck = []
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] >= 0:
                    mincheck.append(dp[i - coin])

            if not mincheck:
                dp.append(-1)
            else:
                dp.append(min(mincheck) + 1)

        return dp[-1]