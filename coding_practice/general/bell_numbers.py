"""
Bell Numbers

The bell numbers B(n) are a sequence of numbers that represent the number of ways a set of size n can be partitioned.
This is distinct from the number of possible subsets, which is 2^n, because in the case of the bell numbers, all
elements must be inserted into a subset.
For example, for n=3, we have
{{a, b, c}}, {{a}, {b, c}}, {{a, b}, {c}}, {{a, c}, {b}}, {{a}, {b}, {c}} for 5 total possible partitions

The first 9 bell numbers (including B(0)) are [1, 1, 2, 5, 15, 52, 203, 877, 4140].

The bell numbers come up when the problem boils down to set partitioning. For example, the number of ways a 4 line
poem can be rhymed (i.e. line 1 rhymes with line 3 and line 2 rhymes with line 4, etc) are
AAAA, AAAB, AABA, ABAB, ABAA, ABCA, and so forth, is equivalent to asking to divide the set {1, 2, 3, 4} into all
possible subsets, and {{1, 2, 3, 4}} represents when all lines rhyme, so AAAA, and so forth. The answer is B(4) = 15.

The bell numbers can be computed by computing the bell triangle. Starting with 1, each new row starts with the final
element of the previous row, then for each element in the previous row, appends that element plus the element below it
in the current row. For example:

row 1:
1

row 2:
1
1 --> add 1 and 1 for 2

row 3
1
1  2
2  --> add 1 and 2 for 3, then add 2 and 3 for 5

row 4
1
1  2
2  3  5
5  --> add 2 and 5 for 7, add 3 and 7 for 10, and 10 and 5 for 15

So we need the current row and the previous row, and we can do our computation iteratively. This is O(N^2) time
complexity.
"""


def bell_number(n):
    """
    Returns the nth bell number via computing the bell triangle
    """

    # trivial case
    if n <= 1:
        return 1

    prev_row = [1]
    curr_row = []

    for i in range(2, n + 1):  # we iterate from 2 to n because we know the answer for 0 and 1 as initial conditions
        curr_row.append(prev_row[-1])
        for j in range(len(prev_row)):
            curr_row.append(prev_row[j] + curr_row[-1])

        prev_row = curr_row
        curr_row = []

    return prev_row[-1]


if __name__ == '__main__':
    print(bell_number(4))
