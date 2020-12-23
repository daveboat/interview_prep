"""
LC81 - Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # the difference here is when the array is rotated in the middle of a repeated value, eg
        # [2 2 2 2 2 2 2 2 3 4 5 6 2]
        # when we do our binary search, mid lands at a value of 2 and we're not able to tell if we need to
        # go left or right.
        # so before we do our regular binary search, we cut check if the first and last values are equal
        # if so, we cut them off. this leaves an array where the first and last values are not equal,
        # so we can do binary search as usual by checking against the first value in the array
        #
        # note that the first and last element could still be equal, but in that case the entire rest
        # of the array must just be a single number
        #
        # to remind ourselves, the binary search for an array where the first and last element
        # aren't the same is:
        # we can figure out on which side of the rotated array we are on by comparing the current
        # element to the first and last elements.
        # - if the number we're at is larger than the first element, we must be in the first half
        # - if the number we're at is smaller than the first element, we must be in the second half

        if not nums:
            return False

        left = 0
        right = len(nums) - 1

        if nums[left] == nums[right]:
            n = nums[left]
            if n == target:
                return True
            else:
                while left < len(nums) and nums[left] == n:
                    left += 1
                while right >= 0 and nums[right] == n:
                    right -= 1

        if left > right:  # no array left
            return False

        if nums[left] == nums[right]:
            if nums[left] == target:
                return True
            else:
                return False

        start = nums[left]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[mid] >= start:  # we're in the first half
                if target > nums[mid] or target < start:
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # we're in the last half
                if target < nums[mid] or target >= start:
                    right = mid - 1
                else:
                    left = mid + 1

        return False