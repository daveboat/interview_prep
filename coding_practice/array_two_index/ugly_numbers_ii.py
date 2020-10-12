"""
LC264 - Ugly number ii

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:

    1 is typically treated as an ugly number.
    n does not exceed 1690.
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # we keep indices at the last ugly number which was multiplied by 2, 3, and 5, and increment them
        # the only other thing is that we need to check to make sure we don't add duplicates. If we see a duplicate,
        # we just increment the index without appending a number.

        ugly = [1]

        i2, i3, i5 = 0, 0, 0  # index of previous 2, 3, and 5 ugly number

        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5

            if u2 <= u3 and u2 <= u5:
                if ugly[-1] != u2:
                    ugly.append(u2)
                    n -= 1
                i2 += 1
            elif u3 <= u2 and u3 <= u5:
                if ugly[-1] != u3:
                    ugly.append(u3)
                    n -= 1
                i3 += 1
            else:
                if ugly[-1] != u5:
                    ugly.append(u5)
                    n -= 1
                i5 += 1

        return ugly[-1]