"""
Bubble sort is a sorting algorithm where we perform multiple sweeps through the array, swapping adjacent elements which
are out of order.

Bubble sort is O(N^2) because we have to make N passes through the array, and in each pass we have to make N swaps.
"""
import random

def bubble_sort(lst):
    is_sorted = False
    last_unsorted_index = len(lst) - 1

    while not is_sorted:
        is_sorted = True
        # we can use the fact that, in each pass, the largest remaining value in the rest of the list gets 'bubbled' up
        # to the top, so we only need to iterate our for loop up to the index of the last index that got swapped
        for i in range(last_unsorted_index):
            # swap i and i + 1 if they are out of order
            if lst[i] > lst[i+1]:
                swap(lst, i, i + 1)
                is_sorted = False
                last_unsorted_index = i


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def check_sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))


if __name__ == '__main__':
    my_list = [random.randint(0, 1000) for i in range(1000)]

    bubble_sort(my_list)

    print(check_sorted(my_list))
