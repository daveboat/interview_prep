"""
LC56 - Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of
the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # trivial case
        if len(intervals) <= 1:
            return intervals

        # sort list in ascending order by interval start and descending order by interval end
        # this makes things automatically O(NlogN) in time. space is O(N), since we are making a new array
        # to hold the return values
        intervals.sort(key=lambda x: (x[0], -x[1]))

        # iterate through the intervals, keeping track of the end of the current interval being
        # built. we only need to track the end of the interval being built, because we've already sorted
        # the array, so we'll never get a next interval that has a start before the current start
        ret = [intervals[0]]
        end = intervals[0][1]

        for interval in intervals[1:]:
            # if the start of the iterated interval is less than the end of the current interval being
            # built, check if the end of the iterated interval is greater than the end of the built
            # interval. if so, update. otherwise, do nothing. We only need to check against the end
            # because interval starts have been sorted
            if interval[0] <= end:
                if interval[1] > end:
                    # update things
                    end = interval[1]
                    ret[-1][1] = end
            # otherwise, start a new interval, update end
            else:
                ret.append(interval)
                end = interval[1]

        return ret