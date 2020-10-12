"""
LC1041 - Robot bounded in circle

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

    "G": go straight 1 unit;
    "L": turn 90 degrees to the left;
    "R": turn 90 degress to the right.

The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:

Input: "GGLLGG"
Output: true
Explanation:
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input: "GG"
Output: false
Explanation:
The robot moves north indefinitely.

Example 3:

Input: "GL"
Output: true
Explanation:
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

Note:

    1 <= instructions.length <= 100
    instructions[i] is in {'G', 'L', 'R'}
"""


class Solution(object):
    def get_next_orientation(self, current_orientation, instruction):
        if instruction == 'R':
            return 0 if current_orientation == 3 else current_orientation + 1
        elif instruction == 'L':
            return 3 if current_orientation == 0 else current_orientation - 1

    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # the robot stays bounded if it returns to its original position OR if its final direction before looping
        # is no longer north. In the first case, the robot will return to its original position, and so it's bounded.
        # in the second case, the robot will make a multi-cycle loop

        # so we follow the instructions to the end, and find the final position and direction
        current_position = [0, 0]
        current_orientation = 0  # 0 - North, 1 - West, 2 - South, 3 - East

        for i in instructions:
            if i == 'L' or i == 'R':
                current_orientation = self.get_next_orientation(current_orientation, i)
            elif i == 'G':
                if current_orientation == 0:
                    current_position[1] += 1
                elif current_orientation == 1:
                    current_position[0] -= 1
                elif current_orientation == 2:
                    current_position[1] -= 1
                elif current_orientation == 3:
                    current_position[0] += 1

        if current_position == [0, 0]:
            return True
        elif current_orientation != 0:
            return True
        else:
            return False
