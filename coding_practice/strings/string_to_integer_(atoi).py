"""
LC8 - String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:

Input: str = "42"
Output: 42
Example 2:

Input: str = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: str = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: str = "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-' and '.'.
"""


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # remove whitespace
        s = s.strip()

        # trivial case
        if not s:
            return 0

        # take care of negative numbers. for negative numbers, the minus sign
        # must be the first character. Apparently '+' is also a possible symbol...
        neg = False
        if s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # go through the string to construct our number. if at any time we
        # run into whitespace. keep track of the number of digits so we don't
        # need to go beyond 10 digits (the number of digits in 2^31)
        curr_number = 0
        digits = 0
        valid_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        leading_zero = True

        for c in s:
            if c in valid_numbers:
                # build our number with the current digit
                curr_number = 10 * curr_number + valid_numbers.index(c)

                # keep track of the number of digits we have in our number
                # so that our time complexity is constant. This means keeping
                # track of whether we're not in a region of leading zeros
                if c != '0':
                    leading_zero = False
                if not leading_zero:
                    digits += 1
                    if digits > 10: break
            else:
                break

        # handle the 32 bit integer thing
        if neg:
            curr_number *= -1
            if curr_number < -2147483648:
                curr_number = -2147483648
        else:
            if curr_number > 2147483647:
                curr_number = 2147483647

        return curr_number