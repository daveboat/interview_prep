"""
LC967 - Numbers with same consecutive differences

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is
K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one
leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:

    1 <= N <= 9
    0 <= K <= 9
"""


class Solution(object):
    def recursive_diff(self, N, K, parent):
        # returns a list of valid numbers for each parent num
        ret = []
        if N == 1:
            ret += [parent]
        else:
            for i in range(10):
                if abs(i - parent) == K:
                    ret += [parent * 10 ** (N - 1) + r for r in self.recursive_diff(N - 1, K, i)]

        return ret

    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        # We take a bottom-up recursive approach, where each function call returns a list of valid
        # numbers from its children, until the N counter reaches 1, whereupon the last number is returned

        # A special case is N=1, K=anything. I think this should be the only time when 0 is a possible
        # return value.

        # trivial case
        if N == 1: return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # call our recursive function for numbers from 1 to 10
        ret = []
        for i in range(1, 10):
            ret += [r for r in self.recursive_diff(N, K, i)]

        return ret

