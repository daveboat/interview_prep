"""
LC532 - K-diff pairs in an array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

    0 <= i, j < nums.length
    i != j
    a <= b
    b - a == k

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Example 4:

Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2

Example 5:

Input: nums = [-1,-2,-3], k = 1
Output: 2

Constraints:

    1 <= nums.length <= 104
    -107 <= nums[i] <= 107
    0 <= k <= 107
"""


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # use a dictionary, keep track of count of encountered numbers, for each new number, check for k-num
        # and k+num in the array, and add that number to ret, then update the dict with the new number.
        # the exception is if k is 0, in which case only previous instances of the number itself need to be checked
        #
        # we are looking for unique pairs, so use a set to keep track?

        s = set()
        d = dict()

        for num in nums:
            # first check how many k-num and k+num we've already encountered
            if k == 0:
                if num in d:
                    s.add((num, num))
            else:
                if num - k in d:
                    s.add((num - k, num))
                if num + k in d:
                    s.add((num, num + k))

            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        return len(s)