"""
LC384 - Shuffle an array

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""


import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # store the nums
        self.nums = nums
        # remember the original by creating a deep copy. This makes a new list with the contents of the old list
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        # set nums to be a deep copy of the original
        self.nums = list(self.original)
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # we perform an in-place fisher-yates shuffle. The FY shuffle iterates through the array, swapping the ith
        # element with a randomly selected element between i and the end of the array
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))  # an important thing is that it should be possible to swap an index with itself. Otherwise some permutations become more likely than others
            self.swap(i, j)

        return self.nums

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


if __name__ == '__main__':
    S = Solution([1, 2, 3, 4, 5, 6, 7, 8])

    print(S.shuffle())
    print(S.reset())
    print(S.shuffle())
    print(S.shuffle())
    print(S.shuffle())
    print(S.shuffle())
    print(S.shuffle())
    print(S.reset())

