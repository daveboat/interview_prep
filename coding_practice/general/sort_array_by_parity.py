"""
LC905 - Sort array by parity

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the
odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:

    1 <= A.length <= 5000
    0 <= A[i] <= 5000
"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # can do it easily in O(N) time with extra space. Doing it without extra space is also possible
        # but requires a little more bookkeeping: keep an even index, starting at 0. When encounting an odd number,
        # do nothing and move on to the next number. When encounting an even number, swap it with the element at
        # the even index, then increment the even index by 1 and move on to the next number. This is O(N) and uses
        # no extra space.
        even = []
        odd = []

        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)

        return even + odd
