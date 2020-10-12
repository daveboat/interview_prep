"""
LC275 - H-index II

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a
function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h
citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.

Note:

If there are several possible values for h, the maximum one is taken as the h-index.
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # use a binary search strategy. if citations[N-index] >= index, then N-index is a possible h-number. We
        # store the largest yet discovered, and look to the left for larger h-numbers
        # if citations[N-index] < index, then N-index is not an h-number, and we look to the right

        # edge case
        if not citations:
            return 0

        N = len(citations)

        left = 0
        right = N-1

        # the smallest possible h is 0, if all papers have 0 citations
        h = 0

        while left <= right:
            index = (left + right) // 2

            if citations[index] >= N - index:
                if N - index > h:
                    h = N - index

                right = index - 1

            else:
                left = index + 1

        return h
