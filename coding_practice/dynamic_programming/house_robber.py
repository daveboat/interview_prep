"""
LC198 - House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

    0 <= nums.length <= 100
    0 <= nums[i] <= 400
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is a straightforward DP problem. The max after i steps is whichever is larger out
        # of (sum_up_to_i-2 + nums[i]) and sum_up_to_i-1, since we can't use consecutive values and we never
        # want to skip more than one number in a row. to initialize, we need sum_up_to_0 and sum_up_to_1,
        # which are nums[0] and max(nums[0], nums[1]), respectively

        # trivial cases
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))

        return dp[-1]
