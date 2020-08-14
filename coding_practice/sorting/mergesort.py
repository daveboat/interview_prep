"""
Merge sort is a divide-and-conquer algorithm, applied to sorting. The steps are,

1. Mergesort the left half array
2. Mergesort the right half array
3. Merge the two halves. To do this, loop through both left and right arrays, copying whichever element is larger to

recursively applied.

Mergesort is always O(NlogN) in time because it's always doing the same thing, regardless of the arrangement of the
source array. However, it always also requires at least an extra array of size N (O(N) in space complexity) to handle
copying during the merge operation.

I'm doing it inefficiently in space here because I'm making a new python list and appending to it every time I merge. A
faithful C-like implementation would be to keep track of the left and right indices in the starting array when divide-
and-conquering, and have a single temporary array in memory which gets copied to and from.
"""
import random


def merge(left, right):
    """
    Merge two arrays which are sorted
    """
    merged = []

    # iterate while there are elements in both the left and right
    index_left = 0
    index_right = 0
    while index_left < len(left) or index_right < len(right):
        if index_left < len(left) and index_right < len(right):
            if left[index_left] < right[index_right]:
                merged.append(left[index_left])
                index_left += 1
            else:
                merged.append(right[index_right])
                index_right += 1
        elif index_left >= len(left):
            merged.append(right[index_right])
            index_right += 1
        elif index_right >= len(right):
            merged.append(left[index_left])
            index_left += 1

    return merged


def mergesort(array):

    if len(array) <= 1:
        return array
    else:
        return merge(mergesort(array[:len(array)//2]), mergesort(array[len(array)//2:]))


def check_sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))


if __name__ == '__main__':
    array = [random.randint(1, 1000) for i in range(1000)]

    array = mergesort(array)
    print(array)
    print(check_sorted(array))