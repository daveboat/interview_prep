"""
Heaps using various python data structures
"""

import heapq
from queue import PriorityQueue


class MaxHeap:
    """
    Maxheap using heapq
    """
    def __init__(self):
        self._queue = []

    def __str__(self):
        return str(self._queue)

    def put(self, item):
        heapq.heappush(self._queue, -item)

    def get(self):
        return -heapq.heappop(self._queue)

    def peek(self):
        return -self._queue[0]

    def num_elements(self):
        return len(self._queue)


class MinHeap:
    """
    Minheap using heapq
    """
    def __init__(self):
        self._queue = []

    def __str__(self):
        return str(self._queue)

    def put(self, item):
        heapq.heappush(self._queue, item)

    def get(self):
        return heapq.heappop(self._queue)

    def peek(self):
        return self._queue[0]

    def num_elements(self):
        return len(self._queue)

if __name__ == '__main__':
    # # also, PriorityQueue is a minheap, so
    minheap = PriorityQueue()
    some_numbers = [1, 5, 2, 4, 8, 3, 1]
    for number in some_numbers:
        minheap.put(number)

    while not minheap.empty():
        print(minheap.get())

    print('----')

    # for a maxheap, use PriorityQueue with negative numbers
    maxheap = PriorityQueue()
    for number in some_numbers:
        maxheap.put(-number)

    while not maxheap.empty():
        print(-maxheap.get())