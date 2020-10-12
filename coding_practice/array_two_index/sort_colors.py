"""
LC75 - Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then
    1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?
"""


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # three index solution

        i0 = 0  # index for 0
        i1 = 0  # index for 1
        i2 = 0  # index for 2

        while i0 < len(nums) or i1 < len(nums):

            # if there's no more ones or zeroes left in the rest of the array, we can break

            # get indices in place
            while i0 < len(nums) and nums[i0] != 0:
                i0 += 1

            while i1 < len(nums) and nums[i1] != 1:
                i1 += 1

            while i2 < len(nums) and nums[i2] != 2:
                i2 += 1

            # there are six situations. if i2 < i1 < i0, then we want to switch i0 with i2, unless i0 is out of bounds,
            # in which case we want to switch i1 with i2
            if i2 < i1 < i0:
                if i0 < len(nums):
                    swap(nums, i0, i2)
                    i0 += 1
                    i2 += 1
                else:
                    swap(nums, i2, i1)
                    i1 += 1
                    i2 += 1
            # if i1 < i2 < i0, then we want to switch i0 with i2 and then i2 (which now has 0) with i1
            elif i1 < i2 < i0 and i0 < len(nums):
                swap(nums, i0, i2)
                swap(nums, i1, i2)
                i0 += 1
                i1 += 1
                i2 += 1
            # if i0 < i2 < i1, then we want to switch i1 with i2. This is one of the cases where 1 might still be out
            # of order, so we put the i1 index at where the 1 now is
            elif i0 < i2 < i1 and i1 < len(nums):
                swap(nums, i1, i2)
                i1 = i2
                i2 += 1
            # 102, no need to check if i2 is < len(nums)
            elif i1 < i0 < i2:
                swap(nums, i0, i1)
                i0 += 1
                i1 += 1
            # 201, swap i2 with i1, then i0 with i2. if i1 >= len(nums), then just swap i0 with i2
            elif i2 < i0 < i1:
                if i1 >= len(nums):
                    swap(nums, i0, i2)
                    i0 += 1
                    i2 += 1
                else:  # this is one of the cases where 1 may end up out of order, so we want to set the i1 index to
                    # where the 1 ends up
                    swap(nums, i2, i1)
                    swap(nums, i2, i0)
                    i1 = i0
                    i0 += 1
                    i2 += 1
            # the final case is 012, or one of the cases where one of the indices is outside the array, so no need
            # to do anything except increment our counters
            else:
                if i0 < i1 or i0 < i2:  # we want to try to see if we can increment i0 first, and then recheck
                    i0 += 1
                elif i1 < i2:  # if i0 can't be incremented, check if i1 needs to be incremented
                    i1 += 1


if __name__ == '__main__':
    S = Solution()

    n = [0,2,2,2,0,2,1,1]

    S.sortColors(n)

    print(n)