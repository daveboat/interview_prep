"""
LC1283 - Find the Smallest Divisor Given a Threshold

Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the
array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less
than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3
and 10/2 = 5).

It is guaranteed that there will be an answer.

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
"""

import math


class Solution(object):
    def divisor_check(self, nums, divisor):
        # a helper function to return the sum of nums/divisor, where division is rounded up
        ret = 0
        for n in nums:
            ret += math.ceil(float(n) / divisor)

        return ret

    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        # i guess we can binary search, don't know if there's a fancy mathemathical solution that's faster
        # each check is O(N), and binary search is O(log max(nums)) so time complexity is (N log max(nums))

        # we binary search for the divisor in the range 1, max(nums)
        left = 1
        right = max(nums)

        smallest_divisor = float("inf")

        while left <= right:
            mid = (left + right) // 2

            check_mid = self.divisor_check(nums, mid)

            if check_mid <= threshold:
                if mid < smallest_divisor:
                    smallest_divisor = mid
                right = mid - 1
            else:
                left = mid + 1
            # print(mid, check_mid, smallest_divisor)
        return smallest_divisor