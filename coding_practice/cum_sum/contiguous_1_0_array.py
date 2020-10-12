"""
LC525 - Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

------------------------------------------------------------------------------------------------------------------------

Leetcode problem to find, in an array which only contains 1's and 0's, the longest contiguous array which has equal
ones and zeros.

The solution is to add 1 to a sum and subtract 1 to a sum whenever one sees a 1 or 0, respectively. The first time a
sum appears, add it to a dictionary with the index it was found at. The next time that sum is seen, the array between
when it first appeared and now must have equal ones and zeros, so check the dictionary every time a value already in
the dictionary appears as the sum.
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #         # initial attempt: brute force, O(N^2)
        #         max_interval = 0
        #         for i in range(len(nums)):
        #             ones_sum = 0
        #             zeroes_sum = 0
        #             for j in range(i, len(nums)):
        #                 if nums[j] == 1:
        #                     ones_sum += 1
        #                 else:
        #                     zeroes_sum += 1
        #                 if ones_sum == zeroes_sum:
        #                     if max_interval < j - i + 1:
        #                         max_interval = j - i + 1

        #         return max_interval

        # next attempt: using array sums, keeping track of the first index where we see a value
        max_length = 0
        sum_dict = {}
        current_sum = 0

        for i in range(len(nums)):
            current_sum += 1 if nums[i] == 1 else -1
            if current_sum == 0:
                if i + 1 > max_length:
                    max_length = i + 1
            else:
                if current_sum not in sum_dict:
                    sum_dict[current_sum] = i

                else:
                    if i - sum_dict[current_sum] > max_length:
                        max_length = i - sum_dict[current_sum]

        return max_length