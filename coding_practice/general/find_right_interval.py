"""
LC436 - Find right interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger
than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum
start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval
i. Finally, you need output the stored value of each interval as an array.

Note:

    You may assume the interval's end point is always bigger than its start point.
    You may assume none of these intervals have the same start point.

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
"""


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # kind of a confusing question... for each interval, we need to return the index of the interval with the
        # smallest starting point larger than (or equal to!) its ending point. Because no two intervals have the
        # same start point (but presumably can have the same end point), if we have one list sorted by start point,
        # and another list sorted by end point, we can move through the end point list and, for each end point, move
        # through the start point list until we reach a start point greater than the end point, or -1 if we reach the
        # end of the start point list.
        #
        # We also need to keep track of the original index, so we can augment the original list with the index
        #
        # this is O(N) in extra space and O(NlogN) in time, for the sort
        #
        # Accepted, better than 95% of submissions on time

        L = len(intervals)

        # step 1: augment list with index
        for i in range(len(intervals)):
            intervals[i].append(i)

        # step 2: make start and end sorted lists
        start_list = sorted(intervals)
        end_list = sorted(intervals, key=lambda x: x[1])

        # step 3: for each item in end_list, go through start_list until we either reach the end of the list or
        # we find a start that's greater.
        return_list = [0] * len(intervals)
        start_index = 0
        end_index = 0

        while end_index < L:
            while start_index < L and start_list[start_index][0] < end_list[end_index][1]:
                start_index += 1

            if start_index < L:
                return_list[end_list[end_index][2]] = start_list[start_index][2]
            else:
                return_list[end_list[end_index][2]] = -1

            end_index += 1

        return return_list
