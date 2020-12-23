"""
LC213 - House robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of
money you can rob tonight without alerting the police.

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [0]
Output: 0

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
"""


class Solution(object):
    def rob_noncircular(self, nums):
        # simple DP approach. DP array starts with nums[0] and max(nums[0], nums[1]). For 2 to len(nums)-1, we
        # append max(nums[i] + DP[i-2], DP[i-1]), i.e. we can either skip robbing the current house or rob the
        # current house.
        if len(nums) == 0:
            return 0
        elif 1 <= len(nums) <= 2:
            return max(nums)

        DP = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            DP.append(max(DP[i - 1], nums[i] + DP[i - 2]))

        return DP[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # trivial case:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)

        # we just need the algorithm for the non circular case, and take the max of nums[:-1] and nums[1:]
        return max(self.rob_noncircular(nums[:-1]), self.rob_noncircular(nums[1:]))