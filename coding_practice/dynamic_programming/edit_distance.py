"""
LC72 - Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # This is the levenshtein distance. First, let's consider the recursive solution to this problem.
        # For D('XXXx', 'YYYy'), if x != y there are three possibilities:
        # 1. we change XXX to YYY, and then replace a character (replace x with y in this case)
        # 2. we change XXX to YYYy, and then delete a character (delete x in this case)
        # 3. we change XXXx to YYY, and then add a character (add y in this case)
        # so the edit distance of D('XXXx', 'YYYy') is equal to the minimum of the edit distances of D('XXX', 'YYY'),
        # D('XXXx', 'YYY'), and D('XXX', 'YYYy'), plus one
        # for D('XXXx', 'YYYy'), if x == y, then the edit distance of D('XXXx', 'YYYy') is equal to the
        # edit distance of D('XXX', 'YYY')
        # the base case is D('', 'XXX'), D('XXX', ''), and DP('', ''), which is trivial

        # The easiest way to solve this is with a DP table

        DP = [[j for j in range(len(word2) + 1)]] + [[i] + [0] * len(word2) for i in range(1, len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] != word2[j - 1]:
                    DP[i][j] = 1 + min(DP[i - 1][j], DP[i][j - 1], DP[i - 1][j - 1])
                else:
                    DP[i][j] = DP[i - 1][j - 1]

        return DP[len(word1)][len(word2)]


if __name__ == '__main__':
    word1 = 'horse'
    word2 = 'ros'

    S = Solution()

    print(S.minDistance(word1, word2))