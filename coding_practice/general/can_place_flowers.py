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
        # we iterate through flowerbed. when we encounter a 1, we increment our index by 2.
        # when we encounter a 0, we check if the next spot is either out of the array or a 0. if so
        # we add 1 to flowers and increment our counter by 2
        # otherwise (if next spot is a 1) we increment our counter by 1

        flowers = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            elif flowerbed[i] == 0:
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    flowers += 1
                    if flowers == n:
                        return True
                    i += 2
                else:
                    i += 1

        return True if flowers >= n else False