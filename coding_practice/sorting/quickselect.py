"""
The quickselect algorithm, which does partial sorting of an array.

Uses a binary search strategy, along with Lomuto's partitioning algorithm from quicksort, to find the kth largest or
smallest value in an array.

The idea is that we sort towards the index that we're looking for. If the partition element ends up left of the index,
we recurse only on the right part of the array. If the partition element ends up right of the index, we recurse only
on the left part of the array. Since we are certain that, during this whole process, what's left of the partition
is less than the partition element, when we find the index we're looking for, it's guaranteed that the element in the
index is the correct element, and everthing to the left of it and right of it are smaller and larger than it,
respectively.

This gives us the kth largest or smallest value in an array.

Quickselect is average O(N), with worst case of O(N^2). Note that quicksort and heapsort is O(NlogN).
"""

from sorting.quicksort import partition_lomuto


def quickselect(lst, k):
    _quickselect_helper(lst, 0, len(lst) - 1, k)


def _quickselect_helper(lst, left, right, k):
    """
    """
    partition_index = partition_lomuto(lst, left, right)

    if partition_index == k:
        return

    else:
        if partition_index > k:
            _quickselect_helper(lst, left, partition_index - 1, k)
        else:
            _quickselect_helper(lst, partition_index + 1, right, k)


if __name__ == '__main__':
    l = [28, 42, 99, 16, 55, 84, 21, 93, 7, 43, 75, 46, 10, 58, 78, 12, 63, 83, 15, 37, 57, 23, 99, 65, 34, 48, 82, 34,
         11, 98, 4, 87, 23, 5, 95, 40, 33, 85, 32, 86, 40, 38, 58, 13, 91, 48]

    quickselect(l, len(l) - 4)

    print(l)
