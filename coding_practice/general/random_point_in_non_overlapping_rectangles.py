"""
LC497 - Random point in non-overlapping rectangles

Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks
an integer point in the space covered by the rectangles.

Note:

    An integer point is a point that has integer coordinates.
    A point on the perimeter of a rectangle is included in the space covered by the rectangles.
    ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and
    [x2, y2] are the integer coordinates of the top-right corner.
    length and width of each rectangle does not exceed 2000.
    1 <= rects.length <= 100
    pick return a point as an array of integer coordinates [p_x, p_y]
    pick is called at most 10000 times.

Example 1:

Input:
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output:
[null,[4,1],[4,1],[3,3]]

Example 2:

Input:
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output:
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array
of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""


from bisect import bisect_right
from random import random, randint


class Solution(object):
    # Okay, I have to do this problem a little differently, because originally I was thinking in terms of areas
    # but, from the example, the rectangle [1,0,3,0], which has area 0, can result in [3,0] being picked.
    # In other words, even the rectangle [0,0,0,0] can contribute one point
    #
    # so instead, we can do one of two things. One, we can go with the cdf format again, but each rect is weighted
    # by (x1-x0+1)*(y1-y0+1), or we can just simply generate a list of all possible points, since we are dealing
    # with only integer points. Let's go the CDF route.

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        # make cdf
        self.cdf = [(rects[0][3] - rects[0][1] + 1) * (rects[0][2] - rects[0][0] + 1)]
        for i in range(1, len(rects)):
            self.cdf.append((rects[i][3] - rects[i][1] + 1) * (rects[i][2] - rects[i][0] + 1) + self.cdf[i - 1])

    def pick(self):
        """
        :rtype: List[int]
        """
        # get a random rect via the cdf, weighted by the number of points each contains
        return self.pick_within_rect(self.rects[bisect_right(self.cdf, random() * self.cdf[-1])])

    def pick_within_rect(self, rect):
        # pick a random integer point inside a particular rect
        return [randint(rect[0], rect[2]), randint(rect[1], rect[3])]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
