"""
LC918 Maximum sum circular subarray
"""


class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        Given a circular array, the maximum subarray that wraps around is the array sum minus the minimum non-circular
        subarray (i.e. the most negative). The maximum subarray that doesn't wrap around is just the maximum subarray.

        The maximum subarray is the larger of the two, unless the entire array is negative, in which case we return the
        max sum. We can check for this by checking if regular_sum = min_sum

        So, we need to compute the minimum sum, the maximum sum, and the regular sum all at once
        """
        regular_sum = 0
        min_sum = A[0]
        max_sum = A[0]
        min_cur_sum = 0
        max_cur_sum = 0

        for elem in A:
            regular_sum += elem

            min_cur_sum += elem
            max_cur_sum += elem

            if min_cur_sum < min_sum:
                min_sum = min_cur_sum
            if max_cur_sum > max_sum:
                max_sum = max_cur_sum

            if min_cur_sum > 0:
                min_cur_sum = 0
            if max_cur_sum < 0:
                max_cur_sum = 0

        return max_sum if regular_sum == min_sum else max(regular_sum - min_sum, max_sum)


if __name__ == '__main__':
    S = Solution()

    a = [5,-3,5]

    print(S.maxSubarraySumCircular(a))