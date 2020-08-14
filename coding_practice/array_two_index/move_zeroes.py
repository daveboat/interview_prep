"""
LC283 - Move zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""

def swap(lst, i, j):
    # swap elements i and j in a list
    tmp = lst[j]
    lst[j] = lst[i]
    lst[i] = tmp


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # initial try: bubble-sort-ish solution

        # unsorted = True
        # start_index = 0
        # start_index_updated = False
        # end_index = len(nums) - 1
        # while unsorted:
        #     unsorted = False
        #     for i in range(start_index, end_index):
        #         if nums[i] == 0:
        #             j = i + 1
        #
        #             while nums[j] == 0 and j < end_index:
        #                 j += 1
        #
        #             if nums[j] != 0:
        #                 swap(nums, i, j)
        #                 end_index = j
        #                 unsorted = True
        #
        #             if not start_index_updated:
        #                 start_index_updated = True
        #                 start_index = i + 1

        # two-index method. a left and right index start at 0 and 1. right index increments until it reaches a non-zero
        # value, and left pointer increments until it reaches a zero value. Then we swap the values at the indices.
        # after swapping, increment both left and right indices by 1

        if len(nums) <= 1:
            return nums

        left_index = 0
        right_index = 1

        while True:
            if right_index >= len(nums) or left_index >= len(nums):
                break

            if nums[left_index] == 0 and nums[right_index] != 0:
                swap(nums, left_index, right_index)
                left_index += 1
                right_index += 1

            while right_index < len(nums) and nums[right_index] == 0:
                if nums[right_index] == 0:
                    right_index += 1

            while left_index < right_index and left_index < len(nums) and nums[left_index] != 0:
                if nums[left_index] != 0:
                    left_index += 1
                    if left_index == right_index:
                        right_index += 1



S = Solution()
a = [4,2,4,0,0,3,0,5,1,0]#[0,1,0,3,12]#[2, 1]#
S.moveZeroes(a)

print(a)