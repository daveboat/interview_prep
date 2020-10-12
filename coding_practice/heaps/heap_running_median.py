from heaps.heap_lib import MinHeap, MaxHeap

class RunningMedian:
    def __init__(self):
        self.minheap = MinHeap()
        self.maxheap = MaxHeap()

    def insert(self, val):
        # if this is the first number, put it into the maxheap, which holds the smaller half of our numbers
        if self.minheap.num_elements() == 0 and self.maxheap.num_elements() == 0:
            self.maxheap.put(val)
        else:
            if val >= self.maxheap.peek():
                self.minheap.put(val)
            else:
                self.maxheap.put(val)

            self.balance_heaps()

    def balance_heaps(self):
        """
        Balance our two heaps. If the number of elements in the either heap is more than 1 element away from the number
        of elements in the other heap, put
        """
        while self.minheap.num_elements() + 1 < self.maxheap.num_elements():
            # while our minheap is more than 1 element smaller than the number of elements in our maxheap, transfer
            # over elements
            self.minheap.put(self.maxheap.get())

        while self.maxheap.num_elements() + 1 < self.minheap.num_elements():
            # do the same in the opposite situation
            self.maxheap.put(self.minheap.get())

    def get_median(self):
        """
        Return the median.
        """
        if self.minheap.num_elements() >= self.maxheap.num_elements():
            return self.minheap.peek()
        else:
            return self.maxheap.peek()


if __name__ == '__main__':
    some_numbers = [1, 5, 2, 4, 8, 3, 1]
    rm = RunningMedian()

    for num in some_numbers:
        rm.insert(num)

    print(rm.get_median())