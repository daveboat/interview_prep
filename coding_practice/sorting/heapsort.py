"""
The basic idea of heapsort is to use a heap data structure, push all the elements of the unsorted array onto the heap,
then pull from the top of the heap one by one.

Since heaps are stored as arrays, it's relatively painless to do this in-place, by growing the heap one by one, and then
pulling one by one, so your heap size is H, and the size of the unsorted array is len(array) - 1. Inserting into a heap
is O(logN) and pulling from a heap is O(logN), so the sort is O(NlogN)

Here we're too lazy to do it in memory, so we just implement it by returning a new list
"""

import heapq
import random


def heapsort(iterable):
    """
    Heapsort on an iterable, with the simplest possible implementation, using heapq

    Too lazy to do it in place.
    """
    queue = []

    [heapq.heappush(queue, item) for item in iterable]

    return [heapq.heappop(queue) for i in range(len(queue))]


if __name__ == '__main__':
    some_numbers = [random.randint(0, 100) for i in range(100)]

    some_numbers = heapsort(some_numbers)

    print(some_numbers)