"""
Quicksort works like the following, for a single step:
1. Pick a pivot value amongst the values in the array (ideally we want to pick a pivot point which is the median of the
points, but we don't know what the median is obviously, so just pick a pivot arbitrarily)
2. Store a left and right position, which are initialized to the beginning (0) and end (len-1) of the array.
3. Move the left position right and the right position left until they both are at values where the left value is
greater than the pivot and the right value is less than the pivot. Swap these elements, and repeat this whole step until
left >= right
4. Store the partition point, which is the point left ends up being after step 3.
5. Recursively apply quicksort to the left and right subarrays, as divided by partition, with the left subarray having
left = original left, right = partition value - 1, right subarray having left = partition value , right = original right

Quicksort is O(NlogN) in the average case, since we perform log(N) swaps on each (N) elements, and O(N^2) in the worst
case, which is when we pick a bad pivot every time, since we perform N swaps on each (N) elements.

Quicksort is often used in practice because it's generally O(NlogN).

The most direct competitor of quicksort is heapsort. Heapsort is typically somewhat slower than quicksort, but the
worst-case running time is always Θ(nlogn). Quicksort is usually faster, though there remains the chance of worst case
performance except in the introsort variant, which switches to heapsort when a bad case is detected. If it is known in
advance that heapsort is going to be necessary, using it directly will be faster than waiting for introsort to switch to
it.

Note that this code uses one of the two well-known partitioning algorithms, Hoare's partitioning algorithm, which has
indices starting at the left and right of the array, and swaps elements so that elements left of the partition index
are smaller than the partition value, and elements right of, and including the partition index, are larger than the
partition value. The actual partition value doesn't have to be at the partition index.

The other variation is Lamuto's partitioning algorithm, which typically picks the rightmost element of the array as the
partitioning element. One index moves right until it hits a value larger than the partition value, and one index moves
right until it hits a value smaller than the partition value. Once both indices are at appropriate places, they swap
elements and both indices increment by one. Once the array is partitioned, the partition (which was at the final index)
is swapped with the final position of the smaller index. (though this idea is implemented in a more efficient way
below). This way, what you get is an array which has the partition element in its correct final position. Then, instead
of quicksorting left of partition and right of partition including the partition, the right side no longer needs to
include the partition.

The property of Lomuto's partition, where the array ends up with the partition element in its correct final index, with
everything to the left of it smaller than it, and everything to the right of it bigger than it, is useful for algorithms
like quickselect, which partially sorts arrays.

Why quicksort is used in practice (from stackoverflow):
    Heapsort is O(N log N) guaranteed, what is much better than worst case in Quicksort. Heapsort doesn't need more
    memory for another array to putting ordered data as is needed by Mergesort. So why do comercial applications stick
    with Quicksort? What Quicksort has that is so special over others implementations?

    I've tested the algorithms myself and I've seen that Quicksort has something special indeed. It runs fast, much
    faster than Heap and Merge algorithms.

    The secret of Quicksort is: It almost doesn't do unnecessary element swaps. Swap is time consuming.

    With Heapsort, even if all of your data is already ordered, you are going to swap 100% of elements to order the
    array.

    With Mergesort, it's even worse. You are going to write 100% of elements in another array and write it back in the
    original one, even if data is already ordered.

    With Quicksort you don't swap what is already ordered. If your data is completely ordered, you swap almost nothing!
    Although there is a lot of fussing about worst case, a little improvement on the choice of pivot, any other than
    getting the first or last element of array, can avoid it. If you get a pivot from the intermediate element between
    first, last and middle element, it is suficient to avoid worst case.

    What is superior in Quicksort is not the worst case, but the best case! In best case you do the same number of
    comparisons, ok, but you swap almost nothing. In average case you swap part of the elements, but not all elements,
    as in Heapsort and Mergesort. That is what gives Quicksort the best time. Less swap, more speed.

    The implementation below in C# on my computer, running on release mode, beats Array.Sort by 3 seconds with middle
    pivot and by 2 seconds with improved pivot (yes, there is an overhead to get a good pivot).
"""

import random


def quicksort(lst, partition_algo='hoare'):
    if partition_algo not in ['hoare', 'lomuto']:
        raise ValueError('partition_algo must be one of [hoare, lomuto]')

    quicksort_helper(lst, 0, len(lst)-1, partition_algo=partition_algo)


def quicksort_helper(lst, left, right, partition_algo):
    # termination condition is when left >= right
    if left >= right:
        return

    # run the partition function on the list. The partition function also returns the partition index
    partition_index = partition(lst, left, right) if partition_algo == 'hoare' else partition_lomuto(lst, left, right)

    # quicksort on the subarrays
    quicksort_helper(lst, left, partition_index - 1, partition_algo=partition_algo)
    quicksort_helper(lst, partition_index + (0 if partition_algo == 'hoare' else 1), right,
                     partition_algo=partition_algo)


def partition(lst, left, right):
    # pick a pivot point for hoare's algorithm. arbitrarily pick it to be the one at index (left + right) // 2
    pivot = lst[(left+right)//2]

    # outer loop while left <= right
    while left <= right:
        # inner loops to increment left and decrement right until they find appropriate elements to swap
        while lst[left] < pivot:
            left += 1

        while lst[right] > pivot:
            right -= 1

        # here, we should have found elements to swap so do the swap, as long as left <= right. if left > right, then
        # there were no elements to swap
        if left <= right:
            if lst[left] != lst[right]:
                swap(lst, left, right)
            # we have to do this, or we get an infinite loop, since we might be left in a situation where
            # left = right - 1 always
            left += 1
            right -= 1

    return left


def partition_lomuto(lst, left, right):
    # pivot is chosen as the rightmost element
    pivot = lst[right]

    i = left - 1

    for j in range(left, right):
        if lst[j] < pivot:
            i += 1
            swap(lst, i, j)

    i += 1
    swap(lst, right, i)

    return i


def swap(lst, left, right):
    lst[left], lst[right] = lst[right], lst[left]
    # temp = lst[left]
    # lst[left] = lst[right]
    # lst[right] = temp


if __name__ == '__main__':
    # my_list = [random.randint(0, 1000) for i in range(1000)]
    # quicksort(my_list)
    #
    # print(my_list)
    #
    # my_list2 = [3, 2]
    # quicksort(my_list2)
    # print(my_list2)

    l = [10, 3, 8, 2, 4, 6, 9, 5]
    # quicksort(l)
    # print(l)
    # print(partition(l, 0, 7, 4))
    # print(l)

    # print(partition_lomuto(l, 0, 7))
    # print(l)

    quicksort(l, partition_algo='hoare')

    print(l)