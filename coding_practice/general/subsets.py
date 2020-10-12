"""
LC78 - Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # here, we iterate from 0 to 2^len(nums), or 1 << len(nums).
        # at each iteration, we use the binary representation of the index to decide whether or not to
        # add it to the current subset. For example, for a set with three elements, the iteration number in binary
        # is:
        #
        # 000 = 0  100 = 4
        # 001 = 1  101 = 5
        # 010 = 2  110 = 6
        # 011 = 3  111 = 7
        #
        # so 000 means the empty set, 001 means [1], 010 means [2], and so forth. We use bit checking (i & (1 << j))
        # to see if an element should be added
        #
        # An alternative strategy is to do things recursively: If we know the subsets of the set without the first element
        # then the subsets of the full set are those subsets, and those subsets plus the first element. Then, the
        # termination case is the empty set, which returns [[]] So we solve by recursively solving
        # subproblems and combining, using a sort of divide-and-conquer approach. For example, for the set [1, 2, 3],
        # we get [[1 and subsets of [2,3]], subsets of [2,3]]. For [2,3] we get [[2 and subsets of [3]], subsets of [3]],
        # and for [3] we get [[3], [3 and subsets of []]]. Finally, for [], we just return [[]].
        # Returning, we get [3] has subsets [[3], []]. [2,3] then has subsets [[2], [2, 3], [3], []]
        # Finally, [1,2,3] has subsets [[1, 2], [1, 2, 3], [1, 3], [1], [2], [2, 3], [3], []]
        #                               |-----------------------------| |------------------|
        #                                1 with subsets of [2,3]          subsets of [2,3]

        out = []
        x = len(nums)
        for i in range(1 << x):
            out.append([nums[j] for j in range(x) if (i & (1 << j))])

        return out