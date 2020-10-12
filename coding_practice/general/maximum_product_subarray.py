"""
LC152 - Maximum product subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the
largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the idea is to do something similar to kadane's algorithm for maximum subarray sum, but with products.
        # we need to keep track of both the current max and the current min running products because multiplying
        # by a negative number makes the minimum possibly become the maximum and vice versa. This is O(N) in time
        # and O(1) in space

        ret = nums[0]
        current_max = ret
        current_min = ret

        for n in nums[1:]:
            # the candidates for current max and current min are n * current_max, n* current_min, and n. This
            # is because n could be negative, in which case n*current_min might become the new max and
            # n*current_max might become the new min. Also, the number itself might be the new max and/or min
            # if the previous number was 0
            candidates = (n * current_max, n * current_min, n)

            # then, update current max and current min. this automatically takes care of the case where n = 0
            current_max = max(candidates)
            current_min = min(candidates)

            # then, update ret if necessary
            if current_max > ret:
                ret = current_max

        return ret
