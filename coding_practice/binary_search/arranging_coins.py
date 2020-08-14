"""
LC441 - Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""


def arithmetic_sequence(k):
    return k * (k + 1) / 2


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # so, there might be a fancy mathematical way to solve this, but we can at least do it in log(n) time via
        # binary search
        #
        # we know the arithmetic sequence for k is k (k + 1) / 2, so we binary search for the k for which
        # arithmetic_sequence(k) <= n < arithmetic_sequence(k+1)
        #
        # we can search from 1 to n//2 if we return n if n <= 1

        # trivial case
        if n <= 1:
            return n

        low = 1
        high = n // 2

        while low <= high:
            k = (low + high) // 2

            s = arithmetic_sequence(k)
            s_plus = arithmetic_sequence(k + 1)

            if s <= n < s_plus:
                return k
            elif n == s_plus:
                return k + 1
            elif s > n:
                high = k - 1
            else:  # s < n but not s <= n < s_plus
                low = k + 1


if __name__ == '__main__':
    S = Solution()
    for i in range(1000):
        print(S.arrangeCoins(i))
