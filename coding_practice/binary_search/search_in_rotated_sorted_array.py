"""
LC33 - Search in rotated sorted array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # trivial case
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # so, we could do an O(logN) finding the pivot point, and then another O(log(N)) finding the element...
        # is there a better way to do it?
        # well, if nums[mid] < nums[0], we could check if target is between nums[mid] and nums[-1], if so, look to
        # the right, else look to the left
        # and if nums[mid] > nums[0], we could check if target is between nums[0] and nums[mid], if so, look to
        # the left, else look to the right

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if mid + 1 < len(nums) and nums[mid+1] == target:
                return mid+1

            if nums[mid] < nums[0]:
                if nums[mid] <= target <= nums[right]:
                    # we need to look right of mid
                    left = mid + 1
                else:
                    # we need to look left of mid
                    right = mid - 1
            elif nums[mid] > nums[0]:
                if nums[left] <= target <= nums[mid]:
                    # we need to look left of mid
                    right = mid - 1
                else:
                    # we need to look right of mid
                    left = mid + 1
            else:  # the case where nums[mid] == nums[0], i.e. mid = 0, but neither mid nor mid+1 were target
                break

        # if we've left the loop, we haven't found the number, return -1
        return -1


if __name__ == '__main__':
    S = Solution()

    a = [3, 1]

    print(S.search(a, 1))