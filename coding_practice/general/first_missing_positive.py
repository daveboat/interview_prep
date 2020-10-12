"""
Leetcode 41 - First missing positive.

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Follow up:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using constant extra space implies we must use the array itself to keep track of which numbers are
        # there. Because nums is of length N, if there are no missing positive integers less than N, all of
        # the integers from 1 to N must be in the array, and the first missing one must be N+1
        #
        # so we go through the array, marking index i-1 if the number i shows up by turning it negative.
        # in a second pass through the array, we check for positive numbers. if everything is negative, N+1
        # must be the missing number
        #
        # our strategy is messed up by the presence of zero and negative numbers, so we first do a preprocessing
        # pass by setting zero and negative numbers to the value N+1, which doesn't affect our following passes

        N = len(nums)

        # pass 1: set n <= 0 to N+1
        for i in range(N):
            if nums[i] <= 0:
                nums[i] = N + 1

        # pass 2: mark array for numbers between 1 and N. take absolute value so numbers we've already marked as
        # negative get mapped to a positive index
        for i in range(N):
            if 0 < abs(nums[i]) <= N:
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1

        # pass 3: seek the first positive number
        for i in range(N):
            if nums[i] > 0:
                return i + 1

        # return N+1 if we finished the previous loop without returning
        return N + 1
