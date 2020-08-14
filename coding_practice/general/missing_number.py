"""
LC268 - Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # we use the fact that the sum of a power series of order 1 up to n is n(n+1)/2, using faulhaber's formula
        # so the missing number is the power series sum minus the sum of the numbers in the list
        n = len(nums)

        return n * (n + 1) // 2 - sum(nums)