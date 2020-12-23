"""
LC941 - Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""


class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # check the trivial cases
        if len(arr) < 3 or arr[1] <= arr[0]:
            return False

        downhill = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:  # return false immediately if any two consecutive elements are equal
                return False

            if not downhill:  # while going uphill, look for the transition
                if arr[i] < arr[i - 1]:
                    downhill = True
            else:  # while going downhill, look for anywhere where we go uphill
                if arr[i] > arr[i - 1]:
                    return False

        return True if downhill else False  # make sure we've gone downhill