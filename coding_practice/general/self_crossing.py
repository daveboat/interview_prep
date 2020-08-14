"""
LC335 - Self Crossing

You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1]
metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your
direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.



Example 1:

┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true

Example 2:

┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false

Example 3:

┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true


"""

class vertical_line:
    def __init__(self, start_point, end_point):
        self.x = start_point.x
        self.y_range = [min(start_point.y, end_point.y), max(start_point.y, end_point.y)]


class horizontal_line:
    def __init__(self, start_point, end_point):
        self.y = start_point.y
        self.x_range = [min(start_point.x, end_point.x), max(start_point.x, end_point.x)]


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


def check_against_horizontal(start_point, end_point, hor_line):
    """
    Check a line going up or down against an existing horizontal line

    Return true if a collision occurs
    """

    if hor_line is None:
        return False

    return hor_line.x_range[0] <= start_point.x <= hor_line.x_range[1] and min(start_point.y,
                                                                               end_point.y) <= hor_line.y <= max(
        start_point.y, end_point.y)


def check_against_vertical(start_point, end_point, ver_line):
    """
    Check a line going up or down against an existing horizontal line

    Return true if a collision occurs
    """
    if ver_line is None:
        return False

    return ver_line.y_range[0] <= start_point.y <= ver_line.y_range[1] and min(start_point.x,
                                                                               end_point.x) <= ver_line.x <= max(
        start_point.x, end_point.x)


def check_horizontal_against_horizontal(start_point, end_point, hor_line):
    """
    Check if a line going left or right overlaps with an existing horizontal line

    Return true if a collision occurs
    """
    if hor_line is None:
        return False

    start_x = min(start_point.x, end_point.x)
    end_x = max(start_point.x, end_point.x)

    return hor_line.y == start_point.y and max(start_x, hor_line.x_range[0]) <= min(end_x, hor_line.x_range[1])


def check_vertical_against_vertical(start_point, end_point, ver_line):
    """
    Check if a line going up or down overlaps with an existing vertical line

    Return true if a collision occurs
    """
    if ver_line is None:
        return False

    start_y = min(start_point.y, end_point.y)
    end_y = max(start_point.y, end_point.y)

    return ver_line.x == start_point.x and max(start_y, ver_line.y_range[0]) <= min(end_y, ver_line.y_range[1])


class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """

        # basically the idea is that, due to the nature of the direction changing, it's only possible for a line to
        # cross with the previous two perpendicular lines, so we keep track of the current line, and update the
        # previous line when it becomes possible to collide with it. For example, after an up movement, it becomes
        # possible for the next down movement to collide with the right movement before the up movement, so we update
        # the previous right movement. The next down movement then checks against the previous left and right movements

        # note that, in addition to crossings between horizontal and vertical lines, it also counts as a crossing if
        # a vertical line overlaps with another vertical line, or a horizontal line overlaps with another horizontal line

        i = 0

        # for keeping track of the current line
        curr_start = point(0, 0)
        curr_end = point(0, 0)

        # for keeping track of the current horizontal and vertical lines
        curr_up_vert_line = None
        curr_left_hor_line = None
        curr_down_vert_line = None
        curr_right_hor_line = None

        # for keeping track of the previous horizontal and vertical lines
        prev_up_vert_line = None
        prev_left_hor_line = None
        prev_down_vert_line = None
        prev_right_hor_line = None

        for l in x:

            if i == 0:  # up
                # update curr_end
                curr_end.x, curr_end.y = curr_start.x, curr_start.y + l

                # update curr_up_vert_line
                curr_up_vert_line = vertical_line(curr_start, curr_end)

                # check against the previous left and right horizontal lines
                if check_against_horizontal(curr_start, curr_end, prev_left_hor_line) or check_against_horizontal(
                        curr_start, curr_end, prev_right_hor_line) or check_vertical_against_vertical(curr_start,
                                                                                                      curr_end,
                                                                                                      prev_up_vert_line) or check_vertical_against_vertical(
                    curr_start, curr_end, prev_down_vert_line):
                    return True

                # update previous right horizontal line
                prev_right_hor_line = curr_right_hor_line
            elif i == 1:  # left
                # update curr_end
                curr_end.x, curr_end.y = curr_start.x - l, curr_start.y

                # update curr_left_hor_line
                curr_left_hor_line = horizontal_line(curr_start, curr_end)

                # check against previous up and down vertical lines
                if check_against_vertical(curr_start, curr_end, prev_up_vert_line) or check_against_vertical(curr_start,
                                                                                                             curr_end,
                                                                                                             prev_down_vert_line) or check_horizontal_against_horizontal(
                    curr_start, curr_end, prev_left_hor_line) or check_horizontal_against_horizontal(curr_start,
                                                                                                     curr_end,
                                                                                                     prev_right_hor_line):
                    return True

                # update previous up vertical line
                prev_up_vert_line = curr_up_vert_line
            elif i == 2:  # down
                # update curr_end
                curr_end.x, curr_end.y = curr_start.x, curr_start.y - l

                # update curr_down_vert_line
                curr_down_vert_line = vertical_line(curr_start, curr_end)

                # check against the previous left and right horizontal lines
                if check_against_horizontal(curr_start, curr_end, prev_left_hor_line) or check_against_horizontal(
                        curr_start, curr_end, prev_right_hor_line) or check_vertical_against_vertical(curr_start,
                                                                                                      curr_end,
                                                                                                      prev_up_vert_line) or check_vertical_against_vertical(
                    curr_start, curr_end, prev_down_vert_line):
                    return True

                # update previous left horizontal line
                prev_left_hor_line = curr_left_hor_line
            elif i == 3:  # right
                # update curr_end
                curr_end.x, curr_end.y = curr_start.x + l, curr_start.y

                # update curr_right_hor_line
                curr_right_hor_line = horizontal_line(curr_start, curr_end)

                # check against the previous up and down vertical lines
                if check_against_vertical(curr_start, curr_end, prev_up_vert_line) or check_against_vertical(curr_start,
                                                                                                             curr_end,
                                                                                                             prev_down_vert_line) or check_horizontal_against_horizontal(
                    curr_start, curr_end, prev_left_hor_line) or check_horizontal_against_horizontal(curr_start,
                                                                                                     curr_end,
                                                                                                     prev_right_hor_line):
                    return True

                # update previous down vertical line
                prev_down_vert_line = curr_down_vert_line

            # update curr_start
            curr_start.x, curr_start.y = curr_end.x, curr_end.y

            # for keeping track of direction
            i += 1
            if i == 4:
                i = 0

        # if we leave the loop, return false
        return False