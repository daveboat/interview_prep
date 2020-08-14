"""
LC1344 - Angle between hands of a clock

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

Example 1:

Input: hour = 12, minutes = 30
Output: 165

Example 2:

Input: hour = 3, minutes = 30
Output: 75

Example 3:

Input: hour = 3, minutes = 15
Output: 7.5

Example 4:

Input: hour = 4, minutes = 50
Output: 155

Example 5:

Input: hour = 12, minutes = 0
Output: 0
"""


class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        # the hour hand is at 30H + M/2, the minute hand is at 6M. After that, just need to take the complement if
        # the absolute difference is greater than 180

        ret = abs(30 * hour + minutes / 2.0 - 6 * minutes)
        return 360 - ret if ret > 180 else ret


if __name__ == '__main__':
    S = Solution()

    print(S.angleClock(3, 15))
