"""
LC35 - Search insert position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0
"""



# import bisect

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # this is a one-liner with bisect_left or bisect_right, which is accepted but slow. Is coding our own binary
        # search faster?
        # return bisect.bisect_left(nums, target)

        # can check trivial cases here
        if target <= nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            return len(nums)

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid - 1] < target <= nums[mid]:
                return mid
            elif nums[mid] < target <= nums[mid + 1]:
                return mid + 1

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1