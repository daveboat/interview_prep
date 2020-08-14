"""
LC - Pascal's triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""


def generateNthRow(N):
    # nC0 = 1
    prev = 1

    ret = [prev]

    for i in range(1, N + 1):
        # nCr = (nCr-1 * (n - r + 1))/r
        curr = (prev * (N - i + 1)) // i
        ret.append(curr)
        prev = curr

    return ret


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # we can use the fact that, the nth row of pascal's triangle is nC0, nC1, ... nCn,
        # nC0 = 1,
        # and nC(i+1) = nCi * (n-i)/(i+1)
        #
        # This is O(k) in time and O(k) in space

        return generateNthRow(rowIndex)
