"""
LC1217 - Minimum Cost to Move Chips to The Same Position

We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.

Example 1:

Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
Example 2:

Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at poistion 3 to position 2. Each move has cost = 1. The total cost = 2.
Example 3:

Input: position = [1,1000000000]
Output: 1

Constraints:

1 <= position.length <= 100
1 <= position[i] <= 10^9
"""


class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        # i think the solution is conceptually quite simple... since moving over 2 spaces is free, any
        # chips on an even space can be considered to be on the same space, and any chip on an odd space
        # can be considered to be on the same space. Then the number of  points needed to move everything
        # to the same space is just min(number of chips on even spaces, number of chips on odd spaces)

        # this is O(N) in time since we need to check every element of the input array, and O(1) in space

        even = 0
        odd = 0

        for c in position:
            if c % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)