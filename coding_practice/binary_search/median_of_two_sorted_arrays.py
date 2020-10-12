"""
LC4 - Median of two sorted arrays

Algorithm to find the median of two sorted arrays.

This can be done in O(M+N) time by merging the two arrays, but we want to do it in logarithmic time, via a specialized
binary search.

The algorithm is to search the smaller of the two arrays (array A, size M) for a partition point, where A contributes
everything left of the partition point, and since the contribution from A and B (size N) must be (M+N+1)//2, a similar
partition point can be calculated in B if the partition point in A is known.

So we binary search through the smaller array, A. The lower starting index is 0 since it's the smaller of the two
arrays, it's possible for it to contribute nothing. The upper starting index is M since it's the smaller of the two
arrays, it's possible for it to contribute everything. When a partition point is found in A, the partition point in B is
(M+N+1)//2 minus that value.

In order to know if we need to search left of the partition point or right of the partition point for our binary search,
we use the fact that both arrays are sorted. If the contributions from A and B are correct, then larger of the two
elements at the partition indices is the median if it's between the element at the partition index of the other array
and the value after the partition index of the other array. Otherwise, if the larger of the two partition elements is
larger than the value after the partition index in the other array, then we know that something past the partition index
in the other array must be the median, and so we need to look to the left of the partition index in the first array (ie
decreasing the elements contributed by the first array and increasing the number of elements contributed by the second
array).

There are special cases if we're searching A, we need to partition left, but we're already at index 0. In this case,
we just (M+N+1)//2 elements from B, i.e. B contributes all the elements. In the opposite case, if our partition index
is at the final element of A, whichever element is larger between B and A is the median (in case of an even M+N, will
need to do an additional comparison here).

NOTE: Not fully tested for edge cases
"""


from typing import List


def median_of_two_sorted_arrays(A: List[int], B: List[int]):
    # We assume both A and B have at least one element

    # get lengths
    M = len(A)
    N = len(B)

    # figure out if we have an odd-lengthed total array, or an even one
    even = (M + N) % 2 == 0

    # swap things so that A is the smaller array if necessary
    if M > N:
        A, B = B, A
        M, N = N, M

    # calculate max contribution from both arrays for median
    MC = (M + N + 1) // 2

    # get the start and end indicies of A
    low = 0
    high = M - 1

    mid_A = (high + low) // 2
    mid_B = MC - mid_A

    # begin binary search
    while low <= high:
        # get partition point to test
        mid_A = (high + low) // 2

        # from A's partition point, find B's partition point
        mid_B = MC - mid_A - 2  # the -2 is because of indexing -- B_elem = MC - A_elem, but B_elem = B_idx + 1 and
                                # A_elem = A_idx + 1 so we have B_idx + 1 = MC - A_idx - 1, or B_idx = MC - A_idx - 2

        # we need to check for the special cases
        if mid_A == M - 1 and mid_B < N - 1:
            if B[mid_B] <= A[mid_A] <= B[mid_B + 1]:
                return A[mid_A] if not even else (A[mid_A] + B[mid_B + 1]) / 2
            else:
                return B[mid_B] if not even else (B[mid_B] + B[mid_B + 1]) / 2
        elif mid_A < M - 1 and mid_B == N - 1:
            if A[mid_A] <= B[mid_B] <= A[mid_A + 1]:
                return B[mid_B] if not even else (B[mid_B] + A[mid_A + 1]) / 2
            else:
                return A[mid_A] if not even else (A[mid_A] + A[mid_A + 1]) / 2
        else:
            # the general case
            if A[mid_A] > B[mid_B + 1]:
                # here, we need to look to the left of A. This and the next case are the ones that will happen most
                # often
                high = mid_A - 1
            elif B[mid_B] > A[mid_A + 1]:
                # here, we need to look to the right of A
                low = mid_A + 1
            elif B[mid_B] <= A[mid_A] <= B[mid_B + 1]:
                # in this and the next case, we've found the median
                return A[mid_A] if not even else (A[mid_A] + B[mid_B + 1]) / 2
            elif A[mid_A] <= B[mid_B] <= A[mid_A + 1]:
                return B[mid_B] if not even else (B[mid_B] + A[mid_A + 1]) / 2

    # after breaking out of the while loop, we must be in a situation where one of two partition elements is the median,
    # or the average of the partition elements is the median.
    return (A[mid_A] + B[mid_B]) / 2 if even else max(A[mid_A], B[mid_B])


if __name__ == '__main__':
    A = [4, 20, 32, 50, 55, 61]
    B = [1, 15, 22, 30, 70]
    print(median_of_two_sorted_arrays(A, B))