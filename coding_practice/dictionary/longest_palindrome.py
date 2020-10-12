"""
LC409 - Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be
built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def make_hist(self, s):
        # make a histogram out of a string
        hist = dict()
        for c in s:
            if c not in hist:
                hist[c] = 1
            else:
                hist[c] += 1

        return hist

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # so, we dict (O(N)), then we add up all the even contributions, plus 1 if there are any odd numbered letters
        # Accepted (97%)

        # step 1: make hist
        hist = self.make_hist(s)

        # step 2: step through hist, keeping track of if we found an odd number
        odd_found = False
        ret = 0
        for v in hist.values():
            if v % 2 == 0:  # if even, straight up add it to the total
                ret += v
            else:  # if odd, add the value - 1 and set odd_found to True
                odd_found = True
                ret += v - 1

        if odd_found:
            ret += 1

        return ret
