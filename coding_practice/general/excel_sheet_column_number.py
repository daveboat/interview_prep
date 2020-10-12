"""
LC171 - Excel sheet column number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701

Constraints:

    1 <= s.length <= 7
    s consists only of uppercase English letters.
    s is between "A" and "FXSHRXW".
"""


def letter_to_value(letter):
    return ord(letter) - 64


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # this is just a number in base 26 converted to base 10. Here we do it in reverse order, but we can just
        # do something like ret += ret * 26 + letter_to_value(next letter)

        ret = 0

        for i in range(1, len(s) + 1):
            ret += 26 ** (i - 1) * letter_to_value(s[len(s) - i])

        return ret
