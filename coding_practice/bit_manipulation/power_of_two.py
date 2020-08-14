"""
LC231 - Power of Two

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1

Example 2:

Input: 16
Output: true
Explanation: 24 = 16

Example 3:

Input: 218
Output: false
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # first attempt: O(logN) divide by two until we can't or we reach 1
        #         if n <= 0:
        #             return False

        #         while n > 0:
        #             if n == 1:
        #                 return True
        #             elif n % 2 == 0:
        #                 n /= 2
        #             else:
        #                 return False

        #         return True

        # second attempt: bit manipulation. if X is a power of 2, then its most significant bit is 1 and all other bits are zero.
        # also, X - 1 must be the bitwise not of that. For example, 128 is 10000000, and 127 is 01111111. So 128 & 127 is 0. This
        # is an O(1) check.
        if n <= 0: return False
        return n & (n - 1) == 0