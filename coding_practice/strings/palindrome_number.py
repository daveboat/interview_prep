"""
LC9 - Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Can do this without using strings by reversing the number:
def reverse(num):
    res = 0
    while num != 0:
        res = res * 10 + num % 10
        num = num // 10
    return res
"""


def is_palindrome(x):
    # returns if a string is a palindrome
    left = 0
    right = len(x) - 1

    while left < right:
        if x[left] == x[right]:
            left += 1
            right -= 1
        else:
            return False

    return True


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return is_palindrome(str(x))