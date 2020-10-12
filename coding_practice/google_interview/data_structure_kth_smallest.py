"""
Google interview question

Write a data structure that can efficiently handle the following operations: adding numbers to the data structure
(Add()), and returning the kth smallest number (QueryNextSmallest()). The first time QueryNextSmallest() is called,
the smallest number is returned, and the next time the second smallest is returned, and so forth. QueryNextSmallest()
increases k by 1.

Add(2): data structure contains {2}
QueryNextSmallest(): returns 2
Add(3): data structure contains {2, 3}
Add(1): data structure contains {1, 2, 3}
QueryNextSmallest(): returns 2
QueryNextSmallest(): returns 1

------------------------------------------------------------------------------------------------------------------------

The idea here is to use two heaps to create our data structure. Basically, we want a maxheap to hold everything smaller
than our kth smallest value, and a minheap to hold our kth smallest value and everything larger. So when we add a value,
we add it to the maxheap if the minheap isn't empty and the value is smaller than or equal to the top of the minheap.
Otherwise, we add it to the minheap. We'll never be in a situation where the maxheap has values and the minheap is
empty because of the way the rest of the data structure works.

Either when adding a new value, or when querying, we must balance the heaps. We can balance at add-time, one value at a
time, or we can add to the heaps like normal and do a batch-balance at query time. Here I choose to do the latter.

Adding is O(logN), balancing (and therefore querying) is also O(logN). Space complexity is O(N)
"""
import heapq


class MaxHeap:
    def __init__(self):
        self.__heap = []

    def __bool__(self):
        return bool(self.__heap)

    def push(self, val):
        heapq.heappush(self.__heap, -val)

    def pop(self):
        return -heapq.heappop(self.__heap)

    def peek(self):
        return -self.__heap[0]

    def __str__(self):
        return str(self.__heap)

    def __len__(self):
        return len(self.__heap)


class MinHeap:
    def __init__(self):
        self.__heap = []

    def __bool__(self):
        return bool(self.__heap)

    def push(self, val):
        heapq.heappush(self.__heap, val)

    def pop(self):
        return heapq.heappop(self.__heap)

    def peek(self):
        return self.__heap[0]

    def __str__(self):
        return str(self.__heap)

    def __len__(self):
        return len(self.__heap)


class NextSmallest:
    def __init__(self):
        self.maxheap = MaxHeap()
        self.minheap = MinHeap()

        self.k = 0
        self.total = 0

    def add(self, val):
        self.total += 1

        # add it to the maxheap if the minheap has at least one value and the value we're adding is smaller or equal to
        # it. otherwise (minheap doesn't exist, or value is greater than the top of the minheap), add it to the minheap.
        if self.minheap and val <= self.minheap.peek():
            self.maxheap.push(val)
        else:
            self.minheap.push(val)

    def balance(self):
        while len(self.minheap) < self.k:
            self.minheap.push(self.maxheap.pop())
        while len(self.minheap) > self.k:
            self.maxheap.push(self.minheap.pop())

    def QueryNextSmallest(self):
        # make sure we have enough values to do the query
        if self.k + 1 > self.total:
            print('You\'re trying to query more times than you\'ve added values... this command will have no effect.')
            return

        # increment k
        self.k += 1

        # balance the heaps when we query, not every time we add a value
        self.balance()

        # return the top of the minheap
        return self.minheap.peek()


if __name__ == '__main__':
    NS = NextSmallest()
    NS.add(0)
    print(NS.QueryNextSmallest())
    # NS.add(0)
    # NS.add(4)
    # NS.add(6)
    # NS.add(8)
    # NS.add(2)
    # print(NS.QueryNextSmallest())
    # NS.add(9)
    # print(NS.QueryNextSmallest())
    # NS.add(3)
    # NS.add(1)
    # print(NS.QueryNextSmallest())
    # NS.add(3)
    # NS.add(5)
    # print(NS.QueryNextSmallest())
