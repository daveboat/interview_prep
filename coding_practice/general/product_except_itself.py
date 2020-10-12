"""
LC238 - Product of array except itself

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # trivial case
        if len(nums) == 1:
            return nums[0]

        # forward-backward arrays
        forward = [nums[0]]
        backward = [nums[-1]]

        for i in range(1, len(nums)):
            forward.append(forward[i - 1] * nums[i])
            backward.append(backward[i - 1] * nums[len(nums) - 1 - i])

        out = [backward[-2]]

        for i in range(1, len(nums) - 1):
            out.append(forward[i - 1] * backward[-i - 2])

        out.append(forward[-2])

        return out


if __name__ == '__main__':
    S = Solution()

    a = [1, 2, 3, 4]

    print(S.productExceptSelf(a))
