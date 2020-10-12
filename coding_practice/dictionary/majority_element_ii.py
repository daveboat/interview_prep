"""
LC229 - Majority element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # linear time scan through the list, keep track of numbers in a dictionary?

        d = {}
        ret = []
        threshold = len(nums) // 3

        for n in nums:
            if n not in d:
                d[n] = 1
            elif d[n] != -1:
                d[n] += 1

            if d[n] > threshold:
                ret.append(n)
                d[n] = -1  # so we don't count things twice

        return ret
