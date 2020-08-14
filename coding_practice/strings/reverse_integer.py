"""
LC7 - Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = lambda x: (1, -1)[x < 0]
        number = sign(x) * int(str(abs(x))[::-1])
        if number > 2**31 - 1 or number < -2**31:
            return 0
        else:
            return number