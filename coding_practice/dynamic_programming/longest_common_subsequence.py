"""
LC1143 - Longest common subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted
without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is
not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # This is a dynamic programming problem. First, let's look at the recursive solution to this problem.
        # if our two strings are 'acbd' and 'axby', we have
        # lcs(acbd, axby) = max(lcs(acb, axby), lcs(acbd, axb))
        #                 = max(max(lcs(ac, axby), lcs(acb, axb)), max(lcs(acb, axb), lcs(acbd, axb)))
        # and so forth.
        #
        # Note that lcs(acb, axb) = 1 + lcs(ac, ax) and lcs(ac, axby) = max(lcs(a, axby), lcs(ac, axb)),
        # and lcs(any string, '') = lcs('', any string) = lcs('', '') = 0
        #
        # So, we could create a recursive solution by comparing last characters, if they're the same, we return 1 + lcs of the two strings with both characters removed
        # if they're different, we return the max of two lcs calls on the strings each with their last character removed, until we terminate if either or both strings is empty.
        #
        # The dynamic programming version of this is to do this recursive process bottom-up instead of top-down. start with lcs for '' and '', which is zero. Then compute
        # lcs for a and '' and ac and '' and acb and '' and acbd and '', and '' and a and '' and ax and '' and axb and '' and axby, all of which are zero.
        # Then, the comparison of a with a, using our rule, is the comparison of '' and '' plus 1. The comparison of ax and a is the maximum of the comparison of ax with '' and
        # a with a, which is 1. This can be kept track of in a table of size len(text1) + 1 by len(text2) + 1

        # initialize our table
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

        # create the dp table
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]