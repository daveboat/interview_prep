"""
LC260 - Single number iii

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly
twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:

    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # initial attempt: dictionary. O(N) time, O(N) space
        #         d = dict()
        #         out = []

        #         for n in nums:
        #             if n not in d:
        #                 d[n] = 1
        #             else:
        #                 d[n] += 1

        #         for k, v in d.items():
        #             if v == 1:
        #                 out.append(k)

        #         return out

        # second attempt (after reading solution). bit manipulation
        # Explanation: Like the one single number case, we take the XOR of all the numbers. If we call the two single numbers
        # x and y, then the result is x ^ y, since everything else XOR's to zero. The bit value of x ^ y, due to the nature of
        # XOR, is 1 where the bits in x and y aren't equal. Since we know x and y can't be the same number, at least one of these
        # bits must be set. We can get the rightmost bit via (x ^ y) & ~ (x ^ y - 1). Using the rightmost bit, we can partition
        # the numbers in the list into ones which have that bit, and one of x and y, and ones which don't have that bit, and the
        # other one of x and y.
        #
        # at that point, it becomes the same problem as when there's a list with two of every number except one, but twice.

        # calculate the XOR: O(N) time, O(1) space
        xor = 0
        for n in nums:
            xor ^= n

        # calculate the rightmost bit: O(1) time, O(1) space
        mask = xor & ~(xor - 1)

        # calculate x and y by partitioning nums into lists which & mask and not & mask
        x, y = 0, 0
        for n in nums:
            if n & mask:
                x ^= n
            else:
                y ^= n

        return [x, y]
