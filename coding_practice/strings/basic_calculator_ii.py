"""
LC227 - Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division
should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution(object):
    def parse(self, term):
        # parse a string with numbers and multiplies and divides
        divide = False
        result = 1
        current_number = 0
        for c in term:
            if c == '*' or c == '/':
                if divide:
                    result //= current_number
                else:
                    result *= current_number
                divide = True if c == '/' else False
                current_number = 0
            else:  # must be numbers
                current_number = 10 * current_number + int(c)

        # need to handle final number
        if divide:
            result //= current_number
        else:
            result *= current_number

        return result

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # remove white space (could be done in the main loop but I too lazies
        s = s.replace(' ', '')

        # to maintain order of operations, we parse via addition and subtraction first, then for each term, we parse
        # multiplication and division
        ret = 0
        current_term = ''
        multiplier = 1
        for c in s:
            if c == '+' or c == '-':
                if current_term != '':
                    ret += multiplier * self.parse(current_term)
                current_term = ''
                multiplier = 1 if c == '+' else -1
            else:
                current_term += c

        # need to handle final term
        ret += multiplier * self.parse(current_term)

        return ret