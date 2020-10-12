"""
LC567 - Permutation in string

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one
of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""

import string


def make_dict(s):
    d = {letter: 0 for letter in string.ascii_lowercase}

    for c in s:
        d[c] += 1

    return d


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # we use a sliding window approach to compare s1's letter histogram to the histogram of a window in s2.
        # the key is, instead of remaking a histogram for s2's window every time, we update the window by subtracting
        # the last letter and adding the new letter to the histogram

        # trivial case
        if len(s2) < len(s1):
            return False

        l = len(s1)

        # make dicts for s1 and s2
        s1_dict = make_dict(s1)
        s2_dict = make_dict(s2[:l])

        # check first window
        if s1_dict == s2_dict:
            return True

        # iterate through s2 with a sliding window
        for i in range(1, len(s2) - l + 1):
            # update s2_dict
            s2_dict[s2[i - 1]] -= 1
            s2_dict[s2[i + l - 1]] += 1

            if s1_dict == s2_dict:
                return True

        return False