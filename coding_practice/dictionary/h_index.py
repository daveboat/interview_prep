"""
LC274 - H-index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""


# initial solution: quickselect. passes, but very slow.
#
# def swap(lst, left, right):
#     lst[left], lst[right] = lst[right], lst[left]
#
#
# def partition_lomuto(lst, left, right):
#     # pivot is chosen as the rightmost element
#     pivot = lst[right]
#
#     i = left - 1
#
#     for j in range(left, right):
#         if lst[j] < pivot:
#             i += 1
#             swap(lst, i, j)
#
#     i += 1
#     swap(lst, right, i)
#
#     return i
#
#
# class Solution(object):
#     def __init__(self):
#         self.h = 0
#
#     def quickselect_helper(self, lst, left, right, N):
#         # termination condition
#         if right < left:
#             return
#
#         partition_index = partition_lomuto(lst, left, right)
#
#         # if lst[partition_index] is greater than N - partition_index, then N - partition_index
#         # is a valid h, but might not be the largest valid h, so we quickselect left
#         if lst[partition_index] >= N - partition_index:
#             if N - partition_index > self.h:
#                 self.h = N - partition_index
#             self.quickselect_helper(lst, left, right - 1, N)
#         # otherwise, N - partition_index is not a valid h-index, and we quickselect right
#         else:
#             self.quickselect_helper(lst, left + 1, right, N)
#
#
#     def hIndex(self, citations):
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         # Maybe we can use a partial sorting strategy, to accomplish this in logarithmic time. i.e. use quickselect
#         # the same way we used binary search for h-index ii. If citations[current_index] >= len(citations) -
#         # current_index, then len(citations) - current_index is a possible h-number, and we quickselect to the left
#         # for a possible greater h-number. Otherwise, we quickselect to the right for a smaller h-number.
#         if not citations:
#             return 0
#
#         N = len(citations)
#         self.quickselect_helper(citations, 0, N - 1, N)
#
#         return self.h


# next attempt: dictionary
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # quickselecting was very slow, perhaps because we're dealing with a bunch of small arrays instead of a few
        # large arrays as the submission test cases.
        #
        # anyways, instead of quickselecting, we can use a dictionary (or a list) to create a histogram of citations
        # basically a bucket sort. Once we have the histogram, we can go back from the last bucket, and do a cumulative
        # sum. As soon as we hit an index, cum_sum pair where index <= cum_sum, that index must be the largest
        # permissable h-value
        #
        # So we do two O(N) passes, one to make the buckets, and one to find the h-index. This uses O(N) extra space
        # for the buckets.

        N = len(citations)

        # step 1: make our histogram
        buckets = [0] * (N + 1)
        for c in citations:
            if c >= N:
                buckets[N] += 1
            else:
                buckets[c] += 1

        # step 2: cumulative sum from the end
        cum_sum = 0
        for i in range(N, -1, -1):
            cum_sum += buckets[i]
            if i <= cum_sum:
                return i

        return 0