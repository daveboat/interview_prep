"""
LC123 - Best time to buy and sell stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    # Okay, so finding the all increasing subsequences doesn't work, because of the 2 transaction restriction.
    # for example, if my numbers are [1, 4, 2, 7, 2, 100], if I had unlimited transactions I would break it down
    # into [1, 4], [2, 7], [2, 100], which gives me the largest earnings. If I were to naively take the two largest
    # transactions amongst the increasing transactions ([2, 7] and [1, 100]), that would still be incorrect.
    # Since I only have two transactions, I have to do [1, 7], [2, 100], and the subsequence [1, 4, 2, 7]
    # isn't an increasing subsequence.
    #
    # our original idea (find the largest p[j] - p[i] where j > i, then add max(profit in [0, i-1], profit in [j+1, -1])
    # using the same function) doesn't work either for that given example, since the largest possible profit
    # using a single transaction can contain two transactions which sum to a larger profit
    #
    # We can't even just do a nested loop through the list and grab the two largest differences, because we can
    # have a case like [1, 10, 9], where the largest and second largest differences overlap.
    #
    # So, we can think of it like this: given a function to find the largest single-transaction profit, our answer
    # is max_k(ST_profit(prices[0:k]) + ST_profit(prices[k:len(prices)])). In other words, we can check every split
    # and compute the max single transaction in both parts of the split array, and find the maximum amonst all splits.
    # doing it this way is O(N^2), but we can reduce it to O(N) with dynamic programming.
    #
    # Dynamic programming approach: make max single transaction profit arrays for the left->right [0:k] case,
    # and make another one for the right-> left [k:len(prices)] case. Return the largest elementwise sum between
    # the two arrays
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        # left->right DP array
        DP1 = [0] * len(prices)
        p_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < p_min:
                p_min = prices[i]
            else:  # if we're getting a new p_min at this element, we can't be also getting a new max_profit
                if prices[i] - p_min > max_profit:
                    max_profit = prices[i] - p_min
            DP1[i] = max_profit

        # right-> left DP array
        DP2 = [0] * len(prices)
        p_max = prices[-1]
        max_profit = 0
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > p_max:
                p_max = prices[i]
            else:
                if p_max - prices[i] > max_profit:
                    max_profit = p_max - prices[i]
            DP2[i] = max_profit

        # return largest two-element sum
        return max([DP1[i] + DP2[i] for i in range(len(DP1))])
