"""
LC258 - Add digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # The iterative solution is simple, but there's a math solution.
        # consider num = d_n d_n-1 ... d_1 d_0, where d_0 is the least significant digit, and d_n is
        # the most significant.
        #
        # num, written in terms of its digits, is
        # num = d_0 * 10^0 + d_1 * 10^1 + ... + d_n-1 * 10^n-1 + d_n * 10^n
        #
        # For this problem, we want to compute D = d_0 + d_1 + ... + d_n-1 + d_n
        # We note that 10^n mod 9, n = 0, 1, 2, ... is equal to 1. In other words, 10^n = 1 (mod 9)
        #
        # Because of this fact, num and D are the same, mod 9, so the digital root of a positive number
        # is periodic, after an initial 0:
        # num 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17 ...
        # D   0  1  2  3  4  5  6  7  8  9  1    2   3   4   5   6   7   8 ...
        #
        # the relationship between num and D can be then written
        # D = (num - 1) mod 9 + 1 if num > 0, 0 if num == 0
        #
        # This formula accounts for the extra 0 at the beginning. We have to do the extra conditional because -1 % 9 is
        # 8 in python instead of -1 like it should be

        return 0 if num == 0 else (num - 1) % 9 + 1
