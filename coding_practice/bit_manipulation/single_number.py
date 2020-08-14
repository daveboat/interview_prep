"""
LC136 - single number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

------------------------------------------------------------------------------------------------------------------------
Simple O(N) check through the array by using a dictionary.

There's an O(1) space solution to this, using python's bitwise exclusive OR (XOR). Since XOR is associative and
commutative, and A ^ A = 0, and 0 ^ A = A, we have, for a list of numbers where every element appears twice exept for
one,

4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1 ^ 1) ^ (2 ^ 2) = 4 ^ 0 = 4

So if we XOR all of the numbers (starting with 0) as they come in (and we know there must be two of each number except
for one), then the result will be the single number.
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initial solution: dictionary
        #         d = {}

        #         for num in nums:
        #             if num not in d:
        #                 d[num] = 1
        #             else:
        #                 d[num] += 1

        #         for k, v, in d.items():
        #             if v == 1:
        #                 return k

        # better solution, XOR. Since we know that the array will have exactly two of every number except for one number, we can
        # use the property of the bitwise XOR operation, which are that:
        # - a number XOR itself is 0
        # - a number XOR 0 is itself
        # - XOR is commutative and associative (so are AND and OR)
        # Therefore, a set of numbers with the property of the incoming array, all XOR'ed with each other, will return the number
        # that is single.
        #
        # example:
        #
        # [5, 7, 8, 8, 7, 4, 5, 6, 6]
        # 5 ^ 7 ^ 8 ^ 8 ^ 7 ^ 4 ^ 5 ^ 6 ^ 6
        # = (5 ^ 5) ^ (7 ^ 7) ^ (8 ^ 8) ^ (6 ^ 6) ^ 4
        # = 0 ^ 0 ^ 0 ^ 0 ^ 4
        # = 0 ^ 4
        # = 4

        x = 0
        for num in nums:
            x ^= num

        return x