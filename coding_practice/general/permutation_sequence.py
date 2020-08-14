"""
LC60 - Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note:

    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"

------------------------------------------------------------------------------------------------------------------------

The idea is, the ith (i in [1, n]) digit is calculated by calculating idx (k-1)//(n-i)!, after which k is set to the
remainder (i.e. k = k % (n-1)!). The idx-th digit is appended to the solution and then that digit needs to be removed
from the list of possible digits because we are not replacing digits after using them.

For example, with n=5 (values = [1, 2, 3, 4, 5]), and k = 99:

- We first divide k-1 by 24 to see which is the first digit. This returns 4, values[4] is 5 --> output is "5"
- 5 is removed from values. --> values = [1, 2, 3, 4]
- We take the remainder after k is divided by 4! = 24, which is 3 --> k is now 3
- We divide k-1 by 6 now, which is 0, values[0] is 1 --> output is "51"
- 1 is removed from values. --> values is [2, 3, 4]
- We take the remainder after k is divided by 3! = 6, which is still 3 --> k is now 3
- We divide k-1 by 2, which is 1, values[1] is 3 --> output is "513"
- 3 is removed from values. --> values is [2, 4]
- We take the remainder after k is divided by 2! = 2, --> k is now 1
- We divide k-1 by 1, which is 0, values[0] is 2 --> output is "5132"
- 2 is removed from values --> values is [4]
- We take the remainder of k after division by 1 --> k is now 0
- We divide k-1 by 1! = 1, resulting in -1, but we are now on our last value, so indexing by -1 is okay. output is "51324"
- 4 is removed from values --> values is []
- we take the remainder of k after division by 1 --> k is still 0
- Values is empty and so the loop exits
"""


class Solution(object):
    def __init__(self):
        # keep the first 8 factorials (including 0) here for speed!
        self.factorials = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 3628800)

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # remaining values
        values = [i for i in range(1, n + 1)]
        out_string = ''

        while values:
            idx = (k - 1) // self.factorials[n-1]
            k %= self.factorials[n-1]
            out_string += str(values[idx])
            values.remove(values[idx])
            n -= 1

        return out_string


if __name__ == '__main__':

    S = Solution()
    n = 5
    factorials = (1, 1, 2, 6, 24, 120, 720, 5040, 40230, 3628800)
    print(S.getPermutation(n, 99))
    # for k in range(1, factorials[n] + 1):
    #     print(S.getPermutation(n, k))

