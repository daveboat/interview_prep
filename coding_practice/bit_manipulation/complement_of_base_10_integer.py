"""
LC1009 - Complement of base 10 integer

Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as
"1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.
For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.



Note:

    0 <= N < 10^9
    This question is the same as 476: https://leetcode.com/problems/number-complement/
"""


class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # the result we're looking for is 2^k - 1 - N, where 2^k-1 is the next largest power of 2 minus one to N.
        # for example, for N=10, the next largest 2^k-1 is 16-5=15, 15-10=5
        #
        # to find k, we can bit shift N until we get 0, which gives us O(logN) time and O(1) space

        # edge case
        if N == 0:
            return 1

        k = 0
        n = N

        while n > 0:
            k += 1
            n >>= 1

        return 2 ** k - 1 - N
