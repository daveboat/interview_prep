class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # trivial case
        if len(nums) <= 1:
            return nums

        # we can do an O(N^2) solution where we first sort the array (O(NlogN)), and then we search from the end to
        # the beginning of the array, looking for divisible subsets. This is O(NlogN + N^2), which is O(N^2)

        # first, sort the array
        nums = sorted(nums)

        # we can make things a little simpler for ourselves by removing a leading one, since one is the identity,
        # so if we have a one, we can tack it on at the end
        has_one = False
        if nums[0] == 1:
            has_one = True
            nums = nums[1:]

        # an array to keep track of our factors
        factor_array = [[n] for n in nums]

        # a list to keep track of the largest divisible subset
        largest_divisible_subset = [nums[-1]]

        # now, we can enter our main loop. we move from len(nums) - 2 to -1 in increments of -1. At each index, we
        # look ahead to see which numbers are divisible by us. We add the divisible number with the largest number
        # of factors to our list, with ourselves
        for i in range(len(nums) - 2, -1, -1):
            largest_factor_index = -1
            largest_factor_count = 0
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    if len(factor_array[j]) > largest_factor_count:
                        largest_factor_count = len(factor_array[j])
                        largest_factor_index = j
            if largest_factor_count > 0:
                factor_array[i] = [nums[i]] + factor_array[largest_factor_index]

            # update largest divisible subset
            if len(factor_array[i]) > len(largest_divisible_subset):
                largest_divisible_subset = factor_array[i]

        return [1] + largest_divisible_subset if has_one else largest_divisible_subset


if __name__ == '__main__':
    S = Solution()

    a = [1, 2, 4, 8]

    print(S.largestDivisibleSubset(a))