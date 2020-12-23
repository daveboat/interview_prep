"""
LC593 - Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""


def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def sqdist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # what is a necessary and sufficient condition for four points to form a square that is also
        # easy to code? We can check angles via dot product and distances via squared differences

        # first check dot products
        dot_12_13 = dot([p2[0] - p1[0], p2[1] - p1[1]], [p3[0] - p1[0], p3[1] - p1[1]])
        dot_12_14 = dot([p2[0] - p1[0], p2[1] - p1[1]], [p4[0] - p1[0], p4[1] - p1[1]])
        dot_13_14 = dot([p3[0] - p1[0], p3[1] - p1[1]], [p4[0] - p1[0], p4[1] - p1[1]])

        # three possibilities for a possible square out of the dot products. for each, just need
        # to check two distances and an angle
        if dot_12_13 == 0 and dot_12_14 != 0 and dot_13_14 != 0:
            dot_42_43 = dot([p2[0] - p4[0], p2[1] - p4[1]], [p3[0] - p4[0], p3[1] - p4[1]])
            if sqdist(p1, p2) == sqdist(p1, p3) and dot_42_43 == 0:
                return True
        elif dot_12_14 == 0 and dot_12_13 != 0 and dot_13_14 != 0:
            dot_34_32 = dot([p4[0] - p3[0], p4[1] - p3[1]], [p2[0] - p3[0], p2[1] - p3[1]])
            if sqdist(p1, p2) == sqdist(p1, p4) and dot_34_32 == 0:
                return True
        elif dot_13_14 == 0 and dot_12_13 != 0 and dot_12_14 != 0:
            dot_24_23 = dot([p4[0] - p2[0], p4[1] - p2[1]], [p3[0] - p2[0], p3[1] - p2[1]])
            if sqdist(p1, p3) == sqdist(p1, p4) and dot_24_23 == 0:
                return True

        return False