"""
LC605 - Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be
planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number
n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:

    The input array won't violate no-adjacent-flowers rule.
    The input array size is in the range of [1, 20000].
    n is a non-negative integer which won't exceed the input array size.
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # iterate through the array. If we see a 1, increment by 2. If we see a zero, and the next plot is also a zero
        # (since we either skipped past or moved from a zero -- we must have since the existing array obeys the no two
        # flowers can be planted beside each other rule)
        #
        # then increment our count of possible plantings by 1, and skip ahead by 2 again
        # otherwise, increment our index by 1

        N = len(flowerbed)
        counter = 0
        possible_flowers = 0

        while counter <= N - 1:
            if flowerbed[counter] == 1:
                counter += 2
            elif counter == N - 1 or flowerbed[counter + 1] == 0:
                possible_flowers += 1
                counter += 2
            else:
                counter += 1

            if possible_flowers >= n:
                return True

        return False