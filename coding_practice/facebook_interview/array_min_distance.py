"""
Facebook interview question - Given three sorted arrays A, B, C, find the three elements (a, b, c) where max(a, b, c)
- min(a, b, c) is minimized

Idea is to have an index for each of the three arrays. Each iteration, we move increment the index pointing to the
smallest value, and then check.

Note that, once one of the arrays reaches its end, that must mean the other two indices are pointing to values larger
than it, which means that there's no point in incrementing the other numbers any further, since incrementing the others
further can't change min(a, b, c), and can only make max(a, b, c) worse

[1, 3, 5, 6, 12, 14, 20, 100, 1000]
                          ^
[8, 15, 25, 28, 30]
                ^
[2, 17, 18, 23, 45, 80]
                ^
"""


def distance(a, b, c):
    return max(a, b, c) - min(a, b, c)


def array_min_distance(A, B, C):
    l_A = len(A)
    l_B = len(B)
    l_C = len(C)

    i = 0
    j = 0
    k = 0

    min_distance = distance(A[i], B[j], C[k])

    while i < l_A and j < l_B and k < l_C:
        dist = distance(A[i], B[j], C[k])

        if dist < min_distance:
            min_distance = dist

        if A[i] <= B[j] and A[i] <= C[k]:
            i += 1
        elif B[j] <= A[i] and B[j] <= C[k]:
            j += 1
        elif C[k] <= A[i] and C[k] <= B[j]:
            k += 1

    return min_distance


if __name__ == '__main__':
    A = [1, 3, 5, 6, 12, 14, 20, 100, 1000]

    B = [8, 15, 25, 28, 30]

    C = [2, 17, 18, 23, 45, 80]

    print(array_min_distance(A, B, C))