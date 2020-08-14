"""
LC1 - Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # first attempt, brute foce
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i,j]

        # dictionary solution
        d = {}
        for i in range(len(nums)):
            # if complement is in dictionary, we're done
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            # otherwise, add the index keyed by the number, since all numbers are unique
            d[nums[i]] = i