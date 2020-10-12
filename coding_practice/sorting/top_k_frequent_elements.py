"""
LC347 - Top K frequent elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    You can return the answer in any order.
"""


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def partition_lomuto(lst, left, right):
    pivot = lst[right][0]

    i = left - 1

    for j in range(left, right):
        if lst[j][0] < pivot:
            i += 1
            swap(lst, i, j)

    i += 1
    swap(lst, right, i)

    return i


def quickselect_helper(lst, left, right, k):
    partition_index = partition_lomuto(lst, left, right)

    if partition_index == k:
        return
    elif partition_index < k:
        quickselect_helper(lst, partition_index + 1, right, k)
    else:
        quickselect_helper(lst, left, partition_index - 1, k)


def quickselect(lst, k):
    quickselect_helper(lst, 0, len(lst) - 1, k)


def construct_dict(nums):
    d = dict()

    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1

    return d


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # so... hash the numbers ({num: frequency}), then do a partial sort (quickselect) for k largest values
        # quickselect is fine since once we get to partition_index == k, the stuff to the right of k is guaranteed to be
        # larger, and we don't care about order

        # make our dict, which takes O(N) time
        d = construct_dict(nums)

        # make our frequency list
        freq = [[v, k] for k, v in d.items()]

        # quickselect, which takes O(N) time
        quickselect(freq, len(freq) - k)  # len(nums) - k because we want the k largest

        return [n for f, n in freq[len(freq) - k:]]


if __name__ == '__main__':
    S = Solution()
    nums = [1,1,1,2,2,3]
    k = 2

    print(S.topKFrequent(nums, k))