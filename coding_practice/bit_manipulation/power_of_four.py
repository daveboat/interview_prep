"""
LC342 - Power of four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true

Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # naive approach: divide by four
        #         if num == 1: return True  # special case of 4^0

        #         while num > 4 and num % 4 == 0:
        #             num /= 4

        #         return num == 4

        # better approach: bit checking. The valid 32 bit numbers which are powers of 4 are
        # 1, 100, 10000, 1000000, etc, up to 32 bits
        # all of these must also be powers of 2 (i.e. only one bit is set)
        # then we mask them with the number 1010101010.....01 = 1431655765 to make sure that the number is a power of four
        return num != 0 and num & (num - 1) == 0 and num & 1431655765 == num
