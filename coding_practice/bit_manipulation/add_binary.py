"""
LC67 - Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

    Each string consists only of '0' or '1' characters.
    1 <= a.length, b.length <= 10^4
    Each string is either "0" or doesn't contain any leading zero.

------------------------------------------------------------------------------------------------------------------------

We do the logic in this problem by implementing a full adder circuit, and going through the bits in a and b in LSB order

Given two bits and an incoming carry, the equations for a full adder are:

    sum = (x ^ y) ^ carry
    carry = ((x ^ y) & carry) | (x & y)
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        idx_a = len(a) - 1
        idx_b = len(b) - 1
        carry = 0
        output = ''

        while idx_a >= 0 or idx_b >= 0 or carry:
            bit_a = int(a[idx_a]) if idx_a >= 0 else 0
            bit_b = int(b[idx_b]) if idx_b >= 0 else 0

            # construct a full adder
            s = (bit_a ^ bit_b) ^ carry
            carry = ((bit_a ^ bit_b) & carry) | (bit_a & bit_b)

            output += str(s)

            idx_a -= 1
            idx_b -= 1

        return output[::-1]