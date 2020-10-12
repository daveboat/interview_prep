"""
LC215 - Kth largest element in an array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""


# from queue import PriorityQueue

def partition_lomuto(lst, left, right):
    pivot = lst[right]

    i = left - 1

    for j in range(left, right):
        if lst[j] < pivot:
            i += 1
            swap(lst, i, j)

    i += 1

    swap(lst, i, right)

    return i


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def quickselect(lst, left, right, k):
    partition = partition_lomuto(lst, left, right)

    if partition == k:
        return

    else:
        if partition < k:
            quickselect(lst, partition + 1, right, k)
        elif partition > k:
            quickselect(lst, left, partition - 1, k)


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # apparently we can't use the queue library anymore...

        # use a priorityqueue with negative of numbers as a maxheap (priorityqueue is normally a minheap)
        #         heap = PriorityQueue()

        #         [heap.put(-num) for num in nums]
        #         return -[heap.get() for i in range(k)][k-1]

        # return sorted(nums)[len(nums)-k]

        # this is the exact use case of quickselect, which uses lomuto's partitioning algorithm
        # apparently this is much slower than just using python's built-in sorting algorithm
        k = len(nums) - k
        quickselect(nums, 0, len(nums) - 1, k)

        return nums[k]