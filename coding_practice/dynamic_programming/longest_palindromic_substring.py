"""
LC5 - Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # The idea is to use a dp table, where cell (i, j) holds whether or not the substring from character i to
        # character j is a palindrome. We need to iterate diagonally for this, so we use the pattern
        # for i in range(l): for j in range(l - i): row, col = j, j + i
        # this iterates like (row, col) = (0, 0), (1, 1), ..., (l-1, l-1), (0, 1), (1, 2), ..., ..., (0, l-2), (1, l-1),
        # (0, l-1)
        # if i == j, then the cell is always 1, since a single character is by definition a palindrome
        # if i == j - 1, so the second diagonal, the cell is 1 if the ith character is equal to the jth character
        # for all other situations (j > i + 1), or all further diagonals, the cell is 1 if the ith character is equal
        # to the jth character, and if the substring from i+1 to j-1 is a palindrome, which is checked from the dp table
        #
        # Building the DP table is O(N^2). Checking if every possible substring is a palindrome is O(N^3), since you
        # still need to do O(N^2) work for every starting and ending character, but checking if a string is a palindrome
        # is also O(N)

        l = len(s)
        dp = [[0 for _ in range(l)] for _ in range(l)]

        max_row_col = [0, 0]

        for i in range(l):
            for j in range(l - i):
                row, col = j, j + i
                if row == col:
                    dp[row][col] = 1
                elif row == col - 1:
                    dp[row][col] = 1 if s[row] == s[col] else 0
                else:
                    dp[row][col] = 1 if s[row] == s[col] and dp[row + 1][col - 1] == 1 else 0

                if dp[row][col] == 1:
                    if col - row > max_row_col[1] - max_row_col[0]:
                        max_row_col = [row, col]

        return s[max_row_col[0]:max_row_col[1] + 1]


if __name__ == '__main__':
    s = "321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"

    S = Solution()

    print(S.longestPalindrome(s))