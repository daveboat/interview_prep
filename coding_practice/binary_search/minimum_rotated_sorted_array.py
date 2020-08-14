"""
LC153 - Minimum of a sorted, rotated array
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we could do an O(N) linear search, but I think we can do better with a binary search in O(logN)
        # We look for a situation where nums[mid+1] < nums[mid]

        # trivial case
        if len(nums) == 1:
            return nums[0]

        # check if the array is already in order
        if nums[-1] > nums[0]:
            return nums[0]

        # initial positions
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid + 1] < nums[mid]:  # the ending condition, we've found what we're looking for
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] < nums[0]:  # the number is less than the initial number, so we need to look to the left
                right = mid - 1
            elif nums[mid] > nums[0]:  # the number is greater than the initial number, so we need to look to the right
                left = mid + 1

        # if we've left the loop, then the array must be in order
        return nums[0]


if __name__ == '__main__':
    a = [4,5,1,2,3]
    S = Solution()

    print(S.findMin(a))