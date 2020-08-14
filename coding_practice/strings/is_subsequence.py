"""
LC392 - Is subsequence

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde"
while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has
its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # just do a linear check i guess, how else would you do it?
        # this would be O(s + t) in time

        # i = 0
        # j = 0
        #
        # while i < len(s):
        #
        #     if j == len(t):
        #         return False
        #
        #     if t[j] == s[i]:
        #         j += 1
        #         i += 1
        #     else:
        #         j += 1
        #
        # return True

        # follow up:

        # For one t and lots of s's, a better way is to create a dictionary or other kind of lookup table for t.
        # for example, a dictionary with all the letters, and each letter is mapped to a list of indices where the
        # letter appears in order then, for each s, we can look up the letter and whether it has an instance after the
        # last letter. We can even use binary search for this instead of linear search, in the letter lists (bisect
        # works for this)

        # this looks like (untested):

        # build a dict for t (this would be done during initialization for the actual follow up example)
        import string
        t_dict = {l: [] for l in string.ascii_lowercase}
        i = 0
        for c in t:
            t_dict[c].append(i)
            i += 1

        # when an s comes in, we iterate through s, checking that an appropriate character can be found in t
        from bisect import bisect_left
        idx = 0
        for c in s:
            # if the letter doesn't appear in t at all, return false immediately
            if not t_dict[c]:
                return False

            # else find the correct pos of the letter in t using binary search
            pos = bisect_left(t_dict[c], idx)

            # make sure pos is within the array and t_dict[c][pos] is actually greater than or equal to idx
            if pos >= len(t_dict[c]) or t_dict[c][pos] < idx:
                return False

            # set idx to t_dict[c][pos] + 1 for the next letter
            idx = t_dict[c][pos] + 1

        # if we've made it here, return True
        return True