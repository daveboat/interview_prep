"""
Implementation of a minheap data structure
"""


class MinHeap:
    def __init__(self, val=None):
        if val is None:
            self.items = []
            self.num_elements = 0
        else:
            self.items = [val]
            self.num_elements = 1

    def __str__(self):
        return str(self.items)

    def empty(self):
        return self.num_elements <= 0

    # some helper functions
    def get_parent_index(self, index):
        """
        Get parent index given child index
        """
        return (index - 1) // 2

    def get_left_child_index(self, index):
        """
        Get left child index given parent index
        """
        return 2 * index + 1

    def get_right_child_index(self, index):
        """
        Get right child index given parent index
        """
        return 2 * index + 2

    def left_child_exists(self, index):
        """
        Return whether left child exists given parent index
        """
        return self.get_left_child_index(index) < self.num_elements

    def right_child_exists(self, index):
        """
        Return whether right child exists given parent index
        """
        return self.get_right_child_index(index) < self.num_elements

    def parent_exists(self, index):
        """
        Return whether parent exists given child index. Parent would only not exist if the index is 0.
        """
        return index != 0

    def parent(self, index):
        """
        Returns the value of the parent of an index
        """
        return self.items[self.get_parent_index(index)]

    def left_child(self, index):
        """
        Returns the value of the left child of an index
        """
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        """
        Returns the value of the right child of an index
        """
        return self.items[self.get_right_child_index(index)]

    def swap(self, index1, index2):
        """
        Swap the values at two indices
        """
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp

    def peek(self):
        """
        Returns the top of the heap, which must be the minimum element
        """
        if self.num_elements == 0:
            raise RuntimeError("Unable to peek, heap has zero elements.")
        return self.items[0]

    def poll(self):
        """
        Removes top of the heap and returns it

        Also keeps heap valid
        """
        if self.num_elements == 0:
            raise RuntimeError("Unable to poll, heap has zero elements.")
        elif self.num_elements == 1:
            self.num_elements -= 1
            return self.items.pop()
        else:
            item = self.items[0]  # store item we're removing
            self.items[0] = self.items.pop()  # put the last element into first place
            self.num_elements -= 1  # decrement the number of elements

            # now, heapify down to keep heap valid
            self.heapify_down()

            return item

    def add(self, val):
        """
        Adds an element to the heap
        """
        self.items.append(val)
        self.num_elements += 1

        # now, heapify up to keep heap valid
        self.heapify_up()

    def heapify_down(self):
        """
        Make heap valid by swapping head element with the smaller of its children elements until heap is valid again

        heapifyDown is O(logN)
        """
        current_index = 0

        # check if I have children. Due to the structure of the heap, I only need to check if there's a left child
        while self.left_child_exists(current_index):
            # find the index of the smaller of my two children
            smaller_child_index = self.get_left_child_index(current_index)
            if self.right_child_exists(current_index) and self.right_child(current_index) < self.items[smaller_child_index]:
                smaller_child_index = self.get_right_child_index(current_index)

            # if i'm smaller than my smaller child index, do nothing
            if self.items[current_index] <= self.items[smaller_child_index]:
                break
            else:
                # swap me with my smaller child index, update index
                self.swap(current_index, smaller_child_index)
                current_index = smaller_child_index

    def heapify_up(self):
        """
        Make heap valid by swapping last element with its parent until heap is valid again

        HeapifyUp is O(logN)
        """
        current_index = self.num_elements - 1

        while self.parent_exists(current_index) and self.items[current_index] < self.parent(current_index):
            parent_index = self.get_parent_index(current_index)
            self.swap(current_index, parent_index)
            current_index = parent_index


if __name__ == '__main__':
    heap = MinHeap()
    some_numbers = [1, 5, 2, 4, 8, 3, 1]
    for number in some_numbers:
        heap.add(number)

    while not heap.empty():
        print(heap.poll())
