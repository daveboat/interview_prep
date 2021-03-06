"""
LC389 - Find the difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""


from collections import Counter


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # take two histograms? O(N) to make the histograms, O(1) space because alphabet is 26 letters, O(1) time to do
        # the histogram comparison
        s_c = Counter(s)
        t_c = Counter(t)

        for k in t_c:
            if k not in s_c or t_c[k] > s_c[k]:
                return k
