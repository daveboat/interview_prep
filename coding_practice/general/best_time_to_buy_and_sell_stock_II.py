"""
LC122 - Best time to buy and sell stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and
sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

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

------------------------------------------------------------------------------------------------------------------------
Basically this problem is just summing the diffs of the array as long as the diff is above zero. The first time I did
it, I used a convoluted algorithm.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # first attempt
#         # return in the trivial case
#         if len(prices) <= 1:
#             return 0

#         if prices[1] <= prices[0]:
#             currently_held_stock = prices[1]
#             current_index = 1
#         else:
#             currently_held_stock = prices[0]
#             current_index = 0

#         earnings = 0

#         while current_index < len(prices) - 1:
#             # if we see a decrease in price between current and next, sell current at high price, buy at low price
#             if prices[current_index] > prices[current_index + 1]:
#                 earnings += prices[current_index] - currently_held_stock
#                 currently_held_stock = prices[current_index + 1]
#             current_index += 1

#             # take care of the case where we reach the end of the array without having sold/bought
#             if current_index == len(prices) - 1 and prices[current_index] > currently_held_stock:
#                 earnings += prices[current_index] - currently_held_stock

#         return earnings


        # second attempt: just sum diffs as long as diffs are above zero
        return sum([prices[i+1] - prices[i] for i in range(len(prices) - 1) if prices[i+1] - prices[i] > 0])