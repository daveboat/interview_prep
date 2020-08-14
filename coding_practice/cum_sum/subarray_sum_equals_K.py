"""
LC560 - Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Constraints:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # attempt 1: brute force DP-ish O(N^2) solution
        #         N = len(nums)
        #         out = 0
        #         dp = [[0] * N for _ in range(N)]

        #         for i in range(N):
        #             for j in range(i, N):
        #                 if i == j:
        #                     dp[i][j] = nums[i]
        #                 else:
        #                     dp[i][j] = dp[i][j - 1] + nums[j]
        #                 if dp[i][j] == k:
        #                     out += 1

        #         return out

        # attempt 2: using a dictionary of cumulative sums (after reading solution)
        d = {}
        cumsum = 0
        count = 0
        for num in nums:
            cumsum += num
            # account for the case where we reach k from the actual cumulative sum from 0
            if cumsum == k:
                count += 1

            # check if cumsum - d is in the dictionary, if it is, then increment count by the number of times it's appeared
            # up til now. This accounts for all cases where intermediate array sums are k
            if cumsum - k in d:
                count += d[cumsum - k]

            # add the current cumulative sum to the dictionary
            if cumsum not in d:
                d[cumsum] = 1
            else:
                d[cumsum] += 1

        return count