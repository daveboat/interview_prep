"""
LC190 - Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so
return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so
return 3221225471 which its binary representation is 10111111111111111111111111111111.

Note:

    Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output
    will be given as signed integer type and should not affect your implementation, as the internal binary
    representation of the integer is the same whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above
    the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Follow up:

If this function is called many times, how would you optimize it?

------------------------------------------------------------------------------------------------------------------------

I initially took a string reversal approach to this, which was accepted and with comprable time to the bit manipulation
approaches

But: there are a few bit manipulation approaches to this, all of which are O(1) space and O(1) time.
the simplest is to just take the bits one by one (n & 1) and shift them to where they are supposed to be
(i.e. 0th bit should end up in the 31st place in the reversed sequence), and do this one by one (n >> 1)

for the follow-up question, we can reverse bytes at a time, i.e. 8 bits at a time (n & 0xff, n >> 8)
and memoize the reversed bytes in a cache so that we don't need to recalculate them. The byte reversal can
be done using a magical line: byte = (byte * 0x0202020202 & 0x010884422010) % 1023
"""


# first attempt, using string reversal
# class Solution:
#     # @param n, an integer
#     # @return an integer
#     def reverseBits(self, n):
#         # need to take into account all of the zeros in front of the number to make it 32 bits
#         # we convert to binary, reverse
#         binary = str(bin(n))[2:]

#         # return the binary in reverse, with zeros appended or bit shifted until the length is 32

#         return int(binary[::-1], 2) << (32 - len(binary))

class Solution:
    def reverseByte(self, byte):
        # a magical line of code to reverse a byte
        return (byte * 0x0202020202 & 0x010884422010) % 1023

    def reverseBits(self, n):
        # reverse a 32-bit unsigned int by reversing bytes (8 bits) at a time. First shift is 24, which is 32 - 8
        # because our byte is 8 bits instead of 1
        p = 24
        ret = 0
        while n:
            ret += self.reverseByte(n & 0xff) << p
            n = n >> 8
            p -= 8

        return ret