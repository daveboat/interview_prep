"""
LC287 - Find the duplicate number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one
duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # I was looking at this trying to come up with a clever bit manipulation solution, but it turns out the clever
        # solution is to treat the array as a linked list where a node points to the index position of its value, so
        # for the array [1, 3, 4, 2, 2], we would get the linked list
        # 1 -> 3 -> 2 -> 4 -> 2 --> 4 --> 2 --> 4 ...
        # When treating the array as a linked list of this construction, a repeated element causes a loop.
        #
        # We use slow-fast pointers to find where the loop is.

        # put the slow and fast pointers at the head of the linked list (index zero)
        slow = 0
        fast = 0

        while True:  # we can loop with a true here because we know that there must be a loop
            slow = nums[slow]  # the slow pointer moves one ahead
            fast = nums[nums[fast]]  # the fast pointer moves two ahead

            if slow == fast:
                break

        # now we need to find the first node of the loop
        slow = 0
        while slow != fast:
            # move slow and fast one at a time. When the pointers are at the same node, that node must be
            # the start of the loop (note that we dont need to keep track of the NEXT node here like we do when we
            # want to remove the loop)
            slow = nums[slow]
            fast = nums[fast]

        return slow

        # note that there is also a clever bit manipulation solution. For each bit from the LSB to the number of bits
        # possible in N, we compare the number of times that bit appears in the array to the number of times that bit
        # appears for the numbers from 1 to N. When the former is greater than the latter, that bit appears in the
        # answer
        # this would look like:
        #
        # l = len(nums)
        # ans = 0
        # for i in range(l.bit_length()):
        #     bit_mask = 1 << i
        #     array_sum = sum(1 if num & bit_mask else 0 for num in nums)
        #     n_sum = sum(1 if num & bit_mask else 0 for num in range(1, l))
        #     # set the bit with an or in the answer if the array sum is greater than the regular sum
        #     if array_sum > n_sum:
        #         ans |= bit_mask


if __name__ == '__main__':
    nums = [3,1,3,4,2]#[1,3,4,2,2]#

    S = Solution()

    print(S.findDuplicate(nums))