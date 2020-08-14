import random
import numpy as np
import bisect


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weights = w
        self.cumsum = np.cumsum(w)

    def pickIndex(self):
        """
        :rtype: int
        """
        # trivial case. don't actually need this, binary search will take care of it
        # if len(self.weights) == 1:
        #     return 0

        # use a cumulative sum and random.random(), which generates a random number between 0 and 1.
        # a search is used to find which index to choose. This is basically sampling from the cumulative distribution
        # function of the probability

        a = random.random() * self.cumsum[-1]

        # for i in range(len(self.cumsum)):
        #     if a < self.cumsum[i]:
        #         return i

        # linear search is too slow, we can binary search for where a lies in self.cumsum. Also can use
        # bisect.bisect_right

        return bisect.bisect_right(self.cumsum, a)
        #
        # left = 0
        # right = len(self.cumsum) - 1
        #
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid == 0 and 0 <= a <= self.cumsum[0]:
        #         return 0
        #     if self.cumsum[mid - 1] <= a <= self.cumsum[mid]:
        #         return mid
        #     elif self.cumsum[mid] <= a <= self.cumsum[mid + 1]:
        #         return mid + 1
        #     elif a > self.cumsum[mid]:
        #         left = mid + 1
        #     elif a < self.cumsum[mid]:
        #         right = mid - 1


if __name__ == '__main__':
    S = Solution([1, 1, 1, 1])
    a = 0
    b = 0
    c = 0
    d = 0
    for _ in range(100):
        foo = S.pickIndex()
        if foo == 0:
            a += 1
        elif foo == 1:
            b += 1
        elif foo == 2:
            c += 1
        elif foo == 3:
            d += 1

    print(a, b, c, d)