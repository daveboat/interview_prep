"""
LC137 - Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find
that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

------------------------------------------------------------------------------------------------------------------------
So, an O(N) solution with extra space is to use a dictionary to keep track of the counts.

A more clever bit manipulation solution is to use a 32 length array which counts bits of each number as they come in.
The final number in each array element is divided by 3, and the remainder should be 1 at the positions of the array
where the bit is 1 in the single number.

The super clever solution is a generalization of the XOR solution for single numbers I, and is described here:
https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
and has to do with implementing a counter with bitwise operations.

For k = number of times all numbers appear except the single number
    p = number of times the single number appears
we compute m = ceil(logk), the number of counters we need.
A mask is needed as long as k != 2^m
The mask for resetting the counters is ~(ym & ym-1 & ... & y1) where yi = xi if the ith bit of k is 1, otherwise yi = ~ xi

The code looks like

xm=0, xm-1=0, ... x1=0
for n in nums:
    xm ^= (xm-1 & xm-2 & ... & x1 & n)
    xm-1 ^= (xm-2 & xm-3 & ... & x1 & n)
    ...
    x1 ^= n

    mask = ~(ym & ym-1 & ... & y1) where yi = xi if the ith bit of k is 1, otherwise yi = ~xi

    xm &= mask
    xm-1 &= mask
    ...
    x1 &= mask
return any xi where the ith bit of p is 1
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initial attempt: add to a dict, which should be O(1), do N times (O(N)), then iterate through dict (O(N/3))

        #         d = {}

        #         for n in nums:
        #             if n not in d:
        #                 d[n] = 1
        #             else:
        #                 d[n] += 1

        #         for k, v in d.items():
        #             if v == 1:
        #                 return k

        # bit manipulation (https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers)

        a = 0
        b = 0

        for n in nums:
            b ^= a & n
            a ^= n
            mask = ~(a & b)
            a &= mask
            b &= mask

        return a