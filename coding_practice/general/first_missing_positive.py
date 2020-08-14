"""
Leetcode 41: first missing positive. For an array of integers, find the first missing positive integer, with a solution
that's O(N) in time and O(1) in space

This is a very contrived problem, the solution only works because we're looking for positive missing numbers
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the key is that we can only use constant extra space. This basically puts us in a territory where we must
        # somehow use the source array itself to mark our data somehow.

        # first, see if 1 is in the array. if it isn't, return 1. For every other element, if it's greater than
        # len(nums), or less than 1, set it to 1
        one_found = False
        l = len(nums)
        for i in range(l):
            if nums[i] == 1:
                one_found = True
            elif nums[i] < 1 or nums[i] > l:
                nums[i] = 1

        # if we couldn't find a true 1, we have the answer
        if not one_found:
            return 1

        # now, go through the array again (we're at O(2N) now), setting the index of the absolute value of the element
        # negative. This marks whether or not we've seen a number between 1 and l
        for i in range(l):
            idx = abs(nums[i]) - 1

            if nums[idx] > 0:
                nums[idx] *= -1

        # finally, loop through the list until we find our first nonnegative number, and return that index + 1
        for i in range(l):
            if nums[i] > 0:
                return i + 1

        # if our entire array is negative, then the number must be one greater than the number of elements in the array
        return l + 1
