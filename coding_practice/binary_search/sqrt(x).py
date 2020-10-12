"""
LC69 - Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is
returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

------------------------------------------------------------------------------------------------------------------------

While we could just do return int(x**0.5), the spirit of this problem is to do a binary search. We want to search from
0 to (x + 1) // 2 with a binary search.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # obvious solution, which is accepted
        # return int(x**0.5)

        # binary search, from 0 to (x+1) // 2
        left = 0
        right = (x + 1) // 2

        while left <= right:
            mid = (left + right) // 2
            # check termination case
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid

            if mid * mid > x:
                right = mid
            elif mid * mid < x:
                left = mid + 1

        return mid