"""
LC442 - Find all duplicates in an array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # It's easy to do this in O(N) time by using a dictionary, but in order to do it in O(1) space, this is a hint
        # that we need to modify the array itself to keep track of our duplicates. This is possible because the integers
        # are constrained to be in [1, len(nums)].
        #
        # We can do this in one pass. Whenever we see a number, we multiply the value at index abs(i)-1 by -1. This way,
        # if we see a number and the value at abs(i)-1 is already negative, we add it to our output list

        output = []

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                output.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1

        return output


if __name__ == '__main__':
    S = Solution()

    a = [2, 6, 8, 3, 2, 1, 7, 5, 5]

    print(S.findDuplicates(a))