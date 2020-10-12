"""
LC15 - 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        # trivial solution
        if len(nums) < 3:
            return ret

        # we can't avoid O(N^2) for this problem, so sorting with O(NlogN) is no problem. Sorting is the easiest way
        # to avoid duplicates. Using a dictionary instead of sorting comes up against a lot of problems when trying
        # to avoid duplicates, and basically you'd end up having to do an O(triples) check every time you add a new
        # triple
        nums.sort()

        # we can do a quick check here for arrays which are impossible to get zero sums
        if nums[0] > 0:
            return ret

        # we loop from i = 0 to i < len(nums) - 2 since we must have at three numbers
        for i in range(len(nums) - 2):
            # the first stage of avoiding duplicates is checking to see if this number is a number we've already seen
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # once we fix one of the numbers, we search to the right of it using a two-pointer strategy
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    # if the sum is zero, we add this to our return list, and then skip past any duplicates for both
                    # left and right (the second stage of avoiding duplicates)
                    ret.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < 0:
                    # if the sum is less than zero, since the array is in order, we need to try a bigger value for
                    # the left index, so we increment it by 1
                    left += 1
                else:
                    # if the sum is greater than zero, since the array is in order, we need to try a smaller value
                    # for the right index, so we decrement it by 1
                    right -= 1

        return ret