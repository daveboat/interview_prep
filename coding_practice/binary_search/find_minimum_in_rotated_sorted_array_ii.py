"""
LC154 - Find minimum in rotated sorted array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1

Example 2:

Input: [2,2,2,0,1]
Output: 0

Note:

    This is a follow up problem to Find Minimum in Rotated Sorted Array.
    Would allow duplicates affect the run-time complexity? How and why?
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Okay, so the problem here, when there are duplicates, is that, when duplicates wrap around, for example
        # [3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3]
        # if i'm at certain indices, it's ambiguous whether I should be binary searching to the right or left
        # in the worst case, if i'm seeing something like
        # [3, 3, ....., 3, 1, 3, 3, 3, ....., 3]
        # I don't think it's possible to do better than linear time
        #
        # how about this: we check if the first and last are equal, if they are, shift the indices until we
        # get the subarray that doesn't equal that value, and then binary search with the resulting left and right
        # indices. This is O(N) in the worst case and O(logN) in the average case, and O(1) in the best case
        # (already sorted), with O(1) space complexity

        # check for wrapping around of duplicate
        left, right = 0, len(nums) - 1
        dup = nums[0]
        if nums[0] == nums[-1]:
            while nums[left] == dup and left < right:
                left += 1
            while nums[right] == dup and left < right:
                right -= 1

        # this covers some edge cases, where the entire array is one number
        if left >= right:
            return min(dup, nums[left])

        # this covers the edge case where the subarray is sorted
        if nums[left] < nums[right]:
            return min(dup, nums[left])

        # keep track of the value that left originally pointed to
        first = nums[left]

        # now, binary search using the left and right indices we've found. we want to either include
        # one of the duplicate numbers here, or we want to check at the end for the minimum between the result
        # of the binary search and the duplicate number. let's try the latter first.
        # duplicates here are no longer a problem. We just check against the first value (where left originally
        # pointed to), as usual

        while left <= right:
            mid = (left + right) // 2

            # return conditions
            if nums[mid + 1] < nums[mid]:
                return min(nums[mid + 1], dup)
            elif nums[mid] < nums[mid - 1]:
                return min(nums[mid], dup)

            # search conditions
            if nums[mid] < first:  # if the number we're on is smaller than the first number, look left
                right = mid - 1
            else:  # nums[mid] >= first
                left = left + 1

        return min(first, dup)
