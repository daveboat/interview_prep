"""
LC713 - Subarray product less than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than
k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2,
6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # we're allowed to divide in this one, so let's do a two index solution.
        # i and j both start at 0, and we iterate until j reaches len(nums)
        # we keep a product variable which keeps track of the current product
        # product starts at 1
        # in each iteration, product gets multiplied by nums[j]
        # if product is less than k, add j - i + 1 to the return value
        # if product is greater than k, then we try dividing by nums[i] and rechecking as long as
        # product is greater than or equal to k and i is less than j. We never want to divide by nums[i]
        # when i is equal to j because that would result in 1, which is always less than k
        # finally, increment j by 1
        #
        # this is O(N) in time and O(1) in space

        i = 0
        product = 1
        ret = 0

        for j in range(len(nums)):
            # multiply product by nums[j]
            product *= nums[j]
            if product < k:  # if product is less than k, add j - i + 1 to the return value
                ret += j - i + 1
            else:  # otherwise, we need to try incrementing i until either i reaches j or product < k
                while i < j:
                    product //= nums[i]
                    i += 1
                    if product < k:
                        ret += j - i + 1
                        break

        return ret
