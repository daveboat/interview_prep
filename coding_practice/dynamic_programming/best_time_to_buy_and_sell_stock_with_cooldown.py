"""
LC309 - Best time to buy and sell stock with cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # this is a dynamic programming problem. Our DP table has len(prices) rows and 2 columns.
        # DP[i][0] represents a case where we are not holding a stock, either because we just sold a stock
        # or we sold a stock previously and still haven't bought a new one.
        # DP[i][1] represents a case where we are holding a stock, either because we just bought a stock,
        # or because we're still holding on to a previously bought stock
        #
        # therefore, DP[i][0] is the maximum of:
        #   DP[i-1][1] + prices[i], the case where I sold a stock, and
        #   DP[i-1][0], the case where I'm holding on to nothing
        # and DP[i][1] is the maximum of:
        #   DP[i-2][0] - prices[i], the case where I went from not having a stock to having a stock (with a cooldown), and
        #   DP[i-1][1], the case where I am holding onto a stock
        #
        # DP[0][0] is 0, where I don't buy the first stock, and DP[0][1] is -prices[i], where I buy the first stock

        if not prices:
            return 0

        DP = [[0, 0] for _ in range(len(prices))]

        DP[0][1] = -prices[0]

        for i in range(1, len(prices)):
            if i < 2:
                DP[i][1] = max(DP[i - 1][1], -prices[i])
            else:
                DP[i][1] = max(DP[i - 1][1], DP[i - 2][0] - prices[i])
            DP[i][0] = max(DP[i - 1][1] + prices[i], DP[i - 1][0])

        return max(DP[-1][:])
