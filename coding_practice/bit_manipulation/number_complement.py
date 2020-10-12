class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # solve via string inversion, converted back to int
        # return int(''.join(['1' if c == '0' else '0' for c in str(bin(num))[2:]]), base=2)

        # solve via xor and bit shifting
        # temp = num
        # bit = 1
        # while temp:
        #     num = num ^ bit
        #     bit = bit << 1
        #     temp = temp >> 1
        # return num

        # solve via bitwise subtraction
        return 2 ** (len(str(bin(num))) - 2) - 1 - num