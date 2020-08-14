"""
LC468 - Validate IP Address

 Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging
from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups
are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we
could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case
ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::)
to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address
02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:

Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:

Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:

Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""


import string


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            return self.validateIPV4(IP)
        elif ':' in IP:
            return self.validateIPV6(IP)
        else:
            return 'Neither'

    def validateIPV4(self, IP):
        numbers = IP.split('.')

        # check that there are four parts to the split, they're all numeric between 0 and 255
        # also need to check if there's a leading zero for a nonzero number
        if len(numbers) == 4 and all(s.isdigit() for s in numbers) and all(0 <= int(s) <= 255 for s in numbers) and not any(len(s) > 1 and s[0] == '0' for s in numbers):
            return 'IPv4'
        else:
            return 'Neither'

    def validateIPV6(self, IP):
        hexes = IP.split(':')

        # check that there are 8 parts, they are all length 0 to 4, and they are all hexes
        if len(hexes) == 8 and all(1 <= len(s) <= 4 for s in hexes) and all(all(c in string.hexdigits for c in s) for s in hexes):
            return 'IPv6'
        else:
            return 'Neither'


if __name__ == '__main__':
    S = Solution()

    h = '2001:0db8:83a3::0000:8a2e:0370:7334'

    print(S.validateIPV6(h))