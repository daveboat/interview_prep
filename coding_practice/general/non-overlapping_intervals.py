"""
LC435 - Non-overlapping intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:

    You may assume the interval's end point is always bigger than its start point.
    Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # we can solve this problem by sorting the intervals by endpoints in increasing order, and if the endpoints
        # are equal, by startpoints in decreasing order. After that, we just need to go through the sorted list,
        # and if the next start point in the list is less than the previous end point, we remove it, and don't count
        # its endpoint as the previous end point.
        #
        # sorting is O(NlogN), rest of algorithm is O(N) for a single pass

        # trivial case
        if not intervals: return 0

        intervals.sort(key=lambda x: (x[1], -x[0]))  # sort [a,b] by a in ascending and then b in descending order

        # iterate through the sorted intervals list
        prev_end = intervals[0][1]
        removed = 0

        for interval in intervals[1:]:
            if interval[0] < prev_end:
                removed += 1  # remove interval
            else:
                prev_end = interval[1]  # update prev_end

        return removed
